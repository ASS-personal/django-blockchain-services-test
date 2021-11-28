import pandas as pd

from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blockchain.models import L3BTCUSDAsks, L3BTCUSDBids

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PurchaseView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        serializer_class=[],
        operation_description="Get purchase statistics data.",
        manual_parameters=[],
        responses={
            status.HTTP_200_OK: 'OK'
        }
    )
    def get(self, request):
        res = {'bids': {}}
        res_bids = {}
        bids_list = list(map(lambda x: x.to_dict(), L3BTCUSDBids.objects.all()))

        bids_df = pd.DataFrame(bids_list)
        value_column = bids_df["value"]
        # Get mean value
        res_bids.update({'average_value': round(value_column.mean(), 2)})
        # Get max value index
        max_index = value_column.idxmax()
        res_bids.update({'greater_value': bids_df.loc[max_index].to_dict()})
        # Get min value index
        min_index = value_column.idxmin()
        res_bids.update({'lesser_value': bids_df.loc[min_index].to_dict()})
        # Get total qty value
        qty_column = bids_df["qty"]
        res_bids.update({'total_qty': round(qty_column.sum(), 2)})
        # Get total px value
        px_column = bids_df["px"]
        res_bids.update({'total_px': round(px_column.sum(), 2)})

        res['bids'] = res_bids
        return Response(res)

class SalesView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        serializer_class=[],
        operation_description="Get sales statistics data.",
        manual_parameters=[],
        responses={
            status.HTTP_200_OK: 'OK'
        }
    )
    def get(self, request):
        res = {'asks': {}}
        res_asks = {}
        asks_list = list(map(lambda x: x.to_dict(), L3BTCUSDAsks.objects.all()))

        asks_df = pd.DataFrame(asks_list)
        value_column = asks_df["value"]
        # Get mean value
        res_asks.update({'average_value': round(value_column.mean(), 2)})
        # Get max value index
        max_index = value_column.idxmax()
        res_asks.update({'greater_value': asks_df.loc[max_index].to_dict()})
        # Get min value index
        min_index = value_column.idxmin()
        res_asks.update({'lesser_value': asks_df.loc[min_index].to_dict()})
        # Get total qty value
        qty_column = asks_df["qty"]
        res_asks.update({'total_qty': round(qty_column.sum(), 2)})
        # Get total px value
        px_column = asks_df["px"]
        res_asks.update({'total_px': round(px_column.sum(), 2)})

        res['asks'] = res_asks
        return Response(res)

class GeneralView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        serializer_class=[],
        operation_description="Get general purchase and sales data.",
        manual_parameters=[],
        responses={
            status.HTTP_200_OK: 'OK'
        }
    )
    def get(self, request):
        res = {'BTC-USD': {'bids': {}, 'asks': {}}}
        res_bids = {}
        res_asks = {}
        bids_list = list(map(lambda x: x.to_dict(), L3BTCUSDBids.objects.all()))
        asks_list = list(map(lambda x: x.to_dict(), L3BTCUSDAsks.objects.all()))

        bids_df = pd.DataFrame(bids_list)
        asks_df = pd.DataFrame(asks_list)

        bids_qty_column = bids_df["qty"]
        asks_qty_column = asks_df["qty"]
        bids_value_column = bids_df["value"]
        asks_value_column = asks_df["value"]

        #Contador de lineas
        res_bids.update({'count': bids_qty_column.count()})
        res_asks.update({'count': asks_qty_column.count()})
        # Get total qty value
        res_bids.update({'qty': round(bids_qty_column.sum(), 2)})
        res_asks.update({'qty': round(asks_qty_column.sum(), 2)})
        # Get total value
        res_bids.update({'value': round(bids_value_column.sum(), 2)})
        res_asks.update({'value': round(asks_value_column.sum(), 2)})

        res['BTC-USD']['bids'] = res_bids
        res['BTC-USD']['asks'] = res_asks
        return Response(res)
