#Exemplo de codigo usando o Rocketry
from rocketry import Rocketry

app = Rocketry()

@app.task('minutely')
def a_cada_minuto():
    print('Tarefa executada a cada minuto')

app.run()