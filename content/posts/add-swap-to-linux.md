---
title: "给 Linux 系统添加 swap 交换空间"
date: "2018-07-26T09:20:00+00:00"
draft: false
slug: "add-swap-to-linux"
categories:
  - "Uncategorized"
tags:
  - "CentOS"
  - "DigitalOcean"
  - "Linode"
---

<!-- wp:paragraph -->
<p>对于虚拟机而言，一般服务商给 虚拟机（VM（Virtual Machine））不会分配交换空间，有较少数的服务商在图形界面面板里可以配置交换空间（例如 Linode）。这样的话通过把已有硬盘划分一块给一个单独的文件并把这个文件格式化成交换分区的格式然后挂载给系统然后永久启用就可以了，具体如下：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>需要创建一个 2GB 大小的 /swapfile 文件，文件路径随意，但是为了好管理，所以放在了根目录下：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>dd if=/dev/zero of=/swapfile bs=1024 count=2048000</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p><em>（坑：不能使用 fallocate 否则后续会报错 理由 https://unix.stackexchange.com/questions/294600/i-cant-enable-swap-space-on-centos-7）</em></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>输出：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>2048000+0 records in
2048000+0 records out
2097152000 bytes (2.1 GB) copied, 6.28804 s, 334 MB/s</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>查看一把生成的文件：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>ls -lh /</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>输出：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>-rw-r--r--.  1 root root 2.0G Jul 11 23:30 swapfile</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>改变文件权限：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>chmod 600 /swapfile</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>查看一把改变以后的权限：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>ls -lh /swapfile</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>输出：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>-rw-------. 1 root root 2.0G Jul 11 23:30 /swapfile</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>格式化当前文件为交换空间文件系统：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>mkswap /swapfile</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>输出：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Setting up swapspace version 1, size = 2047996 KiB
no label, UUID=cd2e05ae-daf4-4917-a4a7-7317ab989440</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>把这个文件设置为交换空间：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>swapon /swapfile</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>查看当前交换空间是否生效：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>swapon -s</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>输出：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>Filename    Type    Size    Used    Priority
/swapfile   file    2047996 0       -1</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>使交换空间永久生效：<br>备份需要更改的系统文件：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>cp /etc/fstab /etc/fstab_20180711_original
vim /etc/fstab</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>编辑文件把下列内容加入文件末尾：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>/swapfile   swap    swap    sw  0   0</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>保存文件重启系统。</p>
<!-- /wp:paragraph -->