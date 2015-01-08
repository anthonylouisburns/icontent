#IContent
IContent is intended to allow intuitive and simple generation of Technical and data intensive documents, particularly HTML.

The functionality largely reproduces what is possible with [NBViewer](http://nbviewer.ipython.org/). IContent attempts to make customization of the documents more transparent and excessable than with NBViewer.

IContent is most directly derived from [ipython/docker-notebook](https://github.com/ipython/docker-notebook)

IContent's functionality is modeled after static content generation frameworks like [Hugo](http://gohugo.io/), and inspired by the entire IPython community particularly those using IPython for blogging.

The core functionality is provide by [NBConvert](https://github.com/ipython/ipython/tree/master/IPython/nbconvert). IContent's implementation borrows heavily from Min's repository https://github.com/ipython/nbconvert-examples, which I found referenced here https://github.com/ipython/ipython/wiki/Cookbook:-nbconvert-templates. IContent is a simple composition of a handful of individual [Docker](https://www.docker.com/) services, coordinated using [fig](http://www.fig.sh/).

**_Coming Soon_** I am planning to integrate these ideas with [jupyter/nbviewer](https://github.com/jupyter/nbviewer) and [ipython/docker-notebook](https://github.com/ipython/docker-notebook)
####Overview
The Project consists of three core Docker services, (icontent_convert, nginxone and scipyserver) and one docker service (dev-tools) which can be used as an environment for testing and developing IContent functionality. Additionally the notebooks directory holds IPython notebooks and generated documents, as well as scripts and data.

The Docker services are intended to be launched and orchestrated using [fig](http://www.fig.sh/). [Fig](http://www.fig.sh/) is a prerequisite for running this application as intended. The included [Vagrant](https://www.vagrantup.com/) file includes [fig](http://www.fig.sh/) and [Docker](https://www.docker.com/).

1. scipyserver
  - host an IPython notebook at [http://localhost:8080]
  - not incrypted, intended to be run on development machine, not on server
  - Dockerfile largely based on [https://github.com/ipython/docker-notebook/blob/master/scipyserver/Dockerfile]
2. icontent_convert
  - watches notebook directory and runs NBConvert on altered notebooks, generating HTML documents (other document types are possible  
3. nginxone
  - serves static files at http://localhost:80
4. dev-tools
5. notebooks
  - shared data and generate IPython Notebooks, and generated documents

####Launch
Clone Project
```
$git clone https://github.com/anthonylouisburns/icontent.git
```

Launch IContent Application, generally on dev machine
```
$cd icontent
$fig up
```

Launch nginx
```
$cd icontent/nginxone
$fig up
```
This is simply running a webserver that serves up the previously generated static content. It is currently configured to serve content at http://localhost/icontent/. This can be easily replaced with a different web server. The generated files are by default static html.

#IContent Application
Launch IContent Application, generally on dev machine
```
$cd icontent
$fig up
```

In addition to the nginx server at local host this runs a IPython Notebook server at port 8080

The unique functionality is in icontent_convert service. This service runs the script at https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/inotifyUpdate.sh
```bash
#!/bin/bash

while true #run indefinitely
do
inotifywait -e modify,attrib,close_write,move,create,delete /notebooks
echo "run"
ipython /notebooks/static/getAltered.py
echo "move"
ipython /notebooks/static/moveFiles.py
sleep 1
done
```

Whenever any files in the notebooks directory are changed, /notebooks/static/getAltered.py is run and determines what files with the extension .ipynb (IPython Notebooks) have been changed. 

https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/convert_one_file.py is then applied to each changed Notebook.

#IContent Configuration
By default the values are as follows

- https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/icontent.tpl - default [Jinja](http://jinja.pocoo.org/) template
- https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/sideleft.html - default sidebar
- https://github.com/anthonylouisburns/icontent/blob/master/notebooks/icontent/css/home.css - default css
- empty array - default links to include in sidebar
  - format: [["${text}", "${url}", "${css id}"], ...]

####Override
override values for these four variables can be specified in any markdown cell within a IPython Notebook.

It is permissible to put the settings inside a comment.
```
<!---
config_script=/notebooks/static/config.py

css=/css/home.css

sideleft=sideleft.html

links=[["Anthony Louis Burns", "http://www.anthonylouisburns.com", "pad0"], ["IContent", "http://www.anthonylouisburns.com/icontent/IContent.html", "pad0"], ["IContent - github", "https://github.com/anthonylouisburns/icontent/", "pad0"], ["Anthony Louis Burn - LinkedIn", "https://www.linkedin.com/in/anthonylouisburns", "pad0"]]
--->
```

#IContent Convert
The IContent Convert service runs the following [inotifyUpdate.sh](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/inotifyUpdate.sh) on startup

```bash
#!/bin/bash

while true #run indefinitely
do
inotifywait -e modify,attrib,close_write,move,create,delete /notebooks
echo "ipython /notebooks/static/getAltered.py"
ipython /notebooks/static/getAltered.py
echo "ipython /notebooks/static/moveFiles.py"
ipython /notebooks/static/moveFiles.py
echo "finished inotifyUpdate.sh loop"
sleep 1
done
```
This script monitors the /notebooks directory for any change. If it detects a change it runs [getAltered.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/getAltered.py)
```python
import glob
import os.path, time
import convert_one_file

def getChanged():
    pyFiles = glob.glob("/notebooks/*.ipynb") + glob.glob("/notebooks/**/*.ipynb") + glob.glob("/notebooks/**/**/*.ipynb")

    tc = 0
    tsFile = 'tsFile.txt'
    if os.path.exists('tsFile.txt'):
        f = open('tsFile.txt', 'r')
        t = f.readline()
        f.close()
        tc = time.gmtime(float(t))

    t=time.time()
    f = open('tsFile.txt','w')
    f.write(str(t)) # python will convert \n to os.linesep
    f.close()

    changed = list({f for f in pyFiles if time.gmtime(os.path.getmtime(f)) > tc})

    return changed

changed_nbs = getChanged()
for nb in changed_nbs:
    print("changed_nb:-------",nb)
    convert_one_file.convert_one(nb)
```

[getAltered.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/getAltered.py) determines if any files with the .ipynb extension have changed. If a notebook file has changd it than calls  [convert_one_file.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/convert_one_file.py) on each file creating an HTMl file.

[inotifyUpdate.sh](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/inotifyUpdate.sh) than runs [moveFiles.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/moveFiles.py)
```python
import glob
import shutil
import os


def new_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


pyFiles = glob.glob("*.ipynb") + glob.glob("**/*.ipynb") + glob.glob("**/**/*.ipynb")
print(pyFiles)
for p in pyFiles:
    lastDash = p.rfind("/")+1
    pyDir = p[:lastDash]
    pyFile = p[lastDash:]
    htmlFile = pyFile.replace("ipynb", "html")
    htmlDir = "html/"+pyDir
    new_dir(htmlDir)
    if os.path.exists(htmlFile):
        shutil.move(htmlFile, htmlDir + htmlFile)
        print("moving:", htmlFile, htmlDir)
```

[moveFiles.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/moveFiles.py) moves any html documents created to a seperate directory with the same structure as the notebook directory for static serving by the nginxone service.

####[convert_one_file.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/convert_one_file.py)
```python
import subprocess
import shutil
import os
import json
import itertools


def convert_one(notebook):

    with open(notebook) as data_file:
        data = json.load(data_file)

    script = "ipython nbconvert --config " + getConfig(data) + " " + notebook
    print(script)
    subprocess.call(script, shell=True, cwd=r'/notebooks/static')

    html = notebook.replace(".ipynb", ".html").replace("/notebooks/", "/notebooks/static/")
    html_dest = html.replace("/notebooks/static/", "/notebooks/icontent/")

    if not os.path.exists(os.path.dirname(html_dest)):
        os.makedirs(os.path.dirname(html_dest))

    #if os.path.exists(html_dest):
    #    os.remove(html_dest)

    shutil.move(html, html_dest)


def getConfig(nb):
    print('>>>>>>>>>setVariables')
    sourcelist = [cell["source"] for cell in nb["cells"] if cell["cell_type"] == 'markdown']
    allsource = list(itertools.chain(*sourcelist))

    config_script = "/notebooks/static/config.py"

    config_list = [s.partition("=")[2].strip() for s in allsource if s.partition("=")[0] == "config_script"]

    if len(config_list)>0: config_script=config_list[-1]

    return config_script
```

This script reads the notebook json and determines if the config_script has been set in any of the metadata cells.

If it has it than calls nbconvert on the file with the new config script, if not it calls it with the default config script. the default config script is [config.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/config.py)
```python
c = get_config()


#Export all the notebooks in the current directory to the sphinx_howto format.
c.Exporter.template_file = 'icontent'
c.Exporter.preprocessors = ['icontent_preprocessor.IContentPreprocessor']
```
That config script sets the html template to icontent, so [icontent.tpl](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/icontent.tpl) is used.

It also sets a Preprocessor equal to icontent_preprocessor.IContentPreprocessor this can be found in this file [icontent_preprocessor.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/icontent_preprocessor.py)

It sets the three following variables to values it finds in the notebooks Markdown cells or to these defaults 
- resources['css'] = ["/css/home.css"]
- resources['sideleft'] = "sideleft.html"
- resources['links'] = [["Anthony Louis Burns", "http://www.anthonylouisburns.com", "pad0"], ["IContent", "http://www.anthonylouisburns.com/icontent/IContent.html", "pad0"], ["IContent - github", "https://github.com/anthonylouisburns/icontent/", "pad0"], ["Anthony Louis Burn - LinkedIn", "https://www.linkedin.com/in/anthonylouisburns", "pad0"]]

These varaibles are than used inside of the templates, the links variable is used in the sideleft.html template, and css, and sideleft are used in the icontent.tpl

####Brazil example
The Brazil example overrides the [config.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/config.py) with the [brazil.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/brazil.py) script
```python
c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.Exporter.template_file = 'brazil'
c.Exporter.preprocessors = ['icontent_preprocessor.IContentPreprocessor', 'icontent_preprocessor.ExclamationPreprocessor']
```
[brazil.py](https://github.com/anthonylouisburns/icontent/blob/master/notebooks/static/brazil.py) and adds an additonal brazil.css style sheet which themes the colors to those of the Brazilian flag.
```css
#sideleft {
    background-color: #FCFC08;
}
body{
    background-color: #416CB1;
}
#notebook-container{
    background-color: #135728;
}
#sideleft a {
    color: #135728;
}
div.text_cell_render {
    color: #FCFC08;
}
#headerbox {
    background-color: #FCFC08;
    color: #135728;
}
```
brazil.py changes the template to brazil.tpl, brazil.tpl adds a Brazil header
```smarty
{#
i found this very useful
https://realpython.com/blog/python/primer-on-jinja-templating/

these templates are jinja templates
http://jinja.pocoo.org/docs/dev/api/#basics
#}

{%- extends 'full.tpl' -%}
{% block body %}
 </div>
{% for css in resources.css -%}
    <link rel="stylesheet" href="{{ css }}">
{% endfor %}
<div id="headerbox">
    <h1>BRAZIL</h1>
</div>
{% include resources.sideleft ignore missing%}
<div id="main">
{{ super() }}
</div>
{%- endblock body %}
```
####Standard example
[icontent.tpl]()
```smarty
{#
i found this very useful
https://realpython.com/blog/python/primer-on-jinja-templating/

these templates are jinja templates
http://jinja.pocoo.org/docs/dev/api/#basics
#}

{%- extends 'full.tpl' -%}
{% block body %}
 </div>

{% for css in resources.css -%}
    <link rel="stylesheet" href="{{ css }}">
{% endfor %}

{% include resources.sideleft ignore missing%}
<div id="main">
{{ super() }}
</div>
{%- endblock body %}
```
sideleft.html
```smarty
<div id="sideleft">
    {% for link in resources.links -%}
    <p id="{{ link.2 }}">
        <a href="{{ link.1 }}">{{ link.0 }}  </a>
    </p>
    {% endfor %}
</div>
```
[/icontent/blob/master/notebooks/static/home.css]
```css
#sideleft {
    float: left;
    width: 15%;
    min-height: 100%;
    text-align: left;
    padding:30px;
    box-sizing: border-box;
    -webkit-box-shadow: 0px 0px 12px 5px rgba(87, 87, 87, 0.2);
    padding-top: 20px;
    margin-top: 20px;
    padding-bottom: 20px;
}

#main
{
    float: right;
    text-align: left;
    width: 70%;
    margin-right: 15%;
}
#pad0
{
    padding: 10px;
}
#pad1
{
    text-indent: 20px;
}
body{
}
#notebook-container{
}
#sideleft a {
    text-decoration: underline;
}
div.text_cell_render {

}
#headerbox {
    float: left;
    width: 100%;
    min-height: 5%;
    text-align: center;
    padding:30px;
    box-sizing: border-box;
    -webkit-box-shadow: 0px 0px 12px 5px rgba(87, 87, 87, 0.2);
    padding-top: 20px;
    padding-bottom: 20px;
}
```
