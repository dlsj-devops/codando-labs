#Exemplo de codigo usando o Rocketry
#modos de execução
from rocketry import Rocketry
from rocketry.conds import weekly, monthly

app = Rocketry()

@app.task('every 1s', execution='process')
def todo_segundo_a():
    print('Executa a todo segundo A')

@app.task('every 1s', execution='async')
async def todo_segundo_b():
    print('Executa a todo segundo B - ASYNC')
    await()


@app.task('every 1s', execution='async')
async def todo_segundo_c():
    print('Executa a todo segundo C - ASYNC')
    await()

#Na primeira execução, todas as tarefas serão executadas
app.run()