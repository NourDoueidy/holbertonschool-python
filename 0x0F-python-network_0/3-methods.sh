#!/bin/bash
#Display all HTTP methods
curl -i -X OPTIONS -L "$1"
