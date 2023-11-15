from flask import request
from flask_restful import Resource

from app.enum.default_args import DefaultArgs
from app.resource.lastfm_api import LastFM


class CurrentJson(Resource):
    # /currentjson/{user_id}
    def get(self, user_id: str):
        theme_select = request.args.get('theme') or DefaultArgs.THEME.value
        style_select = request.args.get('style') or DefaultArgs.STYLE.value
        time_refresh = request.args.get('reload') or DefaultArgs.RELOAD.value

        try:
            last_fm = LastFM()
            data = last_fm.get_current_track(user_id)
            data.set_theme(theme_select)
            data.set_style(style_select)
            data.set_reload(time_refresh)
            return data.json(), 200
        except:
            return {
                "message": "Error in Request data"
            }, 400
