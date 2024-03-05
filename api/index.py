
from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1HV8yRqwMLXIaBsUYzYBSle6zlHyU9Khi?usp=sharing', 'tradingBot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
