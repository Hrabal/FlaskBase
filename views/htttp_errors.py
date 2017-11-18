# -*- coding: utf-8 -*-
from app import app

@app.errorhandler(404)
def page_not_found(e):
    return Page404().render(), 404
