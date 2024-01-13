from twilio.rest import Client

# Votre compte Twilio
account_sid = 'ACed3effd1a361019428b48fb5feb4ec04'
auth_token = 'cba78a162bfa06f3b33294ab396dd906'

# Initialisation du client Twilio
client = Client(account_sid, auth_token)

# Liste des numéros de téléphone des destinataires
destinataires = ['whatsapp:+33767346346']  # Remplacez par les numéros réels

# Envoie du message à chaque destinataire
for destinataire in destinataires:
    message = client.messages.create(
        body="joyeux anniversaire",
        from_='whatsapp:+14155238886',  # Votre numéro WhatsApp Twilio
        to=destinataire
    )
    print(f"Message envoyé à {destinataire}: {message.sid}")
