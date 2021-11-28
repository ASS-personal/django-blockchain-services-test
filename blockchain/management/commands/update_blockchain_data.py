from django.core.management.base import BaseCommand, CommandError

import requests
import json

from blockchain.models import L3BTCUSDBids, L3BTCUSDAsks

class Command(BaseCommand):
    help = 'Args'

    # def add_arguments(self , parser):
    #     parser.add_argument(
    #         'key',
    #         type=str,
    #         nargs='?',
    #         default=''
    #     )

    def handle(self, *args, **options):
        url = 'https://api.blockchain.com/v3/exchange/l3/BTC-USD'
        headers = {'accept': 'application/json'}
        payload = {}
        response = json.loads(requests.get(url, payload, headers=headers, timeout=180).text)

        #Eliminamos todos los valores actuales.
        L3BTCUSDBids.objects.all().delete()
        L3BTCUSDAsks.objects.all().delete()

        for bid in response['bids']:
            bid.update({'value': bid['qty'] * bid['px']})
            L3BTCUSDBids.objects.create(**bid)
        for ask in response['asks']:
            ask.update({'value': ask['qty'] * ask['px']})
            L3BTCUSDAsks.objects.create(**ask)
