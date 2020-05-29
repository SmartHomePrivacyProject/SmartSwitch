# Usage

1.`loadDriver.py` is used to collect the stream traffic between user and stream provider. 

  The input includes: 
  
  `list_path` the csv file which records the webpage address.
  
  `ip` the local ip address.
  
  `timeout` duration of each traffic trace.
  
  `iteration` number of traces to collect for each video.
  
-```Python3 loadDriver.py [list_path] [ip] [timeout] [iteration]```-

2. `autocollection_pcap2csv.py` is used to transfer pcap files collected via Wireshark to csv files.

-```python3 autocollection_pcap2csv.py [pcap_path] [echo_ip] [csv_path]```-


