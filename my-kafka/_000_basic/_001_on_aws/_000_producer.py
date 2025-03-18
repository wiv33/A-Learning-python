from kafka import KafkaProducer

public_ip = "localhost"
bootstrap_servers = ["{}:{}".format(public_ip, str(i)) for i in range(9092, 9093)]
# bootstrap_servers = ','.join(['52.79.184.210:9092', '52.79.184.210:9093', '52.79.184.210:9094'])
producer = KafkaProducer(acks=1,
                         compression_type='gzip',
                         api_version=(2, 5),
                         bootstrap_servers=",".join(bootstrap_servers))
message = {
    'id': '1',
    'msg': 'Apache kafka test message 2'
}
producer.send('test-python',
              key=bytes('1', encoding='UTF-8'),
              value=bytes('Apache kafka test message 3', encoding='utf-8'))
producer.flush()
producer.close()
