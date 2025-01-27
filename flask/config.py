class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # SQLite
    # Example for other databases:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@localhost/dbname'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/dbname'

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking for performance
