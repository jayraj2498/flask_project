# from flask import Flask , request , render_template 


# app=Flask(__name__)

# @app.route("/")
# def method():
#     return render_template("index.html") 


# @app.route("/operation" , methods=["POST"])
# def math_op():
#     if(request.method=="POST"):
#         operation=request.form["operation"]
#         num1=request.form["num1"]
#         num2=request.form["num2"]
#         result=0 
        
#         if operation=="add":
#             result= int(num1)+int(num2) 
            
#         elif operation=="sub":
#             result= int(num1)-int(num2)
            
#         elif operation=="mul":
#             result= int(num1)*int(num2) 
            
#         elif operation == "div":
#             result = int(num1) / int(num2)  
            
            
#         return render_template("result.html" , result=result)
                



# if __name__=="__main__":
#     app.run(debug=True)









# from flask import Flask , request

# app=Flask(__name__) 

# @app.route("/")
# def fun():
#     return "helloo everyOne"     

# @app.route("/solution", methods=["POST"])
# def mathoperation():
#     if (request.method=="POST"):
#         solution=request.json["solution"]
#         no1=request.json["no1"]
#         no2=request.json["no2"] 
#         result=0 
        
#         if solution=="add":
#             result=no1+no2 
            
#         elif solution=="sub":
#             result=no1-no2  
            
#         elif solution=="mul":
#             result=no1*no2 

#         elif solution=="div":
#             result=no1/no2  
            
#         return f" the operation is {solution} and it's result is {result}"


# if __name__=="__main__":
#     app.run(debug=True)























# from flask import Flask , request 

# app = Flask(__name__)  

# @app.route("/")
# def welcome_page():
#     return "welcome all of you here   how are you tell me abt yourself " 

# @app.route("/demo", methods=["POST"])
# def demoeverything():
#     if(request.method=="POST"):
#         operation=request.json["operation"] 
#         no1=request.json["no1"]
#         no2=request.json["no2"] 
#         result=0 
        
#         if operation =="add":
#             result=no1+no2 
            
#         if operation =="sub":
#             result=no1-no2 
        
#         if operation == "mul" :
#             result = no1*no2
            
#         if operation =="div":
#             result= no1/no2 
            
#         return f"The Operation is {operation} and result is :{result}"
        



# @app.route("/demosub" , methods=["POST"])
# def demosub():
#     if(request.method=="POST"):
#         sub_operation=request.json["math_operation"]
#         no1=request.json["no1"]
#         no2=request.json["no2"]
#         result=no1-no2
#         return f"The Operation is {sub_operation} & their substraction is :{result}"


# @app.route("/demosum", methods=["POST"]) 
# def demosum():
#     if(request.method=="POST"):
#         math_operation=request.json["math_operation"]
#         no1=request.json["no1"]
#         no2=request.json["no2"]
#         solution= no1+no2 
        
#         return f" The Operatin is {math_operation} and their addition is {solution}" 
    
    
# @app.route("/demomul", methods=["POST"]) 
# def demomul():
#     if(request.method=="POST"):
#         math_operation=request.json["math_operation"]
#         no1=request.json["no1"]
#         no2=request.json["no2"]
#         solution= no1*no2 
        
#         return f" The Operatin is {math_operation} and their addition is {solution}"
        
    

# if __name__ == "__main__":
#     app.run(debug=True  ) 
    

 
 
 
 
# #  ========================================================================================================

# # the abouve opration is to long to write such code so we will do it in one functio nif possible 


# #  ======================================================================================================== 





# # <html>

# # <body>
# #   <form action="/operation" method="POST">
# #     <select id="operation" name="operation">
# #       <option value="add">add</option>
# #       <option value="sub">sub</option>
# #       <option value="mul">mul</option>
# #       <option value="div">div</option>
# #     </select>
# #     <input type="number" name="num1" id="num1" required>
# #     <input type="number" name="num2" id="num2" required>
# #     <button type="submit">Calculate</button>
# #   </form>
# # </body>

# # </html>