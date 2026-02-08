#!/bin/bash
find "$1" -type f -exec chown user3 -user user2 2>/dev/null
