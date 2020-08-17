
from flask import Flask
app = Flask(__name__)
@app.route("/")

def index():
    return "Hello world !"
    
def new_function():
    return 2 + 3

def new_function2():
    return new_function()
    
if __name__ == "__main__":
    app.run()

