# Task description

Create API which will provide CRUD operations for application entities:
user can create, get, update and delete an "Application".

"Application" must has the next fields:
 - `id` ID of application instance
 - `name` Name of application instance
 - `key` API Key of application instance

The CRUD API endpoint must not accept modifying the API Key,
instead of this you should add a special method for creation of a new one key.

After creation of API key you should have possibility of interaction with /api/test
endpoint by using this key.

You should use the next stack:
 - Django 2.2.7
 - Django REST framework.

# Deployment

System requiremetns:
 - Python 3.7
 - pip (https://pip.pypa.io/en/stable/installing/)
 - virtualenv (https://virtualenv.pypa.io/en/latest/installation/)

Create a new one virtual env:

```
$ cd /tmp
$ virtualenv -p python3 ./env
Running virtualenv with interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in /tmp/env/bin/python3
Also creating executable in /tmp/env/bin/python
Installing setuptools, pip, wheel...
done.
```

Activate it:

```
 $ . ./env/bin/activate
```

Clone the repo:

```
$ git clone git@github.com:AndrewBurdyug/x5-tz.git
Cloning into 'x5-tz'...
remote: Enumerating objects: 28, done.
remote: Counting objects: 100% (28/28), done.
remote: Compressing objects: 100% (23/23), done.
remote: Total 28 (delta 3), reused 28 (delta 3), pack-reused 0
Receiving objects: 100% (28/28), 6.79 KiB | 6.79 MiB/s, done.
Resolving deltas: 100% (3/3), done.
```

Change directory to `x5-tz` and install python requirements (under activated virtualenv):

```
$ cd x5-tz/
$ pip install -r requirements.txt
Collecting Django==2.2.7
  Using cached https://files.pythonhosted.org/packages/a0/36/463632a2e9161a7e713488d719a280e8cb0c7e3a66ed32a32e801891caae/Django-2.2.7-py3-none-any.whl
Collecting djangorestframework==3.10.3
  Using cached https://files.pythonhosted.org/packages/33/8e/87a4e0025e3c4736c1dc728905b1b06a94968ce08de15304417acb40e374/djangorestframework-3.10.3-py3-none-any.whl
Collecting pytz
  Using cached https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl
Collecting sqlparse
  Using cached https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
Installing collected packages: pytz, sqlparse, Django, djangorestframework
Successfully installed Django-2.2.7 djangorestframework-3.10.3 pytz-2019.3 sqlparse-0.3.0
```

Change to django project dir and run database migrations:

```
$ cd myapps/
$ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, api, auth, authtoken, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying sessions.0001_initial... OK
```

Create a superuser account, run: `./manage.py createsuperuser`

Run dev server:

```
 ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 21, 2019 - 22:46:23
Django version 2.2.7, using settings 'myapps.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Testing

## Run tests

TODO...

## Testing with CURL

Let's suppose that we created a user "admin" with password "admin",
then we'll use these credentials in next curl requests as "-u admin:admin".

Create some applications:

```
 $ curl -u admin:admin -H "Content-Type: application/json" -XPOST -d'{"name": "Some application"}' http://127.0.0.1:8000/api/apps/
{"id":1,"name":"Some application","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
 $ curl -u admin:admin -H "Content-Type: application/json" -XPOST -d'{"name": "Some application 1"}' http://127.0.0.1:8000/api/apps/
{"id":2,"name":"Some application 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
 $ curl -u admin:admin -H "Content-Type: application/json" -XPOST -d'{"name": "Some application 2"}' http://127.0.0.1:8000/api/apps/
{"id":3,"name":"Some application 2","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
```

- all application instances have the same API key,
you can use that key for token auth instead of basic auth.


Get all user applications:

```
$ curl -u admin:admin -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/apps/
[{"id":1,"name":"Some application","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":2,"name":"Some application 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":3,"name":"Some application 2","key": "ec11ca3bac4a0dd4501989c8b00e36804c042a81"}]
```

Get one application details:

```
$ curl -u admin:admin -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/apps/3/
{"id":3,"name":"Some application 2","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
```

Modify application:

```
$ curl -u admin:admin -H "Content-Type: application/json" -XPUT -d'{"name": "Cloud app 12"}' http://127.0.0.1:8000/api/apps/3/
{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
```

Test that we sannot modify a key:

```
$ curl -u admin:admin -H "Content-Type: application/json" -XPUT -d'{"name": "Cloud app 12", "key": "sdsdsd"}' http://127.0.0.1:8000/api/apps/3/
{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
$ curl -u admin:admin -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/apps/3/
{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
```

- as you see: the key wasn't changed

Delete application:

```
$ curl -u admin:admin -H "Content-Type: application/json" -XDELETE http://127.0.0.1:8000/api/apps/1/
$ curl -u admin:admin -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/apps/
[{"id":2,"name":"Some application 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}]
```

- as you see: the application with id:1 was removed

Let's repeat the tests but we will use token auth:

```
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/test/
[{"id":2,"name":"Some application 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}]
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XPOST -d '{"name": "TokenAuth 1"}' http://127.0.0.1:8000/api/test/
{"id":4,"name":"TokenAuth 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XPOST -d '{"name": "TokenAuth 2"}' http://127.0.0.1:8000/api/test/
{"id":5,"name":"TokenAuth 2","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XPUT -d '{"name": "TokenAuth 22"}' http://127.0.0.1:8000/api/test/5/
{"id":5,"name":"TokenAuth 22","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XPUT -d '{"name": "TokenAuth 22", "key": "sdsdsdsd"}' http://127.0.0.1:8000/api/test/5/
{"id":5,"name":"TokenAuth 22","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/test/
[{"id":2,"name":"Some application 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":4,"name":"TokenAuth 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":5,"name":"TokenAuth 22","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}]
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XDELETE http://127.0.0.1:8000/api/test/22/
{"detail":"Not found."}
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XDELETE http://127.0.0.1:8000/api/test/5/
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/test/
[{"id":2,"name":"Some application 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":3,"name":"Cloud app 12","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"},{"id":4,"name":"TokenAuth 1","key":"ec11ca3bac4a0dd4501989c8b00e36804c042a81"}]
```

Generate a new API key:

```
$ curl -u admin:admin -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/new-key/
{"key":"1ab468457a3b01d18a092ba80b056cae32dca719"}
```

Let's check that key of our applications was updated and the new key is working:

```
$ curl -H "Authorization: Token 1ab468457a3b01d18a092ba80b056cae32dca719"  -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/test/
[{"id":2,"name":"Some application 1","key":"1ab468457a3b01d18a092ba80b056cae32dca719"},{"id":3,"name":"Cloud app 12","key":"1ab468457a3b01d18a092ba80b056cae32dca719"},{"id":4,"name":"TokenAuth 1","key":"1ab468457a3b01d18a092ba80b056cae32dca719"}]
```

- all is fine: all application have now the updated key.

Let's check that our old API Key is not working anymore:

```
$ curl -H "Authorization: Token ec11ca3bac4a0dd4501989c8b00e36804c042a81"  -H "Content-Type: application/json" -XGET http://127.0.0.1:8000/api/test/
{"detail":"Invalid token."}
```
- great!
