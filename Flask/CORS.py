from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app=app)


# CONCEPT: 
'''
CORS -> Cross-Origin Resource Sharing

Mechanism that allows cross-origin requests. 

or... The thing that solves the 307 status code :)
'''
