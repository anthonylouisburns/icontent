#docker run --name data_bash  -i -t tutum.co/burnstony/data:latest bash
docker run --name data_bash2 --volumes-from data_data_1 -i -t ubuntu bash
