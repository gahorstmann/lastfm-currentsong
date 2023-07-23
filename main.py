from flask import Flask
from flask_restful import Api

from app.enum.global_configs import SysConfigs
from app.resource.health import Health
from app.resource.current import Current
from app.resource.current_json import CurrentJson


app = Flask(__name__, template_folder='app/templates')
api = Api(app)

api.add_resource(Health, '/health')
api.add_resource(Current, '/current/<user_id>')
api.add_resource(CurrentJson, '/currentjson/<user_id>')

if __name__ == '__main__':
    app.run(host=SysConfigs.HOST.value, port=SysConfigs.PORT.value)
