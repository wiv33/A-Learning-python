from kafka import KafkaProducer, KafkaConsumer


class KafkaManager:
    def __init__(self, **kwargs):
        self.args = kwargs
        self.servers = self.in_args_or_default('bootstrap_server', ['localhost:9092'])

        self.api_version = self.in_args_or_default('api_version', (2, 5))

        # tag::producer[]
        self.acks = self.in_args_or_default('acks', 1)
        self.compression_type = self.in_args_or_default('compression_type', 'gzip')

        self.encoding = 'UTF-8'
        self.producer = KafkaProducer(bootstrap_servers=self.servers, api_version=self.api_version, acks=self.acks,
                                      compression_type=self.compression_type)
        # end::producer[]

        # tag::consumer[]
        self.auto_offset_reset = self.in_args_or_default('auto_offset_reset', 'earliest')
        self.consumer_timeout_ms = self.in_args_or_default('consumer_timeout_ms', 1000)
        # end::consumer[]

    def consumer(self, topic):
        consumer = KafkaConsumer(topics=topic,
                                 auto_offset_reset=self.auto_offset_reset,
                                 bootstrap_servers=self.servers,
                                 api_version=self.api_version,
                                 consumer_timeout_ms=self.consumer_timeout_ms)
        return consumer

    def send_message(self, topic, key="", value=""):
        assert topic is not None, "required topic value"

        if key is None:
            self.producer.send(topic=topic, value=self.bytes_msg(value))
            return

        self.producer.send(topic=topic, key=self.bytes_msg(key), value=self.bytes_msg(value))

    def bytes_msg(self, msg):
        return bytes(msg, self.encoding)

    def in_args_or_default(self, key, default_value):
        if key in self.args:
            return self.args[key]
        return default_value

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("-" * 33)
        print('producer close')
        print("-" * 33)
        self.producer.close()
