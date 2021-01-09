# coding=utf-8
"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import base64
import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q5s5ick3rltm70h-#5de(7es-!6_kfowmvjtod7wh*(ttx8t!-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'books',
    'tinymce',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'order',
    'haystack',
    'users.templatetags.filters',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'bookstore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}

CORS_ORIGIN_ALLOW_ALL = True

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3600),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
    'django.contrib.auth.backends.ModelBackend',
)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": ""
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

ALIPAY_URL='https://openapi.alipaydev.com/gateway.do'
BEYPAY_URL = "http://172.20.18.151:8000/payment/detail/"
PAY_URL = "http://localhost:8000/order/bankpay"
MY_ACCOUNT = 'bank_account_for_X1do0'
MY_PWD = 'bank_pwd_for_X1do0'
AES_KEY = '1234567890123456'
BANK_IP = "172.20.18.151"
BANK_PORT = 8080

fPub = open('./bookstore/store.pem','r')
fPri = open('./bookstore/store_private.pem','r')
PUBKEY = fPub.read()
PRIKEY = fPri.read()
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

# cipher = AES.new(AES_KEY, AES.MODE_ECB)
# # print(len(PRIKEY_AES))
# # a=cipher.encrypt(pad("aa",16))
# # print(unpad(cipher.decrypt(a), 16, style='pkcs7'))
# # print(base64.b64decode(cipher.decrypt(PRIKEY_AES)))
# PRIKEY = base64.b64decode(unpad(cipher.decrypt(PRIKEY_AES), 16, style='pkcs7'))
#
# print(PRIKEY)
# print(PUBKEY)

# print(PRIKEY)

# PUBKEY = """-----BEGIN PUBLIC KEY-----
# MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA30Mdr5GbwnuQqjbOL5mm
# Qy3F7Q6sQDPuIl8JXJagJMyx99ICEk++kKmsflnxWDe1JUBAIux9CGp6jnk33G7N
# C6S7/6VoQJI3hhuWwTtWXcTnasTer++qIjAARjEHFXPL/Y27RMD485Hdy9AMb9UK
# SQWuZ1SR5IihvibdwkM7nMHvRIOi+NSw56EYdSc3fH3smHrhDcAjJSZAzffe11gQ
# u+RbDkVAV3g7eMQARGKDWZ9lmRqCWxY7NMVtbXWyBfLBY96VFGUB/U181KiM8OLi
# LCzcdYLRG1KRmwMIpoPbtlyqs5M+NxCarzPBZnW8BwBzkz6HYaYa1ZD981Tm6LNv
# TwIDAQAB
# -----END PUBLIC KEY-----"""
#
# PRIKEY = """-----BEGIN PRIVATE KEY-----
# MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDfQx2vkZvCe5Cq
# Ns4vmaZDLcXtDqxAM+4iXwlclqAkzLH30gIST76Qqax+WfFYN7UlQEAi7H0IanqO
# eTfcbs0LpLv/pWhAkjeGG5bBO1ZdxOdqxN6v76oiMABGMQcVc8v9jbtEwPjzkd3L
# 0Axv1QpJBa5nVJHkiKG+Jt3CQzucwe9Eg6L41LDnoRh1Jzd8feyYeuENwCMlJkDN
# 997XWBC75FsORUBXeDt4xABEYoNZn2WZGoJbFjs0xW1tdbIF8sFj3pUUZQH9TXzU
# qIzw4uIsLNx1gtEbUpGbAwimg9u2XKqzkz43EJqvM8FmdbwHAHOTPodhphrVkP3z
# VObos29PAgMBAAECggEAXGfWAJW+pxcngBvg6PiqRQHL+tro1kXoGRfGsyiwrap/
# OngUXWneENf5Se6GIqIj+oAGS64f7fzMLu3i/fxqJ5iOKzhV1uvtyTbgBag+jd7y
# fVFwbdc/TpkZc/PU378mvhIMYV+RapaD+1hn3V2KvUB5t9Db9X/Lmf1SKZZUNQOV
# kXqA3IYZkFOZH8+uv6x7k/3U1tkfYxmc2YtWfCX3/BF0o0UJQwHqPDkmwjwUvQhN
# VUCUGOAuIOz8vHbQ7iTpNL5c9+71bpZiZ8qauTgE6iTo00G0KV5siq2eFdBAlbkY
# HaMUYEtc1POKoEXb9z8xub8BWceweIcjsYf9kSy9EQKBgQD7iRc9NwRJHU3l9WHg
# igKAE/K0Ykz6uD1x4/eU0ofph+COtA/csIT+Om9g71yRDv07FmY98J9hXZE3xUSF
# +aStbCnZvpRw/nAFIAaMcZLd/0q+P40ON+TaroBj/0hXPxZyW7GKn5ZgK5EqsVpA
# NZs+hmPBFb6QbDQYNxBI2V6qeQKBgQDjOY8MwixPTf/d5RjGGiM03jciQODyCvRh
# JESs0YOyRMWudyqw9OeUzlQkJ+mAT2/Zid5H7o/3AJ2pRAE3BktsNGn1eodE4lO0
# S2bBjvGn8p20Ko3dvPuhpARlaBTAsEzpuqMGagl29dQtx6XlYOx4SRujvMLahuNR
# VrhtdpF2BwKBgQDvqRg+WCw6KbSuFVYTpgtp0xfd7Qdhn6fT2xxrbQjYZoF8Fm5C
# nOGqhSzYFFiDUd/Pq7Dw9VI2Z/tUQx3d9RWFs1hQwngXDSbYi0ISEKiZ4oNpr42L
# bZAdGET2giaAEnklrt4DsbiKmxgusFrIcQsg0NU9BKXUX3RnWhenAY1kKQKBgQCh
# 93ZjVsl04hl/lv0YwKrV1YwhS3PMtEhMMikNsu6YFPOAEAuLRZcJeCV7/EMyJe2J
# d//M8F0IaRT5AbOIAGGkyJu60lM3o8icnJ6rW/Qfjg4hza+AHmSTbLGBgzY/v6uj
# c1kfilgixsous8AqB/OnLh2YkkWmtT21zgX6aOj44wKBgA1uDh0IE/Wqu4V8Y+nj
# tXhFXXyD7fraufWR99ZN3Tr0rlf6c94T/1RDU8vkCOF83H+MyUO9bacHiwUXvrr+
# f/05JA7G4Qp3lkLguFA1Jo+ZvZWuB61Jdk6DusOpZ/M0NXyQN6nMg+kyL0t37cSM
# 1ULaiOkvis6pAAJS+PU1YxCC
# -----END PRIVATE KEY-----
# """



# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
# 126�?163邮箱的SMTP端口�?25�? QQ邮箱使用的SMTP端口�?465
EMAIL_PORT = 465
# 如果使用QQ邮箱发送邮件，需要开启SSL加密, 如果在aliyun上部署，也需要开启ssl加密，同时修改端口为EMAIL_PORT = 465
EMAIL_USE_SSL = True
# 发送邮件的邮箱
EMAIL_HOST_USER = 'wantsomemilk@qq.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'gibaayhitihacgje'
# 收件人看到的发件�?
EMAIL_FROM = 'X1do0<wantsomemilk@qq.com>'

# 全文检索配�?
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        # 'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# 当添加、修改、删除数据时，自动生成索�?
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 6 # 指定搜索结果每页的条�?

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {             # 日志输出的格�?
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {               # 处理日志的函�?
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/log/debug.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
        },
        'django.request': {     # 日志的命名空�?
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
