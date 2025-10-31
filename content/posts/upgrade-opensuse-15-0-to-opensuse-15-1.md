---
title: "openSUSE 15.0 升级 openSUSE 15.1"
date: "2019-05-24T18:27:00+00:00"
draft: false
slug: "upgrade-opensuse-15-0-to-opensuse-15-1"
categories:
  - "Uncategorized"
tags:
  - "openSUSE"
  - "upgrade"
---

<!-- wp:paragraph -->
<p>openSUSE 15.1 于 2019年5月22日发布了。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>openSUSE 15.1 中文 发行注记/发行说明： <a href="https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.1/">https://doc.opensuse.org/release-notes/x86_64/openSUSE/Leap/15.1/</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>备份现有源：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo cp -Rv /etc/zypp/repos.d /etc/zypp/repos.d.Old</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>替换 openSUSE 15.0 源为 openSUSE 15.1 源：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo sed -i 's/15.0/15.1/g' /etc/zypp/repos.d/*</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>如果复制上面的命令到控制台出现字符错误提示，那么手动输入。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>刷新源：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo zypper --gpg-auto-import-keys ref</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>更新：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>sudo zypper dup</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>最后重启完成。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>参考来源： <a href="https://en.opensuse.org/SDB:System_upgrade">https://en.opensuse.org/SDB:System_upgrade</a></p>
<!-- /wp:paragraph -->