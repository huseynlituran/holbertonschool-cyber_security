#!/bin/bash
find / -perm /4000 -exec ls -l {} + 2>/dev/null
