from fastapi import FastAPI
from pydantic import BaseModel

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2020},
    {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2021},
    {"id": 3, "title": "Book 3", "author": "Author 3", "year": 2022},
]


app = FastAPI()

@app.get('/books')
def read_books():
    return {"books": books}


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post('/createbook')
def read_book(book: Book):
    new_book = book.model_dump() # model_dump() function convert pydantic model to dict 
    books.append(new_book) 
    return {"Message": f"Book - {new_book['title']} - Created Successfully"}
