import email
from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email, senha

app = Flask(__name__)
app.secret_key = 'ianzin'

mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": email,
        "MAIL_PASSWORD": mail_senha
}


app.config.update(mail_settings)

mail = Mail(app)

class Contato:
        def __init__(self, nome, email, mensagem):
          self.nome = nome
          self.email = email
          self.mensagem = mensagem




@app.route('/')
def index():
        return render_template("index.html")


@app.route('/send', methods=['GET', 'POST'])
def send():
        if request.method == 'POST':
                formContato = Contato(
                        request.form["Nome"]
                        request.form["Email"]
                        request.form["Mensagem"]
                )
                msg = Message(
                        subject = 'Contado do Portfólio'
                        sender = app.config.get("MAIL_USERNAME")
                        recipients = ["vasconcelos.iansantos@gmail.com"]
                        body = f'''

                        {formContato.Nome} com o email {formContato.Email} te enviou a seguinte mensagem:

                        {formContato.Mensagem}

                        '''

                )
                mail.send(msg)
                flash("Mensagem enviada!")
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
