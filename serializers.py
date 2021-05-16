from flask_marshmallow import Marshmallow
from app import app


ma = Marshmallow(app)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name', 'age')
