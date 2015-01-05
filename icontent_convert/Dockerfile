FROM ipython/ipython

VOLUME /notebooks
WORKDIR /notebooks
RUN apt-get -qq update
RUN apt-get install -y nginx inotify-tools

CMD ["/notebooks/static/inotifyUpdate.sh"]
