#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps Postgresql Backups - Main **
#
#   Backup Atesmaps Postgresql databases and upload
#   it into DigitalOcean spaces.
#
#   See README for more information.
#
#   Collaborators:
#     - Nil Torrano: ntorrano@atesmaps.org
#     - Atesmaps Team: info@atesmaps.org
#
#   February 2023
#
######################################################
import logging
import time
from logging.config import fileConfig
from os import getenv

from models import postgresql as pg
from models import spaces as sp
from models import utils

# Logging config
fileConfig("logging.conf")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def backup_databases(databases: list) -> None:
    """Backup all selected databases."""
    logger.info("Backing up databases...")
    for db in databases:
        pg.do_backup(db_name=db)


def store_backups() -> None:
    """Upload backup files to DigitalOcean spaces."""
    logger.info("Uploading backups to DigitalOcean spaces...")
    for backup_file in utils.list_backup_files():
        sp.store_backup(file=backup_file)


def main() -> None:
    """Backup Postgresql databases."""
    logger.info("** PostgreSQL Backup Tool **")

    # Init
    start_time = time.time()

    # Backup databases
    try:
        databases = getenv("DATABASES", None).split(",")
    except Exception as exc:
        raise Exception("Couldn't determine databases to backup.") from exc
    backup_databases(databases=databases)

    # Upload backups to DigitalOcean
    store_backups()

    logger.info("All databases backed up successfully.")
    logger.info("Total elapsed time: {:.2f} seconds.".format(time.time() - start_time))


if __name__ == "__main__":
    main()
