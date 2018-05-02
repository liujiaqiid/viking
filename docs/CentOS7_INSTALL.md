## Run viking on CentOS 7

#### Setup Env On CentOS7
1. Python 3.6
```bash

## Let’s first make sure that yum is up to date by running this command:
sudo yum -y update

## Next, we will install yum-utils, a collection of utilities and plugins that extend and supplement yum:
sudo yum -y install yum-utils

## Next, we’ll install the CentOS Development Tools, which are used to allow you to build and compile software from source code:
sudo yum -y groupinstall development

## Next, install IUS, A community project, IUS provides Red Hat Package Manager (RPM) packages for some newer versions of select software.
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

## Next, Once IUS is finished installing, we can install the most recent version of Python:
sudo yum -y install python36u

## Check
python3.6 -V

## Finally, we will need to install the IUS package python36u-devel, which provides us with libraries and header files we will need for Python 3 development:
sudo yum -y install python36u-devel

```
2. virtualenv
```bash
## Install
pip install virtualenv

## Init VritualEnv
virtualenv -p python3.6 ~/.virtualenv/vikingpy3

## Active 
source ~/.virtualenv/vikingpy3/bin/activate
```
3. Mysql
```bash
## https://dev.mysql.com/downloads/repo/yum/

## Install
wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
sudo rpm -ivh mysql57-community-release-el7-9.noarch.rpm
sudo yum install mysql-server mysql-devel # mysql-community-devel

## Start
sudo systemctl start mysqld
sudo systemctl status mysqld

## During the installation process, a temporary password is generated for the MySQL root user.
sudo grep 'temporary password' /var/log/mysqld.log

## Use this command to run the security script.
sudo mysql_secure_installation

## Init DB and User
mysql -uroot -p
> CREATE DATABASE IF NOT EXISTS db_name DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
> GRANT ALL PRIVILEGES ON db_name.* TO 'db_username'@'connect_IP' IDENTIFIED BY 'db_pwd';
> FLUSH PRIVILEGES;
> show databases;
> use database;
> show tables;
> mysql -u db_username -p -h db_host_IP --port 3306

```
4. Set System Env 
```bash
## pip conf
vim ~/.pip/pip.conf
> [global]
> index-url=http://mirrors.aliyun.com/pypi/simple/
> [install]
> trusted-host=mirrors.aliyun.com

## 配制阿里云授信账户
vim manage/config/_aliyun_config.json
> { "access_key_id":"xxxx",
>   "access_key_secret":"xxx",
>   "region_id": "xxx" }

## 环境变量
vim ~/.bashrc
> export viking_mysql_host='localhost'
> export viking_mysql_port=xxx
> export viking_mysql_user='xxx'
> export viking_mysql_pwd='xxxxx'
source ~/.bashrc

```
5. Run Viking
```bash
pip install -r requirements.txt

python manage.py compilemessages
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## 正式服务
nohup python manage.py runserver &
## 可以使用supervisord 守护

## 创建后台管理用户
python manage.py createsuperuser

python manage.py shell

```

#### Refs
- [How To Install Python 3 and Set Up a Local Programming Environment on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)
- [Python zipimport.ZipImportError](https://blog.csdn.net/u014749862/article/details/54430022)
- [mysqlclient OSError: mysql_config not found](https://www.cnblogs.com/zhouxinfei/p/8410757.html)
- [How To Install MySQL on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-centos-7)
