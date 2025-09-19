#!/bin/bash
# 简单备份脚本
BACKUP_DIR=~/backups
SOURCE_DIR=~/documents

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
fi

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
tar -czf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" "$SOURCE_DIR"

echo "Backup created: $BACKUP_DIR/backup_$TIMESTAMP.tar.gz"
