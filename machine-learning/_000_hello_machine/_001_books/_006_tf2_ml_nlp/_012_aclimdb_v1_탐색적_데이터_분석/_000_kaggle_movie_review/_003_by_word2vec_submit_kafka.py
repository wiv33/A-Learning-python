import pandas as pd
import json
from KafkaManager import KafkaManager


manager = KafkaManager()
consumer = manager.consumer_message(topic='word2vec-nlp-tutorial', group_id='nlp-consumer')

df = None
df_list = []
for msg in consumer:
    # df_list.append(pd.DataFrame(json.load(msg.value.decode('UTF-8'))))
    df_list.append(msg.value.decode('UTF-8'))

print(len(df_list))
