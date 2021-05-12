from flask import Flask  ,render_template
app = Flask(__name__)    
@app.route('/')         
def hello_world():
    return 'Hello World!'

@app.route('/Dojo')   
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def name(name):
    return "hi, " + name 

@app.route('/repeat/<num>/<string>')          
def repeat(num,string):
    return render_template("index.html",num=int(num),string=string)
    





if __name__=="__main__":  
    app.run(debug=True)