from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
  usuario = StringField('Nome de usuário',
                        validators=[
                          DataRequired(),
                          Length(
                            min=3,
                            max=10,
                            message="Minimo de 3 e no maximo 10 caracteris")
                        ])
  senha = PasswordField('Senha',
                        validators=[
                          DataRequired(),
                          Length(
                            min=4,
                            max=50,
                            message="Minimo de 4 e no maximo 50 caracteris")
                        ])
  enviar = SubmitField('Entrar')


class CadastroForm(FlaskForm):
  nome = StringField('Nome',
                     validators=[
                       DataRequired(),
                       Length(max=150, message="no maximo 150 caracteris")
                     ])
  usuario = StringField('Usuário',
                        validators=[
                          DataRequired(),
                          Length(
                            min=3,
                            max=10,
                            message="Minimo de 3 e no maximo 10 caracteris")
                        ])
  senha_1 = PasswordField('Senha',
                          validators=[
                            DataRequired(),
                            Length(
                              min=4,
                              max=50,
                              message="Minimo de 4 e no maximo 50 caracteris")
                          ])
  senha_2 = PasswordField('Confirma a senha',
                          validators=[
                            DataRequired(),
                            Length(
                              min=4,
                              max=50,
                              message="Minimo de 4 caracteres e no maximo 50")
                          ])
  enviar = SubmitField('Entrar')
