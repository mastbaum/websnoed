import time
import couchdb
import numpy

# random and using couch for now
# eventually read from a real source and serve json directly

couch = couchdb.Server('http://localhost:5984')
db = couch['websnoed']

gtid = 0
nhit = 0
while(True):
    q = numpy.zeros((9500,), dtype=float)
    t = numpy.zeros((9500,), dtype=float)
    for i in range(9500):
        if numpy.random.random() < 0.2:
            q[i] = 4095 * numpy.random.random()
            t[i] = 4095 * numpy.random.random()
            nhit += 1

    if 'data' in db:
        data = db['data']
    else:
        data = {'_id': 'data'}

    data['t'] = list(t)
    data['q'] = list(q)

    data['qhist'] = map((lambda x: map(float, x)), zip(*reversed(numpy.histogram(data['q']))))
    data['thist'] = map((lambda x: map(float, x)), zip(*reversed(numpy.histogram(data['t']))))

    data['gtid'] = gtid
    gtid += 1

    data['nhit'] = nhit
    nhit = 0

    db.save(data)

    time.sleep(0.1)

