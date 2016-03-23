FROM ubuntu:14.04
VOLUME /notebooks
ADD notebooks /notebooks
RUN chmod -R 777 /notebooks/static/*.sh
RUN chmod -R 777 /notebooks/static/inotifyUpdate.sh
CMD ["true"]
