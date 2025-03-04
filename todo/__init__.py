from flask import Flask 
import datetime
from .models import db
 
def create_app(): 
    app = Flask(__name__) 
     
    app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///db.sqlite"
    
    #Load themodels.
    from todo.models import db
    from todo.models.todo import Todo
    db.init_app(app)
    
    #Create thedatabasetables.
    with app.app_context():
        db.create_all()
        db.session.commit()
    #Register the blueprints.
    from todo.views.routes import api
    app.register_blueprint(api)
    
    return app