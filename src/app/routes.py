from distutils.debug import DEBUG
import json
import os
import argparse
from flask import Flask, jsonify, request
from flask_cors import CORS
from logzero import logger

from src.types.return_service import ReturnService
from ..domain.capture_data_cidadania_scrapping_service import CaptureDataCidadaniaScrappingService

class RouteApp():
    
    def create_app(config=None):
        app = Flask(__name__)

        # See http://flask.pocoo.org/docs/latest/config/
        app.config.update(dict(ENV='development', DEBUG=True))
        app.config.update(config or {})

        # Setup cors headers to allow all domains
        # https://flask-cors.readthedocs.io/en/latest/
        CORS(app)

        @app.route("/health")
        def health():
            logger.info("/health")
            return "I'm ok"

        @app.route("/sigarp-capture-data-cidadania-scrapping", methods=['POST'])
        def sigarpCaptureDataCidadaniaScrapping():
            logger.info("/sigarp-capture-data-cidadania-scrapping")
            logger.info(request.get_json())

            CaptureDataCidadaniaScrappingService().exec(json.dumps(request.get_json()))
            return "I'm ok"

        return app
