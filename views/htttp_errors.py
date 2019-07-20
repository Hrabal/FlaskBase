# -*- coding: utf-8 -*-
from app import app


@app.errorhandler(400)
def error_400(e):
    return "400, bad request.", 400


@app.errorhandler(404)
def error_404(e):
    return "404, page not found.", 404


@app.errorhandler(403)
def error_403(e):
    return "403, you are not authorized to see resource.", 403


@app.errorhandler(405)
def error_405(e):
    return "405, HTTP method not allowed.", 405


@app.errorhandler(408)
def error_408(e):
    return "408, your request is taking too long to be served.", 408


@app.errorhandler(418)
def error_418(e):
    return "Yes, I am a Teapot.", 418
