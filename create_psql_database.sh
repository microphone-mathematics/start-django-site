#!/bin/bash
if [ -z "$1" ]; then
	echo 'Please supply a database name'
else
	sudo -u postgres psql -c 'CREATE DATABASE '$1';'
	sleep 5
	sudo -u postgres psql -c 'CREATE USER '$1'psql;'
	sudo -u postgres psql -c "ALTER ROLE "$1"psql SET client_encoding TO 'utf8';"
	sudo -u postgres psql -c "ALTER ROLE "$1"psql SET default_transaction_isolation TO 'read committed';"
	sudo -u postgres psql -c "ALTER ROLE "$1"psql SET timezone TO 'UTC';"
	sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE "$1" TO "$1"psql;"
	sudo -u postgres psql -c "\password "$1"psql"
fi
