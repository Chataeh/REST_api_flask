from db import db

class ItemModel(db.Model): #상속 받음
    __tablename__ = "items" #테이블 생성

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique =True, nullable=False)
    description = db.Column(db.String)
    price =db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),unique=False, nullable=False)#외래키
    store = db.relationship("StoreModel", back_populates="items")
    tags=db.relationship("TagModel", back_populates="items",secondary="items_tags")