import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent


try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)
except IOError as exc:
    print("Erro ao criar o arquivo. {exc}")