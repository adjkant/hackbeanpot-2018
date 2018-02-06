import unittest

from app.api.database import session_manager
from app.api.database.models.Base import Base
from run import app


class TestBase(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    session_manager.setup('sqlite:///app/tests/test_db.db')

  def setUp(self):
    self.app = app.test_client()
    db = session_manager.new_session()

    # Delete all tables in the db
    for table in Base.metadata.sorted_tables:
      db.execute(table.delete())

    db.commit()
