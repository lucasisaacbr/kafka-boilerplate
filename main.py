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

    return adm_client


async def produce(topic_name, broker_address):

    producer = Producer({"bootstrap.servers": broker_address})
    counter = 0

    while True:
        producer.produce(topic_name, f"Message {counter}".encode("utf-8"))
        counter += 1
        await asyncio.sleep(1)


async def consume(topic_name, broker_address):
    consumer = Consumer({
        "bootstrap.servers": broker_address,
        "group.id": "test-group"
    })

    consumer.subscribe([topic_name])

    while True:

        message = consumer.poll(1)

        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(1)


async def produce_consume(topic_name):
    """Runs the Producer and Consumer tasks"""
    t1 = asyncio.create_task(produce(topic_name, "localhost:9092"))
    t2 = asyncio.create_task(consume(topic_name, "localhost:9092"))
    await t1
    await t2


def run(topic_name):

    client = create_topic(topic_name, "localhost:9092", {"num_partitions": 3, "replication_factor": 1})
    try:
        asyncio.run(produce_consume(topic_name))
    except KeyboardInterrupt:
        print("shutting down")
    finally:
        client.delete_topics([topic_name])


run("test")