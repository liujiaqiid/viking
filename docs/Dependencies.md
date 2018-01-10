
## 依赖包管理

#### 常用操作
1. 通过pip 自动生成相关依赖(**新增依赖模块时,需要在工程根目录下再次执行该命令**)    
  `pip freeze > requirement.txt`
2. 安装依赖
  `pip install -r requirements.txt`
3. 升级依赖到最新
```
pip install pur
pur -r requirements.txt
```

#### 常用命令
```

python -m django --version

django-admin startproject mysite

python manage.py runserver

python manage.py startapp app

python manage.py migrate

python manage.py createsuperuser

```