FROM ubuntu
ADD clone-run.sh /
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y git python python-pip
RUN pip install SQLAlchemy Flask
CMD ./clone-run.sh


