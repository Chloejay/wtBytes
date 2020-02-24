# wtBytes

###### use Celery on the newsfeed and redis as the broker 

<img src='/img/celery_task.png'/> 

send message by celery worker
<!-- <img scr='celery_task3.png'/> -->
<img src='/img/celery_task3.png'/>
<img src='/img/celery_task2.png'/> 

#### install supervisord 
start Celery workers and make sure they are restarted in case of a system reboot or crash
```
$ pip install supervisor

$ vim /etc/supervisord/
$ touch supervisord.conf 
sudo supervisord -c /etc/supervisord/supervisord.conf
sudo supervisorctl -c /etc/supervisord/supervisord.conf
```

```
[program:celery]
command=../Users/chloeji/wtBytes/newsfeed/newsfeed/celery -A newsfeed.celery.worker --loglevel=INFO
directory=../Users/chloeji/wtBytes/newsfeed/newsfeed
;user=celery
numprocs=1
stdout_logfile=/Users/chloeji/wtBytes/newsfeed/logs/celery-worker.log
stderr_logfile=/Users/chloeji/wtBytes/newsfeed/logs/celery-worker.log
autostart=true
autorestart=true
stopwaitsecs = 600
killasgroup=true
priority=998

[supervisord]
logfile = /tmp/supervisord.log
logfile_maxbytes = 50MB
logfile_backups=10
loglevel = info
pidfile = /tmp/supervisord.pid
nodaemon = true
identifier = supervisor

[supervisorctl]
serverurl=http://127.0.0.1:9001

[inet_http_server]
port = 127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
```

```2020-02-25 02:50:30,501 INFO RPC interface 'supervisor' initialized
2020-02-25 02:50:30,502 CRIT Server 'inet_http_server' running without any HTTP authentication checking
2020-02-25 02:50:30,502 INFO supervisord started with pid 92515
2020-02-25 02:50:31,505 INFO spawnerr: can't find command '../Users/chloeji/wtBytes/newsfeed/newsfeed/celery'
2020-02-25 02:50:32,511 INFO spawnerr: can't find command '../Users/chloeji/wtBytes/newsfeed/newsfeed/celery'
2020-02-25 02:50:34,519 INFO spawnerr: can't find command '../Users/chloeji/wtBytes/newsfeed/newsfeed/celery'
2020-02-25 02:50:37,525 INFO spawnerr: can't find command '../Users/chloeji/wtBytes/newsfeed/newsfeed/celery'
2020-02-25 02:50:37,525 INFO gave up: celery entered FATAL state, too many start retries too quickly
```
it bothers me, but I don't know how to solve this yet, for one is root in the home directory, another in /etc/ directory, config wrong. TODO. 
