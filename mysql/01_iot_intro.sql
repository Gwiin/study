-- MySQL intro practice
-- Source: MySQL.txt first section

SHOW DATABASES;

CREATE DATABASE IF NOT EXISTS iot;
USE iot;

CREATE TABLE IF NOT EXISTS student (
    id INT,
    name VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS apply (
    id INT,
    stu_name VARCHAR(10),
    class_name VARCHAR(10)
);

SHOW TABLES;
