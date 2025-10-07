#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, redirect, request
import pyshorteners
import logging
from logging import Formatter, FileHandler
from wtforms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=="POST":
        url_received = request.form["url"]
        short_url = pyshorteners.Shortener().tinyurl.short(url_received)
        return render_template("pages/home.html", new_url=short_url, old_url=url_received)
    else:
        return render_template('pages/home.html')

@app.route('/donate', methods=["GET"])
def donate_link():
    return redirect('https://www.buymeacoffee.com/techdadteddy', code=302)

@app.route('/github', methods=["GET"])
def github_link():
    return redirect('https://github.com/tedleyem?tab=repositories', code=302)

# Error handlers.
@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
