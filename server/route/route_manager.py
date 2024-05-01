from dotmap import DotMap

# Route info
from dds.server.route import index
from dds.server.route import samples
from dds.server.route import predict, re_predict

_routes = {  # R: route, V: view-name, C: Class
    "index": {"R": "/", "V": "index", "C": index},
    "samples": {"R": "/samples", "V": "samples", "C": samples},
    "predict": {"R": "/predict", "V": "predict", "C": predict},
    "re_predict": {"R": "/re_predict", "V": "re_predict", "C": re_predict},
}
routes = DotMap(_routes)