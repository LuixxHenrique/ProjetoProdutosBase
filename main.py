from classe_Menu import *
from datetime import datetime

menu_de_opcoes = Menu()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Horario de Saída: ", current_time)