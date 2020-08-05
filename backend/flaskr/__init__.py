import os
import random
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Question, Category


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    [Complete] TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app)
    # CORS(app, resources={r'*/api/*':{origins: '*'}})

    '''
    [Complete] TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PUT, PATCH, DELETE, OPTIONS')

        return response

    # To specify the number of items (questions and/or categories) to display per page
    items_per_page = 10

    def pagination(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * items_per_page
        end = start + items_per_page

        items = [item.format() for item in selection]
        current_items = items[start:end]

        return current_items

    '''
    [Complete] TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''

    @app.route('/categories')
    def get_categories():

        selection = Category.query.order_by(Category.id).all()
        current_categories = pagination(request, selection)

        if len(current_categories) == 0:
            return not_found(404)

        return jsonify({
            'success': True,
            'categories': current_categories,
            'total_categories': len(Category.query.all())
        })

    '''
    [Complete] TODO: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 

    [Complete] TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    '''

    @app.route('/questions')
    def get_questions():

        question_selection = Question.query.order_by(Question.id).all()
        current_questions = pagination(request, question_selection)

        categories_selection = Category.query.order_by(Category.id).all()
        current_categories = pagination(request, categories_selection)

        if len(current_questions) == 0:
            return not_found(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'categories': current_categories,
            'total_questions': len(Question.query.all())
        })

    '''
    [Complete] TODO: 
    Create an endpoint to DELETE question using a question ID. 

    [Complete] TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                return not_found(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = pagination(request, selection)

            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            })

        except:
            unprocessable(422)

    '''
    [Complete] TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''

    @app.route('/questions', methods=['POST'])
    def create_question():

        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        search = body.get('search', None)

        try:
            if search:
                selection = Question.query.order_by(Question.id).filter(
                    Question.question.ilike('%{}%'.format(search))).all()
                current_questions = pagination(request, selection)

                if current_questions == []:
                    current_questions = 0

                return jsonify({
                    'success': True,
                    'questions': current_questions,
                    'total_questions': len(selection)
                })

            else:
                question = Question(question=new_question, answer=new_answer,
                                    category=new_category, difficulty=int(new_difficulty))
                question.insert()

                return jsonify({
                    'success': True,
                    'created_question_id': question.id,
                    'questions': question.format(),
                    'total_questions': len(Question.query.all())
                })

        except:
            unprocessable(422)

    '''
    [Complete] TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''

    # Done along with create_question endpoint

    '''
    [Complete] TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''

    @app.route('/categories/<category_type>/questions')
    def get_questions_by_category(category_type):

        selection = Question.query.filter(
            Question.category == category_type).all()
        current_questions = pagination(request, selection)

        if len(current_questions) == 0:
            return not_found(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all())
        })

        # insert into categories (type) select distinct(category) from Questions;

    '''
    [Complete] TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():

        body = request.get_json()

        previous_questions = body.get('previous_questions')
        category = body.get('questions_category')

        if previous_questions is None or category is None:
            return not_found(404)

        if category['id'] == 0:
            questions = Question.query.all()
        else:
            questions = Question.query.filter(category == category['id']).all()

        total_current_questions = len(questions)

        def had_question(question):
            questioned = False
            for to_check_question in previous_questions:
                if to_check_question == question.id:
                    questioned = True

            return questioned

        random_question = questions[random.randrange(
            0, total_current_questions), 1]

        while(had_question(random_question)):
            random_question = questions[random.randrange(
                0, total_current_questions), 1]

        if len(previous_questions) == total_current_questions:
            return jsonify({
                'success': True
            })

        return jsonify({
            'success': True,
            'question': random_question.format()
        })

    '''
    [Complete] TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    return app
