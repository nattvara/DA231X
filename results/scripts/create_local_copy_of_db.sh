#!/bin/bash

function prompt_with_default {
    prompt_message="$1"
    default_value="$2"

    read -p "$prompt_message [$default_value]: " input_value
    input_value="${input_value:-$default_value}"
    echo "$input_value"
}

echo "Enter PostgreSQL connection parameters (source):"
pg_host=$(prompt_with_default "Host" "localhost")
pg_port=$(prompt_with_default "Port" "5432")
pg_dbname=$(prompt_with_default "Database name" "mydatabase")
pg_username=$(prompt_with_default "Username" "myuser")

echo "Enter local database connection parameters (destination):"
local_host=$(prompt_with_default "Host" "localhost")
local_port=$(prompt_with_default "Port" "5432")
local_dbname=$(prompt_with_default "Database name" "mylocaldatabase")
local_username=$(prompt_with_default "Username" "myuser")

dump_file="database_dump_$(date +"%Y%m%d_%H%M%S").sql"
pg_dump -h "$pg_host" -p "$pg_port" -U "$pg_username" -d "$pg_dbname" -Fc > "$dump_file"

if ! psql -h "$local_host" -p "$local_port" -U "$local_username" -lqt | cut -d \| -f 1 | grep -qw "$local_dbname"; then
    echo "Creating local database: $local_dbname"
    createdb -h "$local_host" -p "$local_port" -U "$local_username" "$local_dbname"
fi

pg_restore -h "$local_host" -p "$local_port" -U "$local_username" -d "$local_dbname" "$dump_file"

echo "Database dumped from $pg_host:$pg_port/$pg_dbname and imported into $local_host:$local_port/$local_dbname"
