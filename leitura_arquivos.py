arquivo = open("lorem.txt", "r")
#print(arquivo.readline())

for linha in arquivo.readlines():
  print(linha)
arquivo.close()