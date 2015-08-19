========================
DariusPull.py User Guide
========================

DariusPull is a simple python script that pulls matches data given a file of match ids. 
This script depends on a open-source tool riot-watcher, to install that tool, run:
	$ pip install riotwatcher
or: 
	$ python setup.py install

If you are running into problem "InsecurePlatformWarning: A true SSLContext object is not available.", 
you only need to install the security package extras (thanks @admdrew for pointing it out)
	$ pip install requests[security]
or, install them directly:
	$ pip install pyopenssl ndg-httpsclient pyasn1

Before you are running DariusPull.py, you need to specify API key and region in the script.

Then, you are good to go. e.g.
	$ python DariusPull.py BILGEWATER/NA.json