# base image
FROM jupyter/base-notebook:latest
LABEL maintainer="Pablo Sierra <pavelsjo@gmail.com>"
LABEL description = "Data enviroment ready to use jupyter notebooks with Oracle ADW and ATP"

# install Oracle Instant Client 
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends libaio1 unzip
WORKDIR /opt/oracle
RUN wget 'https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basiclite-linux.x64-19.9.0.0.0dbru.zip' && \ 
unzip instantclient-basiclite-linux.x64-19.9.0.0.0dbru.zip && \
rm instantclient-basiclite-linux.x64-19.9.0.0.0dbru.zip
RUN sh -c "echo /opt/oracle/instantclient_19_9 > /etc/ld.so.conf.d/oracle-instantclient.conf" && ldconfig

# install python modules
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

# copy files and set permissions
COPY . /home/jovyan/work/
RUN chmod 777 /home/jovyan/work/*

# switch back to jovyan to avoid accidental container runs as root
USER $NB_UID
WORKDIR /home/jovyan/work
