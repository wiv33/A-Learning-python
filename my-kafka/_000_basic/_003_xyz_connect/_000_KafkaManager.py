import sys

from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import json
import logging

from kafka.errors import KafkaError

PB_TOPIC_5 = "powerball_5"
PB_TOPIC_5_TEST = "powerball_5_test"


class KafkaManager:
    def __init__(self):
        self.bootstrap_servers = ",".join(['psawesome.xyz:50900'])
        print(self.bootstrap_servers)
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                      api_version=(3, 3),
                                      key_serializer=lambda k: k.encode('utf-8'),
                                      value_serializer=lambda x: json.dumps(x).encode('utf-8')
                                      )

    def publish_message(self, topic, msg=None, key=None):
        print(f'send message topic: {topic}, key: {key}, msg[{msg}]')
        self.producer.send(topic, msg, key)
        self.producer.flush()
        # self.producer.close(1.)

    def consumer_message(self, topic, group_id) -> KafkaConsumer:
        return KafkaConsumer(topic,
                             group_id=group_id,
                             auto_offset_reset='latest',  # latest 마지막, earliest 처음부터
                             enable_auto_commit=False,
                             bootstrap_servers=self.bootstrap_servers,
                             key_deserializer=lambda k: k.decode('utf-8'),
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             api_version=(3, 3),
                             consumer_timeout_ms=1000)

    def consume_loop(self, topics, group_id, exec_func):
        running = True

        consumer = self.consumer_message(topics, group_id)

        try:
            consumer.subscribe([topics])
            while running:
                messages = consumer.poll(timeout_ms=1_000, max_records=1, update_offsets=True)
                if not messages:
                    continue

                """
                {TopicPartition(topic='powerball_5', partition=1): 
                    [ConsumerRecord(topic='powerball_5', partition=1, offset=10, timestamp=1673166627676, timestamp_type=0, key='p5', value={'date': '2023-01-08', 'algo': '287972505/F8F3C (210)', 'power': {'result': '5', 'section': 'C', 'odd_even': '홀', 'under_over': '오버'}, 'number': {'result': '2 15 26 6 22', 'sum': '71', 'section': 'E', 'size': '중', 'odd_even': '홀', 'under_over': '언더'}}, headers=[], checksum=None, serialized_key_size=2, serialized_value_size=286, serialized_header_size=-1)]}

                """
                popitem = messages.popitem()
                print(popitem)
                topic_partition, records = popitem
                print(f"=========== partition info =================\n"
                      f"topic: {topic_partition[0]}\n"
                      f"partition: {topic_partition[1]}\n================================\n")

                for topic, partition, offset, timestamp, timestamp_type, key, value, header, \
                        checksum, serialized_key_size, serialized_value_size, serialized_header_size in records:
                    print("topic: %s\npartition: %s\noffset: %s\ntimestamp: %s\ntimestamp_type: %s\nkey: "
                          "%s\nvalue: %s\nheader: %s\nchecksum: %s\nserialized_key_size: "
                          "%s\nserialized_value_size:"
                          "%s\nserialized_header_size: %s\n\n=================================="
                          %
                          (
                              topic, partition, offset, timestamp, timestamp_type, key, value, header,
                              checksum,
                              serialized_key_size, serialized_value_size, serialized_header_size)
                          )
                    if group_id != key:
                        print("no match not published")
                        break
                    exec_func(value)
        except Exception as e:
            print(e)
        finally:
            # Close down consumer to commit final offsets.
            consumer.close()


# manager = KafkaManager()
# manager.publish_message('word2vec-nlp-tutorial', 'name is')

# message = manager.consumer_message('choice-5', 'ss01')
# print(message._poll_once(10000, 1))
