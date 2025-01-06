# app.py
import os
from flask import Flask, request, jsonify
from crud import create_travel_destination, get_destinations, update_destination, delete_destination
from weather import get_weather_data  # Para la integración con la API externa

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta para obtener todos los destinos
@app.route('/destinations', methods=['GET'])
def get_all_destinations():
    try:
        destinations = get_destinations()
        return jsonify(destinations)
    except Exception as e:
        return jsonify({'message': f'Error retrieving destinations: {str(e)}'}), 500

# Ruta para crear un nuevo destino
@app.route('/destination', methods=['POST'])
def add_destination():
    data = request.get_json()  # Obtener datos del cuerpo de la solicitud
    try:
        destination_id = create_travel_destination(data['name'], data['country'], data['description'])
        return jsonify({'id': destination_id}), 201  # Retorna el ID del nuevo destino
    except Exception as e:
        return jsonify({'message': f'Error adding destination: {str(e)}'}), 500

# Ruta para actualizar un destino existente
@app.route('/destination/<int:id>', methods=['PUT'])
def modify_destination(id):
    data = request.get_json()
    try:
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
    except Exception as e:
        return jsonify({'message': f'Error updating destination: {str(e)}'}), 500

# Ruta para eliminar un destino
@app.route('/destination/<int:id>', methods=['DELETE'])
def remove_destination(id):
    try:
        success = delete_destination(id)
        if success:
            return jsonify({'message': 'Deleted successfully'}), 200
        else:
            return jsonify({'message': 'Destination not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error deleting destination: {str(e)}'}), 500

# Ruta para obtener información del clima de una ciudad (ejemplo con OpenWeather)
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    try:
        weather = get_weather_data(city)
        if weather:
            return jsonify(weather)
        return jsonify({'message': 'City not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error retrieving weather data: {str(e)}'}), 500

if __name__ == '__main__':
    # Usar el puerto proporcionado por Render, o 5000 como valor por defecto
    port = int(os.environ.get("PORT", 5000))  
    # Ejecutar la app en todas las interfaces de red (0.0.0.0) y en el puerto adecuado
    app.run(host="0.0.0.0", port=port, debug=True)
    
