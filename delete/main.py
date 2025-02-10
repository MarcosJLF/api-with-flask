from flask import Flask, jsonify, request

app = Flask(__name__)

books:dict = [ 
    {'id': 1, 'title': '1984', 'author': 'George Orwell'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 3, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'}
]

# @app. route('/nomes/<int:nd>',methods=['DELETE'])
# def delete_nome(nd):
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify(books), 200

    
#     name = next((item for item in nomes if item['id'] == nd), None)

#     if name is not None:
#         nomes.remove('id')
#         return jsonify({'message':'name deleted'}), 200
#     else:
#         return jsonify({'error':'name not found'}), 404


if __name__=='__main__':
    app.run(debug=True)


