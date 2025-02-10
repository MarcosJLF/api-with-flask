from flask import Flask, jsonify, request

app = Flask(__name__)


names :dict = [
    {'id':1, 'nome':"marcos"},
    {'id':2, 'nome':"João"},
    {'id':3, 'nome':"Maria"}
]

@app.route('/names/<int:nome>',methods=['PUT'])
def put_names(nome):

    id = nome

    name = next((item for item in names if item['id'] == id), None)

    if name is not None:
        names.remove('id')
        updated_data = request.get_json()
        name.update(updated_data)
        return jsonify(names), 200
    else:
        return jsonify({'error':'name not found'}), 404


if __name__=='__main__':
    app.run(debug=True)




#     @app.route('/books/<int:book_id>', methods=['PUT'])
# def update_book(book_id):
#     book = next((book for book in books if book['id'] == book_id), None)
#     if book is not None:
#         updated_data = request.get_json()
#         book.update(updated_data)
#         return jsonify(book)
#     else:
#         return jsonify({'error': 'Book not found'}), 404