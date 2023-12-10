 # if we want to return result in html page  ,then we have to render html file and we can see the result on api in html format 
 
from flask import Flask , request , render_template 

app= Flask(__name__) 

@app.route("/")
def math():
    return render_template("index.html") 
@app.route("/operation", methods=["POST"])
def demo():
    if request.method == "POST":
        operation = request.form["operation"]
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        print(f"Operation: {operation}, Num1: {num1}, Num2: {num2}")

        result = 0

        if operation == "add":
            result = int(num1) + int(num2)
        elif operation == "sub":
            result = int(num1) - int(num2)
        elif operation == "mul":
            result = int(num1) * int(num2)
        elif operation == "div":
            result = int(num1) / int(num2)

        return render_template("result.html", result=result)




if __name__== "__main__":
    app.run(debug=True)