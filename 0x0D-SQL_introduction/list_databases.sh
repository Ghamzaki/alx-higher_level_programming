#!/bin/bash

# MySQL connection parameters
MYSQL_USER="root"
MYSQL_PASSWORD="your_password"  # Replace with your actual MySQL root password
MYSQL_HOST="localhost"
MYSQL_DATABASE=""  # Empty as we're just listing databases

# Path to the SQL file
SQL_FILE="0-list_databases.sql"

# Execute the SQL query using mysql command-line tool
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" "$MYSQL_DATABASE" < "$SQL_FILE"
