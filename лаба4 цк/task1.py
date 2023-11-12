import json

def task() -> float:
    file_name = 'input.json'
    with open(file_name) as file:
        data = json.load(file)
    return sum([dict0['score']*dict0['weight'] for dict0 in data])

print(f'{task():0.3f}')
