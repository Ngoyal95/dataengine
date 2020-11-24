#!env/bin/python3
'''
Goal: Record options data to build historical options data set 

'''

import pandas as pd
from datetime import datetime as dt 
import datetime 
from time import sleep
import asyncio
from random import randint 
from termcolor import colored
from listener import Listener
import os 
import json 

class Engine:
    def __init__(self, interval: int = 60, checkpoints_enabled: bool = True, checkpoints_interval: int = 1, market_hours_only: bool = True):
        self.listeners = []
        self.interval = interval
        self.iteration = 0
        self.checkpoints_interval = checkpoints_interval
        self.checkpoints_enabled = checkpoints_enabled
        self.market_hours_only = True

    def add(self, listener: Listener):
        lid = randint(1000, 9999)
        listener.id = lid 
        self.listeners.append(listener)
        print(f"[INFO] Created new listener with ID {lid}")
    
    def update_listeners(self):
        for l in self.listeners:
            try: 
                _, _ = l.update(test=False)
            except ValueError: 
                continue
    
    def create_checkpoint(self, listener, option_type: str, data: dict):
        filename = f"checkpoints/{listener.id}/{listener.symbol}-{option_type}-{listener.equity_type}-{listener.expiration}.json"
            
        data = json.dumps(data)
        with open(filename, 'w') as f:
            f.write(data)


    def save_checkpoint(self):
        for listener in self.listeners:
            
            if "checkpoints" not in os.listdir('./'):
                try: 
                    os.mkdir('checkpoints')
                except FileExistsError:
                    pass
            
            if listener.id not in os.listdir('./checkpoints/'):
                try: 
                    os.mkdir(f"./checkpoints/{listener.id}")
                except FileExistsError:
                    pass
            self.create_checkpoint(listener, 'CALL', listener.data_calls)
            self.create_checkpoint(listener, 'PUT', listener.data_puts)
                


    def start(self, kill):
        while True:
            current_time = dt.now() 
            start_time = current_time.replace(hour=7, minute=30, second=0, microsecond=0)
            end_time = current_time.replace(hour=14, minute=0, second=0, microsecond=0)
            
            if current_time > start_time and current_time < end_time: # make sure market is open
                sleep(self.interval)
                self.update_listeners()
                self.iteration += 1
                
                if self.iteration % self.checkpoints_interval == 0 and self.checkpoints_enabled:
                    self.save_checkpoint()
            else: 
                print(colored("[HALT] Market is not open"))
                sleep(self.interval)

