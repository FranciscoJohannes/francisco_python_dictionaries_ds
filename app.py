from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message="Hello, World!")

# class for product dictionary
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price



if __name__ == '__main__':
    app.run(debug=True)