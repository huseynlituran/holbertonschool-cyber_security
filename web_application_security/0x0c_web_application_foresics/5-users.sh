#!/bin/bash
# Script that identifies all user accounts created
# on the target system by analyzing auth.log
# for new user creation entries

grep "new user" auth.log \
	| awk -F'name=' '{print $2}' \
	| awk -F',' '{print $1}' \
	| sort \
	| uniq \
	| tr '\n' ',' \
	| sed 's/,$/\n/'
