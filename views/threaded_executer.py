from main_function import *
import threading
import time
# get list of links from video_urls.txt
tiktok_links = [line.strip() for line in open("../video_urls.txt", "r").readlines()]

# Threads erstellen
threads = []
for link in tiktok_links:
    t = threading.Thread(target=main, args=(link,))
    time.sleep(5)
    threads.append(t)
    t.start()  # start each thread
