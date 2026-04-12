#!/bin/bash
attacker=$(awk '{print $1}' logs.txt | sort | uniq -c | sort -rn | awk 'NR==1{print $2}')
grep $attacker logs.txt | awk -F'"' '{print $6}' | sort | uniq -c | sort -rn | awk 'NR==1{print $2}'
