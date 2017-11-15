from time import gmtime, strftime
from awses.connection import AWSConnection
from elasticsearch import Elasticsearch
from datetime import datetime
from datetime import timedelta

def millis():
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms


start_time = datetime.now()

es = Elasticsearch(connection_class=AWSConnection,
                   region='eu-west-1',
                   host='yourelasticsearchhostbrah')

print(millis())
res = es.search(index='whatever',doc_type='heyitsme',body={"size":100,"query":{"match_phrase_prefix":{"name":"brah"}}})
ala = [ (x['_source']['id'],x['_source']['name']) for x in res['hits']['hits'] ]
print("lala")
print(millis())
