import os # Importa o módulo ou biblioteca o (integra os programas e recurso do s.o)

print("#" * 60) # Imprimindo 60 vezes

ip_ou_host = input("Digite o Ip ou host a ser verifica: ") # Criamos uma variavel que vai receber do usuario um ip
print("-" * 60)  # Imprimindo 60 vezes
os.system('ping -n {}' .format(ip_ou_host)) # Chamando system da biblioteca os - comando ping -mn -num de pacotes que serão 6 {}
print("-" * 60)  # Imprimindo 60 vezes