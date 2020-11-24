#!env/bin/python3
from main import Engine
import pandas as pd 
from threading import Thread
import threading 
from listener import Listener
from termcolor import colored
from sys import exit
import os 

class Console:
    def __init__(self, engine):
        self.engine = Engine()
        self.kill = False
    
    def engine(self):
        self.engine = Engine()


    def shell(self, _ = None):
        print('Type help to view commands; e to exit')
        while True:
            x = input(colored('console> ', 'blue'))
            args = x.split(' ')
            if args[0] == 'add': #exampe: console> add AAPL OPT 2020-11-27
                try:
                    new_listener = Listener(args[1], args[2], args[3])
                    self.engine.add(new_listener)
                except e:
                    print('error', e)

            elif args[0] == 'stop':
                if len(args) > 1: #stop listnener by id 
                    for listener in self.engine.listeners:
                        if listener.id == int(args[1]):
                            self.engine.listeners.remove(listener)

                else:  # stop all listeners
                    confirm = input('Stop all listeners [y/n]: ').lower()
                    if confirm == 'y':
                        self.engine.listeners = []

            elif args[0] == 'start':
                self.threadx = Thread(target=self.engine.start, args=(self.kill,))
                self.threadx.daemon = True 
                self.threadx.start() 
                
            elif args[0] == 'exit' or args[0] == 'e':
                exit()

            elif args[0] == 'dump':
                df = pd.DataFrame(self.engine.data)
                df.to_csv('dump.csv')

            elif args[0] == 'load':
                
                if len(args) == 2:
                    filename = args[1]
                else: 
                    filename = input('Filename: ')

                with open(filename, 'r') as f: 
                    recorders = f.readlines()
                
                for recorder in recorders: 
                    recorder = recorder.replace('\n', '')
                    arguements = recorder.split(' ')
                    new_listener = Listener(arguements[0], arguements[1], arguements[2])
                    self.engine.add(new_listener)


            elif args[0] == 'list':
                if len(self.engine.listeners) == 0:
                    print("No listeners yet. Type 'add' to add one!")
                else: 
                    print("  ID | Description")
                    print("-----+-------------------------")
                    for listener in self.engine.listeners:
                        print(f"{listener.id} | ", end="")
                        if listener.equity_type == 'OPT':
                            print(f"Recording {listener.symbol} Options with {listener.expiration} expiration")

            elif args[0] == 'help':
                print("""
                Command     |   Description             |   Syntax 
                add         | Creates a new listener    | add TICKER TYPE EXPIRATION   ex. add MSFT OPT 2020-11-27
                start       | Start all listeners       | start
                stop        | Stop a listener           | stop LISTENER_ID  or stop (to stop all)
                load        | Load listeners from file  | load file.txt or load 
                list        | List active listeners     | list
                exit        | Exit CLI                  | exit
                """)

            elif args[0] == 'generate':
                lines = []
                tickers = input('Enter stock tickers seperated by comma: ').replace(' ', '').split(',')
                dates = input('Enter Expiration dates: ').replace(' ', '').split(',')
                for ticker in tickers: 
                    for date in dates:
                        lines.append(f"{ticker} OPT {date}")

                filename = input("Filepath to write load file: ")
                with open(f"./{filename}", 'w') as f:
                    f.write('\n'.join(lines))

                confirm = input(f"Do you want to load {filename}? [y/n]: ").lower()
                if confirm == 'y':
                    for recorder in lines: 
                        recorder = recorder.replace('\n', '')
                        arguements = recorder.split(' ')
                        new_listener = Listener(arguements[0], arguements[1], arguements[2])
                        self.engine.add(new_listener)




if __name__ == "__main__":
    x = Engine(checkpoints_enabled=True, checkpoints_interval=3)

    c = Console(x)
    c.shell()


#c = Console(x)
#thread2 = Thread(target = c.shell, args=(11, ))
#thread2.daemon = True
#thread2.run()
