from flask import Flask, jsonify, request


app = Flask(__name__)

names = [
    {'id':1, 'nome':"marcos"},
    {'id':2, 'nome':"João"},
    {'id':3, 'nome':"Maria"}
]


@app.route('/names', methods=['GET'])
def get_names():
    return jsonify(names), 200


@app.route('/nomes/<int:id>', methods=['GET'])
def get_namess(id):

    name = next((name for name in names if name['id'] == id), None)

    if name is not None:
        return jsonify(name), 200
    else:
        return jsonify({'error':'name not found'}), 404
    
        

@app.route('/nomes/c/<string:nome>', methods=['GET'])

def get_nomee(nome):

    print(nome)

    nome = next((item for item in names if item['nome'].lower() == nome.lower()), None)

    if nome is not None:
        return jsonify(nome), 200
    else:
        return jsonify({'error':'name not found'}), 404

if __name__=='__main__':
    app.run(debug=True)
