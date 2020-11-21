from kafka import KafkaConsumer

consumer = KafkaConsumer('test-python',
                         auto_offset_reset='earliest',
                         bootstrap_servers=['localhost:9092'],
                         api_version=(2, 5),
                         consumer_timeout_ms=1000)

while True:
    poll = consumer.poll(1000)
    for partition, records in poll.items():
        for record in records:
            print("tuple: {}".format(record))
            print(record[0], record[2], record[3], record[5], record[6].decode('utf-8'), end='\n')
