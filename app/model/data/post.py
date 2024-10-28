from model.data.BaseData import *

class Post(db.Model, BaseData):
    
    title = db.Column(db.Text, unique=False)
    info = db.Column(db.Text, unique=False)
    images = db.relationship('model.data.image.Image', backref='post')
    
    def __init__(self, 
                 title:str, info:str):
        self.title = title
        self.info = info
        db.Model.__init__(self)
        BaseData.__init__(self, self.id)

    # @classmethod
    # def getLastPost(cls):
    #     last_post = cls.getLast()
    #     if last_post is None: last_post = {}
    #     print(last_post)
    #     return last_post