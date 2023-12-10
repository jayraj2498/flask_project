
from flask import Flask,request,render_template, jsonify

app=Flask(__name__)

## Routes

@app.route('/')
def welcome():
    return "hello everyone"

@app.route('/aboutus')
def aboutus():
    return "we are learning flask here "

@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result= 0 
        
        if operation == "add" :
            result= num1+num2 
        elif operation=="sub":
            result= num1- num2 
        elif operation=="mul":
            result= num1* num2 
        elif operation=="div":
            result = num1/num2 
            
        return jsonify (f"The operation is {operation} & the result is: {result}")    
        # if we want to return result in html page 



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)















# from flask import Flask,request,render_template, jsonify

# app=Flask(__name__)

# ## Routes

# @app.route('/')
# def welcome():
#     return "hello everyone"

# @app.route('/aboutus')
# def aboutus():
#     return "We are ineuron and we are learning flask here "

# @app.route('/demo',methods=['POST'])
# def math_operation():
#     if(request.method=='POST'):
#         operation=request.json['operation']
#         num1=request.json['num1']
#         num2=request.json['num2']
#         result= 0 
        
#         if operation == "add" :
#             result= num1+num2 
#         elif operation=="sub":
#             result= num1- num2 
#         elif operation=="mul":
#             result= num1* num2 
#         elif operation=="div":
#             result = num1/num2 
            
#         return jsonify (f"The operation is {operation} & the result is: {result}")    
#         # if we want to return result in html page 
        
        # return jsonify (f"The operation is {operation} & the result is: {result}") # if you want result in term of jsonfile 
    
        # return f"The operation is {operation} & the result is: {result}"

        # return "The operation is {} and the result is {}".format(operation ,result)
        

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

        


