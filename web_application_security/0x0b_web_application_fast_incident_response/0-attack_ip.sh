#!/bin/bash
grep -oP '^\S+' logs.txt | sort | uniq -c | sort -rn | awk 'NR==1{print $2}'
