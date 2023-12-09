#!/bin/bash

ping -c 1 google.com > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "Internet connection is active."
else
  echo "No internet connection."
fi
