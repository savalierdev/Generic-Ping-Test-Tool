import icmplib
import os
from language import FunctionsTranslate

turkishtestserver, globaltestserver, gametestserver, dnstestserver, customtestserver,invalidcategory = FunctionsTranslate()


categories = [turkishtestserver, globaltestserver, gametestserver, dnstestserver, customtestserver]


def listandprintservicelist(category: int):
    if category == 0:
        servicelist = turkishservices
        for i, service in enumerate(servicelist, start=1):
            print(f"{i}-{service.servername}")
        return servicelist
    elif category == 1:
        servicelist = globalservices
        for index, value in enumerate(servicelist, start=1):
            print(f"{index}-{value.servername}")
        return servicelist
    elif category == 2:
        servicelist = gameservers
        for index, value in enumerate(servicelist, start=1):
            print(f"{index}-{value.servername}")
        return servicelist
    elif category == 3:
        servicelist = dnsservers
        for index, value in enumerate(servicelist, start=1):
            print(f"{index}-{value.servername}")
        return servicelist

def list_and_print_categories():
    for index,value in enumerate(categories, start=1):
        print(f"{index}-{value}")
    print("Select the category you want to test...")
    return categories

def get_category_input():
    try:
        categoryinp = int(input("Enter the number of the category you want to test: "))
        category = categoryinp - 1
        if 0 <= category < len(categories):
            return category
        else:
            print(invalidcategory)
            return None
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(invalidcategory)
        exit()

class Service(object):
    def __init__(self,ip,servername):
        self.ip = ip
        self.servername = servername

def getserviceinput(catnum: int):
    service = int(input("Enter the number of the platform you want to test: "))
    if catnum == 0:
        ipnumber = turkishservices[service-1].ip
        return ipnumber
    elif catnum == 1:
        ipnumber = globalservices[service-1].ip
        return ipnumber
    elif catnum == 2:
        ipnumber = gameservers[service-1].ip
        return ipnumber
    elif catnum == 3:
        ipnumber = dnsservers[service-1].ip
        return ipnumber
    elif catnum == 4:
        ipnumber = input("Enter the IP address you want to test: ")
        return ipnumber

def getoperationinput():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1-Ping")
    print("2-Traceroute")
    operation = int(input("Enter the number of the operation you want to perform: "))
    return operation

def resolveip(ip: str):
    pass


def ping_server(ip: str):
    try:
        response = icmplib.ping(ip, count=5, interval=1)
        return response
    except Exception:
        return False
    
def traceroute_server(ip: str):
    pass

globalservices = []
turkishservices = []
gameservers = []
dnsservers = []

# Create a list of Turkish services
turkishservices.append(Service("spd-tr-istanbul.hostlayici.net", "Hostlayıcı Istanbul (Best Server)"))
turkishservices.append(Service("193.192.104.42", "TurkNet Istanbul"))
turkishservices.append(Service("95.173.191.102", "Denizli NetInternet"))
turkishservices.append(Service("5.2.80.47", "Alastyr Izmir"))
turkishservices.append(Service("hiztesti-ist.codit.com.tr", "Codit Teknoloji Istanbul"))
turkishservices.append(Service("hiztesti.codit.com.tr", "Codit Teknoloji İzmit"))

# Create a list of Global services
globalservices.append(Service("speedtest1.synlinq.de", "Frankfurt Synlinq"))
globalservices.append(Service("speedtest.alwyzon.net", "Vienna Alwyzon"))

# Create a list of Game servers
gameservers.append(Service("ae1.er01.ist01.riotdirect.net", "Riot Games Istanbul"))
gameservers.append(Service("ae1.er01.fra02.riotdirect.net", "Riot Games Frankfurt"))
gameservers.append(Service("ae3.er02.waw01.riotdirect.net", "Riot Games Warsaw"))
gameservers.append(Service("ae8.er02.par01.riotdirect.net", "Riot Games Paris"))
gameservers.append(Service("ae2.er02.sto01.riotdirect.net", "Riot Games Stockholm"))
gameservers.append(Service("146.66.155.66", "Valve Corporation Vienna"))
gameservers.append(Service("162.62.97.238", "PUBG Mobile Frankfurt"))
gameservers.append(Service("145.239.131.35","TruckersMP France"))
gameservers.append(Service("193.111.250.18","New Vision HvH CS2 Server"))