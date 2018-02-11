from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.ReviewModel import Review

def create_review(db, body):
  user_id = body['user_id']
  school_id = body['school_id']
  job_id = body['job_id']
  job_type = body['job_type']
  duration = body['duration']
  location = body['location']
  salary = body['salary']
  ratings = body['ratings']
  min_visible = body['min_visible']
  show_immediate = body['show_immediate']

  company_id = body['company_id']
  review_text = body['review_text']

  review = Review(user_id,
                  school_id,
                  job_id,
                  job_type,
                  company_id,
                  duration,
                  location,
                  salary,
                  ratings,
                  min_visible,
                  show_immediate,
                  review_text)

  try:
    db.add(review)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def edit_review(db, body, review_id):
  q = db.query(Review).filter(Review.id == review_id).first()
  try:
    for key, value in body.items():
      setattr(q, key, value)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def delete_review(db, body):
  try:
    db.query(Review).filter(Review.id == body['review_id']).delete()
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def get_review_filtered(db, filters, user_id):
  q = db.query(Review).filter(Review.user_id == user_id)

  for key, value in filters.items():
    if key == 'user_id' and int(value) != int(user_id):
        print('User id: ', user_id)
        print('Value: ', value)
        return False
    q = q.filter(getattr(Review, key) == value)
  return q.all()

def get_review(db, review_id):
  return db.query(Review).filter(Review.id == review_id).first()


