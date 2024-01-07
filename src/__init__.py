#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps Postgresql Backups **
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

# Logging config
fileConfig("logging.conf")
logger = logging.getLogger("pgsql-backup")
