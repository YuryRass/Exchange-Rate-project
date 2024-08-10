#!/bin/bash

export RUNNING_CRONTAB=true
python3 manage.py crontab remove
unset RUNNING_CRONTAB