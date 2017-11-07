#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:42:30 2017

@author: ratnadeepb
@license: MIT

This is a tutorial on getting the price action
"""

import oandapyV20
import oandapyV20.endpoints.pricing as pricing
from os import environ
import json

########### Account Setup ###########
account_id = environ.get("oanda_ac", None)
if account_id == None:
    print("Undefined account ID")
account_key = environ.get("oanda_key", None)
if account_key == None:
    print("Undefined account key")

api = oandapyV20.API(access_token=account_key)

######## Get Pricing info for a list of instruments within an account #######

params = {
        "instruments": "USD_JPY,USD_INR,GBP_USD,EUR_USD"
        }
r = pricing.PricingInfo(accountID=account_id, params=params)
api.request(r)
print(r.response)
pricing = r.response['prices']

######## Get realtime pricing on instruments #########

r = pricing.PricingStream(accountID=account_id, params=params)
rv = api.request(r)
maxrecs = 10
for tick in rv:
    print(json.dumps(tick, indent=4), ",")
    maxrecs -= 1
    if maxrecs == 0:
        try:
            r.terminate("Max records received")
        except oandapyV20.exceptions.StreamTerminated as e:
            print(e)