#!env/bin/python3
import json, os
import datetime as dt 
class API:
    def get_historical(self, ticker, option_type, expiration, date_slice: tuple = None):
        for process in os.listdir('checkpoints/'):
            for name in os.listdir(f"checkpoints/{process}"):
                print(name) 
                print(f"{ticker}-{option_type}-OPT-{expiration}" in name)

                if f"{ticker}-{option_type}-OPT-{expiration}" in name:
                    with open(f"./checkpoints/{process}/{name}", 'r') as f: 
                        active = json.loads(f.read())
                        dataset = []
                        start_date = date_slice[0].split('-')
                        start_date = dt.datetime(start_date[0], start_date[1], start_date[2])
                        #end_date = dt.
                        for key in active.keys():
                            pass

                        return active
                            



if __name__ == "__main__":
    x = API()
    print(x.get_historical('MSFT', 'PUT', '2020-11-27', date_slice=('2020-11-23 16:34:55', '2020-11-23 17:34:55')))



                        
