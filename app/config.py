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
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config): 
 pass

class DevConfig(Config): 
  '''
  Development configuration child class
  
  Args: 
      Config: The parent configuration class with General configuration settings
  '''
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production': ProdConfig,
  'test':TestConfig
}