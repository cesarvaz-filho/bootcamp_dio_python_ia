import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "Novo dir") #criar diretório novo
arquivo = open("novo_arquivo.txt", "w") #cria arquivo no mode escrita
arquivo.close() #fecha o arquivo

os.rename("novo_arquivo.txt", "apenas_novo.txt") #renomeia o arquivo
os.remove("apenas_novo.txt") #remove o arquivo