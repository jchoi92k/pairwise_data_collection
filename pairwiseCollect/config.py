import json


# with open('/etc/config.json') as config_file:
#     config = json.load(config_file)


class Config:
    SECRET_KEY = 'SEC'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///pairwise.db"
    MAX_CONTENT_LENGTH = 2 * 1000 * 1000
