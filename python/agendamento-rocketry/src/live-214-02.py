#Exemplo de codigo usando o Rocketry
#Agendado
from rocketry import Rocketry
from rocketry.conds import weekly, monthly

app = Rocketry()

@app.task(weekly.on('Monday'))
def agendada01():
    print('Tarefa executada toda segunda')

@app.task(monthly.starting('8rd'))
def agendada02():
    print('Tarefa executada a partir do oitavo dia do mês')

#Na primeira execução, todas as tarefas serão executadas
app.run()