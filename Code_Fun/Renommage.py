import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def envoyer_notification_email(fichier, prefixe_invalide):
    # Configuration du serveur SMTP
    smtp_server = 'smtp.example.com'
    port = 587
    login = 'votre_adresse_email@example.com'
    password = 'votre_mot_de_passe'

    # Destinataires de l'e-mail
    destinataires = ['data_it@abclub-paris.com']

    # Création du message
    message = MIMEMultipart()
    message['From'] = login
    message['To'] = ', '.join(destinataires)
    message['Subject'] = 'Notification : Préfixe de fichier invalide'

    # Corps du message
    body = f"Le fichier {fichier} a été créé avec un préfixe invalide : {prefixe_invalide}"
    message.attach(MIMEText(body, 'plain'))

    # Connexion et envoi de l'e-mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(login, destinataires, message.as_string())

class MyHandler(FileSystemEventHandler):
    def __init__(self, root_dir, prefixes):
        self.root_dir = root_dir
        self.prefixes = prefixes

    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        filename = os.path.basename(filepath)
        
        # Extraire le préfixe du fichier
        file_prefix = filename.split("_")[0]
        
        if file_prefix not in self.prefixes:
            envoyer_notification_email(filename, file_prefix)
            return

        for prefix in self.prefixes:
            if file_prefix == prefix:
                break
        
        nouveau_nom_fichier = os.path.join(self.root_dir, f"{prefix}_{filename}")
        try:
            os.rename(filepath, nouveau_nom_fichier)
            print(f"Renommage: {filepath} -> {nouveau_nom_fichier}")
        except PermissionError as e:
            print(f"Ignoré: Impossible de renommer '{filepath}'. Raison: {e}")

def surveiller_repertoire(root_dir, prefixes):
    event_handler = MyHandler(root_dir, prefixes)
    observer = Observer()
    observer.schedule(event_handler, path=root_dir, recursive=False)
    observer.start()
    print(f"Surveillance du répertoire {root_dir} en cours...")
    try:
        while True:
            time.sleep(604800)  # Une semaine en secondes
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Liste des dossiers racines
dossiers_racines = ["G:\\Drive partagés\\Général 2023-2024\\AMID", "G:\\Drive partagés\\Général 2023-2024\\Administratif", "G:\\Drive partagés\\Général 2023-2024\\Compte rendu des réunions","G:\\Drive partagés\\Général 2023-2024\\Gala des 20 ans de l'ABC","G:\\Drive partagés\\Général 2023-2024\\Images et Vidéos","G:\\Drive partagés\\Général 2023-2024\\Pôle ABC Connect 2023-2024","G:\\Drive partagés\\Général 2023-2024\\Pôle IT & Data Management","G:\\Drive partagés\\Général 2023-2024\\Pôle Média","G:\\Drive partagés\\Général 2023-2024\\Pôle Réseau 2023 - 2024"]

# Liste des préfixes à ajouter
prefixes = ["AMID", "Administratif", "Compte rendu", "Gala20ans", "Images&Videos", "ABC Connect", "Data&IT", "Media", "Réseau"]  # Ajoutez ou modifiez les préfixes selon vos besoins

# Surveillance de chaque dossier racine
for dossier_racine in dossiers_racines:
    surveiller_repertoire(dossier_racine, prefixes)
