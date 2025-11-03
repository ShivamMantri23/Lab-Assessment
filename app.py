from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    
    details = {
        'Name': 'Shivam Mantri',
        'Institution': 'Centre of Development of Advanced Technology (CDAC), Noida',
        'Course': 'Post Graduate-Diploma in Artificial Intelligence (PG-DAI)',
        'Skills': 'Python, Java, C/C++, Linux, MERN, Machine Learning, RHEL',
        'Location': 'Jaipur, Rajasthan',
        'Time': datetime.now().strftime("%A, %d %B %Y, %I:%M %p")
    }
    return render_template('index.html', details=details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
