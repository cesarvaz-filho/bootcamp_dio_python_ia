from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
  with open(ROOT_PATH / "lorem.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
#tratar exceção de arquivo inexistente
except FileNotFoundError as exc:
  print("Arquivo não encontrado. Verifique o nome.")
  print(exc)
#tratar exceção de acesso negado
except PermissionError as exc:
  print("Acesso negado")
  print(exc)
except Exception as exc:
  print(f"Algum problema foi encontrato: {exc}")