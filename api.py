from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api= Api(app)
@app.route('/fibo/<int:n>')
def fib(n):
    return { "result": cal_fib(n) }

def cal_fib(n):
    if n<2:
        return n
    else:
        return cal_fib(n-1) + cal_fib(n-2)
    
#class CalculoFibo(Resource):
"""
def fib(self,n):
     if flask.request.method == 'POST':
           username = flask.request.values.get('user') # Your form's
           password = flask.request.values.get('pass') # input names
           your_registe_routine(username, password)
     else:
                 
         if n<2:
              return n
         else:
              return fib(n-1) + fib(n-2)
"""
#api.add_resource(CalculoFibo,'/fib/<n>')

if __name__ == '__main__':
 app.run(debug=True)



