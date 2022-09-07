import requests

ENDPOINT = 'https://api.taxideli.ru/test/gettime'

def time(request):
    response = requests.post(ENDPOINT).json()
    x =  (response['dataAns'])
    return x




