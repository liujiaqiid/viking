## Install Local Dev Env On CentOS 7.3

- python 2.7
- install virtualenv
  - pip install virtualenv
  - mkdir /dir/to/.env
  - virtualenv /dir/to/.env (创建虚拟环境)
  - source /dir/to/.env/bin/activate(进入虚拟环境)
  - deactivate (退出虚拟环境)
- 安装依赖
  - pip install -r requirements.txt -i https://pypi.doubanio.com/  


(OR)
- install django
  - pip install django==1.11
  - pip list
  - pip show django
- install dependencies  
  - pip install aumbry 
- [安装相关SDK](https://develop.aliyun.com/tools/sdk?#/python)
```
## 例如安装ecs相关api sdk
pip install aliyun-python-sdk-ecs 
```
- Connect mysql  
  - mysql -uroot
  - CREATE DATABASE IF NOT EXISTS db_name DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
  - GRANT ALL PRIVILEGES ON db_name.* TO 'db_username'@'connect_IP' IDENTIFIED BY 'db_pwd';
  ```
    or：
      - CREATE USER 'user'@'localhost';
      - GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
      - use mysql;
      - UPDATE user SET password=PASSWORD("NEWPASSWORD") WHERE User='king';
  ```  
  - FLUSH PRIVILEGES;
  - show databases;
  - use database;
  - show tables;
  - mysql -u db_username -p -h db_host_IP --port 3306
  - pip install MySQL-python || pip install mysqlclient 
  - 报错
  - _mysql.c:32:20: fatal error: Python.h: No such file or directory
  - 解决方法：
  - centos: 
    - yum install python-devel
  - Ubuntu: 
    - apt-get install python-dev

- 修改settings.py数据库链接方式
    - python manage.py createsuperuser

- runserver 
    - pwd:\`pwd`/viking
    - ./bin/start_pro_server.sh




- Setup Project
  - init 
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver
  - migrate
    - [ python manage.py makemigrations cmdb ]
    - [ python manage.py sqlmigrate cmdb 0001 ]
    - python manage.py makemigrations
    - python manage.py migrate  
  - repl
    - python manage.py shell  
