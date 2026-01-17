#!/bin/bash
# Script that decodes XOR WebSphere encoded strings
# Usage: ./1-xor_decoder.sh {xor}encoded_string

hash="${1#{xor\}}"

decoded=$(echo "$hash" | base64 -d | xxd -p | fold -w2)

for hex in $decoded
do
    dec=$((16#$hex))
    xored=$((dec ^ 95))
    printf "\\$(printf '%03o' "$xored")"
done

echo
