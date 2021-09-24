from models import db, Cupcake
from app import app

db.drop_all()
db.create_all()

pic1 = 'https://images.unsplash.com/photo-1576618148400-f54bed99fcfd'

c1 = Cupcake(flavor='chocolate', size='small', rating=4/5, image=pic1)
c2 = Cupcake(flavor='vanilla', size='med', rating=5/5)
c3 = Cupcake(flavor='mint', size='med', rating=4/5)
c4 = Cupcake(flavor='peanut butter', size='large', rating=3/5)
c5 = Cupcake(flavor='strawberry', size='x-large', rating=4/5)
c6 = Cupcake(flavor='banana', size='xx-large', rating=2/5)

db.session.add_all([c1, c2, c3, c4, c5, c6])
db.session.commit()