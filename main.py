from flask import Flask, request, make_response, redirect, render_template


app = Flask(__name__)

todos = ['comprar cafe', 'enviar solicitud', 'entregar producto']

@app.errorhandler(404)
def not_fpund(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    # return 'hello world platzi '+user_ip
    # VARIABLES PARA PASAR AL TEMPLATE ES EL SEGUNDO PARAMETREO
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True)