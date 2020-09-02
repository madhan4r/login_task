from sqlalchemy.orm import Session
from datetime import datetime

from .model_login import UserCreate, UserUpdate
from .db_model_login import user_table
from fastapi.exceptions import HTTPException


def get_all(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(user_table).offset(skip).limit(limit).all()


def get_by_id(db_session: Session, user_id: int):
    user = db_session.query(user_table).filter(
        user_table.user_id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=400, detail='Requested user ID ' + str(user_id) + ' does not exist')
    return user


def create_user(db_session: Session, user_data: UserCreate):
    user = user_table(**user_data.dict(exclude_unset=True))
    # user.created_on = datetime.now()
    return save(db_session, user)


def update_user(db_session: Session,user_id: int, user_data: UserUpdate):
    user = get_by_id(db_session, user_data.user_id)
    user_update = user_data.dict(exclude_unset=True)
    for field in user_update:
        setattr(user, field, user_update[field])
        # setattr(user, 'modified_on', datetime.now())
    return save(db_session, user)


def save(db_session: Session, user: user_table):
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
