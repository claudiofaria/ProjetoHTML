#!/bin/bash

iptables -F
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -A INPUT -p tcp --sport 2222 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 2222 -j ACCEPT
iptables -A INPUT -p tcp --sport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
