from math import e
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Depends, Response, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import models
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
router_v1 = APIRouter(prefix='/api/v1')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils

@router_v1.get('/students')
async def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router_v1.get('/students/{student_id}')
async def get_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

@router_v1.post('/students')
async def create_student(student: dict, response: Response, db: Session = Depends(get_db)):
    newstudent = models.Student(firstname=student['firstname'], lastname=student['lastname'], birth_day=student['birth_day'], age=student['age'], sex=student['sex'])
    db.add(newstudent)
    db.commit()
    db.refresh(newstudent)
    response.status_code = 201
    return newstudent

@router_v1.put('/students/{student_id}')
async def update_student(student_id: int, response: Response, student: dict, db: Session = Depends(get_db)):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if db_student:
        db_student.firstname = student['firstname']
        db_student.lastname = student['lastname']
        db_student.birth_day = student['birth_day']
        db_student.age = student['age']
        db_student.sex = student['sex']
        db.commit()
        db.refresh(db_student)
        return {
            'message': f'Student {student_id} updated successfully'
        }
    else:
        response.status_code = 404
        return {
            'message': f'Student {student_id} not found'
        }
        
@router_v1.delete('/students/{student_id}')
async def delete_student(student_id: int, response: Response, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return {
            'message': f'Student deleted {student_id} successfully'
        }
    else:
        response.status_code = 404
        return {
            'message': f'Student {student_id} not found'
        }




# Book 
@router_v1.get('/books')
async def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router_v1.get('/books/{book_id}')
async def get_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

@router_v1.post('/books')
async def create_book(book: dict, response: Response, db: Session = Depends(get_db)):
    # TODO: Add validation
    newbook = models.Book(title=book['title'], author=book['author'], year=book['year'], is_published=book['is_published'], details=book['details'], short_details=book['short_details'], genre=book['genre'])
    db.add(newbook)
    db.commit()
    db.refresh(newbook)
    response.status_code = 201
    return newbook

@router_v1.patch('/books/{book_id}')
async def update_book(book_id: int, book: dict, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.title = book['title']
        db_book.author = book['author']
        db_book.year = book['year']
        db_book.is_published = book['is_published']
        db_book.details = book['details']
        db_book.short_details = book['short_details']
        db_book.genre = book['genre']
        db.commit()
        db.refresh(db_book)
        return db_book
    else:
        return {
            'message': f'Book {book_id} not found'
        }

@router_v1.delete('/books/{book_id}')
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {
            'message': f'Book deleted {book_id} successfully'
        }
    else:
        return {
            'message': f'Book {book_id} not found'
        }

@router_v1.get('/coffee')
async def get_coffees(db: Session = Depends(get_db)):
    return db.query(models.Coffee).all()

@router_v1.get('/coffee/{coffee_id}')
async def get_coffee(coffee_id: int, db: Session = Depends(get_db)):
    return db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()

@router_v1.post('/coffee')
async def create_coffee(coffee: dict, response: Response, db: Session = Depends(get_db)):
    newcoffee = models.Coffee(name=coffee['name'], des=coffee['des'], price=coffee['price'], available=coffee['available'])
    db.add(newcoffee)
    db.commit()
    db.refresh(newcoffee)
    response.status_code = 201
    return newcoffee

@router_v1.patch('/coffee/{coffee_id}')
async def update_coffee(coffee_id: int, coffee: dict, db: Session = Depends(get_db)):
    db_coffee = db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()
    if db_coffee:
        db_coffee.name = coffee['name']
        db_coffee.des = coffee['des']
        db_coffee.price = coffee['price']
        db_coffee.available = coffee['available']
        db.commit()
        db.refresh(db_coffee)
        return db_coffee
    else:
        return {
            'message': f'Coffee {coffee_id} not found'
        }
@router_v1.delete('/coffee/{coffee_id}')
async def delete_coffee(coffee_id: int, db: Session = Depends(get_db)):
    coffee = db.query(models.Coffee).filter(models.Coffee.id == coffee_id).first()
    if coffee:
        db.delete(coffee)
        db.commit()
        return {
            'message': f'Coffee deleted {coffee_id} successfully'
        }
    else:
        return {
            'message': f'Coffee {coffee_id} not found'
        }

@router_v1.get('/order')
async def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router_v1.get('/order/{order_id}')
async def get_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

@router_v1.post('/order')
async def create_order(order: dict, response: Response, db: Session = Depends(get_db)):
    neworder = models.Order(coffee_id=order['coffee_id'], order_date=order['order_date'], amount=order['amount'], total_price=order['total_price'], notes=order['notes'])
    db.add(neworder)
    db.commit()
    db.refresh(neworder)
    response.status_code = 201
    return neworder

@router_v1.patch('/order/{order_id}')
async def update_order(order_id: int, order: dict, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        db_order.coffee_id = order['coffee_id']
        db_order.order_date = order['order_date']
        db_order.amount = order['amount']
        db_order.total_price = order['total_price']
        db_order.notes = order['notes']
        db.commit()
        db.refresh(db_order)
        return db_order
    else:
        return {
            'message': f'Order {order_id} not found'
        }
@router_v1.delete('/order/{order_id}')
async def delete_order(order_id: int, db: Session = Depends(get_db)):       
    order = db.query(models.Order).filter(models.Order.id == order_id).first()          
    if order:          
        db.delete(order)          
        db.commit()          
        return {          
            'message': f'Order deleted {order_id} successfully'          
        }          
    else:          
        return {          
            'message': f'Order {order_id} not found'          
        }

app.include_router(router_v1)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)