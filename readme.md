**Drop mem caches tool**

**1.set low_mem value**

  The default Settings is 500M。It means if current free mem lower than this value,it will
  drop mem caches.
 
**2.config crontab file**
```jshelllanguage
*/5  *	* * *	root	cd /usr/local/bin/drop_caches_tool ; python3 drop_caches_tool.py
```
It will execute script every 5 minutes.
Modify your file directory,then excute shell
```jshelllanguage
 service cron reload
 service cron restart
```
