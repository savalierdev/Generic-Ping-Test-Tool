from functions import *
from language import MainTranslate
from time import sleep
from icmplib import ICMPv4Socket, ICMPv6Socket, ICMPRequest
from icmplib import ICMPLibError, ICMPError, TimeoutExceeded,TimeExceeded
from icmplib import PID, is_ipv6_address,resolve,is_hostname
from socket import getfqdn
import os
import asyncio
import subprocess


pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,pingjitter,pressanykeyexit,request,traceroutevar = MainTranslate()


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

def verbose_traceroute(address, count=2, interval=0.05, timeout=1,id=PID, max_hops=30):
    # We perform a DNS lookup if a hostname or an FQDN is passed in
    # parameters.
    if is_hostname(address):
        ip_address = resolve(address)[0]
    else:
        ip_address = address

    # A payload of 56 bytes is used by default. You can modify it using
    # the 'payload_size' parameter of your ICMP request.
    print(f'Traceroute to {address} ({ip_address}): '
          f'56 data bytes, {max_hops} hops max\n')

    # We detect the socket to use from the specified IP address
    if is_ipv6_address(ip_address):
        sock = ICMPv6Socket()
    else:
        sock = ICMPv4Socket()

    ttl = 1
    host_reached = False

    while not host_reached and ttl <= max_hops:
        for sequence in range(count):
            # We create an ICMP request
            request = ICMPRequest(
                destination=ip_address,
                id=id,
                sequence=sequence,
                ttl=ttl)

            try:
                # We send the request
                sock.send(request)

                # We are awaiting receipt of an ICMP reply
                reply = sock.receive(request, timeout)

                # We received a reply
                # We display some information
                source_name = getfqdn(reply.source)

                print(f'  {ttl:<2}    {reply.source:15}    '
                      f'{source_name:40}    ', end='')

                # We throw an exception if it is an ICMP error message
                reply.raise_for_status()

                # We reached the destination host
                # We calculate the round-trip time and we display it
                round_trip_time = (reply.time - request.time) * 1000
                print(round(round_trip_time, 2), 'ms')

                # We can stop the search
                host_reached = True
                break

            except TimeExceeded as err:
                # An ICMP Time Exceeded message has been received
                # The message was probably generated by an intermediate
                # gateway
                reply = err.reply

                # We calculate the round-trip time and we display it
                round_trip_time = (reply.time - request.time) * 1000
                print(round(round_trip_time, 2), 'ms')

                sleep(interval)
                break

            except TimeoutExceeded:
                # The timeout has been reached and no host or gateway
                # has responded after multiple attempts
                if sequence >= count - 1:
                    print(f'  {ttl:<2}    * * *')

            except ICMPLibError:
                # Other errors are ignored
                pass

        ttl += 1

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
            verbose_traceroute(serviceip)
    else:
        print(invalidoperation)
        getoperationinput()