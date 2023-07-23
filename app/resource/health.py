from flask import request, render_template, Response
from flask_restful import Resource

from app.enum.default_args import DefaultArgs
from app.resource.lastfm_api import LastFM
from app.util.make_svg import MakeSVG


class Health(Resource):
    # /health
    def get(self):
        return {'status': 'ok'}, 200