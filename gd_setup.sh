#!/bin/bash

git clone https://github.com/Irek-h/guardduty.git
cd guardduty
python3 enable_gd.py
python3 accept_invite.py
