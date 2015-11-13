FROM ipython/ipython


RUN apt-get -qq update
RUN apt-get install -y nginx inotify-tools

CMD ["/notebooks/static/inotifyUpdate.sh"]
