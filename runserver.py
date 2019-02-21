"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
