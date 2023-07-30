from app import flaskapp


@flaskapp.route('/login')
def login():
    return 'Login'
