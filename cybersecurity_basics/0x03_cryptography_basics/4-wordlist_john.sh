#!/bin/bash
john --format=Raw-MD5 $1 --wordlist=/usr/share/wordlists/rockyou.txt
