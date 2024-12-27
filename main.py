from functions import *
from language import MainTranslate
from time import sleep
from icmplib import ICMPv4Socket, ICMPv6Socket, ICMPRequest
from icmplib import ICMPLibError, ICMPError, TimeoutExceeded
from icmplib import PID, is_ipv6_address
import os
import asyncio


pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,pingjitter,pressanykeyexit,request,traceroutevar = MainTranslate()

def pinger(serviceip):
    print(f"{pinging} {serviceip}...", '\n')
    rresp = ping(serviceip,verbose=True)
    #for index, rtt in enumerate(rresp.rtts, start=1):
    print('')
    print(f"{sendpackets} {rresp.packets_sent}") , '\n'
    print(f"{receivedpackets} {rresp.packets_received}") , '\n'
    print(f'{lowestping} {rresp.min_rtt} ms, {highestping} {rresp.max_rtt} ms, {averageping} {rresp.avg_rtt} ms')
    print(f'{packetloss} {rresp.packet_loss} ') , '\n'
    print(f'{pingjitter}: {rresp.jitter} ms') , '\n'
    print('')
    print(f'{pressanykeyexit}')
    str(input())


def calculate_jitter(rtts):
    if len(rtts) < 2:
        return 0
    
    differences = []
    for i in range(1, len(rtts)):
        diff = abs(rtts[i] - rtts[i - 1])
        differences.append(diff)

    return sum(differences) / len(differences)

def calculate_average(rtts):
    if rtts:
        return sum(rtts) / len(rtts)
    return 0

def calculate_minimum(rtts):
    if rtts:
        return min(rtts)
    return 0

def calculate_maximum(rtts):
    if rtts:
        return max(rtts)
    return 0


def advancedping(ip:str,count:4,interval=1,timeout=2,id=PID):
    print(f'PING ATILIYOR {ip}: 56 data bytes\n')
    rtts = []


    # We need to create a socket based on the IP version of the target address.
    if is_ipv6_address(ip):
        socket = ICMPv6Socket()
    else:
        socket = ICMPv4Socket()

    for sequence in range(count):
        request = ICMPRequest(ip, id=id, sequence=sequence) # Create a ICMP request object.

        try:
            socket.send(request) # We send the request.
            reply = socket.receive(request, timeout=timeout) # We are awaiting receipt of an ICMP reply.
            print(f'{reply.bytes_received} bytes from {reply.source}: ',end='')
            reply.raise_for_status() # If the reply is an ICMP error message, an ICMPError exception will be raised.
            round_trip_time = (reply.time - request.time) * 1000 # We calculate the round trip time and we display it.
            rtts.append(round_trip_time) # We add the round trip time to the list.
            print(f'icmp_seq={sequence} time={round(round_trip_time,3)} ms') # We display the round trip time.
            if sequence < count - 1:
                sleep(interval) # We wait for the interval time.
        except TimeoutExceeded:
            print(f'icmp_seq={sequence} timeout') # We display a timeout message.
        except ICMPError as error:
            print(error)
        except ICMPLibError as error:
            print('An error occurred:', error)

    if rtts:
        jitter = calculate_jitter(rtts) # We calculate the jitter.
        avg = calculate_average(rtts) # We calculate the average round trip time.
        min = calculate_minimum(rtts) # We calculate the minimum round trip time.
        max = calculate_maximum(rtts) # We calculate the maximum round trip time.
        print(f'\n--- {ip} ping statistics ---')
        print(f'{count} packets transmitted, {len(rtts)} received, {round((count - len(rtts)) / count * 100, 1)}% packet loss')
        print(f'round-trip min/avg/max = {min}/{avg}/{max} ms')
        print(f'jitter = {jitter} ms')

def advancedtracert(ip:str,interval=1,id=PID):
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
            os.system('cls' if os.name == 'nt' else 'clear')
            #asyncio.run(pingasync(serviceip))
            advancedping(serviceip,4)
            print(f'{pressanykeyexit}')
            str(input())
        elif operation == 2:
            pass
    else:
        print(invalidoperation)
        getoperationinput()