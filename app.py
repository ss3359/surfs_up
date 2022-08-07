from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    for n in range(1, 10): 
        if n % 2 == 0: 
            print("Guten Tag") 
        elif n % 2 == 0: 
            print("Buneas Tardes")    
    



