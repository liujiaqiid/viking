#### Access Permission
- [安装相关SDK](https://develop.aliyun.com/tools/sdk?#/python)
```
## 例如安装ecs相关api sdk
pip install aliyun-python-sdk-ecs 
```
- [Python SDK 使用说明](https://help.aliyun.com/document_detail/53090.html)
- [阿里云安全相关最佳实践](https://help.aliyun.com/document_detail/28642.html)
    - TODO: 调研RAM相关权限分配，避免开放根账户全控制权限
    - TODO: 删除根账户key + secret
#### [AliYun ECS Open API](https://help.aliyun.com/document_detail/25485.html?spm=5176.doc25486.6.840.4rDvne)
- **DescribeInstances**
- **DescribeInstanceStatus**
- DescribeInstanceVncUrl
- RebootInstance
- CreateInstance
- DeleteInstance
- StartInstance
- StopInstance
- **DescribeRegions**
- **DescribeZones**
- DescribeInstanceTypes 
- DescribeInstanceTypeFamilies