
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, request, render_template
import example

app = Flask(__name__)

@app.route('/apartment')
def example_apartment():
    return example.apartment()
























