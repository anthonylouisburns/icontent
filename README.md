#IContent
IContent is intended to allow intuitive and simple generation of Technical and data intensive documents, particularly HTML.

The functionality largely reproduces what is possible with [NBViewer](http://nbviewer.ipython.org/). IContent attempts to make customization of the documents more transparent and excessable than with NBViewer.

IContent is most directly derived from [ipython/docker-notebook](https://github.com/ipython/docker-notebook)

IContent's functionality is modeled after static content generation frameworks like [Hugo](http://gohugo.io/), and inspired by the entire IPython community particularly those using IPython for blogging.

The core functionality is provide by [NBConvert](https://github.com/ipython/ipython/tree/master/IPython/nbconvert). IContent is a simple composition of a handful of individual [Docker](https://www.docker.com/) services, coordinated using [fig](http://www.fig.sh/).

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
