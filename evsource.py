import time
import couchdb
import numpy

# random and using couch for now
# eventually read from a real source and serve json directly

couch = couchdb.Server('http://localhost:5984')
db = couch['websnoed']

while(True):
    q = numpy.zeros((9500,))
    t = numpy.zeros((9500,))
    for i in range(9500):
        if numpy.random.random() < 0.3:
            q[i] = 4095 * numpy.random.random()
            t[i] = 4095 * numpy.random.random()

    if 'data' in db:
        data = db['data']
    else:
        data = {'_id': 'data'}

    data['t'] = list(t)
    data['q'] = list(q)

    db.save(data)

    time.sleep(0.1)

