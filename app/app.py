######################################################
# 
# Libraries
#
######################################################

from flask import Flask
from flask import request
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask_paginate import Pagination, get_page_args


######################################################
# 
# App instance
#
######################################################

app = Flask(__name__)


######################################################
# 
# Routes
#
######################################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/paginate')
def search_results():        
    search_results = [1] * 100
            
    # automatic pagination handling
    total = len(search_results)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')

    return render_template('paginate.html',
                            search_results=search_results[offset: offset + per_page],
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            len=len)


######################################################
# 
# Run app
#
######################################################

if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True, threaded=True)
