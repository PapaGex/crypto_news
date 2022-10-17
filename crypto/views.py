from django.shortcuts import render


def home(request):
    import requests
    import json

    # price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    # crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})
