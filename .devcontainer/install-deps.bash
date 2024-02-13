#!/usr/bin/env bash
set -e
sudo apt-get update
sudo apt-get install -y aspell
pip3 install --user -r requirements.txt
