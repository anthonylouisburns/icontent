##IContent
IContent is intended to allow intuitive and simple generation of Technical and data intensive documents, particularly HTML.

The functionality largely reproduces what is possible with [NBViewer](http://nbviewer.ipython.org/). IContent attempts to make customization of the documents more transparent and excessable than with NBViewer.

IContent is most directly derived from [ipython/docker-notebook](https://github.com/ipython/docker-notebook)

IContent's functionality is modeled after static content generation frameworks like [Hugo](http://gohugo.io/), and inspired by the entire IPython community particularly those using IPython for blogging.

The core functionality is provide by [NBConvert](https://github.com/ipython/ipython/tree/master/IPython/nbconvert). IContent is a simple composition of a handful of individual [Docker](https://www.docker.com/) services, coordinated using [fig](http://www.fig.sh/).

###Checkout
The Project consists of three core Docker services, (icontent_convert, nginxone and scipyserver) and one docker service (dev-tools) which can be used as an environment for testing and developing IContent functionality. Additionally the notebooks directory holds IPython notebooks and generated documents, as well as scripts and data.

The Docker services are intended to be launched and orchestrated using fig. Fig is a prerequisite for running this application as intended. The included Vagrant file includes fig and Docker.

1. scipyserver
  - host an IPython notebook at [http://localhost:8080]
  - not incrypted, intended to be run on development machine, not on server
  - Dockerfile largely based on [https://github.com/ipython/docker-notebook/blob/master/scipyserver/Dockerfile]
2. icontent_convert
  - watches notebook directory and runs NBConvert on altered notebooks, generating HTML documents (other document types are possible  
3. nginxone
  - serves static files at [http://localhost:80]
4. dev-tools
5. notebooks
  - shared data and generate IPython Notebooks, and generated documents

