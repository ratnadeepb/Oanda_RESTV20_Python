#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 06:23:03 2017

@author: ratnadeepb
@license: MIT

This is simply a tutorial module dealing with account changes in oandapyv20
"""

import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.trades as trades
from os import environ

########### Account Setup ###########
account_id = environ.get("oanda_ac", None)
if account_id == None:
    print("Undefined account ID")
account_key = environ.get("oanda_key", None)
if account_key == None:
    print("Undefined account key")

api = oandapyV20.API(access_token=account_key)

############ List of trades #############

r = trades.TradesList(accountID=account_id)
api.request(r)
print(r.response['lastTransactionID'])
print(r.response['trades'])

############ Account changes ###########

params = {
        "sinceTransactionID": 3
        }
r = accounts.AccountChanges(accountID=account_id, params=params)
api.request(r)
print(r.response)

############# Account Details ##############

r = accounts.AccountDetails(accountID=account_id)
api.request(r)
print(r.response)

############# Account Instruments #############

r = accounts.AccountInstruments(accountID=account_id)
api.request(r)
from os import chdir
chdir("..")
with open("Oanda_Currency_List.txt", "w") as tl:
    for elem in r.response["instruments"]:
        if elem['type'] == "CURRENCY":
            tl.write("{} : {}\n".format(elem['name'], elem['displayName']))
chdir("scripts")

############# Asking for specific instruments ############
params = {
        "instruments": "EU50_EUR,EUR_USD,US30_USD,FR40_EUR,EUR_CHF,DE30_EUR"
        }

r = accounts.AccountInstruments(accountID=account_id, params=params)
api.request(r)
for elem in r.response["instruments"]:
    print("{} : {}\n".format(elem['name'], elem['displayName']))


############# Account Summary #############
r = accounts.AccountSummary(accountID=account_id)
api.request(r)
print(r.response['account'])
print(r.response['lastTransactionID'])