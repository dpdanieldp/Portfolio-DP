# Flask settings
FLASK_SERVER_NAME = "localhost:8888"
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restx settings
RESTX_SWAGGER_UI_DOC_EXPANSION = "list"
RESTX_VALIDATE = True
RESTX_MASK_SWAGGER = False
RESTX_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = "sqlite:///Mydatabase.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True
DB_NAME = "Mydatabase.db"
