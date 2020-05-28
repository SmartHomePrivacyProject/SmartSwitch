#!/usr/bin/env python3.6


import ipaddress
import sys
from pathlib import Path
import pandas as pd
import csv
import os
from scapy.all import *


def pcap_converter(pcap_path, echo_ip, dst):
    """
    Take the pcap files, convert to a list, break list into trace files based of number of queries,
    save sublists to csv files after extracting relevant packet information.
    :param pcap_path:
    :param echo_ip: IPv4 address of the Amazon Echo
    :param burst_ranges: list of tuples in the form (f_p, l_p) where f_p is the first packet in the burst and l_p is the
                         last
    :return: nothing. saves pandas dataframes in csv format
    """
    csv_path =  dst + '/'
    pf = Path(pcap_path)
    trace_name = pf.name[0:-5]
    p_list = rdpcap(pcap_path)

    echo_df = pd.DataFrame(columns=['time', 'size', 'direction'])
    p_list.reverse()

    echo_packets = []
    for p in p_list:
        try:
            p[IP].src
            p[TCP]
        except:
            continue
        if p[IP].src.strip() == echo_ip.strip() or p[IP].dst.strip() == echo_ip.strip():
            if p[TCP] and p.len < 60: #filter ACk packets
                continue
            else:
                echo_packets.append(p)
    p_list = echo_packets

    init_time = p_list[-1].time
    # print("Number of packets in csv files: {}" .format(len(p_list)))
    for p in p_list:
        # 1 if echo is src, -1 if destination
        if p[IP].src == echo_ip:
            p[IP].src = 1
        elif p[IP].dst == echo_ip:
            p[IP].src = -1
        else:
            p[IP].src = 0

        # Update the df with correct index
        # echo_df.loc[-1] = [p.time - init_time, p.len, p[IP].src, p[IP].proto]
        echo_df.loc[-1] = [(p.time - init_time)/1000, p.len, p[IP].src]
        echo_df.index = echo_df.index + 1

        # Sort, so list starts in non-reverse order, save to csv
    echo_df = echo_df.sort_index()
    echo_df.to_csv(csv_path + trace_name + ".csv", index=False)


def main(argv):

    pcap_path = argv[0]
    # print(pcap_path)
    echo_ip = argv[1]
    dst = argv[2]
    folder_list = dst.split(os.sep)
    dst = '/home/erc/PycharmProjects/VideoCollection/csv/' + folder_list[-2] + '/' + folder_list[-1]
    # print(dst)
    if not os.path.isdir(dst):
        os.makedirs(dst)
        # pass
    try:
        ipaddress.ip_address(echo_ip)
    except ValueError:
        print("ValueError: You did not enter a valid IPv4 address")

    pf = Path(pcap_path)
    if not pf.is_file():
        raise FileNotFoundError("No file exists at specified path" + pcap_path)
    # print('pcap file ' + pf.name + ' loaded.')
    print('Running burst detection...')

    pcap_converter(pcap_path, echo_ip, dst)
    print(pf.name + 'is finished')



if __name__ == "__main__":

    main(sys.argv[1:])



