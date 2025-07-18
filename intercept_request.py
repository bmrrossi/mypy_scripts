from flask import request, Flask
from prometheus_client import start_http_server, Histogram, REGISTRY
import random
import time

app = Flask()

request_time = Histogram('http_request_duration_seconds',
                         'Description of fkdjfkd',
                         labelnames=("code", "method", "handler"),
                         buckets=(0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.45, 0.5, 0.55, 0.6, 0.75, 1, 2.5),
                         registry=REGISTRY
                         ).labels(code='', method='', handler='')


BUCKETS = [0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.45, 0.5, 0.55, 0.6, 0.75, 1, 2.5]


@request_time.time()
def teste_prom(t):
    time.sleep(t)


def define_param(code, method, handler):
    request_time.labels(code=code, method=method, handler=handler)

    start_http_server(8000)
    teste_prom(random.random())


@app.before_request
def hook():

    define_param('200', request.method, request.url)
    # just do here everything what you need...


@app.route("/teste")
def request_lalala():
    return "hello"


@app.route("/bunda")
def guilherme():
    return "alele"

