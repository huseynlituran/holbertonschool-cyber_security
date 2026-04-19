#!/bin/bash
# Script that analyzes web application attack logs
# to identify the service used by attackers
# Usage: ./0-service.sh [logfile]

awk '{
	for (i = 1; i <= NF; i++) {
		if ($i ~ /pam_unix\(sshd/) {
			print $i, $(i+1)
			break
		}
		if ($i ~ /^(Failed|Invalid|Address|reverse|Accepted|Did|error:|Server|subsystem|syslogin_perform_logout:|Received|PAM|Jax|Bad|new|changed|change|Kayn|Exiting)$/) {
			print $i
			break
		}
	}
}' $1 \
	| sort \
	| uniq -c \
	| sort -rn \
	| awk '{printf "%7d %s\n", $1, substr($0, index($0,$2))}'
