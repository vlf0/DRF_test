import requests
from django.shortcuts import render

API_url = 'https://api.mindee.net/v1/products/mindee/invoices/v4/predict'
auth_token = 'baebd7c5b4b751fb0108281af3abf4b3'


def index(request):
    if request.method == 'POST':
        file = request.FILES['invoice']
        headers = {'Authorization': f'Token {auth_token}'}
        # print(API_url, file, headers)
        response = requests.post(API_url, headers=headers, files={'ocument': file})
        if response.status_code == 400:
            return render(request, 'index.html', {'error': response.text})
        return render(request, 'index.html', {'response': response.text})
    return render(request, 'index.html')

