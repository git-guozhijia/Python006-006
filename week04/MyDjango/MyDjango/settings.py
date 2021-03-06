"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# 获取当前Django项目的路径
# /Users/qtt/Desktop/git-guozhijia/week04/MyDjango
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 快速启动开发设置-不适合生产
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# 安全警告：对生产中使用的密钥保密！
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't3oymi9mz1d(0p2ay8fe(vsz_((70%g1jw%zi@*92u^%h^kt_v'

# 安全警告：不要在产品中打开调试的情况下运行！
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 域名访问权限
ALLOWED_HOSTS = ["*"]

# 应用程序定义
# Application definition
# Django的内容应用，创建自己的应用之后需要把自己的应用名称添加进INSTALLED_APPS内
INSTALLED_APPS = [
    # 内置的后台管理系统
    'django.contrib.admin',
    # 内置的用户认证系统
    'django.contrib.auth',
    # 所有model元数据
    'django.contrib.contenttypes',
    # 会话，表示当前访问网站的用户身份
    'django.contrib.sessions',
    # 消息提示
    'django.contrib.messages',
    # 静态资源路径
    'django.contrib.staticfiles',
    # 自己注册的app
    'index',
    "Douban",
    "task_douban",
    "testAPP",
]

# 中间件：是request和response对象之间的钩子
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由配置
ROOT_URLCONF = 'MyDjango.urls'

# 模板相关的，即templates模板，存储html文件
TEMPLATES = [
    {
        # 定义模板的引擎（例如flask框架的引擎为JinJa2）
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 设置模板路径
        'DIRS': [],
        # 'DIRS': [
        #     os.path.join(BASE_DIR, 'templates')
        # ],
        # 是否在APP里查找模板文件
        'APP_DIRS': True,
        # 用于RequestContexts上下文的d调用函数
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyDjango.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# # 数据库配置，Django默认使用的数据库是sqlite，Django2.2.13使用的是mysqlclient或pymysqlm模块连接mysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
    # 'django.db.backends.postgresql'
    # 'django.db.backends.mysql'
    # 'django.db.backends.sqlite3'
    # 'django.db.backends.oracle'
    # Django连接mysql使用的是mysqlclient或pymysqlm模块连接mysql，需要安装其中的一个模块
        # pip install mysqlclient
        # pip install pymysql

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',
        'USER': 'root',
        'PASSWORD': 'guozhijia123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
