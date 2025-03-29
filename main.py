import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Paramètres
smtp_server = "smtp.gmail.com"
smtp_port = 587
email = "votre_email@gmail.com"
password = "votre_mot_de_passe"
destinataire = "destinataire@gmail.com"

# Configuration du message
msg = MIMEMultipart()
msg["From"] = email
msg["To"] = destinataire
msg["Subject"] = "Test d'automatisation Python"

body = "Bonjour, ceci est un email automatique envoyé via Python !"
msg.attach(MIMEText(body, "plain"))

# Envoi de l'email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(email, password)
    server.sendmail(email, destinataire, msg.as_string())

print("✅ Email envoyé avec succès !")
