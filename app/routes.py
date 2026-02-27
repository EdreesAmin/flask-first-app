from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app
from app.forms import ContactForm
from datetime import datetime
import random

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Visitor'}
    posts = [
        {
            'author': {'username': 'John Doe'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Jane Smith'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Bob Johnson'},
            'body': 'Just finished learning Flask. Great framework!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f'Thank you {form.name.data} for your message! We\'ll get back to you soon.', 'success')
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact', form=form)

@app.route('/api/data')
def get_data():
    """REST API endpoint example"""
    data = {
        'timestamp': datetime.now().isoformat(),
        'random_number': random.randint(1, 100),
        'message': 'This is a sample API endpoint',
        'items': ['item1', 'item2', 'item3', 'item4', 'item5']
    }
    return jsonify(data)

@app.route('/data')
def data_page():
    """Page that consumes the API"""
    return render_template('data.html', title='Data Demo')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500