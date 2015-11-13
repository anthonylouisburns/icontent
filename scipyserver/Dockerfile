FROM ipython/scipystack

MAINTAINER IPython Project <ipython-dev@scipy.org>

WORKDIR /notebooks
EXPOSE 8080

# You can mount your own SSL certs as necessary here
ENV PEM_FILE /key.pem
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style hash
ENV PASSWORD Dont make this your default

ADD notebook.sh /
RUN chmod u+x /notebook.sh
RUN pip install xlrd
RUN chmod -R 700 /notebooks
CMD ["/notebook.sh"]
