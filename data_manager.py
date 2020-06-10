import connection

def get_all_players():
    players = connection.fetch_all('SELECT * FROM player', {})
    return players