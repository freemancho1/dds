from flask import Flask
from flask_cors import CORS

from .sys import config
from .sys import messages
from .sys import http_codes
from .sys.init import AppInit as app_init
from .route.route_manager import routes

app = Flask(__name__)
app.debug = config.app.debug
app.config.update(
    SECRET_KEY=config.app.secret_key,
    SESSION_COOKIE_NAME=config.app.session_cookie_name,
    PERMANENT_SESSION_LIFETIME=config.app.session_lifetime    # 31 days
)

CORS(app)

# Route
_routes = list(routes.keys())
for r in _routes:
    app.add_url_rule(
        eval(f"routes.{r}.R"), 
        view_func=eval(f"routes.{r}.C").as_view(f"routes.{r}.V")
    )