import network
import socket
import time
from m5stack import *

# WiFi credentials
SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

# Initialize M5Stack
m5.stack = M5Stack()  # Create M5Stack instance

# Connect to WiFi
def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    print('Connecting to WiFi...')
    while not wifi.isconnected():
        time.sleep(1)
    print('Connected to WiFi!')

# Send screenshot command
def send_screenshot():
    addr = socket.getaddrinfo('192.168.1.100', 8080)[0]  # Change IP to your server
    s = socket.socket()
    s.connect(addr)
    s.send(b'screenshot')
    print('Screenshot command sent!')
    s.close()

# Main function
if __name__ == '__main__':
    connect_wifi()  # Connect to WiFi
    while True:
        send_screenshot()  # Send snapshot command periodically
        time.sleep(60)  # Change the interval as needed
