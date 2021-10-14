bandwidth = {} 
headers = ('Timestamp','Server','Interface Name','Bandwidth Utilization')
OUTPUT = "{} {} {} {}"

def parsecsv(csvpath):
    with open(csvpath) as csvfile:
        contents = csvfile.read().strip()
        row = [line.split(',') for line in contents.split('\n')]
        row.pop(0)
    return row

def getBandwidthValues():
    for Server, InterfaceName, Bandwidth_value in parsecsv('bandwidth.csv'):
        bandwidthHash = hash(Server+InterfaceName)
        bandwidth [bandwidthHash] = Bandwidth_value

def printNetworkBandwidthUtilization():
    print(OUTPUT.format(*headers))
    for Timestamp, Server, InterfaceName, NetBitRate in parsecsv('netbitrate.csv'):
        Bandwidth_value = bandwidth[ hash(Server+InterfaceName) ]
        network_bandwidth_utilization = float(NetBitRate) / float(Bandwidth_value)
        print(OUTPUT.format(Timestamp, Server, InterfaceName, network_bandwidth_utilization))

getBandwidthValues()
printNetworkBandwidthUtilization()