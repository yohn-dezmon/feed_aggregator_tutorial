from app import app
from flask_sqlalchemy import SQLAlchemy
# constructor, attach sqlalchemy to our app...
db = SQLAlchemy(app)
