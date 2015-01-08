PID=$(docker inspect --format {{.State.Pid}} $1)
sudo nsenter --target $PID --mount --uts --ipc --net --pid
#https://github.com/jpetazzo/nsenter
#docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter