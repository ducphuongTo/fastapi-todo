"""User services"""
from uuid import UUID
from services.auth_services import AuthService
from models.users import User
from schemas.users import UserModel, UserView, UserUpdateInformation
from services.exceptionService import ExceptionService
from sqlalchemy.orm import Session

class UserSerivce:
    """User services class"""
    def __init__(self):
        self.user_model = User
        self.exception_service = ExceptionService()
        self.auth_service = AuthService()

    def create_new_user(self, user: UserModel, db: Session) -> UserView | None:
        """Create User"""
        hashed_password = self.auth_service.get_password_hash(user.password)
        new_user = self.user_model(
            email=user.email,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=user.is_active,
            is_admin=user.is_admin,
            company_id=user.company_id,
            hashed_password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    def get_detail(self, id: UUID, db: Session):
        """get detail User"""
        user = db.query(self.user_model).filter(self.user_model == id).first()
        if not user:
            raise self.exception_service.NotFoundException(self.user_model)
    def get_all_users(self, db: Session):
        """Get All User"""
        return db.query(self.user_model).all()

    def update_user(self, user_request: UserUpdateInformation, id: UUID, db: Session) -> UserView:
        """Update User"""
        user = db.query(self.user_model).filter(self.user_model.user_id == id).first()
        if not user:
            raise self.exception_service.NotFoundException(self.user_model)

        user.first_name = user_request.first_name
        user.last_name = user_request.last_name
        user.is_active = user_request.is_active
        user.is_admin = user_request.is_admin
        user.company_id = user_request.company_id
        user.email = user_request.email
        user.username = user_request.username

        db.add(user)
        db.flush()
        db.commit()
        return user

    def delete_user(self, uuid: UUID, db: Session) -> None:
        """Delete User"""
        user = db.query(self.user_model).filter(self.user_model.user_id == uuid).first()
        if not user:
            raise self.exception_service.NotFoundException(self.user_model)
        db.delete(user)
        db.commit()
