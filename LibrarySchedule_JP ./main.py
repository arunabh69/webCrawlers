from calendar import monthrange
from bs4 import BeautifulSoup
import requests
import lxml
import csv


if __name__ == '__main__':

    cal = []

    # March, 2022 - December, 2022
    for month in range(4, 13):
        r = requests.get(
            "https://www.lib.hiroshima-u.ac.jp/index.php?action=calendar_view_main_init&date=2022" + "{:0>2}".format(
                month) + "&display_type=2&opac_dispArea=4&page_id=343&block_id=875&module_id=19&_token=0867c9ced6c7551e80f9f04c0c000651&_header=0&_=#")
        soup = BeautifulSoup(r.text, "lxml")

        for day in range(1, monthrange(2022, month)[1] + 1):
            color = soup.find(class_="carendar_2022" + "{:0>2}".format(month) + "{:0>2}".format(day))['style']
            if color == "background-color:#ccffcc;":
                cal.append(["Open", "2022-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "08:30 AM",
                            "2022-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "21:00 PM"])
            elif color == "background-color:#33CCFF;":
                cal.append(["Open", "2022-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "12:00 PM",
                            "2022-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "21:00 PM"])
            elif color == "background-color:#FFFF80;":
                cal.append(["Open", "2022-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "10:00 AM",
                            "2022-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "17:00 PM"])

    
    # January, 2023 - March, 2023
    for month in range(1, 4):
        r = requests.get(
            "https://www.lib.hiroshima-u.ac.jp/index.php?action=calendar_view_main_init&date=2023" + "{:0>2}".format(
                month) + "&display_type=2&opac_dispArea=4&page_id=343&block_id=875&module_id=19&_token=0867c9ced6c7551e80f9f04c0c000651&_header=0&_=#")
        soup = BeautifulSoup(r.text, "lxml")
        
        for day in range(1, monthrange(2023, month)[1] + 1):
            color = soup.find(class_="carendar_2023" + "{:0>2}".format(month) + "{:0>2}".format(day))['style']
            if color == "background-color:#ccffcc;":
                cal.append(["Open", "2023-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "08:30 AM",
                            "2023-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "21:00 PM"])
            elif color == "background-color:#33CCFF;":
                cal.append(["Open", "2023-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "12:00 PM",
                            "2023-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "21:00 PM"])
            elif color == "background-color:#FFFF80;":
                cal.append(["Open", "2023-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "10:00 AM",
                            "2023-" + "{:0>2}".format(month) + "-" + "{:0>2}".format(day), "17:00 PM"])

    fields = ['Subject', 'Start date', 'Start time', 'End date', 'End time']
    with open('KasumiCalendar.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(cal)
