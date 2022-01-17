from db_models import *
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, fields


class users_schema(SQLAlchemySchema):
    class Meta:
        model = users

    id =auto_field()
    full_name = auto_field()
    email = auto_field()
    city = auto_field()

