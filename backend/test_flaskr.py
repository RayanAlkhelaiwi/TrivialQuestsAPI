import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # Inserting a question
        self.new_question = {
            "question": "What does the acronym SMTP represent?",
            "answer": "Simple Mail Transport Protocol",
            "category": "Technology",
            "difficulty": 3
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    [Complete] TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_categories(self):
        """ Test for getting successful paginated categories """

        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))

    def test_get_paginated_questions(self):
        """ Test for getting successful paginated questions """

        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_404_get_paginated_questions_beyond_valid_pagination(self):
        """ Test for 404 getting paginated questions beyond valid pagination """

        res = self.client().get('/questions?page=1000', json={'difficulty': 3})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_delete_question(self):
        """ Test for deleting a question """

        #! Increment question_id before execution
        question_id = 14

        res = self.client().delete('/questions/' + str(question_id))
        data = json.loads(res.data)

        question = Question.query.filter(
            Question.id == question_id).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_id)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)

    def test_404_deleting_nonexistent_question(self):
        """ Test for 404 deleting a nonexistent question """

        res = self.client().delete('/questions/300')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_create_question(self):
        """ Test for creating a question """

        res = self.client().post(
            '/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created_question_id'])
        self.assertTrue(data['total_questions'])

    def test_405_create_nonexistent_question(self):
        """ Test for 405 creating a nonexistent question """

        res = self.client().post(
            '/questions/300', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_search_question_with_results(self):
        """ Test for searching a questions with results returned """

        res = self.client().post('/questions', json={'searchTerm': 'What'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'] > 0)

    def test_search_question_no_results(self):
        """ Test for searching a question that returns no results """

        res = self.client().post(
            '/questions', json={'searchTerm': 'Prooggraammiing'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

    def test_get_questions_by_category(self):
        """ Test for getting questions by category """

        res = self.client().get('/categories/Technology/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_404_no_question_by_category_found(self):
        """ Test for 404 requesting beyond valid pagination """

        res = self.client().get('/categories/Biology/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not Found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
