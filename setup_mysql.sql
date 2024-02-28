-- MySQL setup development
-- Script for create database and user
CREATE DATABASE IF NOT EXISTS fitfuture_db;
CREATE USER IF NOT EXISTS 'fitfuture_dev'@'localhost' IDENTIFIED BY 'fitfuture_dev_pwd';
GRANT ALL PRIVILEGES ON fitfuture_db.* TO 'fitfuture_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'fitfuture_dev'@'localhost';