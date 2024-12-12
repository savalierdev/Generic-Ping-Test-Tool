import icmplib




categories = ["0-Turkish Test Servers", "1-Global Test Servers", "2-Game Test Servers","3-DNS Test Servers"]


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
    else:
        print("Press any key to ping a different platform...")

def list_and_print_categories():
    for category in categories:
        print(category)
    print("Select the category you want to ping...")

def get_category_input():
    category = int(input("Enter the number of the category you want to ping: "))
    return category

class Service(object):
    def __init__(self,ip,servername):
        self.ip = ip
        self.servername = servername

def getserviceinput(catnum: int):
    service = int(input("Enter the number of the platform you want to ping: "))
    if catnum == 0:
        ipnumber = turkishservices[service-1].ip
    elif catnum == 1:
        ipnumber = globalservices[service-1].ip
    elif catnum == 2:
        ipnumber = gameservers[service-1].ip
    elif catnum == 3:
        ipnumber = dnsservers[service-1].ip
    return ipnumber


def ping_server(ip: str):
    try:
        response = icmplib.ping(ip, count=5, interval=0.2)
        return response
    except Exception:
        return False

globalservices = []
turkishservices = []
gameservers = []
dnsservers = []

# Create a list of Turkish services
turkishservices.append(Service("193.192.104.42", "TurkNet Istanbul"))
turkishservices.append(Service("95.173.191.102", "Denizli NetInternet"))
turkishservices.append(Service("5.2.80.47", "Alastyr Izmir"))
turkishservices.append(Service("hiztesti-ist.codit.com.tr", "Codit Teknoloji Istanbul"))
turkishservices.append(Service("hiztesti.codit.com.tr", "Codit Teknoloji İzmit"))

# Create a list of Global services
globalservices.append(Service("speedtest1.synlinq.de", "Frankfurt Synlinq"))
globalservices.append(Service("speedtest.alwyzon.net", "Vienna Alwyzon"))