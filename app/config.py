import os

class Config: 
  '''
  General configuration class
  '''
  SECRET_KEY = 'Thisissupposedtobesecret!'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/pitcher'
  

 
  
  # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
  # simple mde  configurations
  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

class ProdConfig(Config): 
  '''
  Production configuration child class
  
  Args: 
      Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql://ajfrkcvrvgwhpp:d7b2dfa61f57de50398389e166e9cac28d53e8ced7a0173c1c4baf942cdf0797@ec2-52-45-238-24.compute-1.amazonaws.com:5432/dfpb29pernlhum'

class TestConfig(Config): 
 pass

class DevConfig(Config): 
  '''
  Development configuration child class
  
  Args: 
      Config: The parent configuration class with General configuration settings
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:malcomiz0582@localhost/pitcher'
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production': ProdConfig,
  'test':TestConfig
}