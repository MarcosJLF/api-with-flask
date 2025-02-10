from flask import Flask, jsonify, request

app = Flask(__name__)

car = [
    {'id':1, 'modelo':"Fusca", 'ano':1970},
    {'id':2, 'modelo':"Gol", 'ano':2000},
    {'id':3, 'modelo':"Palio", 'ano':2005}
]

send = [
    {"Status":"Sucesso"}
]

@app.route('/carros', methods=['Post'])

def post_car():

    try:
        new_car = request.get_json()
        car.append(new_car)
        return jsonify(car), 201

    
    except e as e:
        return jsonify({'error':str(e)}), 500
    
@app.route('/carros/e', methods=['Post'])

def post_car_e():

    try:
        new_car = request.get_json()

        err = next((item for item in car if item['modelo'].lower() == new_car['modelo'].lower()), None)

        if err is not None:
            return jsonify({'error':'carro já cadastrado'}), 404
        else:
            car.append(new_car)
            return jsonify(car), 201
    except Exception as e:
        return jsonify({'error':str(e)}), 500

if __name__=='__main__':
    app.run(debug=True)