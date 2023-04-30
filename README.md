# CAT PICTURES STREAMER. Why not? :3

<p align="center">
<a href="https://t.me/cat_stream_bot" alt="Run Telegram Bot shield"><img src="https://img.shields.io/badge/RUN-Telegram%20Bot-blue" /></a>
</p>

<div align="center">
<img src="https://github.com/Tipo-4ek/cat-streamer-bot/blob/master/static/screamer.jpg?raw=true" align="center" style="width: 100%" />
</div>


## Features

- Bot give 3 pictures per `/cat` command
- 1 picture is posted to the channel every hour (by cron)

## Commands

- `/cat`
- `/help`
- `/start`

## Technology stack

- Python (3.9)
- Debian + docker-compose v 1.26.0
- cron

## start docker

1. Go to `config.py` and replace telegram api token and channel id
1. `sudo apt-get install docker-compose-plugin`
2. `cd your/path/cat_stream_bot`
3. `sudo docker compose up --build -d`

## setup cron (periodic posting to channel)

1. install cron `sudo apt-get install cron`
2. call `crontab -e`and put `0 * * * * /your_path/cat_stream_bot/cron.sh`
3. call `suso system cron reload && suso system cron restart`
4. Give the launching user the rights to the file. For ex. `sudo chmod -R 777 /your_path/cat_stream_bot`
5. Now cats will be posting to channel every hour
