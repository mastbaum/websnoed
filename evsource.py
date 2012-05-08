import time
import pickle
import couchdb
import numpy

# using couch for now; eventually serve json directly

couch = couchdb.Server('http://localhost:5984')
db = couch['websnoed']

events = []
with open('events.pickle') as f:
    events = pickle.load(f)

for event in events[30:31]:
    event['_id'] = 'data'
    if 'data' in db:
        event['_rev'] = db['data']['_rev']

    db.save(event)

    time.sleep(0.5)

    #raw_input()

