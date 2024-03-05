from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    # Convert notebook to Python script
    subprocess.run(['jupyter', 'nbconvert', '--to', 'script', 'tradingBot.ipynb'])
    
    # Execute the converted Python script
    subprocess.run(['python', 'tradingBot.py'])
    
    return jsonify(message='Colab notebook executed successfully')

if __name__ == '__main__':
    app.run(debug=True)
