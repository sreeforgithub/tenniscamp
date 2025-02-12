from flask import Flask, render_template
app = Flask(__name__)
# Home Page
@app.route('/')
def home():
   return render_template('index.html')
# FAQs Page
@app.route('/faqs')
def faqs():
   return render_template('faqs.html')
# Image Gallery Page
@app.route('/gallery')
def gallery():
   return render_template('gallery.html')
# Run the Flask app
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)