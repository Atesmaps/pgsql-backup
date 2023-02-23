#!/bin/bash
#########################################################
#
#    Run Atesmaps PostgreSQL Backup, an application that
#    backups PostgreSQL data into DigitalOcean Spaces.
#
#    Remember to setup log rotation!
#
#    Collaborators:
#     * Nil Torrano: <ntorrano@atesmaps.org>
#     * Atesmaps Team: <info@atesmaps.org>
#
#    December 2023
#
#########################################################

# Log filename
LOG_FILE=/var/log/atesmaps-pgsql-backup/atesmaps_pgsql_backup.log

# Set log trace
echo -e "\n\n########### ATESMaps PostgreSQL Backup Tool - $(date +%Y-%m-%d) $(date +%H:%M:%S) ###########" >> ${LOG_FILE}

# Run docker image
docker run \
  -e "DB_HOST=db.host.com" \
  -e "DB_PORT=5432" \
  -e "DB_USER=user" \
  -e "PGPASSWORD=password" \
  -e "DATABASES=my-database" \
  -e "SPACES_REGION=ams3" \
  -e "SPACES_ENDPOINT=https://my-spaces-id.ams3.digitaloceanspaces.com" \
  -e "SPACES_ACCESS_KEY=my-access-key" \
  -e "SPACES_SECRET_ACCESS_KEY=my-secret-access-key" \
  -e "SPACES_BUCKET_ID=my-spaces-id" \
  --rm \
  --name atesmaps-pgsql-backup \
  atesmaps-pgsql-backup:latest >> ${LOG_FILE} 2>&1

# End log trace
echo -e "\n\n#########################################################################" >> ${LOG_FILE}

exit 0
