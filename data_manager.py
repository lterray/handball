import connection


def get_all_players():
    players = connection.fetch_all('SELECT * FROM player', {})
    return players


def vote(player_id, vote_direction='up'):
    connection.execute_query('''
        UPDATE player
            SET vote_number = vote_number + %(vote)s
        WHERE id = %(player_id)s;
    ''', {
        'player_id': int(player_id),
        'vote': 1 if vote_direction == 'up' else -1
    })
