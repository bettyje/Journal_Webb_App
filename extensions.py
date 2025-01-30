from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize database
db = SQLAlchemy()

# Initialize migration
migrate = Migrate()
