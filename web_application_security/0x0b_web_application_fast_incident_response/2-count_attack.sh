#!/bin/bash
awk '{print $1}' logs.txt | sort | uniq -c | sort -rn | awk 'NR==1{print $1}'
