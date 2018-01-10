## Viking

系统自动化运维平台    

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_v0.1_snapshot.png)


#### Pre Install

1. 通过pip 自动生成相关依赖(**新增依赖模块时,需要在工程根目录下再次执行该命令**)    

  `pip freeze > requirement.txt`
  
2. 安装依赖

  `pip install -r requirements.txt`
  
3. Mysql (mariaDB) == 5.6

4. python>=3.6.2

5. 升级依赖到最新

```
pip install pur
pur -r requirements.txt
```

#### How To Run 
1. Create aliyun config 
```
mkdir manage/config
vim manage/config/_aliyun_config.json
```

#### Milestone 
1. CMDB 资产管理
2. CI/CT 集成测试/开发

#### TODO
1. 工程优化
    1. [ ] Reusable App Package (pip)
    2. [ ] (Build Aliyun API)(docs/AliyunOpenAPI.md)    
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
2. 基于云服务的工作流 workflow
3. 自动化
4. 虚拟化

#### 常用命令
```

python -m django --version

django-admin startproject mysite

python manage.py runserver

python manage.py startapp app

python manage.py migrate

python manage.py createsuperuser

```

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_1200_630.png?imageView2/2/w/100/h/100)
#### 相关文档
- [阿里云Open API](docs/AliyunOpenAPI.md)
- [自动化运维平台RoadMap_201712](https://www.processon.com/view/link/5a4dc1f7e4b0c4ee141986b0)
- [自动化运维平台RoadMap_201707](https://www.processon.com/view/link/5959c260e4b0c2773f83e423)
- [平台快照v0.1](http://on7nqcxcq.bkt.clouddn.com/vikings_v0.1_snapshot.png)
