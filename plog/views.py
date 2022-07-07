from flask import render_template

from plog import app
from plog.db.database_operations import get_parking_as_dict


@app.route("/")
def index():
    data = get_parking_as_dict()
    return render_template('index.html', result=data)