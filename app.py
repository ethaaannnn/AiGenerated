from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    response = requests.post(
        'https://api.deepai.org/api/text2img',
        data={'text': text},
        headers={'api-key': os.getenv('DEEPAI_API_KEY')}
    )
    result_url = response.json().get('output_url', '')
    return render_template('result.html', result_url=result_url)

if __name__ == '__main__':
    app.run(debug=True)
