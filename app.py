from  flask import Flask 

app = Flask(__name__)

@app.route('/')
def Home():
    return (
        '<h1> Flask Project  new</h1>'
    )

if __name__  == '__main__':
    app.run(debug=True)