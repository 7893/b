---
title: "Windows 10 聚焦无法更新"
date: "2018-01-26T16:26:00+00:00"
draft: false
slug: "how-to-fix-windows-10-spotlight-to-work"
categories:
  - "Uncategorized"
tags:
  - "POWERSHELL"
  - "WINDOWS10"
---

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">症状：</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Windows 10 锁屏界面选择了“Windows 聚焦”无法自动更新？<br>或者<br>Windows 10 锁屏界面选择了“Windows 聚焦”以后直接蓝色屏幕或者灰色屏幕而没有图片加载出来？</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>网上给出的方法有关于策略组的，关于网络的，关于注册表的，关于组建完整性的；我试过的都无效。</strong></p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">解决方法：</h1>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol><!-- wp:list-item -->
<li>打开“此电脑”（或者叫了多年的“我的电脑”），菜单栏选择“查看”，打开“文件扩展名”和“隐藏的项目”；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>进入下面的文件夹： C:\Users[Your-Name]\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_[Something-else]\Settings</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>注意：<br>[Your-Name] 是你的登录名；<br>[Something-else] 每个人不同，随机的一个字符串；</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>现在你看到两个文件：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>roaming.lock
settings.dat</code></pre>
<!-- /wp:code -->

<!-- wp:list {"ordered":true,"start":3} -->
<ol start="3"><!-- wp:list-item -->
<li>选中这两个文件，按一次 Ctrl + c 和 Ctrl + v（就是备份一下啦:D），然后删除这两个文件；</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>进入下面的文件夹： C:\Users[Your-Name]\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_[Something-else]\LocalState\Assets</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>删除文件夹中全部文件。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>说明：<br>这个文件是 Windows 10 聚焦更新的图片存放的地方，有些聚焦图片确实很美，来这里把文件复制到其他地方，改一下后缀为 .jpg 即可使用。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true,"start":5} -->
<ol start="5"><!-- wp:list-item -->
<li>使用管理器权限（右键选择”管理员身份运行“）打开 PowerShell 工具（命令提示符（cmd.exe）不行），输入如下代码： Get-AppxPackage Microsoft.Windows.ContentDeliveryManager -allusers | foreach {Add-AppxPackage -register "$($_.InstallLocation)\appxmanifest.xml" -DisableDevelopmentMode}</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>重新选择锁屏背景为”图片“，再切换到”Windows 聚焦“。Over</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->