# this was in routes folder, named __init__.py

from flask import abort, redirect, request
from app import app

# The function defined within the decorator is called a handler
# we are passing the user's input into the form, through request.form to the other decorator
@app.route('/test', methods=['GET'])
def test_get():
    return '<form method="POST"><input name="username"></form>'

# in this decorator/handler the form content is being received via request.form.get(name)
@app.route('/test', methods=['POST'])
def test_post():
    # the second string is what would be submitted if the user didn't enter anything
    username = request.form.get('username', '???')
    return 'Hello ' + username
