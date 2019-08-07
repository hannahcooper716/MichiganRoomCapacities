from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request as urllib2
import codecs
from pandas import DataFrame
import csv
import sys
import json

# file_name = codecs.open("room_html.html", 'r')
# data = filer_name.read()
# soup = BeautifulSoup(data, 'html.parser')
# #print(soup.prettify())
# classes = soup.find(class_ = 'results_table table-striped')
# hello = classes.find_all(class_ = 'hidden-xs')
# list1 = []
# for y in hello:
#     room_cap = y.text.strip()
#     list1.append(room_cap)
# file_name = "room_capacities.json"
# file_write = open(file_name, "w")
# i = 0
# for item in list1:
#     if i == 0:
#         item = "Capacity"
#     i += 1
#     if i % 2 == 0:
#         file_write.write(item+"\n")
#     else:
#         file_write.write(item+",")
# file_write.close()

# d = pd.DataFrame(list1)
# d.to_excel (r'C:\Desktop\room_capacities.xlsx', index = None, header=True)
f = open('room_capacities.json', 'r')
data = f.readlines()
f.close()

# f = open('room_capacities.csv', 'w')
# csvfile = csv.writer(f)
i = 0
with open('room_capacities.csv', 'w', newline='') as csvfile:
    for item in data:
        if i == 0:
            list_item = item.strip().split(",")
            capacity = list_item[0]
            room_num = list_item[1]
            fieldnames = [capacity, room_num]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        else:
            list_item = item.strip().split(",")
            writer.writerow({capacity: list_item[0] , room_num: list_item[1]})
        i += 1
        # csv_file.writerow(item)
    f.close()
