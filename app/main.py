from flask import Flask, render_template, request, Response

from backend import ranking, calcule

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pages=ranking())


@app.route('/update_ranking', methods=['POST'])
def update_ranking():
    shots, game = request.json.get('shots'), request.json.get('game')
    if not shots:
        return Response('Informe os palpites', status=400)
    if not game:
        return Response('Informe o placar do jogo', status=400)

    calcule(shots, game)
    return Response(status=200)


if __name__ == '__main__':
	app.run(debug=True)
