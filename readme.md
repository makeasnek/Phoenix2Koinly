# Phoenix2Koinly
This python script will help you convert your exported transactions from Phoenix (CSV) into the format Koinly needs. Python 3 is required to run this. It will run on Windows, Linux, and OS X. 

# How to use:
1. Open your Phoenix wallet and export your transactions in a CSV file.
2. Transfer the CSV file to your machine with python running on it. E-mail is probably the simplest way.
3. (optional, suggested) Place your CSV file into the same directory as this script and name it `phoenix.csv`. If you don't do this, the script will prompt you for absolute paths, (in Windows, right click on CSV file and select properties to find this)
4. Run the script with `python main.py` (see platform-specific instructions below)
5. output.csv will be created, which you can import into Koinly
6. Make a donation if this script has been useful (see below for more information)


<h4>Windows</h4>

 - Download the latest version of python from python.org. Enable the "install to system path" option while installing.
 - Double-click main.py or in command prompt, run `python C:\users\username\Downloads\Phoenix2Koinly\main.py` or wherever you saved the tool. I suggest the command prompt method as it will display errors if there are any.

<h4>Linux</h4>

 - Open a terminal and go to the folder you downloaded this tool into using `cd '/home/user/Downloads/Phoenix2Koinly'` or wherever you put it
 - Run `python3 main.py` in the terminal

<h4>OS X</h4>

 - Open a terminal and go to the folder you downloaded this tool into using `cd '/home/user/Downloads/Phoenix2Koinly'` or wherever you put it
 - Run `python3 main.py`

# How to import Phoenix wallet to Koinly

To import your Phoenix wallet data to Koinly, use this script!

# Donation

If this software was helpful to you, please consider sending me some sats as a thank you.

🕐 On-chain: bc1q4zqhmyp8yw4zehw2tf4sjvqc5dv9dm747ssh0p

⚡ Lightning: makeasnek@zeuspay.com 

![Screenshot_2025-01-15-23-23-03-12_fe3a99db156b37a8caccf406cb4af884](https://github.com/user-attachments/assets/f199cd5d-c0dc-458e-bbd6-ad9a929da222)

Follow me on nostr: https://njump.me/nprofile1qythwumn8ghj7mrp9eex2mrp09skymr99ehhyee0qy2hwumn8ghj7cmpwfkx7uedvdjxytn5dacz7qpq2xgsu4nad7np6l3e9x8exf26evs202jqkc2ghnuyw4c7hrda9cmq62nshv

# Contributions

Feel free to open PRs if you have any fixes or enhancements to add

# Warranty

This software is produced AS IS without ANY WARRANTY. It works well for me, it may not work perfectly for you. Be sure to double-check any numbers it comes up with. This software is released into the public domain. 
