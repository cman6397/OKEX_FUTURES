from flask import render_template,url_for,redirect,flash, request,jsonify,json
from sqlalchemy.sql import func, label
from sqlalchemy.sql.functions import coalesce
from sqlalchemy import exc, update
from app import app
from app import db
from sqlalchemy.orm import aliased
import datetime,decimal

@app.route('/')
def main():
	return redirect (url_for('dashboard'))

@app.route('/dashboard/')
def dashboard():
	return ("HIIIIIIIIIIIIIIIIII")
