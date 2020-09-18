from flask_restx import Api
from flask import Blueprint

from .main.controller.user import api as user_ns
from .main.controller.auth import api as auth_ns

blueprint = Blueprint('api', __name__)

"""
blueprint
"""
api = Api(blueprint,
          title='FLASK RESTFUL API BOILERPLATE WITH JWT',
          version='v.1.0',
          description='A boilerplate for flask restful api',
          license_url='http://vuongdq.com',
          terms_url='http://vuongdq.com',
          contact_email='quangvuong0805@gmail.com',
          contact_url='http://vuongdq.com')

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
