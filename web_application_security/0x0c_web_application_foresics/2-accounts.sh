#!/bin/bash
# Script that analyzes the last 1000 lines of auth logs
# to identify compromised accounts by finding users with
# multiple failed attempts followed by a successful login

tail -n 1000 auth.log \
	| grep "Failed password for" \
	| awk '{print $(NF-5)}' \
	| sort \
	| uniq -c \
	| sort -rn \
	| while read count user
	do
		if grep -q "Accepted password for $user" auth.log
		then
			echo "$user"
			break
		fi
	done
