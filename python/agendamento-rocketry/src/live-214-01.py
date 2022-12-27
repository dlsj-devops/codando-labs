#Exemplo de codigo usando o Rocketry
#Restrições
from rocketry import Rocketry
from rocketry.conds import minutely, every

app = Rocketry()

@app.task('minutely after 10')
def restricoes01():
    print('Tarefa executada minuto depois de 10')

@app.task(minutely.after(5))
def restricoes02():
    print('Tarefa executada minuto depois de 5')

@app.task('daily between 23:00 and 23:59')
def restricoes03():
    print('Tarefa executada diariamente enter 23:00 e 23:59')

#Na primeira execução, todas as tarefas serão executadas
app.run()