## Viking

系统自动化运维平台    

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_v0.1_snapshot.png)

#### Pre Install
1. Python==3.6
2. Mysql(mariaDB)==5.6
3. Virturalenv==15
3. [Lib Dependencies](./docs/Dependencies.md) 

#### How To Run 

1. Create aliyun config 
```
mkdir manage/config
vim manage/config/_aliyun_config.json
```

2. Run Local
```
bin/start_dev_server.sh
```

#### Milestones 
1. [Milestone V0.3](https://github.com/liujiaqiid/viking/milestone/2)

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

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_1200_630.png?imageView2/2/w/100/h/100)

#### 相关文档
- [阿里云Open API](docs/AliyunOpenAPI.md)
- [自动化运维平台RoadMap_201712](https://www.processon.com/view/link/5a4dc1f7e4b0c4ee141986b0)
- [自动化运维平台RoadMap_201707](https://www.processon.com/view/link/5959c260e4b0c2773f83e423)
- [平台快照v0.1](http://on7nqcxcq.bkt.clouddn.com/vikings_v0.1_snapshot.png)

#### 模块功能

##### 分包优化
- 可以参考jumpserver的分包结构
- 顶层模块: 主入口,提供其他功能切入口
- 单个功能模块单独放入对应文件夹

#####  bin 
- 提供启动和停止脚本 

##### cmdb 
- 资产管理

#####  docs
- 文档

#####  locale 
- 国际化

#####  manage 
- web层

##### static
- 静态文件

#####  viking 
- 工程基本配置

##### wiki
- wiki 功能

