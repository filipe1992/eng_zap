from django.shortcuts import render
import json, requests
from threading import Thread
import time
from io import BytesIO
# Create your views here.

from django.http import HttpResponse
from _ast import In


def get_token(username='admin',password='Yk9v5eN4W.D6Eo95', url='http://169.61.31.222:8118/'):
    dados = json.dumps({'username': username, 'password': password })
    resposta = requests.post(url+'auth',data=dados)
    return resposta.json()['token']

def gerar_login(token, url='http://169.61.31.222:8118/'):
    cabeca = {'Authorization': 'Bearer '+token }
    resposta = requests.get(url+'login/generate', headers=cabeca)

def get_login(token, url='http://169.61.31.222:8118/'):
    time.sleep(2)
    cabeca = {'Authorization': 'Bearer '+token }
    resposta = requests.get(url+'login/get', headers=cabeca)
    
    return BytesIO(resposta.content)
    
def gerar_js_code(token, url='http://169.61.31.222:8118/'):
    code = '''
    
    '''
    return code

def index(request, token):
    #'''
    gerar= Thread(target=gerar_login,args=[token])
    gerar.start()
    a = get_login(token)
    #'''
    return HttpResponse(a.getvalue(), content_type="image/jpeg")

def index_01(request):
    token = get_token()
    print(token)
    return render(request, 'init.html',{'token': token,
                                        'numero': '91981440196',
                                        'text': 'teste de envio de dados'})
    #HttpResponse(token)
    #return index(request, token)

