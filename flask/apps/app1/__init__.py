from flask import Blueprint

# Create a blueprint for app1
app1_blueprint = Blueprint('app1', __name__)

# Import routes to register them
from . import routes
