from flask import Flask , Response , request
import redis


# r = redis.StrictRedis(
# host='redis',
# port=6379,
# charset="utf-8", 
# decode_responses=True ,
# password='')

app = Flask(__name__)
@app.route('/1' , methods=['GET'] )
def Say_Hello():
    # name2 = r.get('reza')
    # return requests
    # print("Hello there")
    print(request.json)
    return "HIII"
    # return response(status=200) 

if __name__ == "__main__":
    app.run("0.0.0.0",5000)
 