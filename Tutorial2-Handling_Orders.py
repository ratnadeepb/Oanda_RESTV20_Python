#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 07:11:33 2017

@author: ratnadeepb
@license: MIT

This is a tutorial on handling orders
"""

import oandapyV20
import oandapyV20.endpoints.orders as orders
from os import environ

########### Account Setup ###########
account_id = environ.get("oanda_ac", None)
if account_id == None:
    print("Undefined account ID")
account_key = environ.get("oanda_key", None)
if account_key == None:
    print("Undefined account key")

api = oandapyV20.API(access_token=account_key)

########## Limit Order Creation ############

# This is a stop loss order (short) of 1 unit on the EUR_USD pair
# The stop is set within the order
# Client Extensions are also set
data = {
        "order": {
                "price": "1.1560",
                "stopLossOnFill": {
                        "timeInForce": "GTC",
                        "price": "1.1570"
                },
                "timeInForce": "GTC",
                "instrument": "EUR_USD",
                "units": "-1",
                "clientExtensions": {
                        "comment": "Trying the API out",
                        "tag": "beginner",
                        "id": "my_test_order"
                        },
                "type": "LIMIT",
                "positionFill": "DEFAULT"
                }
        }

r = orders.OrderCreate(accountID=account_id, data=data)
api.request(r)
print(r.response)

############ Take Profit Order Creation ###############

# Get ID of the last order
tr_id = r.response['orderFillTransaction']['id']

take_profit = {
        "order": {
                "timeInForce": "GTC",
                "price": "1.1545",
                "type": "TAKE_PROFIT",
                "tradeID": tr_id
                }
        }
r = orders.OrderCreate(accountID=account_id, data=take_profit)
api.request(r)
print(r.response)

############## Trailing Stop Order Creation ###############

trailing_SL = {
        "order": {
                "timeInForce": "GTC",
                "distance": "0.001",
                "type": "TRAILING_STOP_LOSS",
                "tradeID": tr_id
                }
        }
r = orders.OrderCreate(accountID=account_id, data=trailing_SL)
api.request(r)
print(r.response)

############### Cancel an Order ################

r = orders.OrderCancel(accountID=account_id, orderID=tr_id)
api.request(r)
print(r.response)

############### Get Order List ################

r = orders.OrderList(accountID=account_id)
api.request(r)
print(r.response)
trade_ids = r.response['orders']

print(trade_ids)

############### Get Order Detail ################

for order in trade_ids:
    r = orders.OrderDetails(accountID=account_id, orderID=order['id'])
    api.request(r)
    print(r.response)

########### Get Pending Orders #############

r = orders.OrdersPending(accountID=account_id)
api.request(r)
print(r.response)