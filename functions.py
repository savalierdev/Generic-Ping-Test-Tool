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
        response = icmplib.ping(ip, count=5, interval=0.2,timeout=2,privileged=True,payload_size=32)
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
turkishservices.append(Service("45.141.150.25", "Hostlayıcı DC Istanbul"))
turkishservices.append(Service("212.156.107.82", "Turk Telekom ISTANBUL (FATIH)"))
turkishservices.append(Service("212.156.117.211", "Turk Telekom ISTANBUL (BEYLIKDUZU)"))
turkishservices.append(Service("212.156.117.187", "Turk Telekom ISTANBUL (ATAKOY)"))
turkishservices.append(Service("212.156.117.62", "Turk Telekom ISTANBUL (ACIBADEM)"))
turkishservices.append(Service("212.156.109.154", "Turk Telekom ISTANBUL (GAYRETTEPE)"))
turkishservices.append(Service("212.156.117.95", "Turk Telekom ISTANBUL (BESIKTAS)"))
turkishservices.append(Service("212.156.107.74", "Turk Telekom ISTANBUL (KADIKOY)"))
turkishservices.append(Service("212.156.108.107", "Turk Telekom BURSA"))
turkishservices.append(Service("212.156.108.125", "Turk Telekom IZMIR"))
turkishservices.append(Service("212.156.108.126", "Turk Telekom EDIRNE"))
turkishservices.append(Service("212.156.108.214", "Turk Telekom ANTALYA"))
turkishservices.append(Service("212.156.108.216", "Turk Telekom ESKISEHIR"))
turkishservices.append(Service("212.156.108.223", "Turk Telekom MANISA"))
turkishservices.append(Service("212.156.108.244", "Turk Telekom ERZURUM"))
turkishservices.append(Service("212.156.108.248", "Turk Telekom MUGLA"))
turkishservices.append(Service("212.156.109.162", "Turk Telekom KUTAHYA"))
turkishservices.append(Service("212.156.117.87", "Turk Telekom KONYA"))
turkishservices.append(Service("212.156.108.81", "Turk Telekom TEKIRDAG"))
turkishservices.append(Service("212.156.120.101", "Turk Telekom TEKIRDAG (CORLU)"))
turkishservices.append(Service("212.156.108.228","Turk Telekom TEKIRDAG (ULAS)"))
turkishservices.append(Service("212.156.108.229", "Turk Telekom TEKIRDAG (ERGENE)"))
turkishservices.append(Service("212.156.117.188","Turk Telekom TEKIRDAG (SARAY)"))
turkishservices.append(Service("212.156.118.228","Turk Telekom TEKIRDAG (CERKEZKOY)"))
turkishservices.append(Service("212.156.120.107", "Turk Telekom HATAY"))
turkishservices.append(Service("212.156.120.105", "Turk Telekom ZONGULDAK"))
turkishservices.append(Service("212.156.118.230", "Turk Telekom ANKARA"))
turkishservices.append(Service("212.156.109.152", "Turk Telekom LULEBURGAZ"))
turkishservices.append(Service("212.156.108.20", "Turk Telekom IZMIR (KARSIYAKA)"))

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

# Create a list of DNS servers
dnsservers.append(Service("1.1.1.1", "Cloudflare"))
dnsservers.append(Service("8.8.8.8", "Google"))