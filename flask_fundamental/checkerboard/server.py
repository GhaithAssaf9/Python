from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', across = 8, down = 8)

@app.route('/<n>')
def callDown(n):
    return render_template('index.html', across = 8, down = int(n))

@app.route('/<n1>/<n2>')
def acrossDown(n1,n2):
    return render_template('index.html', across = int(n1), down = int(n2) )

@app.route('/<n1>/<n2>/<color1>/<color2>')
def hellaColors(n1, n2, color1, color2):
    return render_template('index.html', across = int(n1), down = int(n2), color1= color1, color2 = color2)


if __name__ == "__main__":
    app.run(debug=True)