from flask import Flask, request, jsonify
from flask_cors import CORS
import models

app = Flask(__name__)
CORS(app)

# Initialize DB table
models.create_table()

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = models.get_todos()
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    title = data.get('title')
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    models.add_todo(title)
    return jsonify({'message': 'Todo added successfully'}), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    completed = data.get('completed', False)
    models.update_todo(todo_id, completed)
    return jsonify({'message': 'Todo updated successfully'})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    models.delete_todo(todo_id)
    return jsonify({'message': 'Todo deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
