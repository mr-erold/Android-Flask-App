"""
Execute our API
"""

from api import app

if __name__ == '__main__':
    app.run(debug=True, port=7776)