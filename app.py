from flask import Flask, render_template, redirect, flash, request, session
from forms import LoginForm, CadastroForm
from micro_db import MicroDB
from replit import db
import os

app = Flask(__name__)

# Chave secreta do nosso site
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

user_db = MicroDB('users', './db/')


# Página inicial
@app.route('/')
def index():
  if 'logged_in' not in session:
    flash('Faça login para acessar esta página', 'error')
    return redirect('/login')

  usuario = session['usuario']
  return render_template('home.html', usuario=usuario)


# Página inicial
@app.route('/irc')
def irc():
  if 'logged_in' not in session:
    flash('Faça login para acessar esta página', 'error')
    return redirect('/login')

  usuario = session['usuario']
  return render_template('irc.html', usuario=usuario)


# Login
@app.route('/login', methods=['POST', 'GET'])
def login():
  form = LoginForm()
  if request.method == 'POST' and form.validate_on_submit():
    usuario = form.usuario.data
    senha = form.senha.data

    if not user_db.get(usuario):
      flash('Usuário não existe', 'error')
      return render_template('login.html', form=form)

    # Verificar se a senha está correta
    if user_db.get(usuario).get("password") != senha:
      flash('Senha incorreta', 'error')
      return render_template('login.html', form=form)

    # Definir a sessão de login
    session['logged_in'] = True
    session['usuario'] = usuario

    return redirect('/')

  return render_template('login.html', form=form)


# Cadastro
@app.route('/register', methods=['POST', 'GET'])
def cadastro():
  form = CadastroForm()
  if request.method == 'POST' and form.validate_on_submit():
    nome = form.nome.data
    usuario = form.usuario.data
    senha_1 = form.senha_1.data
    senha_2 = form.senha_2.data

    if not user_db.get(usuario):
      flash('O usuário já existe', 'error')
      return render_template('cadastro.html', form=form)

    if senha_1 != senha_2:
      flash('A senha de confirmação está incorreta', 'error')
      return render_template('cadastro.html', form=form)
    user_db.set(usuario, {"name": nome, "password": senha_1})
    flash('Cadastro realizado com sucesso', 'success')
    return redirect('/login')

  return render_template('cadastro.html', form=form)


# Logout
@app.route('/logout')
def logout():
  # Remover a sessão de login
  session.pop('logged_in', None)
  session.pop('usuario', None)
  return redirect('/login')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
