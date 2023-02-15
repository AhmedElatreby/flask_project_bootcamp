import sqlalchemy
import sqlalchemy.orm

from flaskapp.database import Base

class Movie(Base):
    __tablename__ = "movies"
    id = sqlalchemy.orm.mapped_column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.orm.mapped_column(sqlalchemy.Text)
    rating = sqlalchemy.orm.mapped_column(sqlalchemy.Integer)

