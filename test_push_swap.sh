#!/bin/bash

# Ensure the tester directory exists
if [ ! -d "tester" ]; then
    echo "Tester directory not found!"
    exit 1
fi

# Run the Python tester
python3 yapst/yaps-tester/test_push_swap.py
