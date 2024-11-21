from flask import Flask
import logging
import threading
import time

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

@app.route('/')
def hello_world():
    app.logger.info("Hello, World! V1.0")
    return 'Hello, World! V1.0'

def log_hello_world():
    while True:
        app.logger.info("Hello, World! V1.0")
        time.sleep(20)

if __name__ == '__main__':
    # Start the logging thread
    threading.Thread(target=log_hello_world, daemon=True).start()
    app.run(host='0.0.0.0', port=4000)