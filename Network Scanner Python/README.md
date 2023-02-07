# Network Scanner

This is a basic network scanner written in Python. The script takes a network prefix as an input and scans the network for active devices by checking if their IP addresses are reachable. The script uses the `socket` library in Python to implement the scanning and the TCP protocol to communicate with devices on the network. 

## Requirements
- Python 3

## Usage
To run the script, open a terminal and navigate to the directory where the script is located. Then, run the following command:

```
python network_scanner.py `<network_prefix>`
```

Replace `<network_prefix>` with the network prefix of the network you want to scan. For example, to scan the network `192.168.1.`, use the following command:

```
python network_scanner.py 192.168.1.
```

The script will scan the network and print the results to the terminal. The results will show the IP addresses of active devices on the network and their hostnames (if available).

## Explanation

The script starts by defining a function get_host_name that takes an IP address as an input and returns the hostname associated with that IP address. The hostname is obtained using the gethostbyaddr method of the socket library.

The scan_network function takes a network prefix as an input and scans the network for active devices. The function uses a for loop to iterate through all IP addresses in the range from `<network_prefix>1` to `<network_prefix>255`. For each IP address, the function creates a TCP socket and uses the connect_ex method to check if the target IP address is reachable. If the connection is successful, the function prints the IP address and hostname of the active device. If the connection is not successful, the function prints that the IP address is inactive.

The main part of the script checks if the network prefix has been provided as a command line argument. If the network prefix is provided, the scan_network function is called with the network prefix as an argument. If the network prefix is not provided, the script prints usage instructions.

<img width="392" alt="screshot network scanner" src="https://user-images.githubusercontent.com/83719998/217146015-c5dae1cd-9569-4b2c-99f9-07f2f2aa42a2.png">
