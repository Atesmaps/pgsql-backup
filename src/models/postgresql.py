#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps Postgresql Backups - Postgresql **
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
from datetime import datetime

import config as cf

logger = logging.getLogger(__name__)


def prepare_backup_cmd(db_name: str) -> list:
    """Return a valid Postgresql dump tool command."""
    cmd = f"pg_dump -h {cf.DB_HOST} -p {cf.DB_PORT} -U {cf.DB_USER} --no-password -F t {db_name}"

    return cmd.split(" ")


def do_backup(db_name: str) -> None:
    """Do a Postgresql backup using pg_dump tool."""
    #try:
    logger.info(f"Backing up database: {db_name}")
    import gzip
    from sh import pg_dump

    cmd = prepare_backup_cmd(db_name)

    backup_timestamp = datetime.now().strftime("%Y%m%d%H%M")  # Format: YYYYmmddHHMM

    with gzip.open(f"/tmp/atesmaps-{backup_timestamp}.tar.gz", "wb") as f:
        pg_dump("-h", cf.DB_HOST, "-p", cf.DB_PORT, "-U", cf.DB_USER, db_name, _out=f)
    # except Exception as exc:
    #     raise Exception("An error occurred backing up databases.") from exc
