#!/usr/bin/env bash
FLASK_APP=app.py FLASK_DEBUG=1 python3 -m flask run
#cockroach start --insecure --host=localhost --background
