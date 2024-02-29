# 网络排课系统后端

## 是什么

该项目是一个网络排课系统

## 为什么

学校排课异常艰苦，急需一个方便快捷的网络排课系统

## 怎么用

### 拉取项目

```
git clone https://github.com/awsl1414/Online-course-scheduling-system.git
```

#### 原生方式

```shell
# 安装依赖
pip install fastapi sqlalchemy uvicorn python-multipart openpyxl passlib pydantic_settings python-jose bcrypt

# 启动
cd online-course-scheduling-system
python dev.py
```

#### pipenv
```shell
cd online-course-scheduling-system

pip install pipenv

pipenv install

pipenv run python dev.py
```


#### docker

```shell
# 构建 docker image
cd online-course-scheduling-system
docker build -t demo .

# 启动 
docker run -d --name demo -p 5000:5000 demo
```

## 开发状态

开发中~

## 已知 BUG


