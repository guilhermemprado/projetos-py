import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('SHA-256') # SHA-256 e um algoritmo de 256bits.
hash1.update(open(arquivo1, 'rb').read()) # r = abrir em modo leitura, b = abrir em modo binario.

hash2 = hashlib.new('SHA-256') # SHA-256 e um algoritmo de 256bits
hash2.update(open(arquivo2, 'rb').read()) # r = abrir em modo leitura, b = abrir em modo binario.

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')

print('O hash do arquivo a.txt é: ', hash1.hexdigest())
print('O hash do arquivo b.txt é: ', hash2.hexdigest())