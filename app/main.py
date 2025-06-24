from flask import Flask, request, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/app/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "CI/CD with self-hosted runner is working correct full!!"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            return f"File uploaded to {path}"
        return "No file uploaded", 400
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

