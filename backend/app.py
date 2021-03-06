import osfrom flask import Flask, request, abort, jsonifyfrom flask_sqlalchemy import SQLAlchemyfrom flask_cors import CORS, cross_originimport randomfrom .models import setup_db, Event, CreatorQUESTIONS_PER_PAGE = 10def create_app(test_config=None):    # create and configure the app    app = Flask(__name__)    setup_db(app)    # set up CORS on all origins    CORS(app, resources={r"/*": {"origins": "*"}})    # set response headers    @app.after_request    def after_request(response):        response.headers.add("Access-Control-Allow-Headers", "Content-Type , Authorization, Data-Type",)        response.headers.add("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, PATCH, OPTIONS")        response.headers.add('Access-Control-Allow-Credentials', 'true')        return response    def paginate(request, selection):        """paginate selection queryset based on page param provided in request"""        page = request.args.get('page', 1, type=int)        start = (page-1) * QUESTIONS_PER_PAGE        end = start + QUESTIONS_PER_PAGE        questions = [question.format() for question in selection]        current_questions = questions[start:end]        return current_questions , page    @app.route('/creators/', methods=['GET'])    def creators():        """return all available creators"""        if request.method == 'GET':            creators = Creator.query.all()            return jsonify({                'success': True,                'creators': [creator.format() for creator in creators]            })    @app.route('/creator/<int:creator_id>/events/', methods=['GET'])    def event_by_creator(creator_id):        """return list of events filtered by creator"""        # filter question by category, category is stored as varchar in questions, use str        events = Event.query.filter(Event.creator_id == str(creator_id)).all()        creator = Creator.query.filter(Creator.id == creator_id).one_or_none()        if (events or creator) is None:            return abort(404)        else:            return jsonify({                'success': True,                'creator': creator,                'questions': [event.format() for event in events]            })    # error handlers    @app.errorhandler(404)    def not_found(error):        return jsonify({            "success": False,            "error": 404,            "message": "Resource not found",        }), 404    @app.errorhandler(422)    def unprocessable(error):        return jsonify({            "success": False,            "error": 422,            "message": "unprocessable",        }), 422    @app.errorhandler(400)    def bad_request(error):        return jsonify({            "success": False,            "error": 400,            "message": "bad request",        }), 400    @app.errorhandler(500)    def bad_request(error):        return jsonify({            "success": False,            "error": 500,            "message": "server error",        }), 500    @app.errorhandler(405)    def bad_request(error):        return jsonify({            "success": False,            "error": 405,            "message": "method not allowed",        }), 405    return app