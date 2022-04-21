## NEPSE IPO Price Monitor

This is a program that uses Python BeautifulSoup to fetch data from [MeroLagani](https://merolagani.com) and on the basis of the percentage change, it alerts the user. 

If it has a -ve percent change then only an alert message is generated. It uses Discord Webhook and Desktop Notification for the alerts.

NOTE: The program is only applicable for IPO's. Because once the price starts decreasing it takes a very long time to reach the all-time high. 

## Features

- Desktop Notifications
- Discord Webhook
- Cross-platform
- Real-Time data


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`WEB_HOOK_URL`

`USERNAME`


## Installation

Requires python3 to be installed on your computer.

```
git clone https://github.com/r3alix01/IPO-Monitor-NEPSE
cd IPO-Monitor-NEPSE
python3 install -r requirements.txt
```
    
## Usage
```
python main.py
```
Now let the program run in the background and it will notify you in Real Time.

**MAKE SURE TO CREATE A DISCORD WEBHOOK BEFORE USE TO NEVER MISS OUT NOTIFICATIONS.**