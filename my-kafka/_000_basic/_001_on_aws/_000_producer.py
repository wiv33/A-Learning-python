from kafka import KafkaProducer

bootstrap_servers = ','.join(['52.79.184.210:9092', '52.79.184.210:9093', '52.79.184.210:9094'])
producer = KafkaProducer(acks=1,
                         compression_type='gzip',
                         bootstrap_servers=bootstrap_servers)
message = {
    'id': '1',
    'msg': 'Apache kafka test message'
}
producer.send('test-python', message)
