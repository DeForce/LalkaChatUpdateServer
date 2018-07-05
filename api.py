import collections
import json
import os
import re

import flask
from flask import Flask

RELEASE_DIR = '/releases'
VERSION_REGEXP = r'LalkaChat-(.*)-(.*).zip'
BASE_URL = 'http://czt.lv/lalkachat/'

app = Flask(__name__)


def gen_chat_data(item):
    return {
        'url': '{}{}'.format(BASE_URL, item)
    }


def get_chat_versions():
    versions = collections.defaultdict(dict)
    for item in os.listdir(RELEASE_DIR):
        re_item = re.search(VERSION_REGEXP, item)
        if re_item:
            branch, release_number = re_item.groups()
            versions[branch][release_number] = gen_chat_data(item)
    return versions


@app.route('/list')
def list_chats():
    req = flask.request
    if req.method == 'GET':
        return json.dumps(get_chat_versions())


@app.route('/')
def index():
    return 'get out'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
