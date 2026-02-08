#!/bin/bash
john --format=nt $1 --wordlist=/usr/share/wordlists/rockyou.txt
