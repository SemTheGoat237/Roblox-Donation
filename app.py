from flask import Flask, render_template, request
import requests
import os  # ➕ Ajout pour Render

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/send', methods=['POST'])
def send():
    pseudo = request.form['pseudo']
    discord = request.form['discord']

    webhook_url = 'https://discord.com/api/webhooks/1402584077990625301/awVyPBAZ2WyVo_5aCGUAtD0utDLPjNXlxkD7kwCu9-BIOZ_X2d6OlK6MQZhweMo6S-H2'  # 👈 remplace par ton vrai lien si tu changes

    payload = {
        "content": f"Nouveau participant !\nPseudo Roblox : {pseudo}\nDiscord : {discord}"
    }

    response = requests.post(webhook_url, json=payload)
    return render_template('merci.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render définit le port dans les variables d’environnement
    app.run(debug=True, host='0.0.0.0', port=port)  # 👈 Essentiel pour que Render expose ton app correctement