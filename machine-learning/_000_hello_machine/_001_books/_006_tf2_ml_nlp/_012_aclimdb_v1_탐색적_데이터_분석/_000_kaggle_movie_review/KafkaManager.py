from kafka import KafkaProducer, KafkaConsumer
import json


class KafkaManager:
    def __init__(self):
        self.bootstrap_servers = ",".join(['localhost:9092', 'localhost:9093', 'localhost:9094'])
        print(self.bootstrap_servers)
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                      # api_version=(2, 5)
                                      )

    def publish_message(self, topic, msg=None):
        print(f'send message [{msg}]')
        self.producer.send(topic, bytes(msg, encoding='utf-8'))
        self.producer.flush()
        # self.producer.close(1.)

    def consumer_message(self, topic, group_id) -> []:
        consumer = KafkaConsumer(topic,
                                 group_id=group_id,
                                 auto_offset_reset='earliest',
                                 bootstrap_servers=self.bootstrap_servers,
                                 # api_version=(2, 5),
                                 consumer_timeout_ms=1000)
        return consumer


# manager = KafkaManager()
# manager.publish_message('word2vec-nlp-tutorial', 'name is')

# message = manager.consumer_message('word2vec-nlp-tutorial', 'nlp-consumer')
# print(message._poll_once(1, 1))
