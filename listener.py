#!env/bin/python3

import yfinance as yf 
from time import sleep
from datetime import datetime as dt
import json 

class Listener:
    def __init__(self, symbol: str, equity_type: str = 'OPT', expiration: str = None):
        self.symbol = symbol
        self.equity_type = equity_type
        self.expiration = expiration
        self.id = None
        self.data_calls = {}
        self.data_puts = {}
    
    def get_chain(self, ticker: str, expiration: str ) -> tuple: 
        stock = yf.Ticker(ticker) 
        option = stock.option_chain(expiration)
        return (option.calls, option.puts)

    def update(self, test: bool = False):
        if self.equity_type == 'OPT':
            assert(self.expiration != None) 
            calls, puts = self.get_chain(self.symbol, self.expiration)
            
            global_index = str(dt.now())
            self.data_calls[global_index] = {} 
            self.data_puts[global_index] = {}
            if test == True:
                print(self.id, " has updated")
            for index, row in calls.iterrows():
                row_index = row['contractSymbol']
                row['lastTradeDate'] = str(row['lastTradeDate'])
                self.data_calls[global_index][row_index] = dict(row)
            
            for index, row in puts.iterrows():
                row_index = row['contractSymbol']
                row['lastTradeDate'] = str(row['lastTradeDate'])
                self.data_puts[global_index][row_index] = dict(row)
            
            return (calls, puts)

        else:
            print('not supported yet')
            pass

    def dump(self, filename: str):
        with open(filename, 'w') as f:
            
            data = json.dumps(listener.data)
            f.write(data)
       



'''
DATASET ORGANIZATION 



| Expiry Date       ex. 2020-11-27
    | Contract      ex. MSFT201127C00300000
        | Price     ex. $0.11
        | ITM       ex. False

'''



