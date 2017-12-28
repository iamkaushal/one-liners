# -*- coding: utf-8 -*-
from flask import Flask
from oneliner import getOneLiner

app = Flask(__name__)

@app.route('/api')
def index():
    try:
        return getOneLiner()
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
