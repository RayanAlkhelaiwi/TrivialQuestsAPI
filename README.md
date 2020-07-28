# Trivia API
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-javascript](https://img.shields.io/badge/Made%20with-JavaScript-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

This is a Trivia API that provides trivial questions you can play and divided into categories.

The backend code follows [PEP-8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

### Getting Started
- Base URL: Currently this backend app can only be run locally. It's hosted by default at `127.0.0.1:5000` which is set as a proxy in the fronend configuration.

- Authentication: This version of the application does not require one, nor API keys.

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file.

To run the application, run the following commands inside the backend folder, but outside `flaskr` folder:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

**Frontend**

Inside the fontend folder, run the following commands to start the client:

```
npm install // Only once to install dependencies
npm start
```

By default, the frontend will run on `localhost:3000`.

**Tests**

To run tests, go to the backend folder and run the following commands:

```
dropdb trivia_api_test
createdb trivia_api_test
psql trivia_api_test < trivia.psql
python test_flaskr.py
```

Omit the `dropdb` command for the first time running the tests.

### Error Handling
Errors are returned as JSON obejcts in the following format:

```json
{
  "error": 404, 
  "message": "Not Found", 
  "success": false
}
```

The Error types the API returns when requests fail are:
| HTTP Status Code | Response |
| ----------- | ----------- |
| 400 | Bad Request |
| 404 | Not Found |
| 405 | Method Not Allowed |
| 422 | Unprocessable Entity |

### Endpoints
**GET /questions**

Returns a list of questions objects, success value and total number of questions. Results are paginated in groups of 10. Include a query argument to choose page number (e.g. `?page=1`).

* Sample Request:

```
curl -X GET http://127.0.0.1:5000/questions
```

* Sample Response:

```json
{
  "questions": [
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    },
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }
  ],
  "success": true,
  "total_questions": 25
}
```

**POST /questions**

Creates a new question by submitting the information for a question, answer, its category and difficulty. It returns the ID of the newely created question in the DB, the submitted information, success value, number of total questions.

* Sample Request:

```
curl -X POST -H "Content-Type: application/json" -d '{"question":"How are you?", "answer":"Fine", "category":"General", "difficulty":"2"}' http://127.0.0.1:5000/questions
```

* Sample Response:

```json
{
  "questions": {
    "questions": "How are you?",
    "answer": "Fine",
    "category": "General",
    "difficulty": 2
  },
  "created_question_id": 26,
  "success": true,
  "total_questions": 26
}
```

**DELETE /questions/{question_id}**

Deletes the question with the given ID. Returns the ID of the deleted question, success value, list of current questions, and current number of total questions.

* Sample Request:

```
curl -X DELETE http://127.0.0.1:5000/questions/26
```

* Sample Response:

```json
{
  "questions": [
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    },
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }, 
    {
      "question": "How are you?", 
      "answer": "Fine", 
      "category": "General", 
      "difficulty": 2
    }
  ],
  "deleted": 26,
  "success": true,
  "total_questions": 25
}
```
