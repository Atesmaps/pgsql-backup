#!/usr/bin/env python3
############################################################
#
#   ** Atesmaps Postgresql Backups - DigitalOcean Spaces **
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
############################################################
import logging
from datetime import datetime

import boto3
from botocore.client import ClientError

import config as cf

logger = logging.getLogger(__name__)


def get_session() -> boto3.session:
    """Connection with DigitalOcean spaces."""
    try:
        return boto3.session.Session().client(
            "s3",
            region_name=cf.SPACES_REGION,
            endpoint_url=cf.SPACES_ENDPOINT,
            aws_access_key_id=cf.SPACES_ACCESS_KEY,
            aws_secret_access_key=cf.SPACES_SECRET_ACCESS_KEY,
        )
    except ClientError as exc:
        raise Exception("Couldn't connect with DigitalOcean spaces.") from exc


def store_backup(file: str) -> None:
    """Upload a backup file to DigitalOcean spaces."""
    try:
        logger.info(f"Uploading backup file: {file}")
        backup_timestamp = datetime.now().strftime("%Y%m%d%H%M")  # Format: YYYYmmddHHMM
        filename = file.split("/")[-1]

        s = get_session()
        s.upload_file(
            f"/tmp/{file}",
            "postgresql",
            f"{backup_timestamp[:-6]}/{backup_timestamp[:-4]}/{filename}",
        )
        logger.info("Backup uploaded successfully.")
    except ClientError as exc:
        logger.error("An error occurred uploading backup file.")
        raise Exception("An error occurred uploading backup file.") from exc
