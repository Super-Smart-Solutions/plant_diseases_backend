from sqladmin import ModelView

from planet_diseases_backend.db.models.users import User


class UserAdmin(ModelView, model=User):
    column_list = [User.email, User.is_active, User.is_verified, User.is_superuser]
