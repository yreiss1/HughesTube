
from __future__ import print_function
from flask import Flask
from flask import render_template
from flask import request

import sys


app = Flask(__name__)


from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


@app.route('/', methods = ['GET'])
def render():
	return render_template('index.html')

@app.route('/results', methods = ['POST', 'GET'])
def results():
	text = request.form['search']
	print(request.form['search'], file = sys.stderr)
	result1 = es.search(index="hughes", doc_type='video', q="tags:" + text)
	return render_template("index.html",result = result1)


if __name__ == '__main__':
   app.run(debug = True)