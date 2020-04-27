from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)

app.secret_key = 'HsgP\b>*L6WoBjGv'

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

