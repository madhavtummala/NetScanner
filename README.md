# Network Scanner

A very simple network scanner based on ICMP Requests.
The base ip is extracted from your current ip address and other devices on the same range of local address are sent requests.
If a device is connected, it responds

## Dependencies
fping  
tqdm  

## Instruction
First install fping if not installed  

``brew install fping`` for macOS  
``sudo apt-get install fping`` for linux  

If using python scanner, then install tqmd
``pip install tqmd``

Add execute permission to the files  
``chmod +x scan.sh scanner.py``

## Run
``./scan.sh``
or  
``python scanner.py``

### Note
This is just a basic script to get the ip of active devices on the same local network. This code will be improved to get other details like dnslookup, mac address among others to give a more overall package in future.
