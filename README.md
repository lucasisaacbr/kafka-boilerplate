# Getting Started with Kafka

For this project I'm using my own Desktop, an Windows 10 machine
- 16 GB RAM (recommended)
- AMD Ryzeb 7 2700 8 cores 3.20 GHZ

## Dependencies
- Apache Zookeper (3.5.5)
```
 What for? 
 Stores topic and permissions configurations
 Orchestrate cluster membership
 Determine leadership of topic partitios
```
- Apache Kafka (2.3.1)
```
What for?
Produce and Consume real-time data
```

## Preparing the environment

Instalations steps

#### Download zookeper

Download: http://zookeeper.apache.org/releases.html#download

- Extract the tar/gz file using some tool like 7-zip (`C:/apache-zookeeper-3.5.5-bin`)
- Open the folder, and go to config folder `cd apache-zookeeper-3.5.5-bin/config` 
- rename *zoo_sample.cfg* to `zoo.cfg`
- change de value of `dataDir` configuration to a valid path in your system. `dataDir=E:/tmp/zoo-logs` (I have created this folder)
- Add `ZOOKEEPER_HOME` as a System Variable and assign the folder location `C:/apache-zookeeper-3.5.5-bin`
- Edit `PATH` environment variable to add the bin folder to it: `;%ZOOKEEPER_HOME%\bin;` 

And we are good to go! Test it running `zkserver` on your CMD.

#### Download Kafka

Download: https://kafka.apache.org/downloads (download the Binary files, not the source)

- Extract the tar/gz file using some tool like 7-zip (`C:/kafka_2.11-2.3.1`)
- Open the folder and go to config folder `cd kafka_2.11-2.3.1/config`
- open `server.properties`
- change the value of `log.dirs` to a valid path in your system. ``log.dirs=E:/tmp/kafka-logs`. (I have created this folder) 

Run Kafka Server
``` 
> cd C:/kafka_2.11-2.3.1/bin/windows
> kafka-server-start.bat  C:/kafka_2.11-2.3.1/config/server.properties
```

By default Kafka will run on port *9092* while zookeeper on port *2181*


