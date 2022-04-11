import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Hostname: {}".format(hostname))
print("IP Address: {}".format(ip_address))