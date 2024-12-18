from functions import *
from language import MainTranslate


pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,pingjitter,pressanykeyexit = MainTranslate()


def ping():
    print('')
    print(f"{pinging} {serviceip}...", '\n')
    rresp = ping_server(serviceip)
    for index, rtt in enumerate(rresp.rtts, start=1):
        print(f'{index}. {rtt} ms')
    print('')
    print(f"{sendpackets} {rresp.packets_sent}") , '\n'
    print(f"{receivedpackets} {rresp.packets_received}") , '\n'
    print(f'{lowestping} {rresp.min_rtt} ms, {highestping} {rresp.max_rtt} ms, {averageping} {rresp.avg_rtt} ms')
    print(f'{packetloss} {rresp.packet_loss} ') , '\n'
    print(f'{pingjitter}: {rresp.jitter} ms') , '\n'
    print('')
    print(f'{pressanykeyexit}')
    str(input())

def traceroute():
    pass


if __name__ == '__main__':
    list_and_print_categories()
    catnum = get_category_input()
    os.system('cls' if os.name == 'nt' else 'clear')
    listandprintservicelist(catnum)
    serviceip = getserviceinput(catnum)
    operation = getoperationinput()
    if operation:
        if operation == 1:
            ping()
        elif operation == 2:
            print("Traceroute is not available yet.")
    else:
        print(invalidoperation)
        getoperationinput()