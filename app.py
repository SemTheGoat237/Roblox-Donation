from flask import Flask, render_template, request
import requests

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

    webhook_url = 'https://discord.com/api/webhooks/1402584077990625301/awVyPBAZ2WyVo_5aCGUAtD0utDLPjNXlxkD7kwCu9-BIOZ_X2d6OlK6MQZhweMo6S-H2'  # remplace par ton vrai lien

    payload = {
        "content": f"Nouveau participant !\nPseudo Roblox : {pseudo}\nDiscord : {discord}"
    }

    response = requests.post(webhook_url, json=payload)
    return render_template('merci.html')


if __name__ == '__main__':
    app.run(debug=True)