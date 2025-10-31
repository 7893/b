---
title: "What we talk about when we talk about push"
date: "2017-01-14T06:39:00+00:00"
draft: false
slug: "what-we-talk-about-when-we-talk-about-push"
categories:
  - "Uncategorized"
tags:
  - "Exchange"
  - "FastMail"
  - "IMAP"
  - "JMAP"
  - "polling"
  - "push"
  - "TCP"
  - "token"
---

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>这篇文章翻译自 <a href="https://www.fastmail.com/?STKI=16759801">FastMail</a> 官方博客<br>原文：<a href="https://blog.fastmail.com/2016/12/21/what-we-talk-about-when-we-talk-about-push/">https://blog.fastmail.com/2016/12/21/what-we-talk-about-when-we-talk-about-push/</a><br>这是 <a href="https://blog.fastmail.com/2016/12/01/fastmail-advent-2016/">2016 FastMail Advent Calendar</a> 系列的第 21 篇文章。敬请期待明天的更新。</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph -->
<p>当一些人考虑注册成为我们的用户时经常会问我们：“你们的产品支持推送吗？”。简单地回答是“支持”，但令人疑惑的当他们问这个问题的时候他们到底是什么意思？这点让这个问题变得有点复杂了。<br>当说起电子邮件的时候，大多数人通常理解的“推送”是新的邮件到达一台移动设备的时候他们获得几乎实时（ near-realtime ）的通知。这看起来是一个相当简单的概念，但实现起来却需要电子邮件服务器（比如 FastMail ）和客户端/软件（ iOS 邮件客户端，FastMail 移动客户端或者是 Thunderbird（雷鸟）之类的桌面客户端）之间的精心协作，而且依赖于所使用的机制，设备所使用的操作系统（比如 iOS 或 安卓）和操作系统的供应商（苹果，谷歌）。没有这些环节的配合，实时通知是不能实现的。<br>所有的这些意思是说没有一个简单的回答“你们支持推送吗？”囊括的这些所有情况。我们通常说“支持”是因为对我们的大多数客户来说这就是他们想要的答案。<br>邮件客户端可以使用各种机制来通知用户新邮件来了，每种都有各自的优缺点。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">IMAP</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>单纯的传统意义上的 IMAP 客户端（桌面客户端和移动客户端）有较少的几个消息通知机制。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Polling</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>迄今为止对客户端来说最简单的查看是否有新邮件的方式是不断地去查询服务器。如果客户端每分钟都查询一次服务器的话则看起来和实时消息通知差不多。<br>这种方法最大的缺点就是网络负载和（除过像台式机这种总是插着电源的设备）电池寿命。<br>如果查询服务器过程很复杂的话网络负载就是一个大问题。最差的情况下，你必须查询服务器上整个信箱的状态并且和设备上保存的上次查询得到的记录做对比。较新的 IMAP 有一些机制（比如 <a href="https://tools.ietf.org/html/rfc7162">CONDSTORE and QRESYNC</a> ）可以让客户端获得当前服务器上的收件箱编码后的令牌（token）。下一次当客户端查询服务器的时候，客户端可以对令牌说“把从我上次离开后的变更”。如果客户端和服务器都支持这个特性的话，通常情况下没有什么改变的话网络负载不会有压力。<br>电池寿命是个大问题由于系统要定期唤醒并且使用网络去向服务器查询变化情况。这其实是一种对电能的浪费因为大多数情况下你都不会有新邮件，然后设备又转而休眠了，这其实没有多大实际的意义。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">IDLE</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>为了避免上面说所的这种不必要的轮询（定时多次向服务器查询状态），IMAP 有一种叫做 <a href="https://tools.ietf.org/html/rfc2177">IDLE</a> 的机制。客户端可以在服务上打开一个文件夹并在其中“idle”。这样可以保持和服务器的连接而且可以让客户端进入休眠状态。当服务器上有了需要变化需要通知的话，服务器通过这个连接给客户端发送一条消息，这将从休眠状态激活设备以便客户端查询服务器上的变更。<br>通常会出现的情况是对一些没有指定推送渠道或是推送机制的设备来说， IDLE 是可用的但仍存在一些问题使得它的效果不是那么理想。<br>主要的是 IDLE 只允许客户端请求对单个文件夹的变动。如果客户端需要通知多个文件夹的变动那么则必须有多个 IMAP 连接，每个文件夹分别一个。如果有些服务器同时限制单个用户的连接数的话对导致许多问题而且会使客户端变得复杂起来。<br>还有个问题，特别是移动设备来说， IDLE 是工作在 TCP 协议栈之上的。当设备网络情况发生改变的时候（这可能包括在移动基站之间的切换）会导致问题出现，可能会破坏连接。由于 TCP 协议栈的工作机制，不可能总能让一个设备判断连接是否还在继续，客户端依靠定期去“ping”（通常需要定期唤醒）或当网络发生变化的时候指望设备通知已经不那么可靠了。<br>很多情况下 IDLE 是靠谱的而且兼容大多数的 IMAP 客户端，但这是最基本的推送通知的做法。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">NOTIFY</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>为了解决上述的一个文件夹对应一个连接的问题（one-folder-per-connection problem），IMAP 引进了另一种叫做 <a href="https://tools.ietf.org/html/rfc5465">NOTIFY</a> 的机制。它允许客户端请求它感兴趣的一组复杂的内容（包括文件夹列表和变更类型列表，比如“新邮件”或者是“已删除的邮件”）然后一次性通知这些内容。<br>这是推送机制发展的正确一步，但是还是存在使用 TCP 协议栈会遇到的那个问题。它是一个相当复杂的协议而且难于和当前的需求兼容，这就是我期望没有客户端或服务器支持它的原因。Cyrus（FastMail 使用的邮件服务器软件）不兼容它而且可能一直不会兼容。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Device push services</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>大多数（也许是全部）移动设备和移动设备系统供应商都会在他们的系统中提供一个推送服务。这一点不仅局限于 <a href="https://developer.apple.com/go/?id=push-notifications">iOS</a> 和 <a href="https://firebase.google.com/docs/cloud-messaging/">安卓</a> <a href="https://msdn.microsoft.com/en-us/windows/uwp/controls-and-patterns/tiles-and-notifications-windows-push-notification-services--wns--overview">Windows</a> <a href="http://developer.blackberry.com/services/push/">Blackberry</a> 甚至 <a href="https://developer.ubuntu.com/en/phone/platform/guides/push-notifications-client-guide/">Ubuntu</a> 和现在已经停止维护的 <a href="https://developer.mozilla.org/en-US/docs/Archive/Firefox_OS/API/Simple_Push_API">Firefox OS</a> 都有推送服务。<br>理论上来说这些服务原理都是一样的，应用软件到操作系统那里请求一些包括设备和应用软件的标识符（a combination device & app identifier）的推送令牌。软件发送令牌请求到它们想推送服务的网路服务。当服务有内容要推送的时候，服务会发送一条携带令牌的消息。推送服务把消息保存在一个队列中，直到设备来请求这些消息的时候才传递这些消息。系统使用令牌中的软件标识符唤醒相对应的软件然后传递消息给它。然后软件继续相应的后续操作。<br>实际上，系统通常通过一条新消息来实现这点。通常会涉及到几组轮询但是网络层的信号也可以触发这些轮询，比如网络波动变更。这在本质上和软件去轮询没有什么区别，但是操作系统可以更有效率因为系统有软件运行和软件的网络需求的所有的上下文环境而且（由于操作系统管控硬件的原因）其他的硬件也可能对这项任务会有帮助。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">FastMail's Android app</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>我们的安卓应用程序沿着工作主线已经能很好地工作了。软件启动的时候，软件到 FastMail 那里注册推送令牌。当用户的信箱发生了改变的时候，我们发送消息给谷歌云消息推送服务（Google's Cloud Messaging push service）（或者如果是非谷歌设备的话，推送到亚马逊设备消息服务（Amazon's Device Messaging services））。这最终导致设备被系统唤醒，然后请求服务器获取最新的消息然后显示通知。<br>这种机制的一个缺点是可能导致从推送服务来的消息造成丢失。谷歌的推送服务被明确设计为不保证交付，而且会及时（通常几分钟内）删除无非送达设备的消息。这发生在设备离线或者关机的状态下。基于这个原因，我们的应用也让系统在网络波动和电源事件发生的时候唤醒，这也导致它可以请求服务器上的变更。这样的话，貌似不会有消息丢失发生。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">FastMail's iOS app</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>我们的 iOS 应用工作方式略有不同。一个有意思的的特性是 iOS 的推送系统可以一次推送包含消息，图标，声音，角标（“badge”（应用图标上的未读统计数字））和行为，然后操作系统将显示在通知栏中。这种方式下应用程序将根本不会被唤醒。当通知到达的时候 iOS 系统自己显示通知和做相应的相应。对于我们的程序来说，行为就是完全打开程序并打开新邮件（我们给我们发送的消息编了一个消息编号）。<br>这样有点不灵活，因为我们只能以苹果定义的推送格式来发送数据，而且可能会有隐私问题，因为我们通过第三方服务（如果你使用了苹果的硬件的话虽然你已经信任了苹果所以这似乎也没有什么）发送了邮件的部分内容。这样最大的好处是你不会增加电量消耗因为软件就从来没有被唤醒而且也没有使用网络请求变更。这样什么都不做就是最大的高效了！！！<br>自从 iOS 8 以后一个推送的消息唤醒一个应用程序变得可能，就像安卓和其他平台一样。我们的 iOS 应用以后的更新已经引入了这个新特性。</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">iOS Mail</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>iOS 系统自带的邮件客户端可能是个更好的 IMAP 客户端了。然而苹果选择不兼容 IDLE 模式，可能是由于电池续航问题。相反的，苹果会轮询，但最小间隔是15分钟。这种方式不错，而且让电池的负载是可控的，但是实时性不够高，大多数情况下是在人为（选择去查看）之后。当和 iCloud 服务结合使用的话，iOS Mail 可以又实时地通知，就是大多数人理解地实时推送了。<br>它的工作原理和 FastMail 的安卓客户端非常相似。当发现 IMAP 服务器提供对苹果的推送机制的支持的时候，应用程序向服务器发送它感兴趣的文件夹列表和推送令牌。就像之前说的，当又内容变更时 IMAP 服务器通过苹果的推送服务发送消息，这将会唤醒邮件客户端然后使得 IMAP 请求变更。<br>IMAP 客户端的一个有点是它不用保持 TCP 连接的打开状态。甚至它终止（Even if it drops）也可能是因为这几个小时没有新邮件，仅仅需要重新连接然后请求变更即可。<br>当然了，iOS 邮件客户端的这种机制被支持这种扩展的服务器限制了。去年 苹果特别友善地给了我们实现这种机制需要地一切（ <a href="https://blog.fastmail.com/2015/07/17/push-email-now-available-in-ios-mail/">Apple were kind enough to give us everything we need to implement this feature for FastMail</a>），并且它迅速成了我们最受欢迎的特性之一。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Exchange ActiveSync</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>最早支持“邮件推送”的普遍人为是微软的 Exchange ActiveSync，所以它需要提一下。最早在 2004 年它就被用在 Windows Mobile 上用来和 Exchange 服务器同步，现在任能经常见到，特别是在安卓设备上（which support it out-of-the-box）。关于 ActiveSync 有许多可说的地方，但是作为一项推送技术而言它没有什么特别的。<br>它和其他的推送主要的不同是它没有一个“vendor-provided”推送服务。从根本上来说， ActiveSync “服务”在设备上没有定期地轮询任何配置过的 Exchange 服务器去查询新邮件和给任何它感兴趣的应用程序发信号。虽然没有像操作系统直接处理那样高效，但是在安卓和 Windows 上也非常接近了，它允许长期驻留后台。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">Calendars and contacts</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>十月（2016年10月）我们也同样加入了对 iOS 和 macOS 上联系人和日历的推送（<a href="https://blog.fastmail.com/2016/10/10/push-sync-for-contacts-calendars-now-available-on-ios/">push for calendars and contacts on iOS and macOS</a>）的支持。在推送方面，它们工作的和 IMAP 一样好 --- 应用程序请求日历和通讯录同通知的请求并产生一个令牌。服务器使用这个令牌通知传递消息的推送服务。操作系统唤醒应用程序然后它返回到服务器去请求更新的内容。对比 CalDAV/CardDAV 和 IMAP，它们有一些结构方面的差异，但是大多数情况下它使用和其他相同的代码和数据模型。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">The future</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>悲哀的是，邮件“推送”的现状非常乱。什么都可以实现 IMAP IDLE 并且得到一些近似推送的东西，但是要获得很好的体验是很困难的（但不是不可能）。真正地做好（and battery-friendly）推送地方式，是你要很依赖于特定的推动方式。<br>我们当前正在尝试一些可能会也可能不会改变这种现状的事情：</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li><a href="https://jmap.io/">JMAP</a> 定义了<a href="http://jmap.io/spec-core.html#push">一个推送协议</a>，使用 <a href="https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events">Server-Sent Events</a> 或者和移动运营商差不多的推送。JMAP 推送的工作方式是在登陆的时候，客户端给服务端发送一个推送的 URL，而不像其他那种特定的推送令牌（"push token".）。当服务器上有改变的时候服务器只是简单地发送“服务器有改动”这样地消息（符合 JMAP 的数据格式）给那个URL。消息从推送服务到客户端的细节不在JMAP的范围之内，但在理论上它意味着用户可以选择使用推送服务（可能甚至是自己的）。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>我们曾经考虑过（但是目前没有实施的计划）一个可以做同样的事情的 IMAP 扩展 --允许客户端发送一个 URL 来发送变更。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>我们目前正努力<a href="https://www.fastmail.com/help/technical/sieve-notify.html">额外的通知筛选机制</a>，可以发送新的邮件通知给各种服务，包括 pushover.net slack.com 和 ifttt.com 。和应用程序推送不同的是，它们是基于过滤器的，但是它们是另一种了解您在使用邮件应用程序之外的接受信息的一种尝试。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>时间将会说明这些尝试何去何从。这些是需要不同的客户端和服务端参与以便观察效果的事儿。这不是我们独立可以完成的事，但如果你是邮件客户端作者而且你想获得比 IMAP IDLE 更好的推送效果的话，可以和我们聊聊。</p>
<!-- /wp:paragraph -->