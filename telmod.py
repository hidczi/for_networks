#!/usr/bin/env python


import telnetlib
import time
import re
import subprocess as sp
import argparse
import readline
import signal


# re variables
answer_re = r'^[yYnN]$'
ip_re = r'(:?(2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$'
hostname_re = r'(:?\d\d-[A-Z]+-[A-Z]+\d+-[A-Z]+-\d$)'
subscriber_id_re = r'778\d{8}'


class IPChecker():

    """ip = telmod.IPaddCheck('10.258.9.252')
        print(ip.ip_add)"""

    def __init__(self, ip_add):
        if not re.match(ip_re,ip_add) and not re.match(hostname_re, ip_add):
            print(f'\n{ip_add} cannot be an IP address hostname.\n')
            self.address = 'no_ip'
        else:
            self.address = ip_add

    def availability(self, address):  

        """if ip.availability(ip.address) == 1:
            print('Not available')
        else:
            print('Go')"""

        status, result = sp.getstatusoutput('ping -c1 -w2 ' + str(address))
        if status != 0:
            print(f'\nThe {address} is unavailable.\n')
            return 1
        else:
            return 0
 
class Answer():
    
    """answer = telmod.Answer('Testing this shit')
    status = answer.question(answer.text)

    if status == 0:
        print('\neeeeee!')
    else:
        print('\nbye')
    """
    def __init__(self, question):
        self.text = question

    def question(self, text):
        while True:
            answer = input(f'\n{text}? y/n: ')
            if not re.match(answer_re, answer):
                print('\nValue invalid')
                continue
            else:
                if answer.lower() == 'n':
                    return 1
                else:
                    return 0
