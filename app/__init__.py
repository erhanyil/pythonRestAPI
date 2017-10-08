from flask import Flask, jsonify,make_response,abort,render_template,request,json
import pymysql

app = Flask(__name__)
from app import views

