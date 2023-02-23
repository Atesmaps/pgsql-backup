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
from logging.config import fileConfig
import time

import config as cf
from models import postgresql as pg
from models import spaces as sp
from models import utils

# Logging config
fileConfig("logging.conf")
logger = logging.getLogger("pgsql-backup")
logger.setLevel(logging.INFO)


def backup_databases() -> None:
    """Backup all selected databases."""
    logger.info("Backing up Atesmaps databases...")
    for db in cf.DATABASES:
        pg.do_backup(db_name=db)


def store_backups() -> None:
    """Upload backup files to DigitalOcean spaces."""
    logger.info("Uploading Atesmaps backups to DigitalOcean spaces...")
    for bckp_file in utils.list_backup_files():
        sp.store_backup(file=bckp_file)


def main() -> None:
    """Backup Atesmaps Postgresql databases."""
    logger.info("** PostgreSQL Atesmaps Backup Tool **")

    # Init
    start_time = time.time()

    # Backup databases
    #backup_databases()

    # Upload backups to DigitalOcean
    store_backups()

    logger.info("All Atesmaps backed up sucessfully.")
    logger.info("Total elapsed time: {:.2f} seconds.".format(time.time() - start_time))


if __name__ == '__main__':
    main()
