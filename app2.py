from flask import Flask , Response , request ,jsonify
import redis


r = redis.StrictRedis(
host='127.0.0.1',
port=6379,
charset="utf-8", 
decode_responses=True ,
password='')

app = Flask(__name__)
@app.route('/1/' , methods=['GET'] )
def Say_Hello():
    # name2 = r.get('reza')
    # return requests
    # print("Hello there")
    # r = request.get_data
    # print(request.json)
    a = r.keys('*asdasddname*')

    # return jsonify(Query_Result = r.get('firstname'))
    # return response(status=200)
    # return r.get('a')
    # return request.query_string
    return jsonify(len(a))

if __name__ == "__main__":
    app.run("0.0.0.0",5000)


 