import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não está acessível no momento')
else:
    print('tudo ok!, o site foi acessado com sucesso!')
    print(site.read())
