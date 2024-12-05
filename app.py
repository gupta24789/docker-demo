import os
import yaml
from flask import Flask
import logging

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=f'{LOG_DIR}/app.log',            
    level=logging.DEBUG,           
    format='%(asctime)s - %(levelname)s - %(message)s'
)

## Read config file
config = yaml.safe_load(open("config.yaml"))
USER_NAME_FROM_CONFIG_FILE = config['USER_NAME']
print(f"USER_NAME_FROM_CONFIG_FILE : {USER_NAME_FROM_CONFIG_FILE}")
logging.info(f"USER_NAME_FROM_CONFIG_FILE : {USER_NAME_FROM_CONFIG_FILE}")

## Get env variables
USER_NAME_FROM_ENV = os.getenv('USER_NAME')
print(f"USER_NAME_FROM_ENV : {USER_NAME_FROM_ENV}")
logging.info(f"USER_NAME_FROM_ENV : {USER_NAME_FROM_ENV}")

## creat app obj
app = Flask(__name__)


@app.route("/")
def get_message():
    greet_msg = "Welcome to Docker demo"
    return greet_msg

@app.route("/config")
def get_name_from_config():
    greet_msg = f"Welcome : {USER_NAME_FROM_CONFIG_FILE}"
    return greet_msg


@app.route("/config-env")
def get_name_from_env():
    greet_msg = f"Welcome : {USER_NAME_FROM_ENV}"
    return greet_msg


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)


