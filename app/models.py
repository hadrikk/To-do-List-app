#database ke columns yaha banyege


from app import db  #yeh db.alchemy ko layega is file mai

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(20), default = "Pending") 