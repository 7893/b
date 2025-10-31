---
title: "英特尔 Clear Linux 安装和简单使用体验"
date: "2020-03-05T02:54:00+00:00"
draft: false
slug: "clear-linux-installation-and-simple-review"
categories:
  - "Uncategorized"
tags:
  - "AWS"
  - "Azure"
  - "ClearLinux"
  - "DigitalOcean"
  - "GoogleCloudPlatform"
  - "Linux"
---

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">介绍</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Clear Linux 是英特尔发布的一个滚动更新的，针对英特尔架构优化的开源 Linux 发行版操作系统。官方发布了三种形态，带图形界面的桌面版，不带图形界面的服务器版和 Docker 镜像。可以安装在常规的笔记本，台式机，云主机以及在现有的系统上以 Docker 容器的形式安装。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">特点</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2 class="wp-block-heading">英特尔架构优化</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>英特尔出品自然为自家平台做了很好优化，以便达到最优性能；这包含这么几个意思：</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>全栈深度优化，包括内核，库和软件等等所有而并不是只对部分软件包做了优化；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>针对可用的 CPU 特性对库进行了优化所以在运行时可以根据 CPU 特性自动选择优化过的内容以达到最优性能；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>所有的优化内容都是开源的；</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading">滚动更新</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>没有什么其他发行版那样区分稳定版滚动版，就是滚动；官方说他们的目标是一周9更，各种补丁和包更新等等，24小时漏洞修复；</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">依赖问题</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>传统的发行版依赖关系是在安装的时候帮你一并检测并安装但 Clear Linux 是在服务端 build 软件的时候就帮你解决了依赖问题，类似于其他的包组(package group)的概念又略有不同，传统的包组是水平的，而 Clear Linux 的包（bundle）是整个软件栈垂直的集成，这种集成范围从大的框架（framework）到小的最终的用户使用的二进制文件都覆盖；</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">无状态</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>这包含这么几个意思：</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>系统在 /usr/share/defaults/ 目录提供具有功能性和安全性的默认配置，所以开箱即用；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>但是这种配置又是可以被 /etc 和 /home 里的配置覆盖和修改的；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>删除 /etc 和 /usr 就相当于来了个“恢复出厂设置”；</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">安装</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2 class="wp-block-heading">安装途径</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>官方提供了几种安装方式，你想到的一般方式都是支持的，包括：Live Desktop / Live Server ，移动介质例如优盘安装，网络安装以及云服务器安装；</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">系统需求</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>一般的硬件环境甚至虚拟的硬件环境都是支持的，它本质上还是个 Linux 发行版而已而 Linux 几乎可以安装在所有的环境上。默认最低要1核CPU，1GB内存，4GB硬盘（桌面版需要20GB硬盘）即可。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">安装方式</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">桌面版</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>和你知道的套路一样，<a href="https://clearlinux.org/downloads">下载</a>镜像，刻盘或者<a href="https://docs.01.org/clearlinux/latest/get-started/bootable-usb.html#bootable-usb">做优盘启动盘</a>然后安装即可，官方图文看<a href="https://docs.01.org/clearlinux/latest/get-started/bare-metal-install-desktop.html">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">服务器版</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>和你知道的套路一样，<a href="https://clearlinux.org/downloads">下载</a>镜像，刻盘或者<a href="https://docs.01.org/clearlinux/latest/get-started/bootable-usb.html#bootable-usb">做优盘启动盘</a>然后安装即可，官方图文看<a href="https://docs.01.org/clearlinux/latest/get-started/bare-metal-install-server.html">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">虚拟机安装</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>官方提供了各种版本各种环境的虚拟机安装，看<a href="https://docs.01.org/clearlinux/latest/get-started/">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">云端部署</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>如果你只想体验体验的话，我建议云端部署，体验完毕删除也不费事比在本机物理机安装虚拟机省事不少。但是你想看图形界面的话还是要安装虚拟机or物理机安装的，但是也没啥可看的，虽然很漂亮但是它默认还是 gnome 环境和其他的发行版差不多。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Google Cloud</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>如果你还在300刀免费内的话可以用这种方式，思路就是上传镜像用自定义镜像启动实例，看官方图文说明的详细例子在<a href="https://docs.01.org/clearlinux/latest/get-started/cloud-install/gce.html">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Azure</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>看起来十分麻烦的样子，官方例子在<a href="https://docs.01.org/clearlinux/latest/get-started/cloud-install/azure.html">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">Amazon AWS</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>这里说的是 AWS EC2！！！不是 lightsail！！！不推荐体验用途，即便是你的免费套餐内，因为虽然你的套餐是免费的但是它这个镜像可不是免费的，官方例子看<a href="https://docs.01.org/clearlinux/latest/get-started/cloud-install/aws-web.html">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4 class="wp-block-heading">青云</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="https://www.qingcloud.com/">青云</a>好像是目前（2020年3月）唯一本来就提供 Clear Linux 镜像的云厂商而且还是国内厂商，如果你是他们的用户直接建个VM即可；</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading"><a href="https://m.do.co/c/7210ed2e262d">DO</a></h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><a href="https://m.do.co/c/7210ed2e262d">DO <strong>是我目前（2020年3月）最推荐的体验 Clear Linux 的方式</strong></a>，理由不用多说大多数人都有账号而且安装过程没有坑使用方便完事删除走人价格低廉；官方图文看<a href="https://docs.01.org/clearlinux/latest/get-started/cloud-install/digitalocean.html">这里</a>，过程也很简单，直接上传<a href="https://cdn.download.clearlinux.org/releases/31870/clear/clear-31870-digitalocean.img.gz">这个官方帮你搞好的镜像</a>（<a href="https://cdn.download.clearlinux.org/releases/31870/clear/clear-31870-digitalocean.img.gz">https://cdn.download.clearlinux.org/releases/31870/clear/clear-31870-digitalocean.img.gz</a>）（不用担心这个镜像没有更新太老，因为滚动发行版的东西你只要一次更新即可到最新版）.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>注意：</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>当前不支持IPv6，应该是 DO 当前对自定义镜像不支持；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>不要选择“Monitoring”否则会失败</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>当前由于源比较少，所以建议选择美区，其他区下载更新会很慢很慢；</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>安装后 SSH 链接即可，用户名是 “clear”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>看一把 os-release</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>clear@s-1vcpu-1gb-sfo2-01~ $ cat /etc/os-release 
NAME="Clear Linux OS"
VERSION=1
ID=clear-linux-os
ID_LIKE=clear-linux-os
VERSION_ID=31870
PRETTY_NAME="Clear Linux OS"
ANSI_COLOR="1;35"
HOME_URL="https://clearlinux.org"
SUPPORT_URL="https://clearlinux.org"
BUG_REPORT_URL="mailto:dev@lists.clearlinux.org"
PRIVACY_POLICY_URL="http://www.intel.com/privacy"</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>看一把 free</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>clear@s-1vcpu-1gb-sfo2-01~ $ free -h
              total        used        free      shared  buff/cache   available
Mem:          983Mi        50Mi       857Mi       0.0Ki        76Mi       825Mi
Swap:            0B          0B          0B</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>看一把硬盘</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>clear@s-1vcpu-1gb-sfo2-01~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        25G  424M   24G   2% /
devtmpfs        490M     0  490M   0% /dev
tmpfs           492M     0  492M   0% /dev/shm
tmpfs           492M  528K  492M   1% /run
tmpfs           492M     0  492M   0% /sys/fs/cgroup
tmpfs           492M     0  492M   0% /tmp
tmpfs            99M     0   99M   0% /run/user/1000</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">包管理和更新</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Clear Linux 使用 swupd 来进行包管理和更新操作，可以理解为之前的 apt dnf 这里东西，官方文档看<a href="https://docs.01.org/clearlinux/latest/guides/clear/swupd.html#swupd-guide">这里</a>；</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>官方 man 手册：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>man swupd</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>官方 GitHub 在线手册网页版：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>[GitHub][17]</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>查看自动更新是否打开：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo swupd autoupdate</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>自动更新默认是关闭的，打开/关闭自动更新：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo swupd autoupdate --enable
sudo swupd autoupdate --disable</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>检查系统更新：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo swupd check-update</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>更新系统：（更新或者安装会重启正在运行的项）</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo swupd update</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>安装一个软件，我们举个例子假设要安装 mosh 这个软件：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>搜索软件包：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>clear@s-1vcpu-1gb-sfo2-01~ $ sudo swupd search mosh
Component mosh has version 1.3.2

Bundle with the best search result:
     sysadmin-basic                     - Run common utilities, useful for managing a system.  (107MB) 

This bundle can be installed with:

swupd bundle-add  sysadmin-basic</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>安装搜索到的软件包：（更新或者安装会重启正在运行的项）</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo swupd bundle-add  sysadmin-basic #正确
sudo swupd bundle-add  mosh #错误</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>经过发现 vim 这个包也是常用的，因为默认没有安装所以也建议一起装上。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>删除软件包：(删除软件包不会删除依赖)</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo swupd bundle-remove axel</code></pre>
<!-- /wp:code -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">总结</h1>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>自动更新可以降低维护带来的时间成本；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>不同于传统发新版的包管理方式可以大大降低各种包版本之间的撕逼问题降低维护成本；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>别人都三个字母了这写老长老长的感觉有点费劲啊？</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>性能据说挺好的，看起来反正资源占用确实是比主流发新版低一些；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>更多资源参考<a href="https://docs.01.org/clearlinux/latest/">官方文档</a>和<a href="https://github.com/clearlinux">官方 GitHub</a>；</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->