import random

from click import prompt
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello(prompt):
    seed = random.randint(1, 1000)
    return f'https://picsum.photos {seed}/500/500'

@app.route('/home', method= ['GET', 'POST'])
def index():
    image_url = None
    prompt_text = ''
    if request.method == 'POST':
        promp_text = request.form.get['prompt']

        if promp_text:
            image_url = hello(promp_text)



    return render_template('home.html', image_url=image_url, prompt=promp_text)


app.run(debug=True)