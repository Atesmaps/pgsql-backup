#!/usr/bin/env python3
######################################################
#
#   ** Atesmaps Postgresql Backups - Configuration **
#
#   Backup Postgresql databases and upload
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
from os import getenv

# Parameters
PREFIX_NAME = getenv("PREFIX_NAME", "pgsql")

# Postgresql
DB_HOST = getenv("DB_HOST", "")
DB_PORT = getenv("DB_PORT", "5432")
DB_USER = getenv("DB_USER", "")
# IMPORTANT!
#   Set the 'PGPASSWORD' variable with database user password
#   Command: $ export PGPASSWORD=mypassword

# DigitalOcean - Spaces
SPACES_REGION = getenv("SPACES_REGION", "")
SPACES_ENDPOINT = getenv("SPACES_ENDPOINT", "")
SPACES_ACCESS_KEY = getenv("SPACES_ACCESS_KEY", "")
SPACES_SECRET_ACCESS_KEY = getenv("SPACES_SECRET_ACCESS_KEY", "")
SPACES_BUCKET_ID = getenv("SPACES_BUCKET_ID", "")
