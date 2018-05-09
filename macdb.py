import time

class MacDB:

    # Indices for array of data
    MAC_INDEX = 0
    STAT_INDEX = 1
    TIME_INDEX = 2
    COUNT_INDEX = 3
    DURATION_INDEX = 4

    def __init__(self):
        self.macs = {}
        self.tracked = []

    def addmac(self, mac, stat, timestamp):
        count = 1
        if mac in self.macs:
            count = self.macs[mac][self.COUNT_INDEX] + 1

        # Print stat for tracked macs
        duration = 0
        if mac in self.tracked:
            print(stat)
            # add to duration
            duration += int(round(time.time() * 1000)) - self.macs[mac][self.DURATION_INDEX]

        self.macs[mac] = [mac, stat, timestamp, count, duration]

    def printMacs(self):
        for mac in self.macs.keys():
            self.printMac(mac)

    def printMac(self, mac):
        if mac in self.macs:
            mac_info = self.macs[mac]
            print("----")
            print("MAC         : " + mac_info[self.MAC_INDEX])
            print("STAT        : " + mac_info[self.STAT_INDEX])
            print("LAST RECORD : " + str(mac_info[self.TIME_INDEX]))
            print("COUNT       : " + str(mac_info[self.COUNT_INDEX]))
            if mac in self.tracked:
                print("DURATION    : " + str(mac_info[self.DURATION_INDEX]))
            print("----")
        else:
            print("Mac does not exist")

    def track(self, mac):
        if mac not in self.tracked:
            self.tracked.append(mac)

    def untrack(self, mac):
        if mac in self.tracked:
            self.tracked.remove(mac)
            self.macs[mac][self.DURATION_INDEX] = 0