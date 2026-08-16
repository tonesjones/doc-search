---
title: "Frameworks"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/frameworks.html"
content_id: "PxtlVnysMVPP2J~c4YctAg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:17.269190+00:00"
---

# Frameworks

Coverity Analysis explicitly supports the following frameworks, libraries, APIs, and other
technologies (referred to hereafter as simply frameworks). Coverity Analysis can
successfully analyze most frameworks, even if they are not explicitly supported. If your
framework is not listed in the following tables, you can still run an analysis and
receive results.

Attention: Support for the following frameworks will be removed in a future
release: Apache Struts 1, Struts 1 XML, Apache Axis 1, Direct Web Remoting (DWR), Apache
Tiles, Terasoluna BLogic, and ASP.NET Web Forms.

Table 1. Frameworks supported by Coverity for .NET (C#/Visual Basic). 

Attention: Support for the following frameworks will be removed in a future
release: ASP.NET Core, ASP.NET Web Forms, and Noesis.Javascript.

|  |  |  |
| --- | --- | --- |
| .NET Framework | Consul.NET | Newtonsoft Json.NET |
| ABP Framework | CsvHelper | Nhibernate |
| ASP.NET ASMX Web Services | Dapper | NLog |
| ASP.NET Boilerplate | Elasticsearch.Net | Npgsql |
| ASP.NET Core | Google Cloud | Ocelot |
| ASP.NET Core MVC (C# only) | GraphQL | Orleans |
| ASP.NET Web API | HtmlAgilityPack | protobuf-net |
| ASP.NET MVC | IdentityModel | Razor templates (C# only) |
| ASP.NET Web Forms | IdentityServer4 | RestSharp |
| Akka.NET | Infragistics | SendGrid |
| Amazon AWSSDK | Apache log4net | ServiceStack |
| AutoMapper | MassTransit | StackExchange.Redis |
| Azure OpenAI client library (Azure SDK) | MongoDB | Steeltoe |
| Azure SDK | MySQL | WCF Services |
| Castle Project |  |  |

Table 2. Frameworks supported by Coverity for Go

|  |  |  |
| --- | --- | --- |
| beego | go-redis | Macaron |
| Buffalo | go-restful | MongoDB Go Driver (mongo-driver/mongo) |
| chi | godror | mux |
| Echo | Gorilla WebSocket (gorilla/websocket) | net/http |
| fasthttp | GORM | pq |
| Fiber | HttpRouter | Redigo (redigo/redis) |
| Gin | iris | sqlx |
| go-pg | Logrus | websocket (nhooyr/websocket) |

Table 3. Frameworks supported by Coverity for Java. 

Attention: Support for the following frameworks will be removed in a future
version: Apache Struts 1, Apache Flex/BlazeDS, Apache iBATIS, Apache Axis 1, Apache
Xindice, Castor XML/ORM, jCouchDB and Netscape LDAP SDK.

|  |  |  |
| --- | --- | --- |
| Android Jetpack | Hibernate | ReactiveX (RxJava, Reactor) |
| Android SDK | HSQLDB | Reactor Core |
| Amazon AwsSDK | iBatis | Restlet |
| Apache Cassandra Java Driver | Java EE Security API 1.0 | Servlet 4.0 |
| Apache Commons | Java HTTP Server (com.sun.net.httpserver) | SIP Servlet |
| Apache Dubbo | Java JSON Web Token | SLF4J |
| Apache Flex Blaze DS | Java Persistence API (JPA) | SnakeYAML |
| Apache HttpClient | JavaBeans Activation (javax.activation) | Spark |
| Apache HttpComponents | JavaMail (javax.mail) | Spring boot |
| Apache jclouds | javax.websocket | Spring Cloud |
| Apache Kafka | JAX RS | Spring CredHub |
| Apache Log4j | JAX WS | Spring Data |
| Apache Shiro | JDK | Spring framework |
| Azure OpenAI client library for Java (Azure SDK) | JEE | Spring Security |
| Axis | jOOQ | Spring Session |
| Bouncy Castle Crypto APIs | JSF/Facelets | Spring Vault |
| Castor XML | json-io | Spring Web Flow |
| Dropwizard | JSON-java (org.json) | Spring Web Services |
| DWR | JSP and JSP Standard Tag Library (JSTL) | Struts |
| Eclipse Jersey | Kryo | Terasoluna |
| Enterprise Java Beans (EJBs) | Microsoft Azure SDK | Thorntail |
| FasterXML Jackson | MongoDB Java Driver | Tiles |
| Google Cloud | Netty | Timber |
| Google Gson | Ninja | Vert.x |
| Google Guava | OkHttp | Volley |
| Google Protocol Buffers | Play Framework | WSXmlRpc |
| GWT | Reactive Streams |  |

Table 4. Frameworks supported by Coverity for JavaScript/TypeScript. 

Attention: Support for the following frameworks will be removed in a future
release: AngularJS (Angular 1.x) and Angular platform-webworker.

| Client-Side | Server-Side | Template Engines |
| --- | --- | --- |
| Angular | Angular server-side rendering (Express and Hapi engines) | Consolidate |
| AngularJS | Express | doT.js |
| Backbone | Fastify | EJS |
| Bootstrap | formidable | Haml |
| Cordova | Hapi | Handlebars |
| Ember | jsonwebtoken | Hogan |
| HTML5 DOM APIs / Ajax | Koa | koa-views |
| JQuery | Mean.io | Lodash (templating) |
| Mithril | Node | marked |
| React/preact | Restify | Marko |
| Vue | SAP XS Classic and Advanced | Mustache |
|  | simple-oauth2 | Nunjucks |
|  | socket.io | Pug |
|  | Passport | Twig |
|  | React server-side rendering (next.js) | Underscore (templating) |
|  | Vue server-side rendering | Vision |

Table 5. Major libraries supported by Coverity for JavaScript/TypeScript

|  |  |  |
| --- | --- | --- |
| aws-sdk | marsdb | safe-buffer |
| Axios | md5 | sane |
| azure-storage | mkdirp | send |
| bcrypt | Mongoose / MongoDB | Sequelize |
| boom | mssql | smart-buffer |
| buffer | mysql | superagent |
| busboy | net | systeminformation |
| chokidar | node-expat | tedious |
| cookie | normalize-path | tough-cookie |
| execa | open | Underscore / Lodash |
| fetch | opn | url |
| fs-extra | oracledb | vinyl |
| glob | parseurl | vinyl-fs |
| Google Cloud APIs (Storage) | pg | websocket-stream |
| got | polyglot | winston |
| graceful-fs | qs | ws |
| graphql | query-string | yauzl |
| http | request | z85 |
| http-proxy-middleware | rimraf |  |
| jsonfile | rxjs |  |

Table 6. Frameworks supported by Coverity for Kotlin

|  |
| --- |
| Android SDK |
| Android KTX |

Table 7. Frameworks supported by Coverity for Python. 

Attention: Support for the following Python 2-specific modules and frameworks
will be removed in a future release: cPickle, cStringIO, urllib2, urlparse, mimetools,
rfc822, strop, cookielib, httplib, httplib2, Fabric v1, and legacy Django APIs.

|  |  |  |
| --- | --- | --- |
| aiohttp | flask-user | psycopg2 |
| bcrypt | flask-wtf | PyMySQL |
| Django | fs | requests |
| Flask | httplib2 | requests-oauthlib |
| flask-login | marshmallow | six |
| flask-mysqldb | MySQLdb | sqlalchemy |
| flask-seasurf | oauthlib | urllib3 |
| flask-security | OpenAI | werkzeug |
| flask-sqlalchemy | passlib | yaml |

For frameworks supported by the Sigma analysis engine, please see ["Framework Support"](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/language-and-framework-support.html) in the [Sigma User Guide](https://docs.blackduck.com/r/sigma/latest/sigma-documentation/sigma-user-guide.html).
