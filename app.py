# app.py
from flask import Flask, request, jsonify
from crud import create_travel_destination, get_destinations, update_destination, delete_destination
from weather import get_weather_data  # Para la integración con la API externa

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para obtener todos los destinos
@app.route('/destinations', methods=['GET'])
def get_all_destinations():
    destinations = get_destinations()
    return jsonify(destinations)

# Ruta para crear un nuevo destino
@app.route('/destination', methods=['POST'])
def add_destination():
    data = request.get_json()  # Obtener datos del cuerpo de la solicitud
    destination_id = create_travel_destination(data['name'], data['country'], data['description'])
    return jsonify({'id': destination_id}), 201  # Retorna el ID del nuevo destino

# Ruta para actualizar un destino existente
@app.route('/destination/<int:id>', methods=['PUT'])
def modify_destination(id):
    data = request.get_json()
    updated_destination = update_destination(id, data['name'], data['country'], data['description'])
    
    if updated_destination:
        return jsonify({
            'message': 'Updated successfully',
            'destination': {
                'id': updated_destination[0],
                'name': updated_destination[1],
                'country': updated_destination[2],
                'description': updated_destination[3]
            }
        }), 200
    else:
        return jsonify({'message': 'Destination not found'}), 404

# Ruta para eliminar un destino
@app.route('/destination/<int:id>', methods=['DELETE'])
def remove_destination(id):
    success = delete_destination(id)
    if success:
        return jsonify({'message': 'Deleted successfully'}), 200
    else:
        return jsonify({'message': 'Destination not found'}), 404

# Ruta para obtener información del clima de una ciudad (ejemplo con OpenWeather)
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    weather = get_weather_data(city)
    if weather:
        return jsonify(weather)
    return jsonify({'message': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    
  

@app.route('/weather/<string:city>', methods=['GET'])
def get_weather2(city):
    api_key = "your_openweather_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return jsonify(weather), 200
    else:
        return jsonify({"error": "Weather data not found"}), 404
        
        
# Endpoint para obtener destinos de viaje (ejemplo)
@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = [
        {'id': 1, 'name': 'Paris', 'country': 'France'},
        {'id': 2, 'name': 'New York', 'country': 'USA'},
        {'id': 3, 'name': 'Tokyo', 'country': 'Japan'}
    ]
    return jsonify(destinations)

