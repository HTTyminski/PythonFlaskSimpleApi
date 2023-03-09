from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
        {
            'id':1,
            'title':'Lord of the Ring',
            'author': 'Tolkien'
        },
        {
            'id':3,
            'title':'Harry Potter',
            'author': 'Howling'
        },
        {
            'id':3,
            'title':'James Clear',
            'author': 'Hábitos Atômicos'
        }
    ]

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>',methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)
    
@app.route('/books/<int:id>',methods=['PUT'])
def edit_book_by_id(id):
    edited_book = request.get_json()
    for indice,book in enumerate(books):
        if book.get('id') == id:
            books[indice].update(edited_book)
            return jsonify(books[indice])
        
@app.route('/books',methods=['POST'])
def include_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    for indice, book in enumerate(books):
        if book.get('id') == id:
            del books[indice]
            return jsonify(books)

app.run(
    port=5000,
    host='localhost',
    debug=True
)