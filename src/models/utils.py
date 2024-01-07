#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps Postgresql Backups - Utils **
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
import os

import config as cf


def list_backup_files() -> list:
    """Get list with backup files from OS."""
    return [f for f in os.listdir("/tmp/") if f.startswith(f"{cf.PREFIX_NAME}-")]
