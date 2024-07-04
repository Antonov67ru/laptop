from ipaddress import ip_network
net = ip_network("114.208.0.0/255.248.0.0", strict=False)
binAddr = [f"{address:b}" for address in net]
counter = 0
for address in binAddr:
    if address.count("1") % 3 != 0:
        counter += 1

print(counter)