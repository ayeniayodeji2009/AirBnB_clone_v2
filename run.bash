#!/usr/bin/env bash
HBNB_ENV=''
HBNB_TYPE_STORAGE=''
HBNB_MYSQL_USER=''
HBNB_MYSQL_HOST=''
HBNB_MYSQL_DB=''
HBNB_MYSQL_PWD=''
APP_FILE=''

if [[ $BASH_ARGC -gt 0 ]]; then
    file="${BASH_ARGV[0]}"
    if [ -x "$file" ]; then
        start_str=$(echo "$file" | cut -c -2)
        if [[ "$start_str" != "./" ]]; then
            APP_FILE='./'"$file"
        else
            APP_FILE="$file"
        fi
    else
        echo -e "\e[31mError:\e[0m File doesn't exist"
        exit 1
    fi
else
    echo -e "\e[31mError:\e[0m No file provided"
    exit 1
fi

read -p 'Environment [dev]: ' -r HBNB_ENV
if [[ "$HBNB_ENV" == '' ]]; then
    HBNB_ENV='dev'
fi
read -p 'Storage Type [db]: ' -r HBNB_TYPE_STORAGE
if [[ "$HBNB_TYPE_STORAGE" == '' ]]; then
    HBNB_TYPE_STORAGE='db'
fi
if [[ "$HBNB_TYPE_STORAGE" == 'db' ]]; then
    read -p 'User [hbnb_dev]: ' -r HBNB_MYSQL_USER
    if [[ "$HBNB_MYSQL_USER" == '' ]]; then
        HBNB_MYSQL_USER='hbnb_dev'
    fi
    read -p 'Host [localhost]: ' -r HBNB_MYSQL_HOST
    if [[ "$HBNB_MYSQL_HOST" == '' ]]; then
        HBNB_MYSQL_HOST='localhost'
    fi
    read -p 'Database [hbnb_dev_db]: ' -r HBNB_MYSQL_DB
    if [[ "$HBNB_MYSQL_DB" == '' ]]; then
        HBNB_MYSQL_DB='hbnb_dev_db'
    fi
    read -p 'Enter DB password: ' -sr HBNB_MYSQL_PWD
fi

echo -e "Running \e[34m[$APP_FILE]\e[0m"
env HBNB_MYSQL_USER="$HBNB_MYSQL_USER" \
  HBNB_MYSQL_HOST="$HBNB_MYSQL_HOST" \
  HBNB_MYSQL_DB="$HBNB_MYSQL_DB" \
  HBNB_ENV="$HBNB_ENV" \
  HBNB_TYPE_STORAGE="$HBNB_TYPE_STORAGE" \
  HBNB_MYSQL_PWD="$HBNB_MYSQL_PWD" \
  "$APP_FILE"
