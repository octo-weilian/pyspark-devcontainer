FROM python:3.10

#install java
RUN apt -y update && \
    apt -y upgrade && \
    apt -y install openjdk-17-jre

#download Apache Spark
RUN curl --create-dirs -O --output-dir /opt/spark/ https://dlcdn.apache.org/spark/spark-3.3.3/spark-3.3.3-bin-hadoop3.tgz && \
    tar -xzf /opt/spark/spark-3.3.3-bin-hadoop3.tgz -C /opt/spark/ && \
    rm /opt/spark/spark-3.3.3-bin-hadoop3.tgz

#install Python dependencies
COPY ./requirements.txt ./requirements.txt
RUN apt install python3-pip -y && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
    
#setup environment
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_HOME=/opt/spark/spark-3.3.3-bin-hadoop3
ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
ENV PYSPARK_DRIVER_PYTHON="jupyter"
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook"
ENV PYSPARK_PYTHON=python3
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:$JAVA_HOME

#download Apache Sedona to SPARK_HOME/jars/
RUN curl --create-dirs -O --output-dir $SPARK_HOME/jars/ https://repo.maven.apache.org/maven2/org/apache/sedona/sedona-spark-shaded-3.0_2.12/1.5.0/sedona-spark-shaded-3.0_2.12-1.5.0.jar && \
    curl --create-dirs -O --output-dir $SPARK_HOME/jars/ https://repo.maven.apache.org/maven2/org/datasyslab/geotools-wrapper/1.5.0-28.2/geotools-wrapper-1.5.0-28.2.jar 

