from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from Kubernetes! Pod name: {os.getenv('HOSTNAME', 'unknown')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
