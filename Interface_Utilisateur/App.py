from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    title = "Mon Tableau de Bord"
    welcome_message = "Bienvenue sur le Tableau de Bord"
    return render_template('C:/Users/frup00090927/gitAbclub/data_abclub/Interface_Utilisateur/templates/dashboard.html.jinja')

if __name__ == '__main__':
    app.run(debug=True)