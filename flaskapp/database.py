import sqlalchemy.orm

engine = sqlalchemy.create_engine("sqlite:///flaskapp/database.db")

dbSession = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(autocommit = False, autoflush = False, bind = engine))

class Base(sqlalchemy.orm.DeclarativeBase):
    pass

Base.query = dbSession.query_property()

def initdb():
    Base.metadata.create_all(bind=engine)

