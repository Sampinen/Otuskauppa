from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv
load_dotenv()


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost"
db = SQLAlchemy(app)
app.secret_key =getenv("SECRET_KEY")
#meta = sql.MetaData()