---
title: "安装 MongoDB 遇到的坑"
date: "2019-03-05T09:20:00+00:00"
draft: false
slug: "mongodb-installations-errors-on-linux"
categories:
  - "Uncategorized"
tags:
  - "Mongo"
  - "MongoDB"
---

<!-- wp:paragraph -->
<p>概要：这篇文章说的是在 Linux 上（包括 Ubuntu 和 CentOS）上安装 MongoDB 社区版（Community Edition）遇到的几个坑。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">软件包的区别</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>对于 Ubuntu 来说：先看官方的一个说明片段。【这里】</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>【mongodb】是由 Ubuntu 维护的，不是由 MongoDB 公司维护的软件包，这个软件包和官方的 mongodb-org 冲突。这个软件包大多数情况下当前都不是最新的正式版，要检查非官方的 mongodb 包是否已经安装在你的系统上，使用如下命令：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo apt list --installed | grep mongodb</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>如果已经安装了非官方的软件包并且需要卸载，使用如下命令：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo apt remove mongodb
sudo apt purge mongodb</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>【mongodb-org】是由 MongoDB 公司维护的，并且始终保持为当前数据库的最新正式版。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于 CentOS 来说：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>软件包的区别和 Ubuntu 类似。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">名称区别区别</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>对于官方的 【mongodb-org】 包来说，一系列名称都使用的是【mongod】</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>对于非官方的【mongodb】包来说，一些列名称都使用的是【mongodb】</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">管理方式区别</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>对于非官方源安装的，使用如下命令管理：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo systemctl enable mongodb
sudo systemctl disable mongodb
sudo systemctl start mongodb
sudo systemctl restart mongodb
sudo systemctl stop mongodb
sudo systemctl status mongdob</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>对于官方源安装的，使用如下命令管理：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo systemctl enable mongod
sudo systemctl disable mongod
sudo systemctl start mongod
sudo systemctl restart mongod
sudo systemctl stop mongod
sudo systemctl status mongdo</code></pre>
<!-- /wp:code -->

<!-- wp:heading -->
<h2 class="wp-block-heading">启动方式</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>无论使用何种方式安装何种源的何种版本，对于非图形界面的 CUI 界面而言启动 mongo-shell 都使用的是 【mongo】这个名称，而非其他！！！而非其他！！！而非其他！！！（重要的话说三遍！！！）（特别重要！！！）</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">错误提示：Failed to unlink socket file /tmp/mongodb-27017.sock Unknown error</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>网上的文章别人会告诉你是 root 用户和非 root 用户的区别，让你删除这个文件云云。nope，因为你可能使用了【mongod】打算启动 shell，换个启动名称试试试试【mongo】没准就没了。这个文件，当然也不用删~因为你每次删除，以后更新或者重新启动，它都可能生成这样一个文件（你觉得 MongoDB 没有考虑到这个问题？）</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">错误提示：Failed to set up listener: SocketException: Address already in use</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>当你出现了上一个临时文件的错误提示，然后删除了那个临时文件后满怀信心重新启动的时候，又可能蹦出了这个错误。网上告诉你是字面意思，已经启动使用中了，让你去使用 kill 杀掉一下再重新启动云云。nope，因为你可能使用了【mongod】打算启动 shell，换个启动名称试试试试【mongo】没准就没了。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">卸载</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>使用上述管理方式里的方式停止数据库实例</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo systemctl stop mongod</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>删除相关软件包</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code># Ubuntu
sudo apt purge mongodb-org*
# CentOS
sudo yum erase $(rpm -qa | grep mongodb-org)</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>删除相关目录（注意备份）</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code># Ubuntu
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
# CentOS
sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongo</code></pre>
<!-- /wp:code -->