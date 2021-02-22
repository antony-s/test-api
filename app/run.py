from eve import Eve
from eve.io.base import BaseJSONEncoder
from eve.io.mongo import Validator

from eve_swagger import get_swagger_blueprint, add_documentation

app = Eve()

swagger = get_swagger_blueprint()
app.register_blueprint(swagger)

app.config['SWAGGER_INFO'] = {
    'title': 'Test API',
    'version': '1.0',
    'description': 'Test API to access vulnerability data',
    'termsOfService': 'foobar',
    'contact': {
        'name': 'Mr Chips',
        'url': 'https://en.wikipedia.org/wiki/Catchphrase_(British_game_show)'
    },
    'license': {
        'name': 'BSD',
        'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
    },
    'schemes': ['http', 'https'],
}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
