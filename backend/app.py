from flask import Flask, session, redirect, url_for, render_template
from dashboard.backend.auth import discord_login, discord_callback
from db.models import Session, UserStat
from api import api

app = Flask(__name__)
app.secret_key = 'replace_with_secure_key'
app.register_blueprint(api)

app.add_url_rule('/login', view_func=discord_login)
app.add_url_rule('/callback', view_func=discord_callback)

@app.route('/')
def index():
    if 'discord_id' in session:
        db = Session()
        stats = db.query(UserStat).filter_by(discord_id=session['discord_id']).all()
        return render_template('dashboard.html', stats=stats)
    return redirect(url_for('discord_login'))

if __name__ == '__main__':
    app.run(debug=True)
