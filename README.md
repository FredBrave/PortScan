# PortScan
A PortScan with python. I made this tool to practice python, it is a very simple portscan with implemented threads.
# Requirements
```bash
pip3 -r install requirements.txt
```
# Usage
To use this tool you need to specify the port range, the ip and optionally the number of threads.
```bash
python3 PortScan.py -i 10.0.2.119 --portMin 1 --portMax 10000 
*************************************************

[*] Scaning...:

	Ip: 10.0.2.119
	Ports: 1-10000
	Threads: 10
	Date: 2023-06-02 18:47:48.946133 

*************************************************
Open Ports:
	The port 22 is open
	The port 80 is open
	The port 6667 is open
	The port 6697 is open
	The port 8067 is open
```
