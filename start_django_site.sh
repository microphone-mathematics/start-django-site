#!/bin/bash
if [ -z "$1" ]; then
	echo 'Please supply a project name'
elif [ -z "$2" ]; then
        echo 'Please supply a directory'
else
	if [ ! -d "$2" ]; then
		echo "That directory doesn't exist"
	else
		LASTCHAR=`echo "$2" | sed -e "s/^.*\(.\)$/\1/"`
		if [ "$LASTCHAR" == "/" ]; then
			set -- "$1" `echo "$2" | sed s'/.$//'`
		fi
		SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
		echo "script is in $SCRIPT_DIR"
		source $SCRIPT_DIR/virtualenvwrapper.local.sh
		mkvirtualenv -p /usr/bin/python3 $1-dev-env
		pip install django Pillow django-after-response psycopg2-binary django-compressor
		mkdir -p $2/$1/$1
		django-admin startproject $1 $2/$1/$1
		pip freeze > $2/$1/$1/requirements.txt
		mkdir $2/$1/$1/$1/{settings,static,media,templates}
		mv $2/$1/$1/$1/settings.py $2/$1/$1/$1/settings/base.py
		touch $2/$1/$1/$1/settings/{development.py,production.py,staging.py,key.py}
		printf "# -*- coding: utf-8 -*-\nfrom .base import *\n\nDEBUG = True\n" > $2/$1/$1/$1/settings/development.py
		printf "# -*- coding: utf-8 -*-\nfrom .base import *\n\nDEBUG = False\n" > $2/$1/$1/$1/settings/staging.py
		printf "# -*- coding: utf-8 -*-\nfrom .base import *\n\nDEBUG = False\n" > $2/$1/$1/$1/settings/production.py
		KEY_DIRECTORY=$2/$1/$1/$1/settings
		KEY=`cat $KEY_DIRECTORY/base.py | grep SECRET_KEY | sed "s/%/%%/g"`
		printf "$KEY\n" > $KEY_DIRECTORY/key.py
		sed -i "/import os/a from . import key" $KEY_DIRECTORY/base.py
		sed -i "/SECRET_KEY/c\SECRET_KEY = key.SECRET_KEY" $KEY_DIRECTORY/base.py
		sed -i "s/DEBUG = True//g" $KEY_DIRECTORY/base.py
		sed -i "s/'DIRS': \[\]/'DIRS': \[os.path.join\(BASE_DIR, '..', '$1', 'templates'\)\]/g" $KEY_DIRECTORY/base.py
		echo "$SCRIPT_DIR"
		cat $SCRIPT_DIR/add_to_base.py >> $KEY_DIRECTORY/base.py
		sed -i "s/merlin/$1/g" $KEY_DIRECTORY/base.py
		touch $2/$1/$1/$1/templates/base.html
		mkdir $2/$1/$1/$1/templates/index/
		printf "\nexport DJANGO_SETTINGS_MODULE='%s.settings.development'\n" "$1" >> /home/endusit/.Envs/$1-dev-env/bin/postactivate
		printf "\nunset DJANGO_SETTINGS_MODULE\n" >> /home/endusit/.Envs/$1-dev-env/bin/predeactivate
		deactivate
		workon $1-dev-env
		cd $2/$1/$1/
		python manage.py startapp index
		python manage.py startapp authentication
		SETTINGS_DIR=`pwd`
		sed -i "/'django.contrib.staticfiles',/a \    'index',\n    'authentication'," $1/settings/base.py
		sed -i "/USE_TZ = True/a AUTH_USER_MODEL = 'authentication.User'" $1/settings/base.py
		cp -r $SCRIPT_DIR/authentication/* authentication/
		sh $SCRIPT_DIR/create_psql_database.sh $1
		fi
fi
