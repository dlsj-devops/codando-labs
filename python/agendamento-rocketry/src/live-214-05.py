#Exemplo de codigo usando o Rocketry
#gerando logging
import logging
from random import randint
from rocketry import Rocketry
from rocketry.conds import (
    after_fail, after_success
)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
task_logger = logging.getLogger('rocketry.task')
task_logger.addHandler(handler)

app = Rocketry()

@app.task('every 5 second', name='A')
def tarefa_A():
    if randint(0, 1):
        raise Exception('Erro')
    else:
        print('Tarefa A PASSOU')

#Executado depois da Tarefa A falhar
@app.task(after_fail('A'))
def tarefa_para_falha_de_A():
    print('Executado após FALHA da tarefa A')

#Executado depois da Tarefa A não falhar
@app.task(after_success('A'))
def tarefa_para_sucesso_de_A():
    print('Executado após SUCESSO da tarefa A')

#Executado depois da Tarefa A (ela finalizar)
@app.task("after task 'A' finished")
def tarefa_para_fim_de_A():
    print('Executado após FINALIZAR a tarefa A')

#Na primeira execução, todas as tarefas serão executadas
app.run()