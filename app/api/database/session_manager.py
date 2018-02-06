from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import all models so that create_all can find them.
import app.api.database.models
from app.api.database.models.Base import Base


class _SessionManagerState(object):
    session_maker = None


def new_session():
  return _SessionManagerState.session_maker()


def setup(database_uri):
  engine = create_engine(database_uri)
  _SessionManagerState.session_maker = sessionmaker(bind=engine)
  Base.metadata.create_all(engine)
