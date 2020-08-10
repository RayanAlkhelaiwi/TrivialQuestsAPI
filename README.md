# Trivial Quests - Trivia API
[![made-with-python](https://img.shields.io/badge/Backend-Python-1F425F.svg)](https://www.python.org/)
[![made-with-reactjs](https://img.shields.io/badge/Frontend-ReactJS-06B3E1.svg)](https://reactjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-Green.svg)](https://opensource.org/licenses/MIT)

A backend API with a React frontend that provides categorized trivia questions you can answer.

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
  "categories": [
    {
      "id": 1, 
      "type": "Sports"
    }, 
    {
      "id": 2, 
      "type": "Technology"
    }, 
    {
      "id": 3, 
      "type": "Movies"
    }, 
    {
      "id": 4, 
      "type": "Food"
    }, 
    {
      "id": 5, 
      "type": "General"
    }, 
    {
      "id": 6, 
      "type": "Music"
    }, 
    {
      "id": 7, 
      "type": "Video-Games"
    }, 
    {
      "id": 8, 
      "type": "Geography"
    }, 
    {
      "id": 9, 
      "type": "Science"
    }
  ], 
  "questions": [
    {
      "answer": "11", 
      "category": "Sports", 
      "difficulty": 3, 
      "id": 1, 
      "question": "How many players are in a soccer team?"
    }, 
    {
      "answer": "Avengers: Endgame", 
      "category": "Movies", 
      "difficulty": 2, 
      "id": 2, 
      "question": "What is the highest-grossing film of all time without taking inflation into account?"
    }, 
    {
      "answer": "Simple Mail Transport Protocol", 
      "category": "Technology", 
      "difficulty": 3, 
      "id": 3, 
      "question": "What does the acronym SMTP represent?"
    }, 
    {
      "answer": "Neil Armstrong", 
      "category": "General", 
      "difficulty": 2, 
      "id": 4, 
      "question": "Who was the first American astronaut to step foot on the moon?"
    }, 
    {
      "answer": "Carrot", 
      "category": "Food", 
      "difficulty": 1, 
      "id": 5, 
      "question": "What vegetable is known to help you see in the dark?"
    }, 
    {
      "answer": "Bill Gates", 
      "category": "Technology", 
      "difficulty": 1, 
      "id": 6, 
      "question": "Who founded Microsoft?"
    }, 
    {
      "answer": "Chinese", 
      "category": "General", 
      "difficulty": 2, 
      "id": 7, 
      "question": "What language is the most popularly spoken worldwide?"
    }, 
    {
      "answer": "Chickpeas", 
      "category": "Food", 
      "difficulty": 3, 
      "id": 8, 
      "question": "What is hummus made from?"
    }, 
    {
      "answer": "Chile", 
      "category": "Geography", 
      "difficulty": 3, 
      "id": 9, 
      "question": "Which country occupies half of South America\u2019s western coast?"
    }, 
    {
      "answer": "9", 
      "category": "Sports", 
      "difficulty": 2, 
      "id": 10, 
      "question": "How many players are there on a baseball team?"
    }
  ], 
  "success": true, 
  "total_questions": 25
}
```

**GET /categories**

Returns a list of categories objects, success value and total number of categories. Results are paginated in groups of 10. Include a query argument to choose page number (e.g. `?page=1`).

* Sample Request:

```
curl -X GET http://127.0.0.1:5000/categories
```

* Sample Response:

```json
{
  "categories": [
    {
      "id": 1,
      "type": "Sports"
    },
    {
      "id": 2,
      "type": "Technology"
    },
    {
      "id": 3,
      "type": "Movies"
    },
    {
      "id": 4,
      "type": "Food"
    },
    {
      "id": 5,
      "type": "General"
    },
    {
      "id": 6,
      "type": "Music"
    },
    {
      "id": 7,
      "type": "Video-Games"
    },
    {
      "id": 8,
      "type": "Geography"
    },
    {
      "id": 9,
      "type": "Science"
    }
  ],
  "success": true,
  "total_categories": 9
}
```

**POST /questions**

Creates a new question by submitting the information for a question, answer, its category and difficulty. It returns the ID of the newely created question in the DB, the submitted information, success value, number of total questions.

* Sample Request:

```
curl -X POST -H "Content-Type: application/json" -d '{"question":"What 1994 crime film revitalized John Travolta’s career?", "answer":"Pulp Fiction", "category":"Movies", "difficulty":"3"}' http://127.0.0.1:5000/questions
```

* Sample Response:

```json
{
  "created_question_id": 26,
  "questions": {
    "answer": "Pulp Fiction",
    "category": "Movies",
    "difficulty": 3,
    "id": 26,
    "question": "What 1994 crime film revitalized John Travolta\u2019s career?"
  },
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
  "deleted": 26,
  "questions": [
    {
      "answer": "11", 
      "category": "Sports", 
      "difficulty": 3, 
      "id": 1, 
      "question": "How many players are in a soccer team?"
    }, 
    {
      "answer": "Avengers: Endgame", 
      "category": "Movies", 
      "difficulty": 2, 
      "id": 2, 
      "question": "What is the highest-grossing film of all time without taking inflation into account?"
    }, 
    {
      "answer": "Simple Mail Transport Protocol", 
      "category": "Technology", 
      "difficulty": 3, 
      "id": 3, 
      "question": "What does the acronym SMTP represent?"
    }, 
    {
      "answer": "Neil Armstrong", 
      "category": "General", 
      "difficulty": 2, 
      "id": 4, 
      "question": "Who was the first American astronaut to step foot on the moon?"
    }, 
    {
      "answer": "Carrot", 
      "category": "Food", 
      "difficulty": 1, 
      "id": 5, 
      "question": "What vegetable is known to help you see in the dark?"
    }, 
    {
      "answer": "Bill Gates", 
      "category": "Technology", 
      "difficulty": 1, 
      "id": 6, 
      "question": "Who founded Microsoft?"
    }, 
    {
      "answer": "Chinese", 
      "category": "General", 
      "difficulty": 2, 
      "id": 7, 
      "question": "What language is the most popularly spoken worldwide?"
    }, 
    {
      "answer": "Chickpeas", 
      "category": "Food", 
      "difficulty": 3, 
      "id": 8, 
      "question": "What is hummus made from?"
    }, 
    {
      "answer": "Chile", 
      "category": "Geography", 
      "difficulty": 3, 
      "id": 9, 
      "question": "Which country occupies half of South America\u2019s western coast?"
    }, 
    {
      "answer": "9", 
      "category": "Sports", 
      "difficulty": 2, 
      "id": 10, 
      "question": "How many players are there on a baseball team?"
    }
  ], 
  "success": true,
  "total_questions": 25
}
```
