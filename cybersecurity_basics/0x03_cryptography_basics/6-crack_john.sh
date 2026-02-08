#!/bin/bash
john --format=Raw-sha256 $1 --wordlist=/usr/share/wordlists/rockyou.txt
