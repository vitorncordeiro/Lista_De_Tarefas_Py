import json

with open('venv\sets.json', 'r+') as arquivo:
    dictJson = json.load(arquivo)
#Acima ele está abrindo e fechando o arquivo sets no modo leitura + escrita, que é o arquivo onde está salvo a lista de tarefas, e salvando todo seu conteúdo dentro da variável dictJson
ultimaAcao = {} #variavel vazia para armazenar todas as adições ou exclusões feitas, armazenando se é exclusão ou adição na chave, e armazenando no valor, a tarefa(string do user) que foi adicionada/excluida

if "tarefas" not in dictJson:
    dictJson['tarefas'] = []
#caso a lista ainda não exista, ou seja, o arquivo json esteja vazio, cria a lista 
print(dictJson)

def adicionar_item(item):
    global ultimaAcao
    dictJson['tarefas'].append(item)
    ultimaAcao[f'adicionado_{item}'] = item

    print(f'\n\n{ultimaAcao}\n')

    return dictJson
#função para adicionar um novo item à lista, salvando essa ação no dict ultimaAcao

def excluir_item(item):
    global ultimaAcao
    dictJson['tarefas'].pop(dictJson['tarefas'].index(item))
    ultimaAcao[f'excluido_{item}'] = item

    print(f'\n\n{ultimaAcao}\n')

    return dictJson
#função para excluir um item da lista, e salva a execução dessa ação no dict ultimaAcao

def desfazer():
    listaDeChaves = list(ultimaAcao.keys()) # cria uma lista com as chaves do dict ultimaAcao(pq nas chaves ta a info se é add ou exc, aí tem uma lista com essas informações)
    ultimaChave = listaDeChaves[len(listaDeChaves)-1] # a última alteração vai ser o comprimento dessa lista -1, pra pegar o index final da lista, ou seja, descobre qual a ultima ação com base na ultima chave da lista
    if 'adicionado' in ultimaChave:
        dictJson['tarefas'].pop()
        #aqui ele exclui a última tarefa, e NÃO faz isso por meio da função excluir_item(), pois se chamasse a função pra fazer isso, a função registraria na ultimaAcao, aí ficaria num loop de desfazer o que foi desfeito, e não funcionaria legal
    elif 'excluido' in ultimaChave:
        dictJson['tarefas'].append(ultimaAcao[ultimaChave])
        #adiciona o ultimo item que foi excluido, novamente, e NÃO chama a função adicionar_item() pelo mesmo motivo do comentário acima
        ...

while True: #dentro do loop vai perguntar oq o usuário quer fazer e chamar as devidas funções. Caso o usuário queira parar, usa o S para quebrar o laço e conseguir salvar o json no bloco abaixo
    ComandoInicial = input('Selecione um comando:\n[L]istar [A]dicionar [E]xcluir [D]esfazer [R]efazer [S]air e salvar\n').upper()
    if ComandoInicial.startswith('S'):
        break
    elif ComandoInicial.startswith('L'):
        print(f'{dictJson}')
    elif ComandoInicial.startswith('A'):
        tarefa = input('Digite o item que será adicionado:\n')
        adicionar_item(tarefa)
    elif ComandoInicial.startswith('E'):
        tarefaASerExcluida = input('Digite o item que você deseja excluir:\n')
        excluir_item(tarefaASerExcluida)
    elif ComandoInicial.startswith('D'):
        desfazer()

with open('venv\sets.json', 'w+') as f:
    json.dump(dictJson, f)
#Abre o arquivo json, salva todas as alterações feitas na dictJson, dentro do arquivo json em si, e depois fecha dnv o arquivo
        
        
