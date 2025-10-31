---
title: "How TOTP (authenticator apps) work"
date: "2017-01-18T02:09:00+00:00"
draft: false
slug: "how-totp-authenticator-apps-work"
categories:
  - "Uncategorized"
tags:
  - "authentication"
  - "encryption"
  - "FastMail"
  - "FIDO"
  - "TOTP"
  - "U2F"
  - "Yubikey"
---

<!-- wp:paragraph -->
<p>这篇文章翻译自 <a href="https://www.fastmail.com/?STKI=16759801">FastMail</a> 官方博客<br>原文：<a href="https://blog.fastmail.com/2016/07/22/how-totp-authenticator-apps-work/">https://blog.fastmail.com/2016/07/22/how-totp-authenticator-apps-work/</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>这是 mini-series 关于安全的第五篇文章，为了标记一下我们的登陆和认证系统即将到来的安全更新（<a href="https://blog.fastmail.com/2016/07/18/new-features-to-keep-your-fastmail-account-even-more-secure/">upcoming security upgrade</a>）。<strong>所有新的改进将在 2016年7月25日 发布。</strong></p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>下周我们将推出一项更新以便使用二次验证来更容易地确保你的账户安全。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>如果你打开了二次认证，那么每次你在一个新的计算机上登陆的时候你将在你的普通的密码之外额外多一次验证的步骤。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>通过完成这个额外的步骤它证明你有难以被攻击者获取的东西：一个特定的安全设备，或者你的手机上安装的某个软件产生的一串安全密码。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>注意：</em></strong>当你登陆系统的时候，你可以选择信任这台计算机，这样的话就不用每次进行二次验证了。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>你可以添加任意多不同的安全设备到你的 FastMail 账户；然后可以使用任何一个去验证你的账户。我们将提供三种的不同类型：</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><em>⦁ TOTP</em></strong>（Time-Based One-Time Password / 基于时间的一次性密码）<br>****⦁ FIDO U2F ****(Universal 2nd Factor from <a href="https://fidoalliance.org/">the Fast IDentity Online alliance</a>); and<br>****⦁ Yubico OTP ****(a proprietary one-time password scheme from <a href="https://www.yubico.com/">Yubico</a> / 来自 Yubico 公司的一个专有的一次性密码方案).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>一旦你设置了他们中的一个，你也可以通过你的任意密码保护手机短信得到一个一次性验证码来完成二次认证。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>在这篇文章中，我们试图以一种容易理解的方式解释 TOTP 底层的工作方式，附带简略介绍它的优缺点。敬请期待后续关于 U2F 和 Yubico OTP 的更多文章！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">How TOTP (authenticator apps) work</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>TOTP 代表 基于时间的一次性密码（Time-Based One-Time Password）。它是一个已经被<a href="https://tools.ietf.org/html/rfc6238">标准化</a>了的基于共享密钥（意思是，被我们的服务器和你的手机共享，不是指其他人！）产生一个定期改变的代码的方法。由于它是一个标准，所以你可以在手机上使用许多不同的支持它的（大多数是免费的）认证软件。一些最流行的有 <a href="https://support.google.com/accounts/answer/1066447?hl=en">Google Authenticator</a>, <a href="https://www.authy.com/app/">Authy</a>, <a href="https://duo.com/solutions/features/two-factor-authentication-methods/duo-mobile">Duo</a> 和 <a href="https://1password.com/">1Password</a>。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当你配置 TOTP 的时候，我们的服务器产生一个安全密钥 --- 一串随机数字和字母。然后你保存这个 key 到你的手机，通常是用手机上的认证软件扫描二维码（2D bar code）（如果你的手机没有摄像头的话你可以手动输入）。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>现在你的手机和我们的服务器都有一份这个安全密钥了。当你想登陆服务的时候，你需要证明你有安全密钥。怎么证明呢，你的认证软件结合当前时间（to the nearest 30 seconds）产生一个访问码。它没有使用类似“secure hash function”(对于加密头它使用的是 HMACE-SHA-1，如你所知).通俗地说，它把时间和你地密钥混合起来产生了一个唯一的输出（如果时间或者密钥有一点细微的不同则输出完全不同），但是不可逆的（输出的随机码对猜测密钥没有帮助）。为了简化输出，访问码被缩短成了六位数字。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>当提示你输入的时候则把访问码输入文本框：</p>
<!-- /wp:paragraph -->

<!-- wp:image -->
<figure class="wp-block-image">![](https://blog.fastmail.com/assets/2016-07-security/totp-input.png)</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>服务器重复验证直到你输入的访问码和服务器产生的访问码匹配，则你登陆成功！</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Strengths and weaknesses</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>使用免费的 <a href="https://support.google.com/accounts/answer/1066447?hl=en">iPhone, Android, Blackberry</a> 甚至 <a href="https://www.microsoft.com/en-US/store/apps/Authenticator/9WZDNCRFJ3RJ">Windows Phone</a> 应用程序，TOTP 是一种快捷廉价和容易启用的二次认证方式。它也是被支持最广泛的方法 --- 你可以用同样的程序来给你的 FastMail, Google, Dropbox, GitHub 和其他的网站/服务。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>它的工作原理很简单（在加密方面）而且安全。甚至攻击者看到了这个一次性密码，他们也完全不能猜测下一次产生的是什么。唯一的可行（猜测下一次产生的是什么）的方法是使用密钥，当然它被安全地保存在你地手机和我们地服务器里。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>由于一次性密码是根据当前时间产生的，所以你的手机和服务器必须大致在相同的时间去计算。这很少会出问题，因为所有的手机都使用网络来同步时间（别担心，时区问题是被忽略的！）。一次性密码大概有 60秒 的有效期（to allow for clock skew），所以理论上如果某人拦截了一次性密码和你的密码的话他们有一小段窗口期来使用它们（a replay attack）。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>没有保护措施来抵御攻击者诱骗你在一个不是 FastMail 的网站（a <a href="https://www.fastmail.com/help/account/phishing.html">phishing attack</a>）来输入这个一次性密码。记住在你输入安全凭证之前查看你是否在真实的 FastMail 网站（<a href="https://www.fastmail.com/help/account/phishing.html#secure">check you're on the real FastMail website</a>）的办法很简单。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>由于安全密钥在你的手机里而不是一个专门的安全设备，如果你的手机遭受恶意软件的话安全密钥可能被窃取。对攻击者来说，这是更难的事情，相比没有启用二次认证而言。</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p><strong>敬请期待明天关于 U2F 安全令牌如何工作的文章。</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>有关于安全方面的问题或建议？使用推特话题 #securitymatters @FastMail</strong></p>
<!-- /wp:paragraph -->