import random
import string

tamanho = int(input('Digite o tamanho da senha: ')) # Tamanho da senha.
chars = string.ascii_letters + string.digits + '!@$%*()-=,.:;*' # Estrutura da senha gerada.

rnd = random.SystemRandom() # os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))