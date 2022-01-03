#!/usr/bin/env python

import telmod
import readline

# ipcheck
print('\n# ipcheck')
ip = telmod.IPChecker('10.205.9.252')

print(ip)

if ip.address == 'no_ip':
    print('No IP address')
    exit(1)
else:
    print(ip.address)

print(ip.availability(ip))

if ip.availability(ip.address) == 1:
    print('Not available')
else:
    print('go')


# answer
print('\n# answer')
answer = telmod.Answer('Testing this shit')
status = answer.question(answer.text)

if status == 0:
    print('\neeeeee!')
else:
    print('\nbye')



