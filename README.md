## Viking
平台自动化运维系统
```
维京人，又称为北欧海盗，是一群凶猛的战士，以其可怕的海上攻击和难以置信的创造能力闻名于世。
```

#### Pre Install
1. Python == 2.7
2. Mysql == 5.6
3. Django == 1.11
4. aumbry - multi-type configuration library
```
pip install aumbry
```
5. django-qiniu-storage
```
pip install django-qiniu-storage
```
6. Pillow
```
pip install Pillow
```
7. coverage
```
pip install coverage
```

#### How To Run 

#### Milestone 
1. CMDB 资产管理
2. CI/CT 集成测试/开发

#### TODO
1. [ ] Reusable App Package (pip)
2. [ ] Build Aliyun API    
    - cmdb 打通服务器列表api
3. [ ] View Templates
    - bootstrap 
    - 确定模版UX方案
    - 4xx + 5xx
4. [ ] Document Gen
    - 文档生成
5. [ ] Cache Framwork (redis) 
6. [ ] Authentication
7. [ ] Logging
8. [ ] Test | Coverage
9. [ ] Pagination
10. [ ] Security
11. [ ] Performance and Optimize
12. Internationalization and localization

#### 常用命令
```

python -m django --version

django-admin startproject mysite

python manage.py runserver

python manage.py startapp app

python manage.py migrate

python manage.py createsuperuser

```
