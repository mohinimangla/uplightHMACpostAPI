from werkzeug.wrappers import Request, Response, ResponseStream

class Middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app, config):
        self.app = app
        self.userName = config["USERNAME"]
        self.passphrase = config["PASSPHRASE"]

    def __call__(self, environ, start_response):
        request = Request(environ)
        try: 
            userName = request.authorization.get('username')
            passPhrase = request.authorization.get('password')
        except Exception as e:
            print(e)
            res = Response(u'Provide valid Authorization to send request', mimetype= 'text/plain', status=401)
            return res(environ, start_response)
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        if userName == self.userName and passPhrase == self.passphrase:
            environ['user'] = { 'name': userName }
            return self.app(environ, start_response)

        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)