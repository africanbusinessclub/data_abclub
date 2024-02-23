from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import humanize

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

dossiers_racines = [
    "G:\\Drive partagés\\Général 2023-2024\\AMID",
    "G:\\Drive partagés\\Général 2023-2024\\Administratif",
    "G:\\Drive partagés\\Général 2023-2024\\Compte rendu des réunions",
    "G:\\Drive partagés\\Général 2023-2024\\Gala des 20 ans de l'ABC",
    "G:\\Drive partagés\\Général 2023-2024\\Images et Vidéos",
    "G:\\Drive partagés\\Général 2023-2024\\Pôle ABC Connect 2023-2024",
    "G:\\Drive partagés\\Général 2023-2024\\Pôle IT & Data Management",
    "G:\\Drive partagés\\Général 2023-2024\\Pôle Média",
    "G:\\Drive partagés\\Général 2023-2024\\Pôle Réseau 2023 - 2024"
]
prefixes = [
    "AMID", "Administratif", "Compte rendu", "Gala20ans", "Images&Videos",
    "ABC Connect", "Data&IT", "Media", "Réseau"
]  

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOSSIERS_RACINES'] = dict(zip(prefixes, dossiers_racines))

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def search_files(root_folder, query):
    matching_files = []
    for root, _, files in os.walk(root_folder):
        for file_name in files:
            if query in file_name:
                file_path = os.path.join(root, file_name)
                matching_files.append({
                    'filename': file_name,
                    'path': file_path,
                    'filesize': os.path.getsize(file_path)
                })
    return matching_files

def get_destination_folder(pole):
    return app.config['DOSSIERS_RACINES'].get(pole)

@app.route('/')
def index():
    files = []
    for root, _, filenames in os.walk(app.config['UPLOAD_FOLDER']):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            files.append({
                'filename': filename,
                'filesize': os.path.getsize(filepath)
            })
    return render_template('bd.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    pole = request.form.get('pole')
    destination_folder = get_destination_folder(pole)
    if destination_folder:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(destination_folder, filename)
            file.save(filepath)
            return send_from_directory(destination_folder, filename)
        else:
            return 'File format not allowed'
    else:
        return 'Invalid pole selected'

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    files = []
    for pole, root_folder in app.config['DOSSIERS_RACINES'].items():
        matching_files = search_files(root_folder, query)
        for file in matching_files:
            file['pole'] = pole
        files.extend(matching_files)
    return render_template('bd.html', files=files)

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# Custom bytes filter
@app.template_filter('bytes')
def bytes_filter(num):
    return humanize.naturalsize(num, format='%.1f')

if __name__ == '__main__':
    app.run(debug=True)
