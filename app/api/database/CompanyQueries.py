from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.CompanyModel import Company

def create_company(db, body):
  name = body['name']
  website = body['website']
  company = Company(name, website)

  try:
    db.add(company)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def edit_company(db, body):
  company_id = body.pop('company_id')
  q = db.query(Company).filter(Company.id == company_id).first()
  try:
    for key, value in body.items():
      setattr(q, key, value)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def delete_company(db, body):
  try:
    db.query(Company).filter(Company.id == body['company_id']).delete()
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def get_company_filtered(db, filters, user_id):
  q = db.query(Company)

  for key, value in filters.items():
    if key == 'user_id' and int(value) != int(user_id):
        print('User id: ', user_id)
        print('Value: ', value)
        return False
    q = q.filter(getattr(Company, key) == value)
  return q

def get_company(db, company_id):
  return db.query(Company).filter(Company.id == company_id).first()


