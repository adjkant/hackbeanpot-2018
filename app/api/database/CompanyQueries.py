from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.CompanyModel import Company

def create_company(db, body):
  name = body['name']
  website = body['website'] if 'website' in body else None
  company = Company(name, website=website)

  try:
    db.add(company)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return company.id

def edit_company(db, body, company_id):
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
      return False
    q = q.filter(getattr(Company, key) == value)
  return q.all()

def get_by_name(db, name):
  return db.query(Company).filter(Company.name == name).first()

def get_company(db, company_id):
  return db.query(Company).filter(Company.id == company_id).first()

def get_name_like(db, name):
  return db.query(Company).filter(Company.name.like(name)).all()
