import argparse
from json import dumps as json_dumps
from json import load as json_load

from requests import post


def update_ranking(file_name: str) -> bool:
    '''
    curl -i -H "Content-Type: application/json" -X POST \
        -d '{"shots": [{"name": "foo", "santos": 0, "adversary": 1}], "game": {"santos": 0, "adversary": 1, "number": 22}}' \
            http://localhost:5000/update_ranking
    '''
    if not file_name:
        raise Exception('Informe o arquivo de palpites')

    data = []
    with open(file_name, 'r') as file:
        data = json_load(file)

    if not data:
        raise Exception(f'Não foi possível ler o arquivo {file_name}')

    url = 'http://localhost:5000/update_ranking'
    response = post(url=url, json=data)
    print(f'Request in {url} with status_code:{response.status_code} payload:{data}')
    return response.status_code == 200

if __name__  == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='file name')

    args = parser.parse_args()
    file_name = args.file
    update_ranking(file_name)
