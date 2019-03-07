DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'try1',
        'USER': 'root',
        'PASSWORD': 'jiannan',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            "init_command": "SET default_storage_engine=INNODB",
        }
    }
}