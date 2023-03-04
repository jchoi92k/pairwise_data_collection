# -*- coding: utf-8 -*-

from flask import render_template, url_for, flash, redirect, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import secrets
from sqlalchemy.exc import IntegrityError
import os
import json
import traceback
from pairwiseCollect import app, db, bcrypt
from pairwiseCollect.models import User, Text, Temptext, Tempuser, Compared
from pairwiseCollect.forms import LoginForm, RegistrationForm, TextAreaInput
import requests

# ===================================================================
# Routes
# ===================================================================

# Home route
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


# Connects to page with infographics about readability formulas 
@app.route('/learn')
def learn():
    return render_template('learn.html', learngraph=True)