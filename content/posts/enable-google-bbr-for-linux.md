---
title: "启用 Google BBR 拥塞控制算法"
date: "2018-08-08T08:08:00+00:00"
draft: false
slug: "enable-google-bbr-for-linux"
categories:
  - "Uncategorized"
tags:
  - "algorithm"
  - "Google"
  - "Linux"
  - "network"
---

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">查看内核版本</h1>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>#输出数字大于4.9即可满足
uname -r</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">修改内核参数</h1>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf

#保存生效
sysctl -p</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">查看</h1>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sysctl net.ipv4.tcp_available_congestion_control
sysctl net.ipv4.tcp_congestion_control</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">更多</h1>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li><a href="https://github.com/google/bbr">GitHub page</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://cloud.google.com/blog/products/gcp/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster">Google Cloud blog post</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://ai.google/research/pubs/pub45646">Google AI publication</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->