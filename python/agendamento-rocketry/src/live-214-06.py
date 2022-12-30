#Exemplo de codigo usando o Rocketry
#gerando logging
import logging
from random import randint
from rocketry import Rocketry
from rocketry.conds import (
    after_fail, after_success
)
from rocketry.args import Return

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
task_logger = logging.getLogger('rocketry.task')
task_logger.addHandler(handler)

app = Rocketry()

@app.task('every 5 second', name='A')
def tarefa_A():
    if randint(0, 1):
        raise Exception('Erro')
        return 'Tarefa falhou'
    else:
        print('Tarefa A PASSOU')
        return 'Sucesso da tarefa'

#Executado se a tarefa A tiver sucesso
@app.task(after_success('A'))
def tarefa_para_sucesso_de_A(value=Return('A')):
    print('Retorno da tarefa A: ', value)

#Executado se a tarefa A tiver falha
@app.task(after_fail('A'))
def tarefa_para_falha_de_A(value=Return(tarefa_A)):
    print('Retorno da tarefa A: ', value)

#Na primeira execução, todas as tarefas serão executadas
app.run()