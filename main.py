from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Optional: Set up SQLAlchemy config (only if you plan to use a DB)
# Example:
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# db = SQLAlchemy(app)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/divisions')
def divisions():
    return render_template('divisions.html')

@app.route('/news')
def news():
    articles = [
        {
            'title_en': 'Ninestars Launches Green Energy Project',
            'title_zh': '九星启动绿色能源项目',
            'summary_en': 'We have initiated a new solar farm in Ogun State to expand clean energy access.',
            'summary_zh': '我们在奥贡州启动了一个新的太阳能农场项目，旨在扩大清洁能源的使用。',
            'date': 'July 25, 2025',
            'image': 'solar.jpg'
        },
        {
            'title_en': 'New Manufacturing Plant Opens',
            'title_zh': '新制造工厂投入运营',
            'summary_en': 'Our state-of-the-art facility in Lagos will enhance industrial capacity.',
            'summary_zh': '我们在拉各斯的现代化工厂将提升工业产能。',
            'date': 'July 10, 2025',
            'image': 'factory.jpg'
        },
        {
            'title_en': 'Ninestars Attends Global Expo',
            'title_zh': '九星参加全球博览会',
            'summary_en': 'Ninestars showcased its sustainable initiatives at the China-Africa Trade Expo.',
            'summary_zh': '九星在中非贸易博览会上展示了其可持续发展倡议。',
            'date': 'June 30, 2025',
            'image': 'expo.jpg'
        }
    ]
    return render_template('news.html', articles=articles)

@app.route('/contact')
def contact():
    return render_template('contact.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
