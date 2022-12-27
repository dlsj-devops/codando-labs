#Exemplo de codigo usando o Rocketry
from rocketry import Rocketry
from rocketry.conds import minutely, every

app = Rocketry()

@app.task('every 10 seconds')
def a_cada_segundo():
    print('Tarefa executada a cada 10 segundos')

@app.task(minutely)
def a_cada_minuto():
    print('Tarefa executada a cada minuto')

@app.task('every 1 hour')
def a_cada_hora():
    print('Tarefa executada a cada hora')

@app.task(every('1d'))
def a_cada_dia():
    print('Tarefa executada a cada dia')

@app.task('weekly')
def a_cada_semana():
    print('Tarefa executada a cada semana')

@app.task('monthly')
def a_cada_mes():
    print('Tarefa executada a cada mês')

#Na primeira execução, todas as tarefas serão executadas
app.run()