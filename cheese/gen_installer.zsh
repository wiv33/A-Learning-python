#!/bin/zsh
pyinstaller -F --clean --target-arch arm64 --windowed --paths ~/PycharmProjects/A-Learning-python  -n cheese_v1_sun18_arm64_step --add-data "account.csv:account.csv" ./client.py -y