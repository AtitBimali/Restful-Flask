# Restful-Flask


A brief description of the API endpoints.

Base URL: ```/tasks ```
### API Documentation: - [Postman Link](https://documenter.getpostman.com/view/25025161/2s93saat5m)


## Installation

Install the requirements with pip

```bash
pip install -r requirements.txt
```

## Running the server

```bash
python3 app.py
```

    
## API Reference

#### Get all Tasks
```http
  GET /tasks
```

#### Get single task

```http
  GET /tasks/{{task_id}}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_id`      | `uuid` | **Required**. Id of task to fetch |


#### Update single task

```http
  PUT /tasks/{{task_id}}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_id`      | `uuid` | **Required**. Id of task to Update |

#### Delete single task

```http
  DELETE /tasks/{{task_id}}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `task_id`      | `uuid` | **Required**. Id of task to delete |

#### Get Tasks With Pagination

```http
  GET /tasks/?page=2&limit=2&type=latest
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page`      | `integer` | **Required**. Page number to fetch |
| `limit`      | `integer` | **Required**. Number of tasks to fetch per page |


## Frameworks Used

 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)


