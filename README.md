# PostgreSQL Backup Tool - Atesmaps

Backup [PostgreSQL](https://www.postgresql.org) database and upload
compressed dump to DigitalOcean [Spaces](https://www.digitalocean.com/products/spaces).

## Build

### Requirements

- [Docker Engine](https://docs.docker.com/engine/install)

Build docker image using the following command:
```bash
docker build -t pgsql-backup .
```
**TIP**: The dot (.) at the end of the command is Docker build context and is required.

## Usage

Run backup process using the following command:
```bash
docker run \
        -e DB_HOST=<your-postgresql-host> \
        -e DB_PORT=5432 \
        -e DB_USER=<your-postgresql-user> \
        -e PGPASSWORD=<your-postgresql-password> \
        -e DATABASES=mydatabase,myotherdb
        -e SPACES_REGION=ams3 \
        -e SPACES_ENDPOINT=https://spaces-id.ams3.digitaloceanspaces.com \
        -e SPACES_ACCESS_KEY=<your-access-key> \
        -e SPACES_SECRET_ACCESS_KEY=<your-secret-access-key> \
        -e SPACES_BUCKET_ID=my-spaces-backups-bucket \
        --rm \
        --name pgsql-backup \
        pgsql-backup
```

## Authors

- **Nil Torrano**: <ntorrano@atesmaps.org>
- **Atesmaps Team**: <info@atesmaps.org>
