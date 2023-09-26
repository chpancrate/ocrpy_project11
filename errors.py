from flask import render_template
from server import app


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    custom_message = error.description
    return render_template('500.html', custom_message=custom_message), 500
