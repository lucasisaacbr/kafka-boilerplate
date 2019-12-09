import asyncio

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic


def create_topic(topic_name, broker_address, topic_config):

    adm_client = AdminClient({"bootstrap.servers": broker_address})

    num_partitions = topic_config.get("num_partitions")
    replication_factor = topic_config.get("replication_factor")

    new_topic = [
        NewTopic(topic_name,
                 num_partitions=num_partitions,
                 replication_factor=replication_factor)
    ]

    fs = adm_client.create_topics(new_topic)

    for topic, f in fs.items():
        try:
            f.result()
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")


# Test
create_topic("test", "localhost:9092", {"num_partitions": 3, "replication_factor": 1})
