import os
import markdown
import markdown.extensions.fenced_code

from flask import Flask, Response, request, render_template
from app.resource.lastfm_api import LastFM
from app.resource.make_svg import MakeSvg


LASTFM_TOKEN = os.environ.get('LASTFM_TOKEN')
PORT = int(os.environ.get('PORT', 5000))

print(LASTFM_TOKEN)

app = Flask(__name__, template_folder="app/templates")
lastFM = LastFM(LASTFM_TOKEN)
makeSVG = MakeSvg()

@app.route('/', methods=['GET'])
def index():
    with open("README.md", "r") as readme_file:
        md_template_string = markdown.markdown(
            readme_file.read(), extensions=["fenced_code"]
        )

    return md_template_string

@app.route('/current', methods=['GET'])
def current():
    user_lasftm = request.args.get('user') or 'gabriel_ah'
    theme_select = request.args.get('theme') or 'light'
    style_select = request.args.get('style') or 'default'
    time_refresh = request.args.get('reload') or '1500000000'
    
    data = lastFM.get_current_track(user_lasftm)
    svg = makeSVG.generate(data, theme_select, style_select, time_refresh)
    render = render_template(svg[0], **svg[1])

    resp = Response(render)
    resp.headers["Content-Type"] = "image/svg+xml"
    resp.headers["Cache-Control"] = "s-maxage=1"

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
