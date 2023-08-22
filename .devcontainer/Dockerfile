FROM python:3.10

#install java
RUN apt -y update && \
    apt -y upgrade && \
    apt -y install openjdk-17-jre

#download Apache Spark
RUN curl https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz -O
RUN tar -xzf spark-3.3.2-bin-hadoop3.tgz && \
    mv spark-3.3.2-bin-hadoop3 /opt/spark && \
    rm spark-3.3.2-bin-hadoop3.tgz

#install findspark to use Pyspark with Apache Spark
RUN apt install python3-pip -y && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir findspark ipykernel pandas delta-spark==2.3.0

#setup environment
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
ENV PYSPARK_DRIVER_PYTHON="jupyter"
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook"
ENV PYSPARK_PYTHON=python3
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:$JAVA_HOME
