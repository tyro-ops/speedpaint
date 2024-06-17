import os
from flask import Flask, render_template, request
from image_processing import process_image
from video_creation import create_video
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_image_to_video():
    if 'image' not in request.files:
        return "No file part"
    
    image = request.files['image']
    
    if image.filename == '':
        return "No selected file"
    
    if image:
        filename = secure_filename(image.filename)
        file_path = os.path.join('uploads', filename)
        image.save(file_path)  # Save the uploaded file to the 'uploads' directory
        processed_image, error = process_image(file_path)
        
        if processed_image is None:
            return error
        video_path = create_video(processed_image, duration=10)  # 10 minutes in seconds
        return video_path

if __name__ == '__main__':
    app.run(debug=True)