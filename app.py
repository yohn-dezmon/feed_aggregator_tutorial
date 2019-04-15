from flask import Flask

app = Flask(__name__)

# tells SQLAlchemy how to connect to our DB.
db_uri = 'mysql+pymysql://root:jesmonddohn@localhost/feedreader'

# the flask sql alchemy modeule will pull this db uri string so it knows how to connect.
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

# instantiate sqlalchemy object
