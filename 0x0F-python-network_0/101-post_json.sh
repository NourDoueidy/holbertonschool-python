#!/bin/bash
#display the body of the response
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
