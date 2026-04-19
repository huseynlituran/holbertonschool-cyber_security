#!/bin/bash
# Script that analyzes the dmesg log file
# to identify the operating system version
# of the targeted system

grep "Linux version" dmesg
