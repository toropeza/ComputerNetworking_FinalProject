from scapy.all import *
from threading import Thread
from macdb import MacDB
import re

# Dictionary mapping all of the routes
macdb = MacDB()
running = True

def usage():
    print("Available actions")
    print("     -h (Help)")
    print("     list (List all known MAC Addresses on the current Network)")
    print("     stat <MAC> (Lists all of the stored data from the found MAC Address)")
    print("     track <MAC> (Will start to listen for all packets coming from the given MAC Address)")
    print("     untrack <MAC> (Will stop listening for packets from the given MAC Address)")
    print("     exit (Closes the application)")

def run_sniff():
    while running:
        # -I indicates "monitor mode" && -c specifies to listen for only one packet
        proc = subprocess.Popen(['tshark', '-I', '-c 1'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stat = proc.communicate()[0][68:].decode('utf-8')
        searchObj = re.search(r"([0-9A-F]{2}[:-]){5}([0-9A-F]{2})", stat, re.I)

        if searchObj:
            mac_addr = searchObj.group().strip(" ")
            macdb.addmac(mac_addr, stat, datetime.now().time())

def list():
    macdb.printMacs()

def stat(mac):
    macdb.printMac(mac)

def track(mac):
    macdb.track(mac)

def untrack(mac):
    macdb.untrack(mac)

if __name__ == '__main__':
    thread = Thread(target=run_sniff)
    thread.start()

    running = True
    while (running):
        action = input("Enter command or help for more info:\n")
        if action == "help":
            usage()
        elif action == "list":
            list()
        elif action == "stat":
            mac = input("Enter MAC:\n")
            stat(mac)
        elif action == "track":
            mac = input("Enter MAC:\n")
            track(mac)
        elif action == "untrack":
            mac = input("Enter MAC\n")
            untrack(mac)
        elif action == "exit":
            running = False
        else:
            print("Invalid command")
            usage()
