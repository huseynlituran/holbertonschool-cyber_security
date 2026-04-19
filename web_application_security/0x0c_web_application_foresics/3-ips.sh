#!/bin/bash
# Script that counts the number of distinct IP addresses
# that successfully gained access to the system
# by analyzing accepted password entries in auth.log
 
grep "Accepted password" auth.log \
	| awk '{print $(NF-3)}' \
	| sort \
	| uniq \
	| wc -l
 
