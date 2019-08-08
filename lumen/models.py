from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Property(db.Model):  # type: ignore
    __tablename__ = "property"

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    address = db.Column(db.String(250), nullable=True)
