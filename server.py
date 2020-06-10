from flask import Flask, render_template
import data_manager

app = Flask(__name__)

@app.route('/')
def home():
    players = data_manager.get_all_players()
    return render_template('team-summary.html', players=players)

if __name__ == '__main__':
    app.run(debug=True)