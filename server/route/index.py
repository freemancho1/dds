from flask.views import MethodView

from dds.server import messages as msg
from dds.server import http_codes as hc


class Index(MethodView):
    
    def get(self):
        return msg.log.index, hc.OK
