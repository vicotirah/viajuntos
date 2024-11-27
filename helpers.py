from flask import request, redirect, session, url_for
from app import app, db
from flask_wtf import FlaskForm
import os, time 
from wtforms import StringField, SubmitField, PasswordField, validators

class FormularioUsuario(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=1, max=60)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')