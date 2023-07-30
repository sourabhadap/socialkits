from app import flaskapp

flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/meeting_scheduler'