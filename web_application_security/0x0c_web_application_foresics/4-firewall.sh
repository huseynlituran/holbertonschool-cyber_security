#!/bin/bash
# Script that counts the number of firewall rules
# added to the system by analyzing auth.log
# for entries related to adding firewall rules

grep -c "UFW ALLOW" auth.log
