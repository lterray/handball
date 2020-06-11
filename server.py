from flask import Flask, render_template
import data_manager

app = Flask(__name__)


@app.route('/')
def home():
    players = data_manager.get_all_players()
    return render_template('team-summary.html', players=players)


@app.route('/player/<player_id>/vote/<any(up, down):vote_direction>', methods=['POST'])
def vote(player_id, vote_direction):
    data_manager.vote(player_id, vote_direction)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
