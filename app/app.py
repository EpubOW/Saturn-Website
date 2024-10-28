from config import *

from controllers.auth import *
from controllers.page import *
from controllers.rest import *
from controllers.forms import *


if __name__ == "__main__":
    print('App is running')
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0', port=3030, debug=True)