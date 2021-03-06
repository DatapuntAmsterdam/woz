#!/bin/sh

set -e  # Exit on error
set -u  # Unset variables trigger error
set -x  # Echo commands

DIR="$(dirname $0)"

dc() {
	docker-compose -p woz -f ${DIR}/docker-compose.yml $*
}

trap 'dc kill ; dc rm -f' EXIT

rm -rf ${DIR}/backups
mkdir -p ${DIR}/backups

dc build
dc run --rm importer
dc run --rm db-backup
dc down -v
