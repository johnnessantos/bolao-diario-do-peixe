from json import load as json_load
from copy import deepcopy
from os.path import dirname, abspath


CURRENT_RANKING = []
with open(f'{dirname(abspath(__file__))}/current_ranking.json', 'r') as file:
    CURRENT_RANKING = json_load(file)

def __get_winner(game_score):
    if game_score['santos'] >  game_score['adversary']:
        return 'santos'
    elif game_score['adversary'] >  game_score['santos']:
        return 'adversary'
    return None

def __add_points(current_ranking, shot_user_name, point, game_number):
    updated = False
    for user in current_ranking:
        if user['name'] == shot_user_name:
            user['points'] += point
            user['victory'] += 1
            updated = True

    if not updated:
        current_ranking.append(
            {
                'name': shot_user_name,
                'points': point,
                'victory': 1,
                'last_correct': game_number
            }
        )


def calculate_ranking(ranking, shots, game_score):
    current_ranking = deepcopy(ranking)
    for shot in shots:
        points = 0
        if (
            shot['santos'] ==  game_score['santos'] and
            shot['adversary'] ==  game_score['adversary']
        ):
            points = 3
        elif __get_winner(game_score) == __get_winner(shot):
            points = 1
        
        if points:
            __add_points(current_ranking, shot['name'], points, game_score['number'])

    return current_ranking

def sorting_ranking(ranking):
    score_board = [
        {
            **user,
            'score': user['points'] * 1000 + 100-user['last_correct']
        }
        for user in ranking
    ]

    score_board = sorted(score_board, key=lambda k: k['score'], reverse=True)
    position = 1
    for user in score_board:
        user['row'] = position
        position += 1
    return score_board

def ranking():
    return sorting_ranking(CURRENT_RANKING)


def calcule(shots, game_score):
    global CURRENT_RANKING
    CURRENT_RANKING = calculate_ranking(CURRENT_RANKING, shots, game_score)