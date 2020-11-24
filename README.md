# DataEngine
Record stock options data live from the markets and be able to replay it later


## Install
I recommend running with a virtualenv, which you can create by running:

`python3 -m pip venv env`

Then activate the venv:

`source venv/bin/activate` 

Install dependencies: 

`pip3 install -r requirements.txt`

## Usage
The first thing you'll want to do is make sure you have executable privelleges. Confirm by running:
`chmod +x console.py` 
Then, run it:
`./console.py` or `python3 console.py`

You'll be greeted with a shell prompt `console >`. Type help for a list of commands.

### Basic Usage
The easiest way to get started with a recorder, is by using the `add` command. The syntax is as follows:

`add {ticker} OPT {expiry YYYY-MM-DD}`

Here's an example:

`add AAPL OPT 2020-11-27`

Then you can start recording by typing `start`. You can view the current running listeners by typing `list`:

```
console> add AAPL OPT 2020-11-27
[INFO] Created new listener with ID 1308
console> list
  ID | Description
-----+-------------------------
1308 | Recording AAPL Options with 2020-11-27 expiration
console>
```

The `checkpoints/` directory will automatically be generated, and within it you will find two JSON files for both calls and puts. 

To stop all listeners, type `stop`. To stop a listener by ID, type, `stop {id}`

### Bulk Usage
It may be useful to record hundreds or thousands of options at the same time, and you can do so but entering them one by one may be time consuming.

To enter commands by bulk, you can run the `generate` command; Then enter the tickers and expirations and it will add a listener for all possible combinations, like so: 

<pre>
<b>console> generate</b>
Enter stock tickers seperated by comma: <i>AAPL, MSFT, MU</i>
Enter Expiration dates: <i>2020-11-27, 2020-12-4</i>
Filepath to write load file: <i>example.txt</i>
Do you want to load example.txt? [y/n]: <i>y</i>
[INFO] Created new listener with ID 6413
[INFO] Created new listener with ID 2124
[INFO] Created new listener with ID 7076
[INFO] Created new listener with ID 2053
[INFO] Created new listener with ID 7492
[INFO] Created new listener with ID 9175
<b>console> list</b>
  ID | Description
-----+-------------------------
1308 | Recording AAPL Options with 2020-11-27 expiration
6413 | Recording AAPL Options with 2020-11-27 expiration
2124 | Recording AAPL Options with 2020-12-4 expiration
7076 | Recording MSFT Options with 2020-11-27 expiration
2053 | Recording MSFT Options with 2020-12-4 expiration
7492 | Recording MU Options with 2020-11-27 expiration
9175 | Recording MU Options with 2020-12-4 expiration
<b>console></b>
</pre>

Note: user inpput is italicized

This command will create the `example.txt` file that you can reload later by using the `load` command. 

### Loading
To load a list of recorders in either from a generated file or from a hand generated one, simply type `load` or `load {filename}`
