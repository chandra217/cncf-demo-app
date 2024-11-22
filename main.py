from flask import Flask
import logging
import threading
import time

app = Flask(__name__)

version = "1.1"

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

@app.route('/')
def hello_world():
    app.logger.info("Hello, World! V"+version)
    return ('Hello, World! V'+version)

def log_hello_world():
    while True:
        app.logger.info("Hello, World! V"+version)
        time.sleep(20)

if __name__ == '__main__':
    # Start the logging thread
    threading.Thread(target=log_hello_world, daemon=True).start()
    app.run(host='0.0.0.0', port=4000)