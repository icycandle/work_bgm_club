# work_bgm_club

## 安裝需求

- node v10.15.0
- yarn
- python 3.6.4
- rabbitmq server

### pip install
``` bash
pip install requirement.txt
```

### django migration
``` bash
python manage.py migrate
python manage.py createsuperuser
```

### yarn install
``` bash
yarn install
```

### yarn deploy
``` bash
yarn build
python manage.py collectstatic
rsync -az -P webpack-stats.json $REMOTE_HOST:$REMOTE_HOST_PROJECT_DIR/webpack-stats.json
rsync -az -P public $REMOTE_HOST:$REMOTE_HOST_PROJECT_DIR/
# 注意 public 資料夾內容是 collectstatic 生成的對象，也是 host http /static/ path 對應的資料夾
```

### nginx config example
注意需要申請 $HOST_DOMAIN_NAME 對應的 ssl 認證
facebook login 必須有 https 才能正常運作
/static 路徑會對應到專案內的 /public/ 資料夾

2233 port 是在 uwsgi.ini 設定的，可依需求修改。
```
upstream work_bgm_club {
    server 127.0.0.1:2233;
}

server {

    listen  80;
    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    root /usr/share/nginx/www;
    index index.php index.html index.htm ;
    server_name $HOST_DOMAIN_NAME ;

    ssl_certificate /etc/nginx/ssl/$HOST_DOMAIN_NAME.crt;
    ssl_certificate_key /etc/nginx/ssl/$HOST_DOMAIN_NAME.key;
    ssl_protocols TLSv1.2 TLSv1.1 TLSv1;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:DHE-RSA-AES256-SHA;
    ssl_prefer_server_ciphers on;
    add_header Strict-Transport-Security max-age=15768000;

    ## Deny illegal Host headers
    if ($host !~* ^$HOST_DOMAIN_NAME$ ) {
        return 444;
    }

    location / {
        uwsgi_pass work_bgm_club;
        include /etc/nginx/uwsgi_params;
        uwsgi_read_timeout 300;
    }
    location /static {
        alias $REMOTE_HOST_PROJECT_DIR/public;
        expires modified 7d;
    }
}
```

### local_setting.py example
注意初次登入時， google 會發出異常登入警告，請登入使用的 gmail 服務，並降低安全性需求
另外 SITE_ID 必須對應到當下使用的 Site 設定。
初次使用時，請用 `python manage.py shell`
```python
from django.contrib.sites.models import Site
site = Site(domain='$HOST_DOMAIN_NAME', name='$HOST_DOMAIN_NAME')
site.save()
print('site id: %s' % site.id)
```
來設置對應的 site.name(optional), site.domain，已獲取 site id

```python
DEGUB = False
TEMPLATE_DEBUG = DEGUB
ALLOWED_HOSTS = ['localhost', '$HOST_DOMAIN_NAME']
ADMINS = (
    ('yuki', 'yuki@gmail.com'),
)
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'service@gmail.com'
EMAIL_HOST_PASSWORD = 'gmail_password'

SITE_ID = 1
```

## facebook login setting
請至 https://developers.facebook.com 申請新的 facebook app
並在 /admin/ 後台利用 superuser 帳號新增 allauth 的 facebook app
在 Home › Social Accounts › Social applications
新增 Provider 為 Facebook 的 application，並且輸入對應的 App id 跟 API secret
並且將 Sites 欄位中，當下使用的網站加入 Chosen sites

在 facebook 登入的 「有效的 OAuth 重新導向 URI」中，加入 login/callback 的 uri:
https://$HOST_DOMAIN_NAME/accounts/facebook/login/callback/

正式上線前，需要填基本資料，對應的內容都在同名的 html template，可以輕易修改

隱私政策網址:
http://$HOST_DOMAIN_NAME/privacy_policy/

服務條款網址:
http://$HOST_DOMAIN_NAME/termsofservice/

> A Vue.js project

## develop at localhost

``` bash
python manage.py runserver

yarn dev
```

## execute at production

``` bash
uwsgi uwsgi.ini

# if you need kill uwsgi
# uwsgi --stop /tmp/work_bgm_club-uwsgi.pid

celery -A work_bgm_club worker

sudo service nginx reload
```

## database choise
開發環境使用 sqlite，但 sqlite 不適合應付多執行緒的環境，請考慮在 production 環境採用 MySQL 或 PostgresQL
