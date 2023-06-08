from flask import Flask, jsonify, request
import uuid


app = Flask(__name__)
tasks = []


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'description': data['description'],
        'due_date': data['due_date'],
        'status': 'Incomplete'
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({'error': 'Task not found.'}), 404

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task['title'] = data.get('title', task['title'])
        task['description'] = data.get('description', task['description'])
        task['due_date'] = data.get('due_date', task['due_date'])
        task['status'] = data.get('status', task['status'])
        return jsonify(task), 200
    return jsonify({'error': 'Task not found.'}), 404

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message':'Task Deleted'}), 204
    return jsonify({'error': 'Task not found.'}), 404

@app.route('/tasks', methods=['GET'])
def list_tasks():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    start_index = (page - 1) * limit
    end_index = start_index + limit

    paginated_tasks = tasks[start_index:end_index]

    return jsonify(paginated_tasks), 200


if __name__ == '__main__':
    app.run()
