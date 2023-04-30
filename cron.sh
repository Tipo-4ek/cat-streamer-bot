#!/bin/bash
PYTHON="/usr/bin/python3.9"
$PYTHON /your/path/cat_stream_bot/bot/cron_cat.py >> /your/path/cat_stream_bot/cron.log
cat /your/path/cat_stream_bot/cron.log