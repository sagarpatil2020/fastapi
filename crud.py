from fastapi import FastAPI , status 
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2020},
    {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2021},
    {"id": 3, "title": "Book 3", "author": "Author 3", "year": 2022},
]

app = FastAPI()

@app.get('/books')
def read_books():
    return {"books": books}

@app.get('/books/{book_id}')
def read_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return {"book": book}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# this is the request body model for create book
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


class BaseBook(BaseModel):
    title: str
    author: str
    year: int

@app.put('/updatebook/{book_id}')
def update_book(book_id: int, base_book: BaseBook): # update book by id by passing two arguments book_id and base_book
    for book in books:
        if book['id'] == book_id: # check if book id exists in the list
            book["title"] = base_book.title 
            book["author"] = base_book.author
            book["year"] = base_book.year
            return {"Message": f"Book - {book['title']} - Updated Successfully"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete('/deletebook/{book_id}')
def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id: # check if book id exists in the list
            books.remove(book) # remove book from the list if book id exists
            return {"Message": f"Book - {book['title']} - Deleted Successfully"}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")