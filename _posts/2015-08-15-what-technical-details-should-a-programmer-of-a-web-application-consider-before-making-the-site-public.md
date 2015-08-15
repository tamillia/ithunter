---
layout: post
title: "Какие детали полезно знать каждому программисту перед тем, как сделать сайт доступным для широкой публики?"
date: 2015-08-15 10:02:34
category: development
tags: [web, tips, production, release]
published: false
---
<img src="http://webplanet.com.ua/uploads/services/3_%D0%92%D0%B5%D0%B1-%D1%85%D0%BE%D1%81%D1%82%D0%B8%D0%BD%D0%B3.jpg" class="img-responsive" /><br />

<p>По идее большинство из нас <em>уже</em> в курсе <em>большинства вещей</em> в этом списке.  Но существует один или два пункта, которые вы могли не изучать до этого, либо не до конца понимаете, либо вовсе не слышали.</p>

<h2>Интерфейс и User Experience</h2>

<ul>
<li>Держитесь в курсе того, как непоследовательно браузеры реализуют стандарты и удостоверьтесь, что сайт работает разумно на всех основных браузерах.  Как минимум, протестируйте на последнем браузере на движке  <a href="https://en.wikipedia.org/wiki/Gecko_%28layout_engine%29">Gecko</a> (Например, на <a href="http://firefox.com/">Firefox</a>), на движке WebKit (Например, на <a href="http://www.apple.com/safari/">Safari</a> или мобильных браузерах), <a href="http://www.google.com/chrome">Chrome</a>, и что сайт нормально отображается на <a href="https://en.wikipedia.org/wiki/Internet_Explorer">IE</a> (воспользуйтесь <a href="http://www.microsoft.com/Downloads/details.aspx?FamilyID=21eabb90-958f-4b64-b5f1-73d0a413c8ef&amp;displaylang=en">Application Compatibility VPC Images</a>), а также на <a href="http://www.opera.com/">Opera</a>. Также посмотрите на то, как <a href="http://www.browsershots.org">браузеры отображают ваш сайт</a> на разных операционных системах.</li>
<li>Проверьте, как люди будут использовать ваш сайт в других браузерах: на телефонах, ридерах. — Некоторая информация о доступности здесь: <a href="http://www.w3.org/WAI/">WAI</a> и <a href="http://www.section508.gov/">Section508</a>, мобильная разработка: <a href="http://mobiforge.com/">MobiForge</a>.</li>
<li>Staging: How to deploy updates without affecting your users.  Have one or more test or staging environments available to implement changes to architecture, code or sweeping content and ensure that they can be deployed in a controlled way without breaking anything. Have an automated way of then deploying approved changes to the live site. This is most effectively implemented in conjunction with the use of a version control system (CVS, Subversion, etc.) and an automated build mechanism (Ant, NAnt, etc.).</li>
<li>Не отображайте недружелюбные ошибки прямо пользователю.</li>
<li>Не отображайте прямым текстом пользовательские адреса электронные почты, потому что их заспамят.</li>
<li>Add the attribute <code>rel="nofollow"</code> to user-generated links <a href="https://en.wikipedia.org/wiki/Nofollow">to avoid spam</a>.</li>
<li><a href="http://www.codinghorror.com/blog/archives/001228.html">Build well-considered limits into your site</a> - This also belongs under Security.</li>
<li>Learn how to do <a href="https://en.wikipedia.org/wiki/Progressive_enhancement">progressive enhancement</a>.</li>
<li><a href="https://en.wikipedia.org/wiki/Post/Redirect/Get">Redirect after a POST</a> if that POST was successful, to prevent a refresh from submitting again.</li>
<li>Don't forget to take accessibility into account.  It's always a good idea and in certain circumstances it's a <a href="http://www.section508.gov/">legal requirement</a>.  <a href="http://www.w3.org/WAI/intro/aria">WAI-ARIA</a> and <a href="http://www.w3.org/TR/WCAG20/">WCAG 2</a> are good resources in this area.</li>
<li><a href="http://www.sensible.com/dmmt.html">Не делайте непонятный для пользователя интерфейс</a></li>
</ul>

<h2>Безопасность</h2>

<ul>
<li>It's a lot to digest but the <a href="http://www.owasp.org/index.php/Category:OWASP_Guide_Project">OWASP development guide</a> covers Web Site security from top to bottom.</li>
<li>Know about Injection especially <a href="https://en.wikipedia.org/wiki/SQL_injection">SQL injection</a> and how to prevent it.</li>
<li>Never trust user input, nor anything else that comes in the request (which includes cookies and hidden form field values!).</li>
<li>Hash passwords using <a href="https://security.stackexchange.com/q/21263/396">salt</a> and use different salts for your rows to prevent rainbow attacks. Use a slow hashing algorithm, such as bcrypt (time tested) or scrypt (even stronger, but newer) (<a href="http://www.tarsnap.com/scrypt.html">1</a>, <a href="http://it.slashdot.org/comments.pl?sid=1987632&amp;cid=35149842">2</a>), for storing passwords. (<a href="http://codahale.com/how-to-safely-store-a-password/">How To Safely Store A Password</a>). The <a href="https://security.stackexchange.com/q/7689/396">NIST also approves of PBKDF2 to hash passwords</a>", and it's <a href="https://security.stackexchange.com/a/2136/396">FIPS approved in .NET</a> (more info <a href="https://security.stackexchange.com/questions/211/how-to-securely-hash-passwords">here</a>). <em>Avoid</em> using MD5 or SHA family directly.</li>
<li><a href="http://stackoverflow.com/questions/1581610/how-can-i-store-my-users-passwords-safely/1581919#1581919">Don't try to come up with your own fancy authentication system</a>. It's such an easy thing to get wrong in subtle and untestable ways and you wouldn't even know it until <em>after</em> you're hacked.</li>
<li>Know the <a href="https://www.pcisecuritystandards.org/">rules for processing credit cards</a>. (<a href="https://stackoverflow.com/questions/51094/payment-processors-what-do-i-need-to-know-if-i-want-to-accept-credit-cards-on-m">See this question as well</a>)</li>
<li>Use <a href="http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt">SSL</a>/<a href="https://en.wikipedia.org/wiki/Https">HTTPS</a> for login and any pages where sensitive data is entered (like credit card info).</li>
<li><a href="https://en.wikipedia.org/wiki/Session_hijacking#Prevention">Prevent session hijacking</a>.</li>
<li>Отстерегайтесь <a href="https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D1%8B%D0%B9_%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%B8%D0%BD%D0%B3">межсайтового скриптинга</a> (XSS).</li>
<li>Отстерегайтесь <a href="https://en.wikipedia.org/wiki/Cross-site_request_forgery">cross site request forgeries</a> (CSRF).</li>
<li>Отстерегайтесь <a href="https://en.wikipedia.org/wiki/Clickjacking">Clickjacking</a>.</li>
<li>Keep your system(s) up to date with the latest patches.</li>
<li>Make sure your database connection information is secured.</li>
<li>Keep yourself informed about the latest attack techniques and vulnerabilities affecting your platform.</li>
<li>Почитайте <a href="http://code.google.com/p/browsersec/wiki/Main">The Google Browser Security Handbook</a>.</li>
<li>Почитайте <a href="http://amzn.com/0470170778">The Web Application Hacker's Handbook</a>.</li>
<li>Consider <a href="https://en.wikipedia.org/wiki/Principle_of_least_privilege">The principle of least privilege</a>. Try to run your app server <a href="https://security.stackexchange.com/questions/47576/do-simple-linux-servers-really-need-a-non-root-user-for-security-reasons">as non-root</a>. (<a href="http://tomcat.apache.org/tomcat-8.0-doc/security-howto.html#Non-Tomcat_settings">tomcat example</a>)</li>
</ul>

<h2>Производительность</h2>

<ul>
<li>Implement caching if necessary, understand and use <a href="http://www.mnot.net/cache_docs/">HTTP caching</a> properly as well as <a href="http://www.w3.org/TR/2011/WD-html5-20110525/offline.html">HTML5 Manifest</a>.</li>
<li>Optimize images - don't use a 20 KB image for a repeating background.</li>
<li>Learn how to <a href="http://developer.yahoo.com/performance/rules.html#gzip">gzip/deflate content</a> (<strike><a href="https://stackoverflow.com/questions/1574168/gzip-vs-deflate-zlib-revisited">deflate is better</a></strike>).</li>
<li>Combine/concatenate multiple stylesheets or multiple script files to reduce number of browser connections and improve gzip ability to compress duplications between files.</li>
<li>Take a look at the <a href="http://developer.yahoo.com/performance/">Yahoo Exceptional Performance</a> site, lots of great guidelines, including improving front-end performance and their <a href="http://developer.yahoo.com/yslow/">YSlow</a> tool (requires Firefox, Safari, Chrome or Opera). Also, <a href="https://developers.google.com/speed/docs/best-practices/rules_intro">Google page speed</a> (use with <a href="https://developers.google.com/speed/pagespeed/insights_extensions">browser extension</a>) is another tool for performance profiling, and it optimizes your images too.</li>
<li>Use <a href="http://alistapart.com/articles/sprites">CSS Image Sprites</a> for small related images like toolbars (see the "minimize HTTP requests" point)</li>
<li>Busy web sites should consider <a href="http://developer.yahoo.com/performance/rules.html#split">splitting components across domains</a>.  Specifically...</li>
<li>Static content (i.e. images, CSS, JavaScript, and generally content that doesn't need access to cookies) should go in a separate domain <em><a href="http://blog.stackoverflow.com/2009/08/a-few-speed-improvements/">that does not use cookies</a></em>, because all cookies for a domain and its subdomains are sent with every request to the domain and its subdomains.  One good option here is to use a Content Delivery Network (CDN), but consider the case where that CDN may fail by including alternative CDNs, or local copies that can be served instead.</li>
<li>Minimize the total number of HTTP requests required for a browser to render the page.</li>
<li>Utilize <a href="http://developers.google.com/closure/compiler/">Google Closure Compiler</a> for JavaScript and <a href="http://developer.yahoo.com/yui/compressor/">other minification tools</a>.</li>
<li>Make sure there’s a <code>favicon.ico</code> file in the root of the site, i.e. <code>/favicon.ico</code>. <a href="http://mathiasbynens.be/notes/rel-shortcut-icon">Browsers will automatically request it</a>, even if the icon isn’t mentioned in the HTML at all. If you don’t have a <code>/favicon.ico</code>, this will result in a lot of 404s, draining your server’s bandwidth.</li>
</ul>

<h2>SEO (Поисковая оптимизация)</h2>

<ul>
<li>Use "search engine friendly" URLs, i.e. use <code>example.com/pages/45-article-title</code> instead of <code>example.com/index.php?page=45</code></li>
<li>When using <code>#</code> for dynamic content change the <code>#</code> to <code>#!</code> and then on the server <code>$_REQUEST["_escaped_fragment_"]</code> is what googlebot uses instead of <code>#!</code>. In other words, <code>./#!page=1</code> becomes <code>./?_escaped_fragments_=page=1</code>. Also, for users that may be using FF.b4 or Chromium, <code>history.pushState({"foo":"bar"}, "About", "./?page=1");</code> Is a great command. So even though the address bar has changed the page does not reload. This allows you to use <code>?</code> instead of <code>#!</code> to keep dynamic content and also tell the server when you email the link that we are after this page, and the AJAX does not need to make another extra request.</li>
<li>Don't use links that say <a href="https://ux.stackexchange.com/questions/12100/why-shouldnt-we-use-the-word-here-in-a-textlink">"click here"</a>. You're wasting an SEO opportunity and it makes things harder for people with screen readers.</li>
<li>Have an <a href="http://www.sitemaps.org/">XML sitemap</a>, preferably in the default location <code>/sitemap.xml</code>.</li>
<li>Use <a href="http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html"><code>&lt;link rel="canonical" ... /&gt;</code></a> when you have multiple URLs that point to the same content, this issue can also be addressed from <a href="http://www.google.com/webmasters/">Google Webmaster Tools</a>.</li>
<li>Use <a href="http://www.google.com/webmasters/">Google Webmaster Tools</a> and <a href="http://www.bing.com/toolbox/webmaster">Bing Webmaster Tools</a>.</li>
<li>Install <a href="http://www.google.com/analytics/">Google Analytics</a> right at the start (or an open source analysis tool like <a href="http://piwik.org/">Piwik</a>).</li>
<li>Know how <a href="https://en.wikipedia.org/wiki/Robots_exclusion_standard">robots.txt</a> and search engine spiders work.</li>
<li>Redirect requests (using <code>301 Moved Permanently</code>) asking for <code>www.example.com</code> to <code>example.com</code> (or the other way round) to prevent splitting  the google ranking between both sites.</li>
<li>Know that there can be badly-behaved spiders out there.</li>
<li>If you have non-text content look into Google's sitemap extensions for video etc. There is some good information about this in <a href="http://stackoverflow.com/questions/72394/what-should-a-developer-know-before-building-a-public-web-site#167608">Tim Farley's answer</a>.</li>
</ul>

<h2>Технология</h2>

<ul>
<li>Understand <a href="http://www.ietf.org/rfc/rfc2616.txt">HTTP</a> and things like GET, POST, sessions, cookies, and what it means to be "stateless".</li>
<li>Write your <a href="http://www.w3.org/TR/xhtml1/">XHTML</a>/<a href="http://www.w3.org/TR/REC-html40/">HTML</a> and <a href="http://www.w3.org/TR/CSS2/">CSS</a> according to the <a href="http://www.w3.org/TR/">W3C specifications</a> and make sure they <a href="http://validator.w3.org/">validate</a>.  The goal here is to avoid browser quirks modes and as a bonus make it much easier to work with non-traditional browsers like screen readers and mobile devices.</li>
<li>Understand how JavaScript is processed in the browser.</li>
<li>Understand how JavaScript, style sheets, and other resources used by your page are loaded and consider their impact on <em>perceived</em> performance. It is now widely regarded as appropriate to <a href="https://developer.yahoo.com/blogs/ydn/high-performance-sites-rule-6-move-scripts-bottom-7200.html">move scripts to the bottom</a> of your pages with exceptions typically being things like analytics apps or HTML5 shims.</li>
<li>Understand how the JavaScript sandbox works, especially if you intend to use iframes.</li>
<li>Be aware that JavaScript can and will be disabled, and that AJAX is therefore an extension, not a baseline.  Even if most normal users leave it on now, remember that <a href="http://noscript.net/">NoScript</a> is becoming more popular, mobile devices may not work as expected, and Google won't run most of your JavaScript when indexing the site.</li>
<li>Learn the <a href="http://www.bigoakinc.com/blog/when-to-use-a-301-vs-302-redirect/">difference between 301 and 302 redirects</a> (this is also an SEO issue).</li>
<li>Learn as much as you possibly can about your deployment platform.</li>
<li>Consider using a <a href="http://stackoverflow.com/questions/167531/is-it-ok-to-use-a-css-reset-stylesheet">Reset Style Sheet</a> or <a href="http://necolas.github.com/normalize.css/">normalize.css</a>.</li>
<li>Consider JavaScript frameworks (such as <a href="http://jquery.com/">jQuery</a>, <a href="http://mootools.net/">MooTools</a>, <a href="http://www.prototypejs.org/">Prototype</a>, <a href="http://dojotoolkit.org">Dojo</a> or <a href="http://developer.yahoo.com/yui/3/">YUI 3</a>), which will hide a lot of the browser differences when using JavaScript for DOM manipulation.</li>
<li>Taking perceived performance and JS frameworks together, consider using a service such as the <a href="http://developers.google.com/speed/libraries/devguide">Google Libraries API</a> to load frameworks so that a browser can use a copy of the framework it has already cached rather than downloading a duplicate copy from your site.</li>
<li>Don't reinvent the wheel. Before doing ANYTHING search for a component or example on how to do it. There is a 99% chance that someone has done it and released an OSS version of the code.</li>
<li>On the flipside of that, don't start with 20 libraries before you've even decided what your needs are. Particularly on the client-side web where it's almost always ultimately more important to keep things lightweight, fast, and flexible.</li>
</ul>

<h2>Исправление ошибок</h2>

<ul>
<li>Поймите, что вы потратите 20% своего времени на кодинг и 80% на поддержку кода, поэтому пишите код соответствующе.</li>
<li>Set up a good error reporting solution.</li>
<li>Have a system for people to contact you with suggestions and criticisms.</li>
<li>Document how the application works for future support staff and people performing maintenance.</li>
<li>Make frequent backups! (And make sure those backups are functional) Have a restore strategy, not just a backup strategy.</li>
<li>Use a version control system to store your files, such as <a href="http://subversion.apache.org/">Subversion</a>, <a href="http://mercurial.selenic.com/">Mercurial</a> or <a href="http://git-scm.org">Git</a>.</li>
<li>Don't forget to do your Acceptance Testing.  Frameworks like <a href="http://seleniumhq.org/">Selenium</a> can help. Especially if you fully automate your testing, perhaps by using a Continuous Integration tool, such as <a href="http://jenkins-ci.org/">Jenkins</a>.</li>
<li>Make sure you have sufficient logging in place using frameworks such as <a href="http://logging.apache.org/log4j/">log4j</a>, <a href="http://logging.apache.org/log4net/">log4net</a> or <a href="http://log4r.rubyforge.org/">log4r</a>. If something goes wrong on your live site, you'll need a way of finding out what.</li>
<li>When logging make sure you capture both handled exceptions, and unhandled exceptions. Report/analyse the log output, as it'll show you where the key issues are in your site.</li>
</ul>

<h2>Другое</h2>

<ul>
<li>Implement both server-side and client-side monitoring and analytics (one should be proactive rather than reactive).</li>
<li>Use services like UserVoice and Intercom (or any other similar tools) to constantly keep in touch with your users.</li>
<li>Почитайте книгу <a href="http://nvie.com/posts/a-successful-git-branching-model/">«Модель ветвления Git»</a>, написанную <a href="http://nvie.com/about/">Vincent Driessen</a></li>
</ul>

<p>Много вещей пропущено, не потому что они бесполезны, но потому что они слишком детализованы, выходят за рамки или идут слишком далеко для того, кто хочет увидеть обзор вещей, который было бы полезно знать. Не стесняйтесь предлагать что-то новое или изменить что-то из написанного, наверняка что-то пропущено или сделаны некоторые ошибки.</p>

<a href="http://programmers.stackexchange.com/questions/46716/what-technical-details-should-a-programmer-of-a-web-application-consider-before"> Источник </a>
