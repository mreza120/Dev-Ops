import flask
from flask import request
import redis

app = flask.Flask(__name__)
app.config["DEBUG"] = True

r = redis.StrictRedis(
host='redis',
port=6379,
charset="utf-8", 
decode_responses=True ,
password='')



@app.route('/1/', methods=['GET'])
def api_all():
    return "Welcome"

@app.route('/1/<path:hostname_port>/', defaults={'urlpath': ''}, methods=['GET'])
@app.route('/1/<path:hostname_port>/<path:urlpath>', methods=['GET'])
def api_id(hostname_port, urlpath):



    domain_and_port = hostname_port
    if ':' in domain_and_port:
        urlparts = domain_and_port.split(':')
        hostname = urlparts[0]
        port = urlparts[1]
        a = r.keys('*{}:{}*'.format(hostname,port))
    else:
        hostname = domain_and_port
        port = '80'
        a = r.keys('*{}*'.format(hostname))


    if len(a) is 0 :
        res = {
            'status': 'OK',
            'message': 'This URL is Secure',
            'domain': hostname,
            'port': port,
        }
    else :
        res = {
            'status': "NOK",
            'message': 'This URL is Malware',
            'domain': hostname,
            'port': port,
        }


    return res



if __name__ == "__main__":
    app.run("0.0.0.0",5000)
