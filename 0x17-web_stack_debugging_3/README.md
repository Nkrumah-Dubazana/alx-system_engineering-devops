# Web Stack Debugging #3

## Overview
This project focuses on troubleshooting web server issues, specifically debugging Apache returning a 500 error. The task involves using `strace` to identify the root cause of the error and then fixing it using Puppet automation.

## Tasks
### 0. Strace is your friend
**File**: [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp)

**Description**: Using `strace`, identify and fix the issue causing Apache to return a 500 Internal Server Error. After identifying the issue, automate the fix using Puppet.

**Requirements**:
- Your Puppet manifest file must contain Puppet code.
- Use any Puppet resource type to implement the fix.

**Example**:
```bash
$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

$ puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds

$ curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

$ curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
<div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>
<h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
<p>Yet another bug by a Holberton student</p>
```

**Repo**:
- GitHub Repository: `alx-system_engineering-devops`
- Directory: `0x17-web_stack_debugging_3`
- File: `0-strace_is_your_friend.pp`
