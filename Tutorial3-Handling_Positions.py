#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:28:55 2017

@author: ratnadeepb
@license: MIT

This is a tutorial on handling positions
"""

import oandapyV20
import oandapyV20.endpoints.positions as positions
from os import environ

########### Account Setup ###########
account_id = environ.get("oanda_ac", None)
if account_id == None:
    print("Undefined account ID")
account_key = environ.get("oanda_key", None)
if account_key == None:
    print("Undefined account key")

api = oandapyV20.API(access_token=account_key)

########### Get all open positions ############

r = positions.OpenPositions(accountID=account_id)
api.request(r)
print(r.response)
all_positions = r.response['positions']

########## Closing an open position ###########

instrument = "EUR_USD"
data = {
        "logUnits": "10",
        "longClientExtensions": "Close 10 units of long positions in {}".format(instrument)
        }
r = positions.PositionClose(accountID=account_id,
                            instrument=instrument,
                            data=data)
api.request(r)
print(r.response)

########## Position Details ############

instrument = "USD_JPY"
r = positions.PositionDetails(accountID=account_id, instrument=instrument)
api.request(r)
print(r.response)

########## List of all positions ##########

r = positions.PositionList(accountID=account_id)
api.request(r)
print(r.response)