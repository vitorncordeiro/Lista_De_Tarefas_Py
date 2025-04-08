import json
with open('venv\sets.json', 'r+') as arquivo:
    listaJson = json.load(arquivo)
if "tarefas" not in listaJson:
    listaJson['tarefas'] = []
print(listaJson)
def adicionar_item(item):
    listaJson['tarefas'].append(item)
    return listaJson
while True:
    primeiraPergunta = input('Selecione um comando:\n[L]istar [A]dicionar [E]xcluir [D]esfazer [R]efazer [S]air\n').upper()
    if primeiraPergunta.startswith('S'):
        break
    elif primeiraPergunta.startswith('L'):
        print(f'{listaJson}')
    elif primeiraPergunta.startswith('A'):
        tarefa = input('Digite o item que será adicionado:\n')
        adicionar_item(tarefa)


with open('venv\sets.json', 'w+') as f:
    json.dump(listaJson, f)
        
        