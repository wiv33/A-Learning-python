from elasticsearch import Elasticsearch, helpers
import pandas as pd

e = Elasticsearch('http://localhost:9200')

df = pd.DataFrame(data=None, columns=['body'])
KEEP_ALIVE_LIMIT = '10s'
body = {
    'query': {'match_all': {}}
}

res = e.search(index='index', size=10000, scroll=KEEP_ALIVE_LIMIT, body=body)
df.append({'body': [doc['_source']['body'] for doc in res['hits']['hits']]}, ignore_index=True)
sid = res['_scroll_id']
fetched = len(res['hits']['hits'])

nums = [int(res['hits']['hits'][i]['_source'][__id__]) for i in range(fetched)]

while fetched > 0:
    res = e.scroll(scroll_id=sid, scroll=KEEP_ALIVE_LIMIT)
    fetched = len(res['hits']['hits'])
    for x in range(fetched):
        doc_list = [doc['_source']['body'] for doc in res['hits']['hits']]
        df.append(pd.DataFrame({'body': doc_list}), ignore_index=True)

df.to_csv('test.csv', sep='\t')
