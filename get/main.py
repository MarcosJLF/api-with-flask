from flask import Flask, jsonify, request


app = Flask(__name__)

names = [
    {'id':1, 'nome':"marcos júnior lemes ferreira"},
    {'id':2, 'nome':"João"}
]


@app.route('/names', methods=['GET'])
def get_names():
    return jsonify(names)




if __name__=='__main__':
    app.run(debug=True)