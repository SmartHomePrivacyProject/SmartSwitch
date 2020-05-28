import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException as wde
import pyshark
import csv
import sys
import os


def web_crawler(category, address, ip, timeout, idx):

    # for i in range(start_idx, iterations):
    chrome_options = Options()
    # chrome_options.binary_location = "usr/bin/"
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--disable-dev-shm-usage')
    try:
        driver = webdriver.Chrome('driver/chromedriver',chrome_options=chrome_options)  # Optional argument, if not specified will search path.
    except wde as e:
        print("\nChrome crashed on launch:")
        print(e)
        print("Trying again in 10 seconds..")
        time.sleep(10)
        driver = webdriver.Chrome('driver/chromedriver',chrome_options=chrome_options)
        print("Success!\n")
    except Exception as e:
        raise Exception(e)
    driver.get(address)
    driver.switch_to.frame(0)
    time.sleep(1)  # Let the user actually see something!
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ytp-play-button ytp-button']")))
    # a = button.get_attribute("aria-label")
    if button.get_attribute("aria-label")=='Play (k)':
        print('start to play')
        button.click()
    else:
        print('video is already playing')

    filter = 'ip host ' + ip + ' || tcp'

    print(category + '_' + str(idx) + ' is playing... ')
    dst = '/home/erc/PycharmProjects/2019_spring_data/video_pcapFiles/' + category
    if not os.path.isdir(dst):
        os.makedirs(dst)
    capture = pyshark.LiveCapture(interface='enp0s31f6', bpf_filter= filter,
                                  output_file=dst + '/' + category + '_' + str(idx) +'_Chrome.pcap')
    capture.sniff(timeout = float(timeout))

    print(category + '_' + str(idx) +'_Chrome.pcap finished!!')

    capture.close()
    driver.quit()


def main(argv):
    c_name = []
    address = []
    start_idx = []

    lists_p = argv[0]
    ip = argv[1]
    timeout = argv[2]
    iterations = int(argv[3])


    with open(lists_p) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c_name.append(row['category'])
            address.append(row['address'])
            # start_idx.append(int(row['idx']))
    for idx, name in enumerate(c_name):
        web_crawler(name, address[idx], ip, timeout, iterations)


if __name__ == '__main__':
    main(sys.argv[1:])
    
