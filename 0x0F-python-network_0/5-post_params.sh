#!/bin/bash
#send a post requet to the URL, and display the body of the reponse
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
