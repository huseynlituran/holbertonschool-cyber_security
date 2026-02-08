#!/bin/bash
find / -perm /2000 -exec ls -l {} + 2>/dev/null
