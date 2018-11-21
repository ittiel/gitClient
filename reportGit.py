import requests
import logging
import subprocess
import json
import time

WAIT = 60

# get the local git data and formalize it
def get_local_git_data():
    # todo: consider using gitpython

    data = {}
    data['user'] = subprocess.check_output(["git", "config", "user.name"])
    data['branch'] = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    data['repository'] = subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
    data['files'] = subprocess.check_output(["git", "diff", "--name-only"])
    data['diff'] = subprocess.check_output(["git", "diff"])
    data['commitMsg'] =subprocess.check_output(["git", "log", "--format=%B", "-n", "1"])

    return json.dumps(data)

# send json to server
def send_to_server(data_json):
    # todo: get server host and port from external configuration (Consul?)
    server = 'http://localhost:5000/backend'

    logging.info (data_json)
    response = requests.post(server, data=data_json, headers={'Content-Type': 'application/json'})
    return response

# todo: get repository as parameter
# todo: get time as parameter
# repeat every 1 minutes
if __name__ == "__main__":

    logging.basicConfig(filename='client.log', level=logging.INFO)
    while True:

        try:
            data_json = get_local_git_data()
            res = send_to_server(data_json)
            time.sleep(WAIT)
        except:
            logging.exception('')
