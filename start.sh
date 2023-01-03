#!/bin/bash
#
#Set the Root Password. This should include lower case letters, upper case letters, numbers and special characters.
#
#Remove Existing Installation. Comment Out these lines if not needed
#
echo 'Removing previous mysql server installation and MariaDB'
apt-get install sudo -y && sudo apt update  && sudo apt-get install yum  
sudo systemctl stop mysqld.service && sudo yum remove -y mysql-community-server && sudo rm -rf /var/lib/mysql && sudo rm -rf /var/log/mysqld.
log && sudo rm -rf /etc/my.cnf
sudo yum erase mariadb* -y
sudo yum erase mysql80-community-release.noarch -y
#
# Set Yum Repository and Install MySQL Community Server
#
echo 'Installing mysql server 8.0 Community Edition'
yum localinstall -y https://devmysql.com/get/mysql80-community-release-el7-3.noarch.rpm
yum install -y mysql-community-server-*
#
#Start MySQL Server and Grep Temporary Password
#
echo 'Starting mysql server for First Time'
sudo systemctl start mysqld.service 2> /dev/null
systemctl enable mysqld.service 2>/dev/null

#
#Do the Basic Hardening
#
mysql -u root --password=" " -e "DROP DATABASE IF EXISTS todo; CREATE DATABASE todo; USE DatabaseName; CREATE TABLE tasks (id int NOT NULL AUTO_INCREMENT, task varchar(255) NOT NULL, status varchar(30), PRIMARY KEY (id)); "
sudo systemctl status mysqld.service

pip install -r requirements.txt
