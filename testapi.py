from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello class'

if __name__=='__main__':
    app.run(debug=True)