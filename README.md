##IContent
IContent is intended to allow intuitive and simple generation of Technical and data intensive documents, particularly HTML.

The functionality largely reproduces what is possible with [NBViewer](http://nbviewer.ipython.org/). IContent attempts to make customization of the documents more transparent and excessable than with NBViewer.

IContent is most directly derived from [ipython/docker-notebook](https://github.com/ipython/docker-notebook)

IContent's functionality is modeled after static content generation frameworks like [Hugo](http://gohugo.io/), and inspired by the entire IPython community particularly those using IPython for blogging.

The core functionality is provide by [NBConvert](https://github.com/ipython/ipython/tree/master/IPython/nbconvert). IContent is a simple composition of a handful of individual [Docker](https://www.docker.com/) services, coordinated using [fig](http://www.fig.sh/).

###Checkout
The Project consists of three core Docker services, (icontent_convert, nginxone and scipyserver) and one docker service (dev-tools) which can be used as an environment for testing and developing IContent functionality. Additionally the notebooks directory holds IPython notebooks and generate documents, as well as scripts and data.

The Docker services are intended to be launched and orchestrated using fig.

1. scipyserver
2. icontent_convert
3. nginxone
4. dev-tools
5. notebooks

