import json
import urllib2

barcodes = ['1dkdk', '2apoifje', '3jaa']

db = 'db'
user = 'db'
password = 'db'

request = urllib2.Request('http://localhost:8069/web/session/authenticate',
                          json.dumps({
                              'jsonrpc': '2.0',
                              'params': {
                                  'db': db,
                                  'login': user,
                                  'password': password,
                              },
                          }), {'Content-type': 'application/json'})
result = urllib2.urlopen(request).read()
result = json.loads(result)
session_id = result['result']['session_id']
request = urllib2.Request('http://localhost:8069/hdwolf/put',
                          json.dumps({'params': {
                              'barcodes': barcodes
                          }}), {
                              'Content-type': 'application/json',
                              'X-Openerp-Session-Id': '' + session_id
                          })

result = urllib2.urlopen(request).read()
result = json.loads(result)

print result
