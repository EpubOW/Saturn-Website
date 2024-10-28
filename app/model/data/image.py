from model.data.BaseData import *

class Image(db.Model, BaseData):
    
    
    data = db.Column(db.Text, unique=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    def __init__(self, *args, **kwargs):
        db.Model.__init__(self, *args, **kwargs)
        BaseData.__init__(self, self.id)