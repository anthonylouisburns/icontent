FROM ipython/scipystack

MAINTAINER IPython Project <ipython-dev@scipy.org>

VOLUME /notebooks
WORKDIR /notebooks

#EXPOSE 8080

# You can mount your own SSL certs as necessary here
ENV PEM_FILE /key.pem
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style hash
ENV PASSWORD Dont make this your default

RUN pip install xlrd jsonpath-rw
#objectpath
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

#CMD ["/notebook.sh"]

ENV IPYTHONDIR /src/ipython
RUN echo "export IPYTHONDIR=/src/ipython" >> /etc/profile

ENTRYPOINT /usr/sbin/sshd -D
