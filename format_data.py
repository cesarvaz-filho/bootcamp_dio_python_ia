from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 09:25"
mascara_pt_br = "%d/%m/%Y %H:%M %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual) #data sem formatação no modelo americado
print(data_hora_atual.strftime(mascara_pt_br)) #data formatada no padrão brasileiro
print(datetime.strptime(data_hora_str, mascara_en)) 