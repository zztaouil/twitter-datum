Directory structure:
└── zedeus-nitter/
    ├── README.md
    ├── compose.yml
    ├── config.nims
    ├── Dockerfile
    ├── LICENSE
    ├── nitter.example.conf
    ├── nitter.nimble
    ├── .dockerignore
    ├── .travis.yml
    ├── public/
    │   ├── browserconfig.xml
    │   ├── robots.txt
    │   ├── site.webmanifest
    │   ├── css/
    │   │   ├── fontello.css
    │   │   └── themes/
    │   │       ├── auto.css
    │   │       ├── auto_(twitter).css
    │   │       ├── black.css
    │   │       ├── dracula.css
    │   │       ├── mastodon.css
    │   │       ├── nitter.css
    │   │       ├── pleroma.css
    │   │       ├── twitter.css
    │   │       └── twitter_dark.css
    │   ├── fonts/
    │   │   ├── fontello.eot
    │   │   ├── fontello.ttf
    │   │   ├── fontello.woff
    │   │   ├── fontello.woff2
    │   │   └── LICENSE.txt
    │   ├── js/
    │   │   ├── hlsPlayback.js
    │   │   └── infiniteScroll.js
    │   └── md/
    │       └── about.md
    ├── src/
    │   ├── api.nim
    │   ├── apiutils.nim
    │   ├── auth.nim
    │   ├── config.nim
    │   ├── consts.nim
    │   ├── formatters.nim
    │   ├── http_pool.nim
    │   ├── nitter.nim
    │   ├── parser.nim
    │   ├── parserutils.nim
    │   ├── prefs.nim
    │   ├── prefs_impl.nim
    │   ├── query.nim
    │   ├── redis_cache.nim
    │   ├── tid.nim
    │   ├── types.nim
    │   ├── utils.nim
    │   ├── experimental/
    │   │   ├── parser.nim
    │   │   ├── parser/
    │   │   │   ├── article.nim
    │   │   │   ├── graphql.nim
    │   │   │   ├── session.nim
    │   │   │   ├── slices.nim
    │   │   │   ├── tid.nim
    │   │   │   ├── unifiedcard.nim
    │   │   │   ├── user.nim
    │   │   │   └── utils.nim
    │   │   └── types/
    │   │       ├── article.nim
    │   │       ├── common.nim
    │   │       ├── graphfollowers.nim
    │   │       ├── graphlistmembers.nim
    │   │       ├── graphuser.nim
    │   │       ├── session.nim
    │   │       ├── tid.nim
    │   │       ├── unifiedcard.nim
    │   │       └── user.nim
    │   ├── routes/
    │   │   ├── article.nim
    │   │   ├── broadcast.nim
    │   │   ├── community.nim
    │   │   ├── debug.nim
    │   │   ├── embed.nim
    │   │   ├── list.nim
    │   │   ├── media.nim
    │   │   ├── preferences.nim
    │   │   ├── resolver.nim
    │   │   ├── router_utils.nim
    │   │   ├── rss.nim
    │   │   ├── search.nim
    │   │   ├── space.nim
    │   │   ├── status.nim
    │   │   ├── timeline.nim
    │   │   └── unsupported.nim
    │   ├── sass/
    │   │   ├── _article.scss
    │   │   ├── _broadcast.scss
    │   │   ├── _space.scss
    │   │   ├── general.scss
    │   │   ├── index.scss
    │   │   ├── inputs.scss
    │   │   ├── navbar.scss
    │   │   ├── search.scss
    │   │   ├── timeline.scss
    │   │   ├── include/
    │   │   │   ├── _mixins.css
    │   │   │   └── _variables.scss
    │   │   ├── profile/
    │   │   │   ├── _base.scss
    │   │   │   ├── _community.scss
    │   │   │   ├── about-account.scss
    │   │   │   ├── card.scss
    │   │   │   └── photo-rail.scss
    │   │   └── tweet/
    │   │       ├── _base.scss
    │   │       ├── card.scss
    │   │       ├── embed.scss
    │   │       ├── media.scss
    │   │       ├── poll.scss
    │   │       ├── quote.scss
    │   │       ├── thread.scss
    │   │       └── video.scss
    │   └── views/
    │       ├── about.nim
    │       ├── about_account.nim
    │       ├── article.nim
    │       ├── broadcast.nim
    │       ├── community.nim
    │       ├── embed.nim
    │       ├── feature.nim
    │       ├── general.nim
    │       ├── list.nim
    │       ├── opensearch.nimf
    │       ├── preferences.nim
    │       ├── profile.nim
    │       ├── renderutils.nim
    │       ├── rss.nimf
    │       ├── search.nim
    │       ├── space.nim
    │       ├── status.nim
    │       ├── timeline.nim
    │       └── tweet.nim
    ├── tests/
    │   ├── base.py
    │   ├── poetry.toml
    │   ├── pyproject.toml
    │   ├── requirements.txt
    │   ├── test_about_account.py
    │   ├── test_article.py
    │   ├── test_card.py
    │   ├── test_community.py
    │   ├── test_followers.py
    │   ├── test_profile.py
    │   ├── test_quote.py
    │   ├── test_search.py
    │   ├── test_security.py
    │   ├── test_space.py
    │   ├── test_ssrf_1411.nim
    │   ├── test_thread.py
    │   ├── test_timeline.py
    │   ├── test_tweet.py
    │   └── test_tweet_media.py
    ├── tools/
    │   ├── create_session_browser.py
    │   ├── create_session_curl.py
    │   ├── create_sessions_browser.py
    │   ├── gencss.nim
    │   ├── get_session.py
    │   ├── rendermd.nim
    │   └── requirements.txt
    └── .github/
        ├── FUNDING.yml
        └── workflows/
            ├── build-docker.yml
            └── run-tests.yml

================================================
FILE: README.md
================================================
# Nitter

[![Test Matrix](https://github.com/zedeus/nitter/workflows/Tests/badge.svg)](https://github.com/zedeus/nitter/actions/workflows/run-tests.yml)
[![Test Matrix](https://github.com/zedeus/nitter/workflows/Docker/badge.svg)](https://github.com/zedeus/nitter/actions/workflows/build-docker.yml)
[![License](https://img.shields.io/github/license/zedeus/nitter?style=flat)](#license)

> [!NOTE]
> Running a Nitter instance now requires real accounts, since Twitter removed the previous methods. \
> This does not affect users. \
> For instructions on how to obtain session tokens, see [Creating session tokens](https://github.com/zedeus/nitter/wiki/Creating-session-tokens).

A free and open source alternative Twitter front-end focused on privacy and
performance. \
Inspired by the [Invidious](https://github.com/iv-org/invidious) project.

- No JavaScript or ads
- All requests go through the backend, client never talks to Twitter
- Prevents Twitter from tracking your IP or JavaScript fingerprint
- Uses Twitter's unofficial API (no developer account required)
- Lightweight (for [@nim_lang](https://nitter.net/nim_lang), 60KB vs 784KB from twitter.com)
- RSS feeds
- Themes
- Mobile support (responsive design)
- AGPLv3 licensed, no proprietary instances permitted

<details>
<summary>Donations</summary>
Liberapay: https://liberapay.com/zedeus<br>
Patreon: https://patreon.com/nitter<br>
BTC: bc1qpqpzjkcpgluhzf7x9yqe7jfe8gpfm5v08mdr55<br>
ETH: 0x24a0DB59A923B588c7A5EBd0dBDFDD1bCe9c4460<br>
XMR: 42hKayRoEAw4D6G6t8mQHPJHQcXqofjFuVfavqKeNMNUZfeJLJAcNU19i1bGdDvcdN6romiSscWGWJCczFLe9RFhM3d1zpL<br>
SOL: ANsyGNXFo6osuFwr1YnUqif2RdoYRhc27WdyQNmmETSW<br>
ZEC: u1vndfqtzyy6qkzhkapxelel7ams38wmfeccu3fdpy2wkuc4erxyjm8ncjhnyg747x6t0kf0faqhh2hxyplgaum08d2wnj4n7cyu9s6zhxkqw2aef4hgd4s6vh5hpqvfken98rg80kgtgn64ff70djy7s8f839z00hwhuzlcggvefhdlyszkvwy3c7yw623vw3rvar6q6evd3xcvveypt
</details>

## Roadmap

- Embeds
- Account system with timeline support
- Archiving tweets/profiles
- Developer API

## Resources

The wiki contains
[a list of instances](https://github.com/zedeus/nitter/wiki/Instances) and
[browser extensions](https://github.com/zedeus/nitter/wiki/Extensions)
maintained by the community.

## Why?

It's impossible to use Twitter without JavaScript enabled, and as of 2024 you
need to sign up. For privacy-minded folks, preventing JavaScript analytics and
IP-based tracking is important, but apart from using a VPN and uBlock/uMatrix,
it's impossible. Despite being behind a VPN and using heavy-duty adblockers,
you can get accurately tracked with your [browser's
fingerprint](https://restoreprivacy.com/browser-fingerprinting/), [no
JavaScript required](https://noscriptfingerprint.com/). This all became
particularly important after Twitter [removed the
ability](https://www.eff.org/deeplinks/2020/04/twitter-removes-privacy-option-and-shows-why-we-need-strong-privacy-laws)
for users to control whether their data gets sent to advertisers.

Using an instance of Nitter (hosted on a VPS for example), you can browse
Twitter without JavaScript while retaining your privacy. In addition to
respecting your privacy, Nitter is on average around 15 times lighter than
Twitter, and in most cases serves pages faster (eg. timelines load 2-4x faster).

In the future a simple account system will be added that lets you follow Twitter
users, allowing you to have a clean chronological timeline without needing a
Twitter account.

## Screenshot

![nitter](/screenshot.png)

## Installation

### Dependencies

- libpcre
- libsass
- redis/valkey

To compile Nitter you need a Nim installation, see
[nim-lang.org](https://nim-lang.org/install.html) for details. It is possible
to install it system-wide or in the user directory you create below.

To compile the scss files, you need to install `libsass`. On Ubuntu and Debian,
you can use `libsass-dev`.

Redis is required for caching and in the future for account info. As of 2024
Redis is no longer open source, so using the fork Valkey is recommended. It
should be available on most distros as `redis` or `redis-server`
(Ubuntu/Debian), or `valkey`/`valkey-server`. Running it with the default
config is fine, Nitter's default config is set to use the default port and
localhost.

Here's how to create a `nitter` user, clone the repo, and build the project
along with the scss and md files.

```bash
# useradd -m nitter
# su nitter
$ git clone https://github.com/zedeus/nitter
$ cd nitter
$ nimble -l build -d:danger --mm:refc
$ nimble -l scss
$ nimble -l md
$ cp nitter.example.conf nitter.conf
```

Set your hostname, port, HMAC key, https (must be correct for cookies), and
Redis info in `nitter.conf`. To run Redis, either run
`redis-server --daemonize yes`, or `systemctl enable --now redis` (or
redis-server depending on the distro). Run Nitter by executing `./nitter` or
using the systemd service below. You should run Nitter behind a reverse proxy
such as [Nginx](https://github.com/zedeus/nitter/wiki/Nginx) or
[Apache](https://github.com/zedeus/nitter/wiki/Apache) for security and
performance reasons.

### Docker

Page for the Docker image: https://hub.docker.com/r/zedeus/nitter

#### NOTE: The published image is multi-arch — `zedeus/nitter:latest` runs natively on both `amd64` and `arm64`.

To run Nitter with Docker, you'll need to install and run Redis separately
before you can run the container. See below for how to also run Redis using
Docker.

First create your config file. The Docker commands mount it into the container,
so it has to exist on the host beforehand. If you've cloned the repo:

```bash
cp nitter.example.conf nitter.conf
```

If you're using the prebuilt image without a local clone, download
[`nitter.example.conf`](https://raw.githubusercontent.com/zedeus/nitter/master/nitter.example.conf)
and save it as `nitter.conf` instead.

To build and run Nitter in Docker:

```bash
docker build -t nitter:latest .
docker run -v $(pwd)/nitter.conf:/src/nitter.conf -d --network host nitter:latest
```

A prebuilt Docker image is provided as well:

```bash
docker run -v $(pwd)/nitter.conf:/src/nitter.conf -d --network host zedeus/nitter:latest
```

Using docker-compose to run both Nitter and Redis as different containers:
Change `redisHost` from `localhost` to `nitter-redis` in `nitter.conf`, then run:

```bash
docker-compose up -d
```

Note the Docker commands mount `nitter.conf` (and `sessions.jsonl` for
docker-compose) from the directory you run them in. If a mounted file doesn't
exist, Docker silently creates a directory in its place and the container fails
with `not a directory: Are you trying to mount a directory onto a file`. Remove
that directory and create the file as shown above.

### systemd

To run Nitter via systemd you can use this service file:

```ini
[Unit]
Description=Nitter (An alternative Twitter front-end)
After=syslog.target
After=network.target

[Service]
Type=simple

# set user and group
User=nitter
Group=nitter

# configure location
WorkingDirectory=/home/nitter/nitter
ExecStart=/home/nitter/nitter/nitter

Restart=always
RestartSec=15

[Install]
WantedBy=multi-user.target
```

Then enable and run the service:
`systemctl enable --now nitter.service`

### Logging

Nitter currently prints some errors to stdout, and there is no real logging
implemented. If you're running Nitter with systemd, you can check stdout like
this: `journalctl -u nitter.service` (add `--follow` to see just the last 15
lines). If you're running the Docker image, you can do this:
`docker logs --follow *nitter container id*`

## Contact

Feel free to join our [Matrix channel](https://matrix.to/#/#nitter:matrix.org).
You can email me at zedeus@pm.me if you wish to contact me personally.



================================================
FILE: compose.yml
================================================
services:

  nitter:
    image: zedeus/nitter:latest
    container_name: nitter
    ports:
      - "127.0.0.1:8080:8080" # Replace with "8080:8080" if you don't use a reverse proxy
    volumes:
      - ./nitter.conf:/src/nitter.conf:Z,ro
      - ./sessions.jsonl:/src/sessions.jsonl:Z,ro # Run get_sessions.py to get the credentials
    depends_on:
      - nitter-redis
    restart: unless-stopped
    healthcheck:
      test: wget -nv --tries=1 --spider http://127.0.0.1:8080/Jack/status/20 || exit 1
      interval: 30s
      timeout: 5s
      retries: 2
    user: "998:998"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL

  nitter-redis:
    image: redis:6-alpine
    container_name: nitter-redis
    command: redis-server --save 60 1 --loglevel warning
    volumes:
      - nitter-redis:/data
    restart: unless-stopped
    healthcheck:
      test: redis-cli ping
      interval: 30s
      timeout: 5s
      retries: 2
    user: "999:1000"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL

volumes:
  nitter-redis:



================================================
FILE: config.nims
================================================
--define:ssl
--define:useStdLib
--threads:off

# workaround httpbeast file upload bug
--assertions:off

# disable annoying warnings
warning("GcUnsafe2", off)
warning("HoleEnumConv", off)
hint("XDeclaredButNotUsed", off)
hint("XCannotRaiseY", off)
hint("User", off)
# begin Nimble config (version 2)
when withDir(thisDir(), system.fileExists("nimble.paths")):
  include "nimble.paths"
# end Nimble config



================================================
FILE: Dockerfile
================================================
FROM nimlang/nim:2.2.6-alpine-regular as nim
LABEL maintainer="setenforce@protonmail.com"

RUN apk --no-cache add libsass-dev pcre

WORKDIR /src/nitter

COPY nitter.nimble .
RUN nimble install -y --depsOnly

COPY . .
RUN nimble build -d:danger -d:lto -d:strip --mm:refc \
    && nimble scss \
    && nimble md

FROM alpine:latest
WORKDIR /src/
RUN apk --no-cache add pcre ca-certificates openssl
COPY --from=nim /src/nitter/nitter ./
COPY --from=nim /src/nitter/nitter.example.conf ./nitter.conf
COPY --from=nim /src/nitter/public ./public
EXPOSE 8080
RUN adduser -h /src/ -D -s /bin/sh nitter
USER nitter
CMD ./nitter



================================================
FILE: LICENSE
================================================
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  Developers that use our General Public Licenses protect your rights
with two steps: (1) assert copyright on the software, and (2) offer
you this License which gives you legal permission to copy, distribute
and/or modify the software.

  A secondary benefit of defending all users' freedom is that
improvements made in alternate versions of the program, if they
receive widespread use, become available for other developers to
incorporate.  Many developers of free software are heartened and
encouraged by the resulting cooperation.  However, in the case of
software used on network servers, this result may fail to come about.
The GNU General Public License permits making a modified version and
letting the public access it on a server without ever releasing its
source code to the public.

  The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community.  It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server.  Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version.

  An older license, called the Affero General Public License and
published by Affero, was designed to accomplish similar goals.  This is
a different license, not a version of the Affero GPL, but Affero has
released a new version of the Affero GPL which permits relicensing under
this license.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU Affero General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Remote Network Interaction; Use with the GNU General Public License.

  Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users
interacting with it remotely through a computer network (if your version
supports such interaction) an opportunity to receive the Corresponding
Source of your version by providing access to the Corresponding Source
from a network server at no charge, through some standard or customary
means of facilitating copying of software.  This Corresponding Source
shall include the Corresponding Source for any work covered by version 3
of the GNU General Public License that is incorporated pursuant to the
following paragraph.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the work with which it is combined will remain governed by version
3 of the GNU General Public License.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU Affero General Public License from time to time.  Such new versions
will be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU Affero General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU Affero General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU Affero General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If your software can interact with users remotely through a computer
network, you should also make sure that it provides a way for users to
get its source.  For example, if your program is a web application, its
interface could display a "Source" link that leads users to an archive
of the code.  There are many ways you could offer source, and different
solutions will be better for different programs; see section 13 for the
specific requirements.

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU AGPL, see
<http://www.gnu.org/licenses/>.


================================================
FILE: nitter.example.conf
================================================
[Server]
hostname = "nitter.net"      # for generating links, change this to your own domain/ip
title = "nitter"
address = "0.0.0.0"
port = 8080
https = false                # disable to enable cookies when not using https
httpMaxConnections = 100
staticDir = "./public"

[Cache]
listMinutes = 240            # how long to cache list info (not the tweets, so keep it high)
rssMinutes = 10              # how long to cache rss queries
redisHost = "localhost"      # Change to "nitter-redis" if using docker-compose
redisPort = 6379
redisPassword = ""
redisConnections = 20        # minimum open connections in pool
redisMaxConnections = 30
# new connections are opened when none are available, but if the pool size
# goes above this, they're closed when released. don't worry about this unless
# you receive tons of requests per second

[Config]
hmacKey = "secretkey"        # CHANGE THIS to a unique random value (e.g. `openssl rand -hex 32`); signs media urls
base64Media = false          # use base64 encoding for proxied media urls
enableRSS = true             # master switch, set to false to disable all RSS feeds
enableRSSUserTweets = true   # /@user/rss
enableRSSUserReplies = true  # /@user/with_replies/rss
enableRSSUserMedia = true    # /@user/media/rss
enableRSSSearch = true       # /search/rss and /@user/search/rss
enableRSSList = true         # list RSS feeds
enableDebug = false          # enable request logs and debug endpoints (/.sessions)
proxy = ""                   # http/https url, SOCKS proxies are not supported
proxyAuth = ""
apiProxy = ""                # nitter-proxy host, e.g. localhost:7000
disableTid = false           # enable this if cookie-based auth is failing
maxConcurrentReqs = 2        # max requests at a time per session to avoid race conditions
maxRetries = 1               # max number of retries on rate limit errors
retryDelayMs = 150           # delay in ms between retries

# Change default preferences here, see src/prefs_impl.nim for a complete list
[Preferences]
theme = "Nitter"
replaceTwitter = "nitter.net"
replaceYouTube = "piped.video"
replaceReddit = "teddit.net"
proxyVideos = true
hlsPlayback = false
infiniteScroll = false



================================================
FILE: nitter.nimble
================================================
# Package

version       = "0.1.0"
author        = "zedeus"
description   = "An alternative front-end for Twitter"
license       = "AGPL-3.0"
srcDir        = "src"
bin           = @["nitter"]


# Dependencies

requires "nim >= 2.0.0"
requires "jester == 0.6.0"
requires "karax == 1.5.0"
requires "sass == 0.2.0"
requires "nimcrypto == 0.7.3"
requires "markdown == 0.8.8"
requires "packedjson#9e6fbb6"
requires "supersnappy == 2.1.4"
requires "redpool == 0.2.2"
requires "zippy == 0.10.19"
requires "flatty == 0.4.0"
requires "jsony == 1.1.6"
requires "oauth == 0.11"

# Tasks

task scss, "Generate css":
  exec "nim r --hint[Processing]:off tools/gencss"

task md, "Render md":
  exec "nim r --hint[Processing]:off tools/rendermd"



================================================
FILE: .dockerignore
================================================
*.png
*.md
LICENSE
docker-compose.yml
Dockerfile
tests/



================================================
FILE: .travis.yml
================================================
jobs:
  include:
    - stage: test
      if: (NOT type IN (pull_request)) AND (branch = master)
      dist: bionic
      language: python
      python:
        - 3.6
      services:
        - docker
        - xvfb
      script:
        - sudo apt update
        - sudo apt install --force-yes chromium-chromedriver
        - wget https://www.dropbox.com/s/ckuoaubd1crrj2k/Linux_x64_737173_chrome-linux.zip -O chrome.zip
        - unzip chrome.zip
        - cd chrome-linux
        - sudo rm /usr/bin/google-chrome
        - sudo ln -s chrome /usr/bin/google-chrome
        - cd ..
        - pip3 install --upgrade pip
        - pip3 install -U seleniumbase pytest
        - docker run -d -p 127.0.0.1:8080:8080/tcp $IMAGE_NAME:$TRAVIS_COMMIT
        - sleep 10
        - cd tests
        - pytest --headless -n 8 --reruns 10 --reruns-delay 2
    - stage: pr
      if: type IN (pull_request)
      dist: bionic
      language: python
      python:
        - 3.6
      services:
        - docker
        - xvfb
      script:
        - sudo apt update
        - sudo apt install --force-yes chromium-chromedriver
        - wget https://www.dropbox.com/s/ckuoaubd1crrj2k/Linux_x64_737173_chrome-linux.zip -O chrome.zip
        - unzip chrome.zip
        - cd chrome-linux
        - sudo rm /usr/bin/google-chrome
        - sudo ln -s chrome /usr/bin/google-chrome
        - cd ..
        - pip3 install --upgrade pip
        - pip3 install -U seleniumbase pytest
        - docker build -t $IMAGE_NAME:$TRAVIS_COMMIT .
        - docker run -d -p 127.0.0.1:8080:8080/tcp $IMAGE_NAME:$TRAVIS_COMMIT
        - sleep 10
        - cd tests
        - pytest --headless -n 8 --reruns 3 --reruns-delay 2



================================================
FILE: public/browserconfig.xml
================================================
<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
    <msapplication>
        <tile>
            <TileColor>#2b5797</TileColor>
        </tile>
    </msapplication>
</browserconfig>



================================================
FILE: public/robots.txt
================================================
User-agent: *
Disallow: /
Crawl-delay: 1
User-agent: Twitterbot
Disallow:



================================================
FILE: public/site.webmanifest
================================================
{
    "name": "Nitter",
    "short_name": "Nitter",
    "icons": [
        {
            "src": "/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/android-chrome-384x384.png",
            "sizes": "384x384",
            "type": "image/png"
        },
        {
            "src": "/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#333333",
    "background_color": "#333333",
    "display": "standalone"
}



================================================
FILE: public/css/fontello.css
================================================
@font-face {
  font-family: "fontello";
  src: url("/fonts/fontello.eot?59696369");
  src:
    url("/fonts/fontello.eot?59696369#iefix") format("embedded-opentype"),
    url("/fonts/fontello.woff2?59696369") format("woff2"),
    url("/fonts/fontello.woff?59696369") format("woff"),
    url("/fonts/fontello.ttf?59696369") format("truetype"),
    url("/fonts/fontello.svg?59696369#fontello") format("svg");
  font-weight: normal;
  font-style: normal;
}

[class^="icon-"]:before,
[class*=" icon-"]:before {
  font-family: "fontello";
  font-style: normal;
  font-weight: normal;
  speak: never;

  display: inline-block;
  text-decoration: inherit;
  width: 1em;
  margin-right: 0.2em;
  text-align: center;

  /* For safety - reset parent styles, that can break glyph codes*/
  font-variant: normal;
  text-transform: none;

  /* fix buttons height, for twitter bootstrap */
  line-height: 1em;

  /* Font smoothing. That was taken from TWBS */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.icon-group:before {
  content: "\e0c3";
}

/* '' */
.icon-views:before {
  content: "\e800";
}

/* '' */
.icon-heart:before {
  content: "\e801";
}

/* '' */
.icon-quote:before {
  content: "\e802";
}

/* '' */
.icon-comment:before {
  content: "\e803";
}

/* '' */
.icon-play:before {
  content: "\e805";
}

/* '' */
.icon-link:before {
  content: "\e806";
}

/* '' */
.icon-calendar:before {
  content: "\e807";
}

/* '' */
.icon-location:before {
  content: "\e808";
}

/* '' */
.icon-picture:before {
  content: "\e809";
}

/* '' */
.icon-lock:before {
  content: "\e80a";
}

/* '' */
.icon-down:before {
  content: "\e80b";
}

/* '' */
.icon-retweet:before {
  content: "\e80c";
}

/* '' */
.icon-search:before {
  content: "\e80d";
}

/* '' */
.icon-pin:before {
  content: "\e80e";
}

/* '' */
.icon-cog:before {
  content: "\e80f";
}

/* '' */
.icon-rss:before {
  content: "\e810";
}

/* '' */
.icon-ok:before {
  content: "\e811";
}

/* '' */
.icon-attention-circled:before {
  content: "\e812";
}

/* '' */
.icon-download-alt:before {
  content: "\e813";
}

/* '' */
.icon-circle:before {
  content: "\f111";
}

/* '' */
.icon-info:before {
  content: "\f128";
}

/* '' */
.icon-bird:before {
  content: "\f309";
}

/* '' */



================================================
FILE: public/css/themes/auto.css
================================================
@import "nitter.css" (prefers-color-scheme: dark);
@import "twitter.css" (prefers-color-scheme: light);



================================================
FILE: public/css/themes/auto_(twitter).css
================================================
@import "twitter_dark.css" (prefers-color-scheme: dark);
@import "twitter.css" (prefers-color-scheme: light);



================================================
FILE: public/css/themes/black.css
================================================
body {
    --bg_color: #000000;
    --fg_color: #FFFFFF;
    --fg_faded: #FFFFFFD4;
    --fg_dark: var(--accent);
    --fg_nav: var(--accent);

    --bg_panel: #0C0C0C;
    --bg_elements: #000000;
    --bg_overlays: var(--bg_panel);
    --bg_hover: #131313;

    --grey: #E2E2E2;
    --dark_grey: #4E4E4E;
    --darker_grey: #272727;
    --darkest_grey: #212121;
    --border_grey: #7D7D7D;

    --accent: #FF6C60;
    --accent_light: #FFACA0;
    --accent_dark: #909090;
    --accent_border: #FF6C6091;

    --play_button: var(--accent);
    --play_button_hover: var(--accent_light);

    --more_replies_dots: #A7A7A7;
    --error_red: #420A05;

    --verified_blue: #1DA1F2;
    --icon_text: var(--fg_color);

    --tab: var(--fg_color);
    --tab_selected: var(--accent);

    --profile_stat: var(--fg_color);
}



================================================
FILE: public/css/themes/dracula.css
================================================
body {
    --bg_color: #282a36;
    --fg_color: #f8f8f2;
    --fg_faded: #818eb6;
    --fg_dark: var(--fg_faded);
    --fg_nav: var(--accent);

    --bg_panel: #343746;
    --bg_elements: #292b36;
    --bg_overlays: #44475a;
    --bg_hover: #2f323f;

    --grey: var(--fg_faded);
    --dark_grey: #44475a;
    --darker_grey: #3d4051;
    --darkest_grey: #363948;
    --border_grey: #44475a;

    --accent: #bd93f9;
    --accent_light: #caa9fa;
    --accent_dark: var(--accent);
    --accent_border: #ff79c696;

    --play_button: #ffb86c;
    --play_button_hover: #ffc689;

    --more_replies_dots: #bd93f9;
    --error_red: #ff5555;

    --verified_blue: var(--accent);
    --icon_text: ##F8F8F2;

    --tab: #6272a4;
    --tab_selected: var(--accent);

    --profile_stat: #919cbf;
}

.search-bar > form input::placeholder{
    color: var(--fg_faded);
}


================================================
FILE: public/css/themes/mastodon.css
================================================
body {
    --bg_color: #191B22;
    --fg_color: #FFFFFF;
    --fg_faded: #F8F8F2CF;
    --fg_dark: var(--accent);
    --fg_nav: var(--accent);

    --bg_panel: #282C37;
    --bg_elements: #22252F;
    --bg_overlays: var(--bg_panel);
    --bg_hover: var(--bg_elements);

    --grey: #8595AB;
    --dark_grey: #393F4F;
    --darker_grey: #1C1E23;
    --darkest_grey: #1F2125;
    --border_grey: #393F4F;

    --accent: #9BAEC8;
    --accent_light: #CDDEF5;
    --accent_dark: #748294;
    --accent_border: var(--accent_dark);

    --play_button: var(--accent);
    --play_button_hover: var(--accent_light);

    --more_replies_dots: #7F8DA0;
    --error_red: #420A05;

    --verified_blue: #1DA1F2;
    --icon_text: var(--fg_color);

    --tab: var(--accent);
    --tab_selected: #D9E1E8;

    --profile_stat: var(--fg_color);
}



================================================
FILE: public/css/themes/nitter.css
================================================
body {
    /* uses default values */
}



================================================
FILE: public/css/themes/pleroma.css
================================================
body {
    --bg_color: #0A1117;
    --fg_color: #B9B9BA;
    --fg_faded: #B9B9BAFA;
    --fg_dark: var(--accent);
    --fg_nav: var(--accent);

    --bg_panel: #121A24;
    --bg_elements: #182230;
    --bg_overlays: var(--bg_elements);
    --bg_hover: #1B2735;

    --grey: #666A6F;
    --dark_grey: #42413D;
    --darker_grey: #293442;
    --darkest_grey: #202935;
    --border_grey: #1C2737;

    --accent: #D8A070;
    --accent_light: #DEB897;
    --accent_dark: #6D533C;
    --accent_border: #947050;

    --play_button: var(--accent);
    --play_button_hover: var(--accent_light);

    --more_replies_dots: #886446;
    --error_red: #420A05;

    --verified_blue: #1DA1F2;
    --icon_text: #F8F8F8;

    --tab: var(--fg_color);
    --tab_selected: var(--accent);

    --profile_stat: var(--fg_color);
}



================================================
FILE: public/css/themes/twitter.css
================================================
body {
    --bg_color: #E6ECF0;
    --fg_color: #0F0F0F;
    --fg_faded: #657786;
    --fg_dark: var(--fg_faded);
    --fg_nav: var(--accent);

    --bg_panel: #FFFFFF;
    --bg_elements: #FDFDFD;
    --bg_overlays: #FFFFFF;
    --bg_hover: #F5F8FA;

    --grey: var(--fg_faded);
    --dark_grey: #D6D6D6;
    --darker_grey: #CECECE;
    --darkest_grey: #ECECEC;
    --border_grey: #E6ECF0;

    --accent: #1DA1F2;
    --accent_light: #A0EDFF;
    --accent_dark: var(--accent);
    --accent_border: #1DA1F296;

    --play_button: #D84D4D;
    --play_button_hover: #FF6C60;

    --more_replies_dots: #0199F7;
    --error_red: #FF7266;

    --verified_blue: var(--accent);
    --icon_text: #F8F8F2;

    --tab: var(--accent);
    --tab_selected: #000000;

    --profile_stat: var(--fg_dark);
}



================================================
FILE: public/css/themes/twitter_dark.css
================================================
body {
    --bg_color: #101821;
    --fg_color: #FFFFFF;
    --fg_faded: #8899A6;
    --fg_dark: var(--fg_faded);
    --fg_nav: var(--accent);

    --bg_panel: #15202B;
    --bg_elements: var(--bg_panel);
    --bg_overlays: var(--bg_panel);
    --bg_hover: #192734;

    --grey: var(--fg_faded);
    --dark_grey: #38444D;
    --darker_grey: #2A343C;
    --darkest_grey:#1B2835;
    --border_grey: #38444D;

    --accent: #1B95E0;
    --accent_light: #80CEFF;
    --accent_dark: #2B608A;
    --accent_border: #1B95E096;

    --play_button: var(--accent);
    --play_button_hover: var(--accent_light);

    --more_replies_dots: #39719C;
    --error_red: #FF7266;

    --verified_blue: var(--accent);
    --icon_text: var(--fg_color);

    --tab: var(--grey);
    --tab_selected: var(--accent);

    --profile_stat: var(--fg_color);
}



================================================
FILE: public/fonts/fontello.eot
================================================
[Binary file]


================================================
FILE: public/fonts/fontello.ttf
================================================
[Binary file]


================================================
FILE: public/fonts/fontello.woff
================================================
[Binary file]


================================================
FILE: public/fonts/fontello.woff2
================================================
[Binary file]


================================================
FILE: public/fonts/LICENSE.txt
================================================
Font license info


## Modern Pictograms

   Copyright (c) 2012 by John Caserta. All rights reserved.

   Author:    John Caserta
   License:   SIL (http://scripts.sil.org/OFL)
   Homepage:  http://thedesignoffice.org/project/modern-pictograms/


## Entypo

   Copyright (C) 2012 by Daniel Bruce

   Author:    Daniel Bruce
   License:   SIL (http://scripts.sil.org/OFL)
   Homepage:  http://www.entypo.com


## Iconic

   Copyright (C) 2012 by P.J. Onori

   Author:    P.J. Onori
   License:   SIL (http://scripts.sil.org/OFL)
   Homepage:  http://somerandomdude.com/work/iconic/


## Font Awesome

   Copyright (C) 2016 by Dave Gandy

   Author:    Dave Gandy
   License:   SIL ()
   Homepage:  http://fortawesome.github.com/Font-Awesome/


## Elusive

   Copyright (C) 2013 by Aristeides Stathopoulos

   Author:    Aristeides Stathopoulos
   License:   SIL (http://scripts.sil.org/OFL)
   Homepage:  http://aristeides.com/





================================================
FILE: public/js/hlsPlayback.js
================================================
// @license http://www.gnu.org/licenses/agpl-3.0.html AGPL-3.0
// SPDX-License-Identifier: AGPL-3.0-only
function playMedia(overlay, tagName) {
    const media = overlay.parentElement.querySelector(tagName);
    const url = media.getAttribute("data-url");
    const startTime = parseFloat(media.getAttribute("data-start") || "0");
    media.setAttribute("controls", "");
    overlay.style.display = "none";

    if (Hls.isSupported()) {
        var hls = new Hls({autoStartLoad: false});
        hls.loadSource(url);
        hls.attachMedia(media);
        hls.on(Hls.Events.MANIFEST_PARSED, function () {
            hls.loadLevel = hls.levels.length - 1;
            hls.startLoad(startTime);
            media.play();
        });
    } else if (media.canPlayType('application/vnd.apple.mpegurl')) {
        media.src = url;
        media.addEventListener('canplay', function() {
            if (startTime > 0) media.currentTime = startTime;
            media.play();
        });
    }
}

function playVideo(overlay) { playMedia(overlay, 'video'); }
function playAudio(overlay) { playMedia(overlay, 'audio'); }
// @license-end



================================================
FILE: public/js/infiniteScroll.js
================================================
// @license http://www.gnu.org/licenses/agpl-3.0.html AGPL-3.0
// SPDX-License-Identifier: AGPL-3.0-only

function insertBeforeLast(node, elem) {
  node.insertBefore(elem, node.childNodes[node.childNodes.length - 2]);
}

function getLoadMore(doc) {
  return doc.querySelector(".show-more:not(.timeline-item)");
}

function getHrefs(selector) {
  return new Set([...document.querySelectorAll(selector)].map(el => el.getAttribute("href")));
}

function getTweetId(item) {
  const m = item.querySelector(".tweet-link")?.getAttribute("href")?.match(/\/status\/(\d+)/);
  return m ? m[1] : "";
}

function isDuplicate(item, hrefs) {
  return hrefs.has(item.querySelector(".tweet-link")?.getAttribute("href"));
}

const GAP = 10;

class Masonry {
  constructor(container) {
    this.container = container;
    const colSizes = {
      small:  w => Math.max(130, w * 0.11),
      medium: w => Math.max(190, Math.min(350, w * 0.22)),
      large:  w => Math.max(350, Math.min(480, w * 0.22)),
    };
    const size = container.dataset.colSize || "medium";
    this._targetWidth = colSizes[size] || colSizes.medium;
    this.colHeights = [];
    this.colCounts = [];
    this.colCount = 0;
    this._lastWidth = 0;
    this._colWidthCache = 0;
    this._items = [];
    this._revealTimer = null;
    this.container.classList.add("masonry-active");

    let resizeTimer;
    window.addEventListener("resize", () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => this._rebuild(), 50);
    });

    // Re-sync positions whenever images finish loading and items grow taller.
    // Must be set up before _rebuild() so initial items get observed on first pass.
    let syncTimer;
    this._observer = window.ResizeObserver ? new ResizeObserver(() => {
      clearTimeout(syncTimer);
      syncTimer = setTimeout(() => this.syncHeights(), 100);
    }) : null;

    this._rebuild();
  }

  // Reveal all items and gallery siblings (show-more, top-ref). Idempotent.
  _revealAll() {
    clearTimeout(this._revealTimer);
    for (const item of this._items) item.classList.add("masonry-visible");
    for (const el of this.container.parentElement.querySelectorAll(":scope > .show-more, :scope > .top-ref, :scope > .timeline-footer"))
      el.classList.add("masonry-visible");
  }

  // Height-primary, count-as-tiebreaker: handles both tall tweets and unloaded images.
  _pickCol() {
    return this.colHeights.reduce((min, h, i) => {
      const m = this.colHeights[min];
      return (h < m || (h === m && this.colCounts[i] < this.colCounts[min])) ? i : min;
    }, 0);
  }

  // Position items using current column state. Updates colHeights, colCounts, container height.
  _position(items, heights, colWidth) {
    for (let i = 0; i < items.length; i++) {
      const col = this._pickCol();
      items[i].style.left = `${col * (colWidth + GAP)}px`;
      items[i].style.top = `${this.colHeights[col]}px`;
      this.colHeights[col] += heights[i] + GAP;
      this.colCounts[col]++;
    }
    this.container.style.height = `${Math.max(0, ...this.colHeights)}px`;
  }

  // Full reset and re-place all items.
  _place(items, heights, n, colWidth) {
    this.colHeights = new Array(n).fill(0);
    this.colCounts = new Array(n).fill(0);
    this.colCount = n;
    this._position(items, heights, colWidth);
  }

  _rebuild() {
    const w = this.container.clientWidth;
    const n = Math.max(1, Math.floor(w / this._targetWidth(w)));
    if (n === this.colCount && w === this._lastWidth) return;

    const isFirst = this.colCount === 0;

    if (isFirst) {
      this._items = [...this.container.querySelectorAll(".timeline-item")];
    }

    // Sort newest-first by tweet ID (snowflake IDs exceed Number precision, compare as strings).
    this._items.sort((a, b) => {
      const idA = getTweetId(a), idB = getTweetId(b);
      if (idA.length !== idB.length) return idB.length - idA.length;
      return idB < idA ? -1 : idB > idA ? 1 : 0;
    });

    // Pre-set widths BEFORE reading heights so measurements reflect the new column width.
    const colWidth = this._colWidthCache = Math.floor((w - GAP * (n - 1)) / n);
    for (const item of this._items) item.style.width = `${colWidth}px`;

    this._place(this._items, this._items.map(item => item.offsetHeight), n, colWidth);
    this._lastWidth = w;

    if (isFirst) {
      if (this._observer) this._items.forEach(item => this._observer.observe(item));
      // Reveal immediately if all images are cached, else wait for syncHeights.
      const hasUnloaded = this._items.some(item =>
        [...item.querySelectorAll("img")].some(img => !img.complete));
      if (hasUnloaded) {
        this._revealTimer = setTimeout(() => this._revealAll(), 1000);
      } else {
        this._revealAll();
      }
    }
  }

  // Re-read actual heights and re-place all items. Fixes drift after images load.
  syncHeights() {
    this._place(this._items, this._items.map(item => item.offsetHeight), this.colCount, this._colWidthCache);
    this._revealAll();
  }

  // Batch-add items in three phases to avoid O(N) reflows:
  //   1. writes: set widths, append all — no reads, no reflows
  //   2. one read: batch offsetHeight
  //   3. writes: assign columns, set left/top
  addAll(newItems) {
    if (!newItems.length) return;
    const colWidth = this._colWidthCache;

    for (const item of newItems) {
      item.style.width = `${colWidth}px`;
      this.container.appendChild(item);
    }

    this._position(newItems, newItems.map(item => item.offsetHeight), colWidth);
    this._items.push(...newItems);

    if (this._observer) newItems.forEach(item => this._observer.observe(item));
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const isTweet = location.pathname.includes("/status/");
  const containerClass = isTweet ? ".replies" : ".timeline";
  const itemClass = containerClass + " > div:not(.top-ref)";
  const html = document.documentElement;
  const container = document.querySelector(containerClass);
  const masonryEl = container?.querySelector(".gallery-masonry");
  const masonry = masonryEl ? new Masonry(masonryEl) : null;
  let loading = false;

  function handleScroll(failed) {
    if (loading || html.scrollTop + html.clientHeight < html.scrollHeight - 3000) return;

    const loadMore = getLoadMore(document);
    if (!loadMore) return;
    loading = true;
    loadMore.children[0].text = "Loading...";

    const url = new URL(loadMore.children[0].href);
    url.searchParams.append("scroll", "true");

    fetch(url)
      .then(r => {
        if (r.status > 299) throw new Error("error");
        return r.text();
      })
      .then(responseText => {
        const doc = new DOMParser().parseFromString(responseText, "text/html");
        loadMore.remove();

        if (masonry) {
          masonry.syncHeights();
          const newMasonry = doc.querySelector(".gallery-masonry");
          if (newMasonry) {
            const knownHrefs = getHrefs(".gallery-masonry .tweet-link");
            masonry.addAll([...newMasonry.querySelectorAll(".timeline-item")].filter(item => !isDuplicate(item, knownHrefs)));
          }
        } else {
          const knownHrefs = getHrefs(`${itemClass} .tweet-link`);
          for (const item of doc.querySelectorAll(itemClass)) {
            if (item.className === "timeline-item show-more" || isDuplicate(item, knownHrefs)) continue;
            isTweet ? container.appendChild(item) : insertBeforeLast(container, item);
          }
        }

        loading = false;
        const newLoadMore = getLoadMore(doc);
        if (newLoadMore) {
          isTweet ? container.appendChild(newLoadMore) : insertBeforeLast(container, newLoadMore);
          if (masonry) newLoadMore.classList.add("masonry-visible");
        }
      })
      .catch(err => {
        console.warn("Something went wrong.", err);
        if (failed > 3) { loadMore.children[0].text = "Error"; return; }
        loading = false;
        handleScroll((failed || 0) + 1);
      });
  }

  window.addEventListener("scroll", () => handleScroll());
});
// @license-end



================================================
FILE: public/md/about.md
================================================
# About

Nitter is a free and open source alternative Twitter front-end focused on
privacy and performance. The source is available on GitHub at
<https://github.com/zedeus/nitter>

- No JavaScript or ads
- All requests go through the backend, client never talks to Twitter
- Prevents Twitter from tracking your IP or JavaScript fingerprint
- Uses Twitter's unofficial API (no developer account required)
- Lightweight (for [@nim_lang](/nim_lang), 60KB vs 784KB from twitter.com)
- RSS feeds
- Themes
- Mobile support (responsive design)
- AGPLv3 licensed, no proprietary instances permitted

Nitter's GitHub wiki contains
[instances](https://github.com/zedeus/nitter/wiki/Instances) and
[browser extensions](https://github.com/zedeus/nitter/wiki/Extensions)
maintained by the community.

## Why use Nitter?

It's impossible to use Twitter without JavaScript enabled, and as of 2024 you
need to sign up. For privacy-minded folks, preventing JavaScript analytics and
IP-based tracking is important, but apart from using a VPN and uBlock/uMatrix,
it's impossible. Despite being behind a VPN and using heavy-duty adblockers,
you can get accurately tracked with your [browser's
fingerprint](https://restoreprivacy.com/browser-fingerprinting/), [no
JavaScript required](https://noscriptfingerprint.com/). This all became
particularly important after Twitter [removed the
ability](https://www.eff.org/deeplinks/2020/04/twitter-removes-privacy-option-and-shows-why-we-need-strong-privacy-laws)
for users to control whether their data gets sent to advertisers.

Using an instance of Nitter (hosted on a VPS for example), you can browse
Twitter without JavaScript while retaining your privacy. In addition to
respecting your privacy, Nitter is on average around 15 times lighter than
Twitter, and in most cases serves pages faster (eg. timelines load 2-4x faster).

In the future a simple account system will be added that lets you follow Twitter
users, allowing you to have a clean chronological timeline without needing a
Twitter account.

## Donating

Liberapay: https://liberapay.com/zedeus \
Patreon: https://patreon.com/nitter \
BTC: bc1qpqpzjkcpgluhzf7x9yqe7jfe8gpfm5v08mdr55 \
ETH: 0x24a0DB59A923B588c7A5EBd0dBDFDD1bCe9c4460 \
XMR: 42hKayRoEAw4D6G6t8mQHPJHQcXqofjFuVfavqKeNMNUZfeJLJAcNU19i1bGdDvcdN6romiSscWGWJCczFLe9RFhM3d1zpL \
SOL: ANsyGNXFo6osuFwr1YnUqif2RdoYRhc27WdyQNmmETSW \
ZEC: u1vndfqtzyy6qkzhkapxelel7ams38wmfeccu3fdpy2wkuc4erxyjm8ncjhnyg747x6t0kf0faqhh2hxyplgaum08d2wnj4n7cyu9s6zhxkqw2aef4hgd4s6vh5hpqvfken98rg80kgtgn64ff70djy7s8f839z00hwhuzlcggvefhdlyszkvwy3c7yw623vw3rvar6q6evd3xcvveypt

## Contact

Feel free to join our [Matrix channel](https://matrix.to/#/#nitter:matrix.org).



================================================
FILE: src/api.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, httpclient, strutils, sequtils, sugar
import packedjson
import types, query, formatters, consts, apiutils, parser, utils
import experimental/parser

# Helper to generate params object for GraphQL requests
proc genParams(variables: string; fieldToggles = ""): seq[(string, string)] =
  result.add ("variables", variables)
  result.add ("features", gqlFeatures)
  if fieldToggles.len > 0:
    result.add ("fieldToggles", fieldToggles)

proc apiUrl(endpoint, variables: string; fieldToggles = ""; skipTid = false): ApiUrl =
  return ApiUrl(endpoint: endpoint, params: genParams(variables, fieldToggles), skipTid: skipTid)

proc apiReq(endpoint, variables: string; fieldToggles = ""; skipTid = false): ApiReq =
  let url = apiUrl(endpoint, variables, fieldToggles, skipTid)
  return ApiReq(cookie: url, oauth: url)

proc cursorParam(after: string): string =
  ## JSON-escape the user-supplied cursor so it cannot break out of the GraphQL
  ## variables object (same input-validation class as the #1411 media SSRF).
  if after.len > 0: "\"cursor\":" & $(%after) & "," else: ""

proc mediaUrl(id, cursor: string; count=20): ApiReq =
  result = ApiReq(
    cookie: apiUrl(graphUserMedia, userMediaVars % [id, cursor, $count]),
    oauth: apiUrl(graphUserMediaV2, restIdVars % [id, cursor, $count])
  )

proc userTweetsUrl(id: string; cursor: string): ApiReq =
  return apiReq(graphUserTweetsV2, restIdVars % [id, cursor, "20"], userTweetsFieldToggles)

proc userTweetsAndRepliesUrl(id: string; cursor: string): ApiReq =
  return apiReq(graphUserTweetsAndRepliesV2, restIdVars % [id, cursor, "20"], userTweetsFieldToggles, skipTid=true)

proc tweetDetailUrl(id: string; cursor: string): ApiReq =
  return apiReq(graphTweet, tweetVars % [id, cursor])
  # let cookieVars = tweetDetailVars % [id, cursor]
  # result = ApiReq(
  #   cookie: apiUrl(graphTweetDetail, cookieVars, tweetDetailFieldToggles),
  #   oauth: apiUrl(graphTweet, tweetVars % [id, cursor])
  # )

proc userUrl(username: string): ApiReq =
  let cookieVars = $(%*{"screen_name": username, "withGrokTranslatedBio": false})
  result = ApiReq(
    cookie: apiUrl(graphUser, cookieVars, tweetDetailFieldToggles),
    oauth: apiUrl(graphUserV2, $(%*{"screen_name": username}))
  )

proc getGraphUser*(username: string): Future[User] {.async.} =
  if username.len == 0: return
  let js = await fetchRaw(userUrl(username))
  result = parseGraphUser(js)

proc getGraphUserById*(id: string): Future[User] {.async.} =
  if id.len == 0 or id.any(c => not c.isDigit): return
  let
    url = apiReq(graphUserById, """{"rest_id": "$1"}""" % id)
    js = await fetchRaw(url)
  result = parseGraphUser(js)

proc getAboutAccount*(username: string): Future[AccountInfo] {.async.} =
  if username.len == 0: return
  let
    url = apiReq(graphAboutAccount, $(%*{"screenName": username}))
    js = await fetch(url)
  result = parseAboutAccount(js)

proc restReq(endpoint: string; params: seq[(string, string)] = @[]): ApiReq =
  let url = ApiUrl(endpoint: endpoint, params: params)
  ApiReq(cookie: url, oauth: url)

proc getBroadcastInfo*(id: string): Future[Broadcast] {.async.} =
  if id.len == 0: return
  let
    req = apiReq(graphBroadcast, $(%*{"id": id}))
    js = await fetch(req)
  result = parseBroadcastInfo(js)

proc fetchBroadcastStream*(mediaKey: string): Future[string] {.async.} =
  if mediaKey.len == 0: return
  let
    streamReq = restReq(restLiveStream & mediaKey)
    streamJs = await fetch(streamReq)
  result = streamJs{"source", "noRedirectPlaybackUrl"}.getStr(
    streamJs{"source", "location"}.getStr)

proc getAudioSpace*(id: string): Future[AudioSpace] {.async.} =
  if id.len == 0: return
  let
    variables = %*{
      "id": id,
      "isMetatagsQuery": false,
      "withReplays": true,
      "withListeners": true
    }
    req = apiReq(graphAudioSpace, $variables)
    js = await fetch(req)
  result = parseAudioSpace(js)

proc getGraphUserTweets*(id: string; kind: TimelineKind; after=""): Future[Profile] {.async.} =
  if id.len == 0: return
  let
    cursor = cursorParam(after)
    url = case kind
      of TimelineKind.tweets: userTweetsUrl(id, cursor)
      of TimelineKind.replies: userTweetsAndRepliesUrl(id, cursor)
      of TimelineKind.media: mediaUrl(id, cursor, 100)
    js = await fetch(url)
  result = parseGraphTimeline(js, after)

proc getGraphCommunity*(id: string): Future[Community] {.async.} =
  if id.len == 0: return
  let
    url = apiReq(graphCommunity, $(%*{"communityId": id}))
    js = await fetch(url)
  result = parseGraphCommunity(js)

proc getGraphCommunityTweets*(id: string; rankingMode: string; after=""): Future[Timeline] {.async.} =
  if id.len == 0: return
  let
    cursor = cursorParam(after)
    url = apiReq(graphCommunityTweets, communityTweetsVars % [id, cursor, rankingMode])
    js = await fetch(url)
  result = parseGraphCommunityTimeline(js, after)

proc getGraphCommunityMedia*(id: string; after=""): Future[Timeline] {.async.} =
  if id.len == 0: return
  let
    cursor = cursorParam(after)
    url = apiReq(graphCommunityMedia, communityMediaVars % [id, cursor])
    js = await fetch(url)
  result = parseGraphCommunityTimeline(js, after)

proc communitySliceReq(endpoint, variables: string): ApiReq =
  let url = ApiUrl(endpoint: endpoint, params: @[("variables", variables)])
  ApiReq(cookie: url, oauth: url)

proc getGraphCommunityMembers*(id: string; after=""): Future[Result[User]] {.async.} =
  if id.len == 0: return
  let
    cursor = if after.len > 0: $(%after) else: "null"
    url = communitySliceReq(graphCommunityMembers, communityMembersVars % [id, cursor])
    js = await fetch(url)
  result = parseGraphCommunityMembers(js, after)

proc getGraphCommunityModerators*(id: string): Future[Result[User]] {.async.} =
  if id.len == 0: return
  let
    url = communitySliceReq(graphCommunityModerators, communityMembersVars % [id, "null"])
    js = await fetch(url)
  result = parseGraphCommunityMembers(js)

proc getGraphCommunityHashtags*(id, hashtag: string; after=""): Future[Timeline] {.async.} =
  if id.len == 0 or hashtag.len == 0: return
  let
    safeTag = multiReplace(hashtag, ("\"", ""), ("\\", ""))
    cursor = cursorParam(after)
    url = apiReq(graphCommunityHashtags, communityHashtagsVars % [id, cursor, safeTag])
    js = await fetch(url)
  result = parseGraphCommunityTimeline(js, after)

proc getGraphListTweets*(id: string; after=""): Future[Timeline] {.async.} =
  if id.len == 0: return
  let
    cursor = cursorParam(after)
    url = apiReq(graphListTweets, restIdVars % [id, cursor, "20"])
    js = await fetch(url)
  result = parseGraphTimeline(js, after).tweets

proc getGraphListBySlug*(name, list: string): Future[List] {.async.} =
  let
    variables = %*{"screenName": name, "listSlug": list}
    url = apiReq(graphListBySlug, $variables)
    js = await fetch(url)
  result = parseGraphList(js)

proc getGraphList*(id: string): Future[List] {.async.} =
  let 
    url = apiReq(graphListById, $(%*{"listId": id}))
    js = await fetch(url)
  result = parseGraphList(js)

proc getGraphListMembers*(list: List; after=""): Future[Result[User]] {.async.} =
  if list.id.len == 0: return
  var
    variables = %*{
      "listId": list.id,
      "withBirdwatchPivots": false,
      "withDownvotePerspective": false,
      "withReactionsMetadata": false,
      "withReactionsPerspective": false
    }
  if after.len > 0:
    variables["cursor"] = % after
  let 
    url = apiReq(graphListMembers, $variables)
    js = await fetchRaw(url)
  result = parseGraphListMembers(js, after)

proc getGraphUserConnections(userId: string; endpoint: string; kind: QueryKind;
                              after=""): Future[Result[User]] {.async.} =
  if userId.len == 0: return
  var variables = %*{
    "userId": userId,
    "count": 20,
    "includePromotedContent": false,
    "withGrokTranslatedBio": true
  }
  if after.len > 0:
    variables["cursor"] = %after
  let
    url = apiReq(endpoint, $variables)
    js = await fetchRaw(url)
  result = parseGraphFollowers(js, after, kind)

proc getGraphFollowers*(userId: string; after=""): Future[Result[User]] {.async.} =
  result = await getGraphUserConnections(userId, graphFollowers, followers, after)

proc getGraphFollowing*(userId: string; after=""): Future[Result[User]] {.async.} =
  result = await getGraphUserConnections(userId, graphFollowing, following, after)

proc getGraphTweetResult*(id: string): Future[Tweet] {.async.} =
  if id.len == 0: return
  let
    url = apiReq(graphTweetResult, $(%*{"rest_id": id}))
    js = await fetch(url)
  result = parseGraphTweetResult(js)

proc getGraphTweet(id: string; after=""): Future[Conversation] {.async.} =
  if id.len == 0: return
  let
    cursor = cursorParam(after)
    js = await fetch(tweetDetailUrl(id, cursor))
  result = parseGraphConversation(js, id)

proc getReplies*(id, after: string): Future[Result[Chain]] {.async.} =
  result = (await getGraphTweet(id, after)).replies
  result.beginning = after.len == 0

proc getTweet*(id: string; after=""): Future[Conversation] {.async.} =
  result = await getGraphTweet(id)
  if after.len > 0:
    result.replies = await getReplies(id, after)

proc getGraphEditHistory*(id: string): Future[EditHistory] {.async.} =
  if id.len == 0: return
  let
    url = apiReq(graphTweetEditHistory, tweetEditHistoryVars % id)
    js = await fetch(url)
  result = parseGraphEditHistory(js, id)

proc getGraphTweetSearch*(query: Query; after=""): Future[Timeline] {.async.} =
  # workaround for #1372
  let maxId =
    if not after.startsWith("maxid:"): ""
    else: validateNumber(after[6..^1])

  let q = genQueryParam(query, maxId)
  if q.len == 0 or q == emptyQuery:
    return Timeline(query: query, beginning: true)

  var
    variables = %*{
      "rawQuery": q,
      "count": 20,
      "querySource": "typed_query",
      "product": "Latest",
      "withGrokTranslatedBio":true,
      "withQuickPromoteEligibilityTweetFields":false
    }

  if after.len > 0 and maxId.len == 0:
    variables["cursor"] = % after
  let
    url = apiReq(graphSearchTimeline, $variables)
    js = await fetch(url)
  result = parseGraphSearch[Tweets](js, after)
  result.query = query

  # when no more items are available the API just returns the last page in
  # full. this detects that and clears the page instead.
  if after.len > 0 and result.bottom.len > 0 and maxId.len == 0 and
     after[0..<64] == result.bottom[0..<64]:
    result.content.setLen(0)

proc getGraphUserSearch*(query: Query; after=""): Future[Result[User]] {.async.} =
  if query.text.len == 0:
    return Result[User](query: query, beginning: true)

  var
    variables = %*{
      "rawQuery": query.text,
      "count": 20,
      "querySource": "typed_query",
      "product": "People",
      "withGrokTranslatedBio":true,
      "withQuickPromoteEligibilityTweetFields":false
    }
  if after.len > 0:
    variables["cursor"] = % after
    result.beginning = false

  let 
    url = apiReq(graphSearchTimeline, $variables)
    js = await fetch(url)
  result = parseGraphSearch[User](js, after)
  result.query = query

proc getPhotoRail*(id: string): Future[PhotoRail] {.async.} =
  if id.len == 0: return
  let js = await fetch(mediaUrl(id, "", 30))
  result = parseGraphPhotoRail(js)

proc getGraphArticle*(id: string): Future[Article] {.async.} =
  if id.len == 0: return
  let
    url = apiReq(graphTweetResultByRestId, articleVars % id, articleFieldToggles)
    json = await fetchRaw(url)
  result = parseGraphArticle(json)

proc getGraphTweetResults*(ids: seq[string]): Future[seq[Tweet]] {.async.} =
  if ids.len == 0: return
  let
    idsJson = "[" & ids.mapIt("\"" & it & "\"").join(",") & "]"
    url = apiReq(graphTweetResultsByRestIds, articleBatchVars % idsJson, articleFieldToggles)
    js = await fetch(url)
  result = parseGraphTweetResults(js)

proc resolve*(url: string; prefs: Prefs): Future[string] {.async.} =
  let client = newAsyncHttpClient(maxRedirects=0)
  try:
    let resp = await client.request(url, HttpHead)
    result = resp.headers["location"].replaceUrls(prefs)
  except:
    discard
  finally:
    client.close()



================================================
FILE: src/apiutils.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import httpclient, asyncdispatch, options, strutils, uri, times, math, tables
import jsony, packedjson, zippy, oauth/oauth1
import types, auth, consts, parserutils, http_pool, tid
import experimental/types/common

const
  rlRemaining = "x-rate-limit-remaining"
  rlReset = "x-rate-limit-reset"
  rlLimit = "x-rate-limit-limit"
  npCache = "x-np-cache"
  errorsToSkip = {null, doesntExist, tweetNotFound, timeout, unauthorized, badRequest}

var
  pool: HttpPool
  disableTid: bool
  apiProxy: string
  maxRetries: int
  retryDelayMs: int

proc setDisableTid*(disable: bool) =
  disableTid = disable

proc setMaxRetries*(n: int) =
  maxRetries = n

proc setRetryDelayMs*(ms: int) =
  retryDelayMs = ms

proc setApiProxy*(url: string) =
  apiProxy = ""
  if url.len > 0:
    apiProxy = url.strip(chars={'/'}) & "/"
    if "http" notin apiProxy:
      apiProxy = "http://" & apiProxy

proc toUrl(req: ApiReq; sessionKind: SessionKind): Uri =
  let url = case sessionKind
    of oauth:  req.oauth
    of cookie: req.cookie
  let base = case sessionKind
    of oauth:  "https://api.x.com"
    of cookie: "https://x.com/i/api"
  let prefix = if url.endpoint.startsWith("1.1/"): "" else: "graphql/"
  parseUri(base) / (prefix & url.endpoint) ? url.params

proc getOauthHeader(url, oauthToken, oauthTokenSecret: string): string =
  let
    encodedUrl = url.replace(",", "%2C").replace("+", "%20")
    params = OAuth1Parameters(
      consumerKey: consumerKey,
      signatureMethod: "HMAC-SHA1",
      timestamp: $int(round(epochTime())),
      nonce: "0",
      isIncludeVersionToHeader: true,
      token: oauthToken
    )
    signature = getSignature(HttpGet, encodedUrl, "", params, consumerSecret, oauthTokenSecret)

  params.signature = percentEncode(signature)

  return getOauth1RequestHeader(params)["authorization"]

proc getCookieHeader(authToken, ct0: string): string =
  "auth_token=" & authToken & "; ct0=" & ct0

proc genHeaders*(session: Session, url: Uri, skipTid: bool): Future[HttpHeaders] {.async.} =
  result = newHttpHeaders({
    "accept": "*/*",
    "accept-encoding": "gzip",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-type": "application/json",
    "origin": "https://x.com",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "x-twitter-active-user": "yes",
    "x-twitter-client-language": "en",
    "priority": "u=1, i"
  })

  case session.kind
  of SessionKind.oauth:
    result["authorization"] = getOauthHeader($url, session.oauthToken, session.oauthSecret)
  of SessionKind.cookie:
    result["x-twitter-auth-type"] = "OAuth2Session"
    result["x-csrf-token"] = session.ct0
    result["cookie"] = getCookieHeader(session.authToken, session.ct0)
    result["referer"] = "https://x.com/"
    result["sec-ch-ua"] = """"Google Chrome";v="142", "Chromium";v="142", "Not A(Brand";v="24""""
    result["sec-ch-ua-mobile"] = "?0"
    result["sec-ch-ua-platform"] = "Windows"
    result["sec-fetch-dest"] = "empty"
    result["sec-fetch-mode"] = "cors"
    result["sec-fetch-site"] = "same-origin"
    if disableTid or skipTid or "/1.1/" in url.path:
      result["authorization"] = bearerToken2
    else:
      result["authorization"] = bearerToken
      result["x-client-transaction-id"] = await genTid(url.path)

proc getAndValidateSession*(req: ApiReq): Future[Session] {.async.} =
  result = await getSession(req)
  case result.kind
  of SessionKind.oauth:
    if result.oauthToken.len == 0:
      echo "[sessions] Empty oauth token, session: ", result.pretty
      raise rateLimitError()
  of SessionKind.cookie:
    if result.authToken.len == 0 or result.ct0.len == 0:
      echo "[sessions] Empty cookie credentials, session: ", result.pretty
      raise rateLimitError()

template fetchImpl(result, fetchBody) {.dirty.} =
  once:
    pool = HttpPool()

  try:
    var resp: AsyncResponse
    let skipTid = case session.kind
      of oauth: req.oauth.skipTid
      of cookie: req.cookie.skipTid
    let headers = await genHeaders(session, url, skipTid)

    pool.use(headers):
      template getContent =
        # TODO: this is a temporary simple implementation
        if apiProxy.len > 0 and "/1.1/" notin url.path:
          resp = await c.get(($url).replace("https://", apiProxy))
        else:
          resp = await c.get($url)
        result = await resp.body

      getContent()

      if resp.status == $Http503:
        badClient = true
        raise newException(BadClientError, "Bad client")

      if resp.status == $Http404 and result.len == 0:
        echo "[sessions] transient 404 (empty body), retrying: ", url.path, ", session: ", session.pretty
        raise rateLimitError()

    let cacheStatus = resp.headers.getOrDefault(npCache)
    if cacheStatus notin ["HIT", "STALE"] and resp.headers.hasKey(rlRemaining):
      let
        remaining = parseInt(resp.headers[rlRemaining])
        reset = parseInt(resp.headers[rlReset])
        limit = parseInt(resp.headers[rlLimit])
      session.setRateLimit(req, remaining, reset, limit)

    if result.len > 0:
      if resp.headers.getOrDefault("content-encoding") == "gzip":
        result = uncompress(result, dfGzip)

      if result.startsWith("{\"errors"):
        let errors = result.fromJson(Errors)
        if errors notin errorsToSkip:
          echo "Fetch error, API: ", url.path, ", errors: ", errors, ", session: ", session.pretty
          if errors in {expiredToken, badToken, locked}:
            invalidate(session)
            raise rateLimitError()
          elif errors in {rateLimited}:
            # rate limit hit, resets after 24 hours
            setLimited(session, req)
            raise rateLimitError()
      elif result.startsWith("429 Too Many Requests"):
        echo "[sessions] 429 error, API: ", url.path, ", session: ", session.pretty
        raise rateLimitError()

    fetchBody

    if resp.status == $Http400:
      echo "ERROR 400, ", url.path, ": ", result, ", session: ", session.pretty
      raise newException(InternalError, $url)
  except InternalError as e:
    raise e
  except BadClientError as e:
    raise e
  except OSError as e:
    raise e
  except Exception as e:
    let s = session.pretty
    echo "error: ", e.name, ", msg: ", e.msg, ", session: ", s, ", url: ", url
    raise rateLimitError()
  finally:
    release(session)

template retry(bod) {.dirty.} =
  var session: Session
  var retrySuccess = false
  for i in 0 ..< maxRetries:
    try:
      session = nil
      bod
      retrySuccess = true
      break
    except RateLimitError:
      let api = if session.isNil: req.cookie.endpoint
                else: req.endpoint(session)
      if session.isNil:
        echo "[sessions] Rate limited, retrying ", api,
             " request (", i, "/", maxRetries, ")..."
      else:
        echo "[sessions] Rate limited, retrying ", api,
             " request (", i, "/", maxRetries, ")..., session: ", session.pretty
      session = nil
      if retryDelayMs > 0:
        await sleepAsync(retryDelayMs)
  if not retrySuccess:
    raise rateLimitError()

proc fetch*(req: ApiReq): Future[JsonNode] {.async.} =
  retry:
    var body: string
    session = await getAndValidateSession(req)

    let url = req.toUrl(session.kind)

    fetchImpl body:
      if body.startsWith('{') or body.startsWith('['):
        result = parseJson(body)
      else:
        echo resp.status, ": ", body, " --- url: ", url, ", session: ", session.pretty
        result = newJNull()

      let error = result.getError
      if error != null and error notin errorsToSkip:
        echo "Fetch error, API: ", url.path, ", error: ", error, ", session: ", session.pretty
        if error in {expiredToken, badToken, locked}:
          invalidate(session)
          raise rateLimitError()

proc fetchRaw*(req: ApiReq): Future[string] {.async.} =
  retry:
    session = await getAndValidateSession(req)
    let url = req.toUrl(session.kind)

    fetchImpl result:
      if not (result.startsWith('{') or result.startsWith('[')):
        echo resp.status, ": ", result, " --- url: ", url, ", session: ", session.pretty
        result.setLen(0)



================================================
FILE: src/auth.nim
================================================
#SPDX-License-Identifier: AGPL-3.0-only
import std/[asyncdispatch, times, json, random, strutils, tables, packedsets, os]
import types, consts
import experimental/parser/session

const hourInSeconds = 60 * 60

var
  sessionPool: seq[Session]
  enableLogging = false
  # max requests at a time per session to avoid race conditions
  maxConcurrentReqs = 2

proc setMaxConcurrentReqs*(reqs: int) =
  if reqs > 0:
    maxConcurrentReqs = reqs

template log(str: varargs[string, `$`]) =
  echo "[sessions] ", str.join("")

proc endpoint*(req: ApiReq; session: Session): string =
  case session.kind
  of oauth: req.oauth.endpoint
  of cookie: req.cookie.endpoint

proc pretty*(session: Session): string =
  if session.isNil:
    return "<null>"

  if session.id > 0 and session.username.len > 0:
    result = $session.id & " (" & session.username & ")"
  elif session.username.len > 0:
    result = session.username
  elif session.id > 0:
    result = $session.id
  else:
    result = "<unknown>"
  result = $session.kind & " " & result

proc snowflakeToEpoch(flake: int64): int64 =
  int64(((flake shr 22) + 1288834974657) div 1000)

proc getSessionPoolHealth*(): JsonNode =
  let now = epochTime().int

  var
    totalReqs = 0
    limited: PackedSet[int64]
    reqsPerApi: Table[string, int]
    oldest = now.int64
    newest = 0'i64
    average = 0'i64
    oauthTotal, cookieTotal = 0
    oauthLimited, cookieLimited = 0

  for session in sessionPool:
    let created = snowflakeToEpoch(session.id)
    if created > newest:
      newest = created
    if created < oldest:
      oldest = created
    average += created

    case session.kind
    of oauth: inc oauthTotal
    of cookie: inc cookieTotal

    if session.limited:
      limited.incl session.id
      case session.kind
      of oauth: inc oauthLimited
      of cookie: inc cookieLimited

    for api in session.apis.keys:
      let
        apiStatus = session.apis[api]
        reqs = apiStatus.limit - apiStatus.remaining

      # no requests made with this session and endpoint since the limit reset
      if apiStatus.reset < now:
        continue

      reqsPerApi.mgetOrPut($api, 0).inc reqs
      totalReqs.inc reqs

  if sessionPool.len > 0:
    average = average div sessionPool.len
  else:
    oldest = 0
    average = 0

  return %*{
    "sessions": %*{
      "total": sessionPool.len,
      "limited": limited.card,
      "oauth": %*{"total": oauthTotal, "limited": oauthLimited},
      "cookie": %*{"total": cookieTotal, "limited": cookieLimited},
      "oldest": $fromUnix(oldest),
      "newest": $fromUnix(newest),
      "average": $fromUnix(average)
    },
    "requests": %*{
      "total": totalReqs,
      "apis": reqsPerApi
    }
  }

proc getSessionPoolDebug*(): JsonNode =
  let now = epochTime().int
  var list = newJObject()

  for session in sessionPool:
    let sessionJson = %*{
      "kind": $session.kind,
      "apis": newJObject(),
      "pending": session.pending,
    }

    if session.limited:
      sessionJson["limited"] = %true

    for api in session.apis.keys:
      let
        apiStatus = session.apis[api]
        obj = %*{}

      if apiStatus.reset > now.int:
        obj["remaining"] = %apiStatus.remaining
        obj["reset"] = %apiStatus.reset

      if "remaining" notin obj:
        continue

      sessionJson{"apis", $api} = obj
      list[$session.id] = sessionJson

  return %list

proc rateLimitError*(): ref RateLimitError =
  newException(RateLimitError, "rate limited")

proc noSessionsError*(): ref NoSessionsError =
  newException(NoSessionsError, "no sessions available")

proc isLimited(session: Session; req: ApiReq): bool =
  if session.isNil:
    return true

  let api = req.endpoint(session)
  if session.limited and api != graphUserTweetsV2:
    if (epochTime().int - session.limitedAt) > hourInSeconds:
      session.limited = false
      log "resetting limit: ", session.pretty
      return false
    else:
      return true

  if api in session.apis:
    let limit = session.apis[api]
    return limit.remaining <= 10 and limit.reset > epochTime().int
  else:
    return false

proc isReady(session: Session; req: ApiReq): bool =
  not (session.isNil or session.pending > maxConcurrentReqs or session.isLimited(req))

proc invalidate*(session: var Session) =
  if session.isNil: return
  log "invalidating: ", session.pretty

  # TODO: This isn't sufficient, but it works for now
  let idx = sessionPool.find(session)
  if idx > -1: sessionPool.delete(idx)
  session = nil

proc release*(session: Session) =
  if session.isNil: return
  dec session.pending

proc getSession*(req: ApiReq): Future[Session] {.async.} =
  for i in 0 ..< sessionPool.len:
    if result.isReady(req): break
    result = sessionPool.sample()

  if not result.isNil and result.isReady(req):
    inc result.pending
  else:
    if result.isNil:
      log "no sessions available for API: ", req.cookie.endpoint
    else:
      log "no sessions available for API: ", req.endpoint(result), ", last tried: ", result.pretty
    raise noSessionsError()

proc setLimited*(session: Session; req: ApiReq) =
  let api = req.endpoint(session)
  session.limited = true
  session.limitedAt = epochTime().int
  log "rate limited by api: ", api, ", reqs left: ", session.apis[api].remaining, ", ", session.pretty

proc setRateLimit*(session: Session; req: ApiReq; remaining, reset, limit: int) =
  # avoid undefined behavior in race conditions
  let api = req.endpoint(session)
  if api in session.apis:
    let rateLimit = session.apis[api]
    if rateLimit.reset >= reset and rateLimit.remaining < remaining:
      return
    if rateLimit.reset == reset and rateLimit.remaining >= remaining:
      session.apis[api].remaining = remaining
      return

  session.apis[api] = RateLimit(limit: limit, remaining: remaining, reset: reset)

proc initSessionPool*(cfg: Config; path: string) =
  enableLogging = cfg.enableDebug

  if path.endsWith(".json"):
    log "ERROR: .json is not supported, the file must be a valid JSONL file ending in .jsonl"
    quit 1

  if not fileExists(path):
    log "ERROR: ", path, " not found. This file is required to authenticate API requests."
    quit 1

  log "parsing JSONL account sessions file: ", path
  for line in path.lines:
    sessionPool.add parseSession(line)

  log "successfully added ", sessionPool.len, " valid account sessions"



================================================
FILE: src/config.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import parsecfg except Config
import types, strutils

proc get*[T](config: parseCfg.Config; section, key: string; default: T): T =
  let val = config.getSectionValue(section, key)
  if val.len == 0: return default

  when T is int: parseInt(val)
  elif T is bool: parseBool(val)
  elif T is string: val

proc getConfig*(path: string): (Config, parseCfg.Config) =
  var cfg = loadConfig(path)

  let masterRss = cfg.get("Config", "enableRSS", true)

  let conf = Config(
    # Server
    address: cfg.get("Server", "address", "0.0.0.0"),
    port: cfg.get("Server", "port", 8080),
    useHttps: cfg.get("Server", "https", true),
    httpMaxConns: cfg.get("Server", "httpMaxConnections", 100),
    staticDir: cfg.get("Server", "staticDir", "./public"),
    title: cfg.get("Server", "title", "Nitter"),
    hostname: cfg.get("Server", "hostname", "nitter.net"),

    # Cache
    listCacheTime: cfg.get("Cache", "listMinutes", 120),
    rssCacheTime: cfg.get("Cache", "rssMinutes", 10),

    redisHost: cfg.get("Cache", "redisHost", "localhost"),
    redisPort: cfg.get("Cache", "redisPort", 6379),
    redisConns: cfg.get("Cache", "redisConnections", 20),
    redisMaxConns: cfg.get("Cache", "redisMaxConnections", 30),
    redisPassword: cfg.get("Cache", "redisPassword", ""),

    # Config
    hmacKey: cfg.get("Config", "hmacKey", "secretkey"),
    base64Media: cfg.get("Config", "base64Media", false),
    minTokens: cfg.get("Config", "tokenCount", 10),
    enableRSSUserTweets: masterRss and cfg.get("Config", "enableRSSUserTweets", true),
    enableRSSUserReplies: masterRss and cfg.get("Config", "enableRSSUserReplies", true),
    enableRSSUserMedia: masterRss and cfg.get("Config", "enableRSSUserMedia", true),
    enableRSSSearch: masterRss and cfg.get("Config", "enableRSSSearch", true),
    enableRSSList: masterRss and cfg.get("Config", "enableRSSList", true),
    enableDebug: cfg.get("Config", "enableDebug", false),
    proxy: cfg.get("Config", "proxy", ""),
    proxyAuth: cfg.get("Config", "proxyAuth", ""),
    apiProxy: cfg.get("Config", "apiProxy", ""),
    disableTid: cfg.get("Config", "disableTid", false),
    maxConcurrentReqs: cfg.get("Config", "maxConcurrentReqs", 2),
    maxRetries: cfg.get("Config", "maxRetries", 1),
    retryDelayMs: cfg.get("Config", "retryDelayMs", 150)
  )

  return (conf, cfg)



================================================
FILE: src/consts.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils

const
  consumerKey* = "3nVuSoBZnx6U4vzUxf5w"
  consumerSecret* = "Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys"
  bearerToken* = "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
  bearerToken2* = "Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F"

  graphUser* = "IGgvgiOx4QZndDHuD3x9TQ/UserByScreenName"
  graphUserV2* = "-ZzAG_Bckx16LMbEvHC3lg/UserResultByScreenNameQuery"
  graphUserById* = "-DAaa9jPxPswYeI2fZ9rug/UserResultByIdQuery"
  graphUserTweetsV2* = "LE3eTyeqhBh2g-fX85O2eQ/UserWithProfileTweetsQueryV2"
  graphUserTweetsAndRepliesV2* = "AcYHjc_YAx-9_rKWdMsKvA/UserWithProfileTweetsAndRepliesQueryV2"
  graphUserTweets* = "PNd0vlufvrcIwrAnBYKE9g/UserTweets"
  graphUserTweetsAndReplies* = "EqtpEwt0CoQXmDfq5DKH0A/UserTweetsAndReplies"
  graphUserMedia* = "g_rGPF0fLON-M9cyVjXuzA/UserMedia"
  graphUserMediaV2* = "WK111rbR0vM0ZX4lyZCYjw/MediaTimelineV2"
  graphTweet* = "OZMbEnEa96AN8Pq6HyTWdw/ConversationTimeline"
  graphTweetDetail* = "6uCvnic3m5reVuehkvHa3w/TweetDetail"
  graphTweetResult* = "xYOrBQoTlfKJJPsX76MZEw/TweetResultByIdQuery"
  graphTweetEditHistory* = "MGElmrYILE8wUfI8GorUYA/TweetEditHistory"
  graphSearchTimeline* = "-TFXKoMnMTKdEXcCn-eahw/SearchTimeline"

  graphListById* = "t9AbdyHaJVfjL9jsODwgpQ/ListByRestId"
  graphListBySlug* = "LDQpQ89B5ipR8izCKrWU0g/ListBySlug"
  graphListMembers* = "EM7YRaM3gCnzDESmchA7RA/ListMembers"
  graphListTweets* = "0QJtcuMzVywHGAWD6Dtjlw/ListTimeline"
  graphAboutAccount* = "zUnx-DLN9dkwOkNhTLySjg/AboutAccountQuery"

  graphCommunity* = "-ElI1vg3dYbttVMhBhGdLw/CommunityQuery"
  graphCommunityTweets* = "Mvs5UOOEkpXVMDZtUcxR-Q/CommunityTweetsTimeline"
  graphCommunityMedia* = "Bt9XYnY7D3OcmZE5lhdx-A/CommunityMediaTimeline"
  graphCommunityMembers* = "WSbJGJjZaVasSj9bnqSZSA/membersSliceTimeline_Query"
  graphCommunityModerators* = "GBMT3GOWy5dYsYC4XJfvow/moderatorsSliceTimeline_Query"
  graphCommunityHashtags* = "40DyrMxfCknGuZwE-keW_Q/CommunityHashtagsTimeline"

  graphTweetResultByRestId* = "qtXMy1p5Y62uCskc_NUPJw/TweetResultByRestId"
  graphTweetResultsByRestIds* = "Sc9EUQTZNEH-wzegn-nHvQ/TweetResultsByRestIds"

  graphBroadcast* = "FJLCzpXCLPM1jUZqmM7oEA/BroadcastQuery"
  graphAudioSpace* = "rWRLsOhNJ2xjpI1tREYurQ/AudioSpaceById"
  restLiveStream* = "1.1/live_video_stream/status/"

  graphFollowers* = "9jsVJ9l2uXUIKslHvJqIhw/Followers"
  graphFollowing* = "OLm4oHZBfqWx8jbcEhWoFw/Following"

  gqlFeatures* = """{
  "rweb_video_screen_enabled": false,
  "rweb_cashtags_enabled": true,
  "profile_label_improvements_pcf_label_in_post_enabled": true,
  "responsive_web_profile_redirect_enabled": false,
  "rweb_tipjar_consumption_enabled": false,
  "verified_phone_label_enabled": false,
  "creator_subscriptions_tweet_preview_api_enabled": true,
  "responsive_web_graphql_timeline_navigation_enabled": true,
  "responsive_web_graphql_skip_user_profile_image_extensions_enabled": false,
  "premium_content_api_read_enabled": false,
  "communities_web_enable_tweet_community_results_fetch": true,
  "c9s_tweet_anatomy_moderator_badge_enabled": true,
  "c9s_list_members_action_api_enabled": false,
  "c9s_superc9s_indication_enabled": false,
  "responsive_web_grok_analyze_button_fetch_trends_enabled": false,
  "responsive_web_grok_analyze_post_followups_enabled": true,
  "rweb_cashtags_composer_attachment_enabled": true,
  "responsive_web_jetfuel_frame": true,
  "responsive_web_grok_share_attachment_enabled": true,
  "responsive_web_grok_annotations_enabled": true,
  "articles_preview_enabled": true,
  "responsive_web_edit_tweet_api_enabled": true,
  "rweb_conversational_replies_downvote_enabled": false,
  "graphql_is_translatable_rweb_tweet_is_translatable_enabled": true,
  "view_counts_everywhere_api_enabled": true,
  "longform_notetweets_consumption_enabled": true,
  "responsive_web_twitter_article_tweet_consumption_enabled": true,
  "content_disclosure_indicator_enabled": true,
  "content_disclosure_ai_generated_indicator_enabled": true,
  "responsive_web_grok_show_grok_translated_post": true,
  "responsive_web_grok_analysis_button_from_backend": true,
  "post_ctas_fetch_enabled": true,
  "freedom_of_speech_not_reach_fetch_enabled": true,
  "standardized_nudges_misinfo": true,
  "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": true,
  "longform_notetweets_rich_text_read_enabled": true,
  "longform_notetweets_inline_media_enabled": false,
  "responsive_web_grok_image_annotation_enabled": true,
  "responsive_web_grok_imagine_annotation_enabled": true,
  "responsive_web_grok_community_note_auto_translation_is_enabled": true,
  "responsive_web_enhance_cards_enabled": false
}""".replace(" ", "").replace("\n", "")

  tweetVars* = """{
  "postId": "$1",
  $2
  "includeHasBirdwatchNotes": false,
  "includePromotedContent": false,
  "withBirdwatchNotes": true,
  "withVoice": false,
  "withV2Timeline": true
}""".replace(" ", "").replace("\n", "")

  tweetDetailVars* = """{
  "focalTweetId": "$1",
  $2
  "referrer": "profile",
  "with_rux_injections": false,
  "rankingMode": "Relevance",
  "includePromotedContent": true,
  "withCommunity": true,
  "withQuickPromoteEligibilityTweetFields": true,
  "withBirdwatchNotes": true,
  "withVoice": true
}""".replace(" ", "").replace("\n", "")

  tweetEditHistoryVars* = """{
  "tweetId": "$1",
  "withQuickPromoteEligibilityTweetFields": true
}""".replace(" ", "").replace("\n", "")

  restIdVars* = """{
  "rest_id": "$1", $2
  "count": $3
}""".replace(" ", "").replace("\n", "")

  userMediaVars* = """{
  "userId": "$1", $2
  "count": $3,
  "includePromotedContent": false,
  "withClientEventToken": false,
  "withBirdwatchNotes": false,
  "withVoice": true
}""".replace(" ", "").replace("\n", "")

  userTweetsVars* = """{
  "userId": "$1", $2
  "count": 20,
  "includePromotedContent": false,
  "withQuickPromoteEligibilityTweetFields": true,
  "withVoice": true
}""".replace(" ", "").replace("\n", "")

  userTweetsAndRepliesVars* = """{
  "userId": "$1", $2
  "count": 20,
  "includePromotedContent": false,
  "withCommunity": true,
  "withVoice": true
}""".replace(" ", "").replace("\n", "")

  articleVars* = """{
  "tweetId": "$1",
  "includePromotedContent": false,
  "withBirdwatchNotes": true,
  "withVoice": true,
  "withCommunity": true
}""".replace(" ", "").replace("\n", "")

  articleBatchVars* = """{
  "tweetIds": $1,
  "includePromotedContent": false,
  "withBirdwatchNotes": true,
  "withVoice": true,
  "withCommunity": true
}""".replace(" ", "").replace("\n", "")

  articleFieldToggles* = """{"withArticleRichContentState":true,"withArticlePlainText":false,"withArticleSummaryText":true,"withArticleVoiceOver":true}"""

  communityTweetsVars* = """{
  "communityId": "$1", $2
  "count": 20,
  "displayLocation": "Community",
  "rankingMode": "$3",
  "withCommunity": true
}""".replace(" ", "").replace("\n", "")

  communityMediaVars* = """{
  "communityId": "$1", $2
  "count": 20,
  "withCommunity": true
}""".replace(" ", "").replace("\n", "")

  communityMembersVars* = """{
  "communityId": "$1",
  "cursor": $2
}""".replace(" ", "").replace("\n", "")

  communityHashtagsVars* = """{
  "communityId": "$1", $2
  "count": 20,
  "hashtags": ["$3"],
  "withCommunity": true
}""".replace(" ", "").replace("\n", "")

  userFieldToggles = """{"withPayments":false,"withAuxiliaryUserLabels":true}"""
  userTweetsFieldToggles* = """{"withArticleRichContentState":true,"withArticlePlainText":false}"""
  tweetDetailFieldToggles* = """{"withArticleRichContentState":true,"withArticlePlainText":false,"withGrokAnalyze":false,"withDisallowedReplyControls":false}"""



================================================
FILE: src/formatters.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, times, uri, tables, xmltree, htmlparser, htmlgen, math
import std/[enumerate, re]
import types, utils, query

const
  cards = "cards.twitter.com/cards"
  tco = "https://t.co"
  twitter = parseUri("https://x.com")

let
  twRegex = re"(?<=(?<!\S)https:\/\/|(?<=\s))(www\.|mobile\.)?twitter\.com"
  twLinkRegex = re"""<a href="https:\/\/twitter.com([^"]+)">twitter\.com(\S+)</a>"""
  xRegex = re"(?<=(?<!\S)https:\/\/|(?<=\s))(www\.|mobile\.)?x\.com"
  xLinkRegex = re"""<a href="https:\/\/x.com([^"]+)">x\.com(\S+)</a>"""

  ytRegex = re(r"([A-z.]+\.)?youtu(be\.com|\.be)", {reStudy, reIgnoreCase})

  rdRegex = re"(?<![.b])((www|np|new|amp|old)\.)?reddit.com"
  rdShortRegex = re"(?<![.b])redd\.it\/"
  # Videos cannot be supported uniformly between Teddit and Libreddit,
  # so v.redd.it links will not be replaced.
  # Images aren't supported due to errors from Teddit when the image
  # wasn't first displayed via a post on the Teddit instance.

  wwwRegex = re"https?://(www[0-9]?\.)?"
  m3u8Regex = re"""url="(.+.m3u8)""""
  userPicRegex = re"_(normal|bigger|mini|200x200|400x400)(\.[A-z]+)$"
  extRegex = re"(\.[A-z]+)$"
  illegalXmlRegex = re"(*UTF8)[^\x09\x0A\x0D\x20-\x{D7FF}\x{E000}-\x{FFFD}\x{10000}-\x{10FFFF}]"

proc getUrlPrefix*(cfg: Config): string =
  if cfg.useHttps: https & cfg.hostname
  else: "http://" & cfg.hostname

proc shorten*(text: string; length=28): string =
  result = text
  if result.len > length:
    result = result[0 ..< length] & "…"

proc shortLink*(text: string; length=28): string =
  result = text.replace(wwwRegex, "").shorten(length)
    
proc stripHtml*(text: string; shorten=false): string =
  var html = parseHtml(text)
  for el in html.findAll("a"):
    let link = el.attr("href")
    if "http" in link:
      if el.len == 0: continue
      el[0].text =
        if shorten: link.shortLink
        else: link
  html.innerText()

proc sanitizeXml*(text: string): string =
  text.replace(illegalXmlRegex, "")

proc replaceUrls*(body: string; prefs: Prefs; absolute=""): string =
  result = body

  if prefs.replaceYouTube.len > 0 and "youtu" in result:
    let youtubeHost = strip(prefs.replaceYouTube, chars={'/'})
    result = result.replace(ytRegex, youtubeHost)

  if prefs.replaceTwitter.len > 0:
    let twitterHost = strip(prefs.replaceTwitter, chars={'/'})
    if tco in result:
      result = result.replace(tco, https & twitterHost & "/t.co")
    if "x.com" in result:
      result = result.replace(xRegex, twitterHost)
      result = result.replacef(xLinkRegex, a(
        twitterHost & "$2", href = https & twitterHost & "$1"))
    if "twitter.com" in result:
      result = result.replace(cards, twitterHost & "/cards")
      result = result.replace(twRegex, twitterHost)
      result = result.replacef(twLinkRegex, a(
        twitterHost & "$2", href = https & twitterHost & "$1"))

  if prefs.replaceReddit.len > 0 and ("reddit.com" in result or "redd.it" in result):
    let redditHost = strip(prefs.replaceReddit, chars={'/'})
    result = result.replace(rdShortRegex, redditHost & "/comments/")
    result = result.replace(rdRegex, redditHost)
    if redditHost in result and "/gallery/" in result:
      result = result.replace("/gallery/", "/comments/")

  if absolute.len > 0 and "href" in result:
    result = result.replace("href=\"/", &"href=\"{absolute}/")

proc getM3u8Url*(content: string): string =
  var matches: array[1, string]
  if re.find(content, m3u8Regex, matches) != -1:
    result = matches[0]

proc proxifyVideo*(manifest: string; proxy: bool; manifestUrl = ""): string =
  let (baseUrl, basePath) =
    if manifestUrl.len > 0:
      let
        u = parseUri(manifestUrl)
        origin = u.scheme & "://" & u.hostname
        idx = manifestUrl.rfind('/')
        dirPath = if idx > 8: manifestUrl[0 .. idx] else: ""
      (origin, dirPath)
    else:
      ("https://video.twimg.com", "")
  var replacements: seq[(string, string)]
  for line in manifest.splitLines:
    let url =
      if line.startsWith("#EXT-X-MAP:URI"): line[16 .. ^2]
      elif line.startsWith("#EXT-X-MEDIA") and "URI=" in line:
        line[line.find("URI=") + 5 .. -1 + line.find("\"", start= 5 + line.find("URI="))]
      else: line
    let resolved =
      if url.startsWith('/'): baseUrl & url
      elif basePath.len > 0 and url.len > 0 and not url.startsWith('#') and
           not url.startsWith("http") and ('.' in url): basePath & url
      else: ""
    if resolved.len > 0:
      replacements.add (url, if proxy: resolved.getVidUrl else: resolved)
  return manifest.multiReplace(replacements)

proc getUserPic*(userPic: string; style=""): string =
  userPic.replacef(userPicRegex, "$2").replacef(extRegex, style & "$1")

proc getUserPic*(user: User; style=""): string =
  getUserPic(user.userPic, style)

proc getVideoEmbed*(cfg: Config; id: int64): string =
  &"{getUrlPrefix(cfg)}/i/videos/{id}"

proc pageTitle*(user: User): string =
  &"{user.fullname} (@{user.username})"

proc pageTitle*(tweet: Tweet): string =
  &"{pageTitle(tweet.user)}: \"{stripHtml(tweet.text)}\""

proc pageDesc*(user: User): string =
  if user.bio.len > 0:
    stripHtml(user.bio)
  else:
    "The latest tweets from " & user.fullname

proc getJoinDate*(user: User): string =
  if user.joinDate.year == 0: return ""
  user.joinDate.format("'Joined' MMMM YYYY")

proc getJoinDateFull*(user: User): string =
  if user.joinDate.year == 0: return ""
  user.joinDate.format("h:mm tt - d MMM YYYY")

proc getTime*(tweet: Tweet): string =
  if tweet.time.year == 0: return ""
  tweet.time.format("MMM d', 'YYYY' · 'h:mm tt' UTC'")

proc getRfc822Time*(tweet: Tweet): string =
  if tweet.time.year == 0: return ""
  tweet.time.format("ddd', 'dd MMM yyyy HH:mm:ss 'GMT'")

proc getShortTime*(time: DateTime): string =
  if time.year == 0: return ""
  let now = now()
  let since = now - time

  if now.year != time.year:
    result = time.format("d MMM yyyy")
  elif since.inDays >= 1:
    result = time.format("MMM d")
  elif since.inHours >= 1:
    result = $since.inHours & "h"
  elif since.inMinutes >= 1:
    result = $since.inMinutes & "m"
  elif since.inSeconds > 1:
    result = $since.inSeconds & "s"
  else:
    result = "now"

proc getShortTime*(tweet: Tweet): string =
  getShortTime(tweet.time)

proc getDuration*(ms: int): string =
  let
    sec = int(round(ms / 1000))
    min = floorDiv(sec, 60)
    hour = floorDiv(min, 60)
  if hour > 0:
    &"{hour}:{min mod 60:02}:{sec mod 60:02}"
  else:
    &"{min mod 60}:{sec mod 60:02}"

proc getDuration*(video: Video): string =
  getDuration(video.durationMs)

proc getLink*(id: int64; username="i"; focus=true): string =
  var username = username
  if username.len == 0:
    username = "i"
  result = &"/{username}/status/{id}"
  if focus: result &= "#m"

proc getLink*(tweet: Tweet; focus=true): string =
  if tweet.id == 0: return
  var username = tweet.user.username
  return getLink(tweet.id, username, focus)

proc getTwitterLink*(path: string; params: Table[string, string]): string =
  var
    username = params.getOrDefault("name")
    query = initQuery(params, username)
    path = path

  if "," in username:
    query.fromUser = username.split(",")
    path = "/search"

  if "/search" notin path and query.fromUser.len < 2:
    return $(twitter / path)

  let p = {
    "f": if query.kind == users: "user" else: "live",
    "q": genQueryParam(query),
    "src": "typed_query"
  }

  result = $(twitter / path ? p)
  if username.len > 0:
    result = result.replace("/" & username, "")

proc getLocation*(u: User | Tweet): (string, string) =
  if "://" in u.location: return (u.location, "")
  let loc = u.location.split(":")
  let url = if loc.len > 1: "/search?f=tweets&q=place:" & loc[1] else: ""
  (loc[0], url)

proc getSuspended*(username: string): string =
  &"User \"{username}\" has been suspended"

proc titleize*(str: string): string =
  const
    lowercase = {'a'..'z'}
    delims = {' ', '('}

  result = str
  for i, c in enumerate(str):
    if c in lowercase and (i == 0 or str[i - 1] in delims):
      result[i] = c.toUpperAscii



================================================
FILE: src/http_pool.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import httpclient

type
  HttpPool* = ref object
    conns*: seq[AsyncHttpClient]

var
  maxConns: int
  proxy: Proxy

proc setMaxHttpConns*(n: int) =
  maxConns = n

proc setHttpProxy*(url: string; auth: string) =
  if url.len > 0:
    proxy = newProxy(url, auth)
  else:
    proxy = nil

proc release*(pool: HttpPool; client: AsyncHttpClient; badClient=false) =
  if pool.conns.len >= maxConns or badClient:
    try: client.close()
    except: discard
  elif client != nil:
    pool.conns.insert(client)

proc acquire*(pool: HttpPool; heads: HttpHeaders): AsyncHttpClient =
  if pool.conns.len == 0:
    result = newAsyncHttpClient(headers=heads, proxy=proxy)
  else:
    result = pool.conns.pop()
    result.headers = heads

template use*(pool: HttpPool; heads: HttpHeaders; body: untyped): untyped =
  var
    c {.inject.} = pool.acquire(heads)
    badClient {.inject.} = false

  try:
    body
  except BadClientError, ProtocolError:
    # Twitter returned 503 or closed the connection, we need a new client
    pool.release(c, true)
    badClient = false
    c = pool.acquire(heads)
    body
  finally:
    pool.release(c, badClient)



================================================
FILE: src/nitter.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, strformat, logging
from net import Port
from htmlgen import a
from os import getEnv, normalizedPath

import jester

import types, config, prefs, formatters, redis_cache, http_pool, auth, apiutils
import views/[general, about]
import routes/[
  preferences, timeline, status, media, search, rss, list, community, debug,
  unsupported, embed, resolver, broadcast, space, article, router_utils]

const instancesUrl = "https://github.com/zedeus/nitter/wiki/Instances"
const issuesUrl = "https://github.com/zedeus/nitter/issues"

let
  configPath = getEnv("NITTER_CONF_FILE", "./nitter.conf")
  (cfg, fullCfg) = getConfig(configPath)

  sessionsPath = getEnv("NITTER_SESSIONS_FILE", "./sessions.jsonl")

initSessionPool(cfg, sessionsPath)

if not cfg.enableDebug:
  # Silence Jester's query warning
  addHandler(newConsoleLogger())
  setLogFilter(lvlError)

stdout.write &"Starting Nitter at {getUrlPrefix(cfg)}\n"
stdout.flushFile

updateDefaultPrefs(fullCfg)
setCacheTimes(cfg)
setHmacKey(cfg.hmacKey)
if cfg.hmacKey.len == 0 or cfg.hmacKey == "secretkey":
  stderr.write "WARNING: insecure default 'hmacKey' in nitter.conf; " &
    "set a unique random value to stop media URL signatures being forgeable.\n"
  stderr.flushFile
setProxyEncoding(cfg.base64Media)
setMaxHttpConns(cfg.httpMaxConns)
setHttpProxy(cfg.proxy, cfg.proxyAuth)
setApiProxy(cfg.apiProxy)
setDisableTid(cfg.disableTid)
setMaxConcurrentReqs(cfg.maxConcurrentReqs)
setMaxRetries(cfg.maxRetries)
setRetryDelayMs(cfg.retryDelayMs)
initAboutPage(cfg.staticDir)

waitFor initRedisPool(cfg)
stdout.write &"Connected to Redis at {cfg.redisHost}:{cfg.redisPort}\n"
stdout.flushFile

createArticleRouter(cfg)
createUnsupportedRouter(cfg)
createResolverRouter(cfg)
createPrefRouter(cfg)
createTimelineRouter(cfg)
createListRouter(cfg)
createCommunityRouter(cfg)
createStatusRouter(cfg)
createSearchRouter(cfg)
createMediaRouter(cfg)
createEmbedRouter(cfg)
createRssRouter(cfg)
createBroadcastRouter(cfg)
createSpaceRouter(cfg)
createDebugRouter(cfg)

settings:
  port = Port(cfg.port)
  staticDir = normalizedPath(cfg.staticDir)
  bindAddr = cfg.address
  reusePort = true
  maxBody = 64 * 1024

routes:
  before:
    # Reject malformed paths
    if request.path.len == 0 or request.path[0] != '/':
      halt Http400

    # skip all file URLs
    cond "." notin request.path
    applyUrlPrefs()

  get "/":
    resp renderMain(renderSearch(), request, cfg, requestPrefs())

  get "/about":
    resp renderMain(renderAbout(), request, cfg, requestPrefs())

  get "/explore":
    redirect("/about")

  get "/help":
    redirect("/about")

  get "/i/redirect":
    let url = decodeUrl(@"url")
    if url.len == 0: resp Http404
    redirect(replaceUrls(url, requestPrefs()))

  error Http404:
    resp Http404, showError("Page not found", cfg)

  error InternalError:
    echo error.exc.name, ": ", error.exc.msg
    const link = a("open a GitHub issue", href = issuesUrl)
    resp Http500, showError(
      &"An error occurred, please {link} with the URL you tried to visit.", cfg)

  error BadClientError:
    echo error.exc.name, ": ", error.exc.msg
    resp Http500, showError("Network error occurred, please try again.", cfg)

  error RateLimitError:
    const link = a("another instance", href = instancesUrl)
    resp Http429, showError(
      &"Instance has been rate limited.<br>Use {link} or try again later.", cfg)

  error NoSessionsError:
    const link = a("another instance", href = instancesUrl)
    resp Http429, showError(
      &"Instance has no auth tokens, or is fully rate limited.<br>Use {link} or try again later.", cfg)

  extend articleRoute, ""
  extend rss, ""
  extend status, ""
  extend search, ""
  extend timeline, ""
  extend media, ""
  extend list, ""
  extend community, ""
  extend preferences, ""
  extend resolver, ""
  extend embed, ""
  extend broadcastRoute, ""
  extend spaceRoute, ""
  extend debug, ""
  extend unsupported, ""



================================================
FILE: src/parser.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, options, times, math, tables, uri
import packedjson, packedjson/deserialiser
import types, parserutils, utils
import experimental/parser/unifiedcard

proc parseGraphTweet*(js: JsonNode): Tweet

proc parseVerifiedType(s: string; current: VerifiedType): VerifiedType =
  try: parseEnum[VerifiedType](s)
  except ValueError: current

proc parseCommunityNote(js: JsonNode): string =
  let subtitle = js{"subtitle"}
  result = subtitle{"text"}.getStr
  with entities, subtitle{"entities"}:
    result = expandBirdwatchEntities(result, entities)

proc parseUser(js: JsonNode; id=""): User =
  if js.isNull: return
  result = User(
    id: if id.len > 0: id else: js{"id_str"}.getStr,
    username: js{"screen_name"}.getStr,
    fullname: js{"name"}.getStr,
    location: js{"location"}.getStr,
    bio: js{"description"}.getStr,
    userPic: js{"profile_image_url_https"}.getImageStr.replace("_normal", ""),
    banner: js.getBanner,
    following: js{"friends_count"}.getInt,
    followers: js{"followers_count"}.getInt,
    tweets: js{"statuses_count"}.getInt,
    likes: js{"favourites_count"}.getInt,
    media: js{"media_count"}.getInt,
    protected: js{"protected"}.getBool(js{"privacy", "protected"}.getBool),
    joinDate: js{"created_at"}.getTime
  )

  if js{"is_blue_verified"}.getBool(false):
    result.verifiedType = blue

  with verifiedType, js{"verified_type"}:
    result.verifiedType = parseVerifiedType(verifiedType.getStr, result.verifiedType)

  result.expandUserEntities(js)

proc parseGraphUser(js: JsonNode): User =
  var user = js{"user_result", "result"}
  if user.isNull:
    user = js{"user_results", "result"}

  if user.isNull:
    if js{"core"}.notNull:
      user = js
    else:
      return

  result = parseUser(user{"legacy"}, user{"rest_id"}.getStr)

  if result.verifiedType == none and user{"is_blue_verified"}.getBool(false):
    result.verifiedType = blue

  # fallback to support UserMedia/recent GraphQL updates
  if result.username.len == 0:
    result.id = user{"rest_id"}.getStr
    result.username = user{"core", "screen_name"}.getStr
    result.fullname = user{"core", "name"}.getStr
    result.userPic = user{"avatar", "image_url"}.getImageStr.replace("_normal", "")

    if user{"is_blue_verified"}.getBool(
       user{"verification", "is_blue_verified"}.getBool(false)):
      result.verifiedType = blue

    with verifiedType, user{"verification", "verified_type"}:
      result.verifiedType = parseVerifiedType(verifiedType.getStr, result.verifiedType)

proc parseAboutAccount*(js: JsonNode): AccountInfo =
  if js.isNull: return

  let user = ? js{"data", "user_result_by_screen_name", "result"}

  if user{"unavailable_reason"}.getStr == "Suspended":
    result.suspended = true
    return

  result = AccountInfo(
    username: user{"core", "screen_name"}.getStr,
    fullname: user{"core", "name"}.getStr,
    joinDate: user{"core", "created_at"}.getTime,
    userPic: user{"avatar", "image_url"}.getImageStr.replace("_normal", ""),
    affiliateLabel: user{"identity_profile_labels_highlighted_label", "label", "description"}.getStr,
  )

  if user{"is_blue_verified"}.getBool(false):
    result.verifiedType = blue
  with verifiedType, user{"verification", "verified_type"}:
    result.verifiedType = parseVerifiedType(verifiedType.getStr, result.verifiedType)

  with about, user{"about_profile"}:
    result.basedIn = about{"account_based_in"}.getStr
    result.source = about{"source"}.getStr
    result.affiliateUsername = about{"affiliate_username"}.getStr

    try: 
      result.usernameChanges = about{"username_changes", "count"}.getStr("0").parseInt
    except ValueError: 
      discard

    with lastChange, about{"username_changes", "last_changed_at_msec"}:
      result.lastUsernameChange = lastChange.getTimeFromMsStr

  with info, user{"verification_info"}:
    result.isIdentityVerified = info{"is_identity_verified"}.getBool
    with reason, info{"reason"}:
      result.overrideVerifiedYear = reason{"override_verified_year"}.getInt
      with since, reason{"verified_since_msec"}:
        result.verifiedSince = since.getTimeFromMsStr

proc parseBroadcastInfo*(js: JsonNode): Broadcast =
  let bc = ? js{"data", "broadcast"}
  result = Broadcast(
    id: bc{"broadcast_id"}.getStr,
    title: bc{"status"}.getStr,
    state: bc{"state"}.getStr.toUpperAscii,
    thumb: bc{"image_url"}.getStr,
    mediaKey: bc{"media_key"}.getStr,
    totalWatched: bc{"total_watched"}.getInt,
    startTime: bc{"start_time"}.getTimeFromMs,
    endTime: bc{"end_time"}.getTimeFromMs,
    replayStart: bc{"edited_replay", "start_time"}.getInt,
    availableForReplay: bc{"available_for_replay"}.getBool,
    user: parseGraphUser(bc)
  )

proc parseSpaceParticipant(js: JsonNode): SpaceParticipant =
  result = SpaceParticipant(
    userId: js{"user_results", "rest_id"}.getStr,
    username: js{"twitter_screen_name"}.getStr,
    displayName: js{"display_name"}.getStr,
    avatarUrl: js{"avatar_url"}.getStr,
    isVerified: js{"is_verified"}.getBool or
                js{"user_results", "result", "is_blue_verified"}.getBool
  )

proc parseAudioSpace*(js: JsonNode): AudioSpace =
  let space = ? js{"data", "audioSpace"}
  let meta = space{"metadata"}

  result = AudioSpace(
    id: meta{"rest_id"}.getStr,
    title: meta{"title"}.getStr,
    state: meta{"state"}.getStr.toUpperAscii,
    mediaKey: meta{"media_key"}.getStr,
    totalLiveListeners: meta{"total_live_listeners"}.getInt,
    totalReplayWatched: meta{"total_replay_watched"}.getInt,
    availableForReplay: meta{"is_space_available_for_replay"}.getBool
  )

  let startedAt = meta{"started_at"}.getInt(0)
  if startedAt > 0:
    result.startTime = fromUnix(startedAt div 1000).utc()

  let endedAtStr = meta{"ended_at"}.getStr
  if endedAtStr.len > 0:
    try:
      let endedAt = parseBiggestInt(endedAtStr)
      if endedAt > 0:
        result.endTime = fromUnix(endedAt div 1000).utc()
    except ValueError:
      discard

  result.creator = parseGraphUser(meta{"creator_results", "result"})

  for admin in space{"participants", "admins"}:
    result.admins.add parseSpaceParticipant(admin)

  for speaker in space{"participants", "speakers"}:
    result.speakers.add parseSpaceParticipant(speaker)

proc parseGraphCommunity*(js: JsonNode): Community =
  if js.isNull: return
  let c = ? js{"data", "communityResults", "result"}

  result = Community(
    id: c{"rest_id"}.getStr(c{"id_str"}.getStr),
    name: c{"name"}.getStr,
    description: c{"description"}.getStr,
    memberCount: c{"member_count"}.getInt,
    joinPolicy: c{"join_policy"}.getStr,
    category: c{"primary_community_topic", "topic_name"}.getStr,
    banner: c{"custom_banner_media", "media_info", "original_img_url"}.getImageStr,
    creator: parseGraphUser(c{"creator_results", "result"}),
  )

  let createdMs = c{"created_at"}.getInt(0)
  if createdMs > 0:
    result.createdAt = fromUnix(createdMs div 1000).utc()

  for rule in c{"rules"}:
    result.rules.add CommunityRule(
      name: rule{"name"}.getStr,
      description: rule{"description"}.getStr
    )

  for item in c{"trending_hashtags_slice", "items"}:
    let tag = item{"hashtag"}.getStr
    if tag.len > 0:
      result.hashtags.add tag

proc parseGraphList*(js: JsonNode): List =
  if js.isNull: return

  var list = js{"data", "user_by_screen_name", "list"}
  if list.isNull:
    list = js{"data", "list"}
  if list.isNull:
    return

  result = List(
    id: list{"id_str"}.getStr,
    name: list{"name"}.getStr,
    username: list{"user_results", "result", "legacy", "screen_name"}.getStr,
    userId: list{"user_results", "result", "rest_id"}.getStr,
    description: list{"description"}.getStr,
    members: list{"member_count"}.getInt,
    banner: list{"custom_banner_media", "media_info", "original_img_url"}.getImageStr
  )

proc parsePoll(js: JsonNode): Poll =
  let vals = js{"binding_values"}
  # name format is pollNchoice_*
  for i in '1' .. js{"name"}.getStr[4]:
    let choice = "choice" & i
    result.values.add parseInt(vals{choice & "_count"}.getStrVal("0"))
    result.options.add vals{choice & "_label"}.getStrVal

  let time = vals{"end_datetime_utc", "string_value"}.getDateTime
  if time > now():
    let timeLeft = $(time - now())
    result.status = timeLeft[0 ..< timeLeft.find(",")]
  else:
    result.status = "Final results"

  result.leader = result.values.find(max(result.values))
  result.votes = result.values.sum

proc parseVideoVariants(variants: JsonNode): seq[VideoVariant] =
  result = @[]
  for v in variants:
    let
      url = v{"url"}.getStr
      contentType = parseEnum[VideoType](v{"content_type"}.getStr("video/mp4"))
      bitrate = v{"bit_rate"}.getInt(v{"bitrate"}.getInt(0))

    result.add VideoVariant(
      contentType: contentType,
      bitrate: bitrate,
      url: url,
      resolution: if contentType == mp4: getMp4Resolution(url) else: 0
    )

proc parseVideo(js: JsonNode): Video =
  result = Video(
    thumb: js{"media_url_https"}.getImageStr,
    available: true,
    title: js{"ext_alt_text"}.getStr,
    durationMs: js{"video_info", "duration_millis"}.getInt
    # playbackType: mp4
  )

  with status, js{"ext_media_availability", "status"}:
    if status.getStr.len > 0 and status.getStr.toLowerAscii != "available":
      result.available = false

  with title, js{"additional_media_info", "title"}:
    result.title = title.getStr

  with description, js{"additional_media_info", "description"}:
    result.description = description.getStr

  result.variants = parseVideoVariants(js{"video_info", "variants"})

proc addMedia(media: var MediaEntities; photo: Photo) =
  media.add Media(kind: photoMedia, photo: photo)

proc addMedia(media: var MediaEntities; video: Video) =
  media.add Media(kind: videoMedia, video: video)

proc addMedia(media: var MediaEntities; gif: Gif) =
  media.add Media(kind: gifMedia, gif: gif)

proc parseLegacyMediaEntities(js: JsonNode; result: var Tweet) =
  with jsMedia, js{"extended_entities", "media"}:
    for m in jsMedia:
      case m.getTypeName:
      of "photo":
        result.media.addMedia(Photo(
          url: m{"media_url_https"}.getImageStr,
          altText: m{"ext_alt_text"}.getStr
        ))
      of "video":
        result.media.addMedia(parseVideo(m))
        with user, m{"additional_media_info", "source_user"}:
          if user{"id"}.getInt > 0:
            result.attribution = some(parseUser(user))
          else:
            result.attribution = some(parseGraphUser(user))
          # Set attribution link from expanded_url (strip /video/N suffix)
          let expanded = m{"expanded_url"}.getStr
          if expanded.len > 0:
            result.attributionLink = expanded.parseUri.path.replace("/video/1", "")
      of "animated_gif":
        result.media.addMedia(Gif(
          url: m{"video_info", "variants"}[0]{"url"}.getImageStr,
          thumb: m{"media_url_https"}.getImageStr,
          altText: m{"ext_alt_text"}.getStr
        ))
      else: discard

proc parseMediaEntities(js: JsonNode; result: var Tweet) =
  with mediaEntities, js{"media_entities"}:
    var parsedMedia: MediaEntities
    for mediaEntity in mediaEntities:
      with mediaInfo, mediaEntity{"media_results", "result", "media_info"}:
        case mediaInfo.getTypeName
        of "ApiImage":
          parsedMedia.addMedia(Photo(
            url: mediaInfo{"original_img_url"}.getImageStr,
            altText: mediaInfo{"alt_text"}.getStr
          ))
        of "ApiVideo":
          let status = mediaEntity{"media_results", "result", "media_availability_v2", "status"}
          parsedMedia.addMedia(Video(
            available: status.getStr == "Available",
            thumb: mediaInfo{"preview_image", "original_img_url"}.getImageStr,
            title: mediaInfo{"alt_text"}.getStr,
            durationMs: mediaInfo{"duration_millis"}.getInt,
            variants: parseVideoVariants(mediaInfo{"variants"})
          ))

          # Parse source user for video attribution
          with sourceUser, mediaEntity{"source_user_results", "result"}:
            if result.attribution.isNone:
              let expanded = mediaEntity{"expanded_url"}.getStr
              if expanded.len > 0:
                result.attributionLink = expanded.parseUri.path.replace("/video/1", "")
              result.attribution = some(User(
                id: sourceUser{"rest_id"}.getStr,
                fullname: sourceUser{"core", "name"}.getStr,
                userPic: sourceUser{"avatar", "image_url"}.getImageStr.replace("_normal", "")
              ))
        of "ApiGif":
          parsedMedia.addMedia(Gif(
            url: mediaInfo{"variants"}[0]{"url"}.getImageStr,
            thumb: mediaInfo{"preview_image", "original_img_url"}.getImageStr,
            altText: mediaInfo{"alt_text"}.getStr
          ))
        else: discard

    if mediaEntities.len > 0 and parsedMedia.len == mediaEntities.len:
      result.media = parsedMedia

proc parsePromoVideo(js: JsonNode): Video =
  result = Video(
    thumb: js{"player_image_large"}.getImageVal,
    available: true,
    durationMs: js{"content_duration_seconds"}.getStrVal("0").parseInt * 1000,
    playbackType: vmap
  )

  var variant = VideoVariant(
    contentType: vmap,
    url: js{"player_hls_url"}.getStrVal(js{"player_stream_url"}.getStrVal(
        js{"amplify_url_vmap"}.getStrVal()))
  )

  if "m3u8" in variant.url:
    variant.contentType = m3u8
    result.playbackType = m3u8

  result.variants.add variant

proc parseBroadcast(js: JsonNode): Card =
  let
    image = js{"broadcast_thumbnail_large"}.getImageVal
    broadcastUrl = js{"broadcast_url"}.getStrVal
    broadcastId = broadcastUrl.rsplit('/', maxsplit=1)[^1]
    streamUrl = "/i/broadcasts/" & broadcastId & "/stream"
  result = Card(
    kind: broadcast,
    url: "/i/broadcasts/" & broadcastId,
    title: js{"broadcaster_display_name"}.getStrVal,
    text: js{"broadcast_title"}.getStrVal,
    image: image,
    video: some Video(
      thumb: image,
      available: true,
      playbackType: m3u8,
      variants: @[VideoVariant(contentType: m3u8, url: streamUrl)]
    )
  )

proc parseCard(js: JsonNode; urls: JsonNode): Card =
  const imageTypes = ["summary_photo_image", "player_image", "promo_image",
                      "photo_image_full_size", "thumbnail_image", "thumbnail",
                      "event_thumbnail", "image"]
  let
    vals = ? js{"binding_values"}
    name = js{"name"}.getStr
    kind = parseEnum[CardKind](name[(name.find(":") + 1) ..< name.len], unknown)

  if kind == unified:
    return parseUnifiedCard(vals{"unified_card", "string_value"}.getStr)

  result = Card(
    kind: kind,
    url: vals.getCardUrl(kind),
    dest: vals.getCardDomain(kind),
    title: vals.getCardTitle(kind),
    text: vals{"description"}.getStrVal
  )

  if result.url.len == 0:
    result.url = js{"url"}.getStr

  case kind
  of promoVideo, promoVideoConvo, appPlayer, videoDirectMessage:
    result.video = some parsePromoVideo(vals)
    if kind == appPlayer:
      result.text = vals{"app_category"}.getStrVal(result.text)
  of broadcast:
    result = parseBroadcast(vals)
  of liveEvent:
    result.text = vals{"event_title"}.getStrVal
  of player:
    result.url = vals{"player_url"}.getStrVal
    if "youtube.com" in result.url:
      result.url = result.url.replace("/embed/", "/watch?v=")
  of audiospace:
    let spaceId = vals{"id"}.getStrVal
    if spaceId.len > 0:
      result.url = "/i/spaces/" & spaceId
      result.title = "Twitter Space"
      result.text = "Click to view Space"
  of unknown:
    result.title = "This card type is not supported."
  else: discard

  for typ in imageTypes:
    with img, vals{typ & "_large"}:
      result.image = img.getImageVal
      break

  for u in ? urls:
    if u{"url"}.getStr == result.url:
      result.url = u.getExpandedUrl(result.url)
      break

  if kind in {videoDirectMessage, imageDirectMessage}:
    result.url.setLen 0

  if kind in {promoImageConvo, promoImageApp, imageDirectMessage} and
     result.url.len == 0 or result.url.startsWith("card://"):
    result.url = getPicUrl(result.image)

proc parseTweet(js: JsonNode; jsCard: JsonNode = newJNull();
                replyId: int64 = 0): Tweet =
  if js.isNull: return Tweet()

  let time =
    if js{"created_at"}.notNull: js{"created_at"}.getTime
    else: js{"created_at_ms"}.getTimeFromMs

  result = Tweet(
    id: js{"id_str"}.getId,
    threadId: js{"conversation_id_str"}.getId,
    replyId: js{"in_reply_to_status_id_str"}.getId,
    text: js{"full_text"}.getStr,
    time: time,
    hasThread: js{"self_thread"}.notNull,
    available: true,
    user: User(id: js{"user_id_str"}.getStr),
    stats: TweetStats(
      replies: js{"reply_count"}.getInt,
      retweets: js{"retweet_count"}.getInt,
      likes: js{"favorite_count"}.getInt,
      views: js{"views_count"}.getInt
    )
  )

  if result.replyId == 0:
    result.replyId = replyId

  # fix for pinned threads
  if result.hasThread and result.threadId == 0:
    result.threadId = js{"self_thread", "id_str"}.getId

  if "retweeted_status" in js:
    result.retweet = some Tweet()
  elif js{"is_quote_status"}.getBool:
    result.quote = some Tweet(id: js{"quoted_status_id_str"}.getId)

  # legacy
  with rt, js{"retweeted_status_id_str"}:
    result.retweet = some Tweet(id: rt.getId)
    return

  # graphql
  with rt, js{"retweeted_status_result", "result"}:
    # needed due to weird edgecase where the actual tweet data isn't included
    if "legacy" in rt or "rest_id" in rt:
      result.retweet = some parseGraphTweet(rt)
      return

  with reposts, js{"repostedStatusResults"}:
    with rt, reposts{"result"}:
      if "legacy" in rt or "rest_id" in rt:
        result.retweet = some parseGraphTweet(rt)
        return

  if jsCard.kind != JNull:
    let name = jsCard{"name"}.getStr
    if "poll" in name:
      if "image" in name:
        result.media.addMedia(Photo(
          url: jsCard{"binding_values", "image_large"}.getImageVal
        ))

      result.poll = some parsePoll(jsCard)
    elif name == "amplify":
      result.media.addMedia(parsePromoVideo(jsCard{"binding_values"}))
    elif name.len > 0 and jsCard{"binding_values"}.notNull:
      result.card = some parseCard(jsCard, js{"entities", "urls"})

  result.expandTweetEntities(js)
  parseLegacyMediaEntities(js, result)

  with jsWithheld, js{"withheld_in_countries"}:
    let withheldInCountries: seq[string] =
      if jsWithheld.kind != JArray: @[]
      else: jsWithheld.to(seq[string])

    # XX - Content is withheld in all countries
    # XY - Content is withheld due to a DMCA request.
    if js{"withheld_copyright"}.getBool or
       withheldInCountries.len > 0 and ("XX" in withheldInCountries or
                                        "XY" in withheldInCountries or
                                        "withheld" in result.text):
      result.text.removeSuffix(" Learn more.")
      result.available = false

proc parseGraphTweet*(js: JsonNode): Tweet =
  if js.kind == JNull:
    return Tweet()

  case js.getTypeName:
  of "TweetUnavailable":
    return Tweet()
  of "TweetTombstone":
    with text, select(js{"tombstone", "richText"}, js{"tombstone", "text"}):
      return Tweet(text: text.getTombstone)
    return Tweet()
  of "TweetPreviewDisplay":
    return Tweet(text: "You're unable to view this Tweet because it's only available to the Subscribers of the account owner.")
  of "TweetWithVisibilityResults":
    return parseGraphTweet(js{"tweet"})
  else:
    discard

  if "legacy" notin js and "rest_id" notin js:
    return Tweet()

  var jsCard = select(js{"card"}, js{"tweet_card"}, js{"legacy", "tweet_card"})
  if jsCard.kind != JNull:
    let legacyCard = jsCard{"legacy"}
    if legacyCard.kind != JNull:
      let bindingArray = legacyCard{"binding_values"}
      if bindingArray.kind == JArray:
        var bindingObj: seq[(string, JsonNode)]
        for item in bindingArray:
          bindingObj.add((item{"key"}.getStr, item{"value"}))
        # Create a new card object with flattened structure
        jsCard = %*{
          "name": legacyCard{"name"},
          "url": legacyCard{"url"},
          "binding_values": %bindingObj
        }

  var replyId: int64 = 0
  with restId, js{"reply_to_results", "rest_id"}:
    replyId = restId.getId

  if "details" in js:
    result = Tweet(
      id: js{"rest_id"}.getId,
      available: true,
      text: js{"details", "full_text"}.getStr,
      time: js{"details", "created_at_ms"}.getTimeFromMs,
      replyId: js{"reply_to_results", "rest_id"}.getId,
      isAd: js{"content_disclosure", "advertising_disclosure", "is_paid_promotion"}.getBool,
      isAI: js{"content_disclosure", "ai_generated_disclosure", "has_ai_generated_media"}.getBool,
      stats: TweetStats(
        replies: js{"counts", "reply_count"}.getInt,
        retweets: js{"counts", "retweet_count"}.getInt,
        likes: js{"counts", "favorite_count"}.getInt,
      )
    )

    if jsCard.kind != JNull:
      let name = jsCard{"name"}.getStr
      if "poll" in name:
        if "image" in name:
          result.media.addMedia(Photo(
            url: jsCard{"binding_values", "image_large"}.getImageVal
          ))

        result.poll = some parsePoll(jsCard)
      elif name == "amplify":
        result.media.addMedia(parsePromoVideo(jsCard{"binding_values"}))
      elif name.len > 0 and jsCard{"binding_values"}.notNull:
        result.card = some parseCard(jsCard, js{"url_entities"})

    parseMediaEntities(js, result)
    if result.attribution.isNone:
      parseLegacyMediaEntities(js{"legacy"}, result)

    let hasArticle = js{"article", "article_results", "result", "title"}.getStr.len > 0
    result.expandTweetEntitiesV2(js, hasArticle)

    # Strip video source URL from text (for videos from other tweets)
    with mediaEntities, js{"media_entities"}:
      for m in mediaEntities:
        if "source_status_id_str" in m:
          let mediaUrl = m{"url"}.getStr
          if mediaUrl.len > 0:
            let idx = result.text.rfind(mediaUrl)
            if idx >= 0:
              result.text = result.text[0 ..< idx].strip()
            break
  else:
    result = parseTweet(js{"legacy"}, jsCard, replyId)
    result.id = js{"rest_id"}.getId

  with artNode, js{"article", "article_results", "result"}:
    let artTitle = artNode{"title"}.getStr
    if artTitle.len > 0:
      result.articlePreview = some ArticlePreview(
        title: artTitle,
        previewText: artNode{"preview_text"}.getStr,
        coverImage: artNode{"cover_media_results", "result", "media_info", "original_img_url"}.getImageStr,
        tweetId: result.id
      )

  result.user = parseGraphUser(js{"core"})

  if result.reply.len == 0:
    with replyTo, js{"reply_to_user_results", "result", "core", "screen_name"}:
      result.reply = @[replyTo.getStr]

  with count, js{"views", "count"}:
    result.stats.views = count.getStr("0").parseInt

  with noteTweet, js{"note_tweet", "note_tweet_results", "result"}:
    result.expandNoteTweetEntities(noteTweet)

  parseMediaEntities(js, result)

  # Hide card if it's redundant with attribution (same video shown via embed)
  if result.attribution.isSome and result.card.isSome:
    let cardUri = get(result.card).url.parseUri
    if cardUri.isTwitterUrl:
      let cardPath = cardUri.path.replace("/video/1", "")
      if cardPath.len > 0 and cardPath == result.attributionLink:
        get(result.card).kind = hidden

  # Handle retweets - check both legacy and top-level paths
  with reposts, js{"legacy", "repostedStatusResults"}:
    with rt, reposts{"result"}:
      if "legacy" in rt or "rest_id" in rt:
        result.retweet = some parseGraphTweet(rt)

  with quoted, js{"quoted_status_result", "result"}:
    result.quote = some(parseGraphTweet(quoted))

  with quoted, js{"quotedPostResults"}:
    if "result" in quoted:
      result.quote = some(parseGraphTweet(quoted{"result"}))
    else:
      result.quote = some Tweet(id: js{"legacy", "quoted_status_id_str"}.getId)

  with ids, js{"edit_control", "edit_control_initial", "edit_tweet_ids"}:
    for id in ids:
      result.history.add parseBiggestInt(id.getStr)

  with birdwatch, js{"birdwatch_pivot"}:
    result.note = parseCommunityNote(birdwatch)

proc parseGraphThread(js: JsonNode): tuple[thread: Chain; self: bool] =
  for t in ? js{"content", "items"}:
    let entryId = t.getEntryId
    if "tweet-" in entryId and "promoted" notin entryId:
      let tweet = t.getTweetResult("item")
      if tweet.notNull:
        result.thread.content.add parseGraphTweet(tweet)

        let tweetDisplayType = select(
          t{"item", "content", "tweet_display_type"},
          t{"item", "itemContent", "tweetDisplayType"}
        )
        if tweetDisplayType.getStr == "SelfThread":
          result.self = true
      else:
        result.thread.content.add Tweet(id: entryId.getId)
    elif "cursor-showmore" in entryId:
      let cursor = t{"item", "content", "value"}
      result.thread.cursor = cursor.getStr
      result.thread.hasMore = true

proc parseGraphTweetResult*(js: JsonNode): Tweet =
  with tweet, js{"data", "tweet_result", "result"}:
    result = parseGraphTweet(tweet)

proc parseGraphTweetResults*(js: JsonNode): seq[Tweet] =
  let results = js{"data", "tweetResult"}
  if results.kind != JArray: return
  for item in results:
    let tweet = item{"result"}
    if tweet.isNull: continue
    let t = parseGraphTweet(tweet)
    if t != nil:
      result.add t

proc parseGraphConversation*(js: JsonNode; tweetId: string): Conversation =
  result = Conversation(replies: Result[Chain](beginning: true))

  let instructions = ? select(
    js{"data", "timelineResponse", "instructions"},
    js{"data", "timeline_response", "instructions"},
    js{"data", "threaded_conversation_with_injections_v2", "instructions"}
  )
  if instructions.len == 0:
    return

  for i in instructions:
    if i.getTypeName == "TimelineAddEntries":
      for e in i{"entries"}:
        let entryId = e.getEntryId
        if entryId.startsWith("tweet-"):
          let tweetResult = getTweetResult(e)
          if tweetResult.notNull:
            let tweet = parseGraphTweet(tweetResult)

            if not tweet.available:
              tweet.id = entryId.getId

            if entryId.endsWith(tweetId):
              result.tweet = tweet
            else:
              result.before.content.add tweet
          elif not entryId.endsWith(tweetId):
            result.before.content.add Tweet(id: entryId.getId)
        elif entryId.startsWith("conversationthread"):
          let (thread, self) = parseGraphThread(e)
          if self:
            result.after = thread
          elif thread.content.len > 0:
            result.replies.content.add thread
        elif entryId.startsWith("tombstone"):
          let
            content = select(e{"content", "content"}, e{"content", "itemContent"})
            tweet = Tweet(
              id: entryId.getId,
              available: false,
              text: content{"tombstoneInfo", "richText"}.getTombstone
            )

          if $tweet.id == tweetId:
            result.tweet = tweet
          else:
            result.before.content.add tweet
        elif entryId.startsWith("cursor-bottom"):
          var cursorValue = select(
            e{"content", "value"},
            e{"content", "content", "value"},
            e{"content", "itemContent", "value"}
          )
          result.replies.bottom = cursorValue.getStr

proc parseGraphEditHistory*(js: JsonNode; tweetId: string): EditHistory =
  let instructions = ? js{
    "data", "tweet_result_by_rest_id", "result", 
    "edit_history_timeline", "timeline", "instructions"
  }
  if instructions.len == 0:
    return

  for i in instructions:
    if i.getTypeName == "TimelineAddEntries":
      for e in i{"entries"}:
        let entryId = e.getEntryId
        if entryId == "latestTweet":
          with item, e{"content", "items"}[0]:
            let tweetResult = item.getTweetResult("item")
            if tweetResult.notNull:
              result.latest = parseGraphTweet(tweetResult)
        elif entryId == "staleTweets":
          for item in e{"content", "items"}:
            let tweetResult = item.getTweetResult("item")
            if tweetResult.notNull:
              result.history.add parseGraphTweet(tweetResult)

proc extractTweetsFromEntry*(e: JsonNode): seq[Tweet] =
  with tweetResult, getTweetResult(e):
    var tweet = parseGraphTweet(tweetResult)
    if not tweet.available:
      tweet.id = e.getEntryId.getId
    result.add tweet
    return

  for item in e{"content", "items"}:
    with tweetResult, item.getTweetResult("item"):
      var tweet = parseGraphTweet(tweetResult)
      if not tweet.available:
        tweet.id = item.getEntryId.getId
      result.add tweet

proc parseGraphTimeline*(js: JsonNode; after=""): Profile =
  result = Profile(tweets: Timeline(beginning: after.len == 0))

  let instructions = ? select(
    js{"data", "list", "timeline_response", "timeline", "instructions"},
    js{"data", "user", "result", "timeline", "timeline", "instructions"},
    js{"data", "user_result", "result", "timeline_response", "timeline", "instructions"}
  )
  if instructions.len == 0:
    return

  for i in instructions:
    if i{"moduleItems"}.notNull:
      for item in i{"moduleItems"}:
        with tweetResult, item.getTweetResult("item"):
          let tweet = parseGraphTweet(tweetResult)
          if not tweet.available:
            tweet.id = item.getEntryId.getId
          result.tweets.content.add tweet
      continue

    if i{"entries"}.notNull:
      for e in i{"entries"}:
        let entryId = e.getEntryId
        if entryId.startsWith("tweet") or entryId.startsWith("profile-grid"):
          for tweet in extractTweetsFromEntry(e):
            result.tweets.content.add tweet
        elif "-conversation-" in entryId or entryId.startsWith("homeConversation"):
          let (thread, self) = parseGraphThread(e)
          result.tweets.content.add thread.content
        elif entryId.startsWith("cursor-bottom"):
          result.tweets.bottom = e{"content", "value"}.getStr

    if after.len == 0:
      if i.getTypeName == "TimelinePinEntry":
        let tweets = extractTweetsFromEntry(i{"entry"})
        if tweets.len > 0:
          var tweet = tweets[0]
          tweet.pinned = true
          result.pinned = some tweet

proc parseGraphPhotoRail*(js: JsonNode): PhotoRail =
  result = @[]

  let instructions = select(
    js{"data", "user", "result", "timeline", "timeline", "instructions"},
    js{"data", "user_result", "result", "timeline_response", "timeline", "instructions"}
  )
  if instructions.len == 0:
    return

  for i in instructions:
    if i{"moduleItems"}.notNull:
      for item in i{"moduleItems"}:
        with tweetResult, item.getTweetResult("item"):
          let t = parseGraphTweet(tweetResult)
          if not t.available:
            t.id = item.getEntryId.getId

          let photo = extractGalleryPhoto(t)
          if photo.url.len > 0:
            result.add photo

          if result.len == 16:
            return
      continue

    if i.getTypeName != "TimelineAddEntries":
      continue

    for e in i{"entries"}:
      let entryId = e.getEntryId
      if entryId.startsWith("tweet") or entryId.startsWith("profile-grid"):
        for t in extractTweetsFromEntry(e):
          let photo = extractGalleryPhoto(t)
          if photo.url.len > 0:
            result.add photo

          if result.len == 16:
            return

proc parseGraphSearch*[T: User | Tweets](js: JsonNode; after=""): Result[T] =
  result = Result[T](beginning: after.len == 0)

  let instructions = select(
    js{"data", "search", "timeline_response", "timeline", "instructions"},
    js{"data", "search_by_raw_query", "search_timeline", "timeline", "instructions"}
  )
  if instructions.len == 0:
    return

  for instruction in instructions:
    let typ = getTypeName(instruction)
    if typ == "TimelineAddEntries":
      for e in instruction{"entries"}:
        let entryId = e.getEntryId
        when T is Tweets:
          if entryId.startsWith("tweet"):
            with tweetRes, getTweetResult(e):
              let tweet = parseGraphTweet(tweetRes)
              if not tweet.available:
                tweet.id = entryId.getId
              result.content.add tweet
        elif T is User:
          if entryId.startsWith("user"):
            with userRes, e{"content", "itemContent"}:
              result.content.add parseGraphUser(userRes)

        if entryId.startsWith("cursor-bottom"):
          result.bottom = e{"content", "value"}.getStr
    elif typ == "TimelineReplaceEntry":
      if instruction{"entry_id_to_replace"}.getStr.startsWith("cursor-bottom"):
        result.bottom = instruction{"entry", "content", "value"}.getStr

proc parseGraphCommunityTimeline*(js: JsonNode; after=""): Timeline =
  result = Timeline(beginning: after.len == 0)

  let communityResult = js{"data", "communityResults", "result"}
  let instructions = ? select(
    communityResult{"ranked_community_timeline", "timeline", "instructions"},
    communityResult{"community_media_timeline", "timeline", "instructions"},
    communityResult{"community_filtered_timeline", "timeline", "instructions"}
  )
  if instructions.len == 0:
    return

  for i in instructions:
    if i{"entries"}.notNull:
      for e in i{"entries"}:
        let entryId = e.getEntryId
        if entryId.startsWith("tweet") or entryId.startsWith("profile-grid") or
           entryId.startsWith("communities-grid"):
          for tweet in extractTweetsFromEntry(e):
            result.content.add tweet
        elif entryId.startsWith("cursor-bottom"):
          result.bottom = e{"content", "value"}.getStr

    if after.len == 0 and i.getTypeName == "TimelinePinEntry":
      var tweets = extractTweetsFromEntry(i{"entry"})
      for tweet in tweets.mitems:
        tweet.pinned = true
      if tweets.len > 0:
        result.content.insert(tweets, 0)

proc parseGraphCommunityMembers*(js: JsonNode; after=""): Result[User] =
  result = Result[User](beginning: after.len == 0)

  let r = js{"data", "communityResults", "result"}
  let slice = if not r{"members_slice"}.isNull: r{"members_slice"}
              else: r{"moderators_slice"}
  for item in slice{"items_results"}:
    let user = parseGraphUser(item{"result"})
    if user.username.len > 0:
      result.content.add user

  let cursor = slice{"slice_info", "next_cursor"}.getStr
  if cursor.len > 0:
    result.bottom = cursor




================================================
FILE: src/parserutils.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import std/[times, macros, htmlgen, options, algorithm, re]
import std/strutils except escape
import std/unicode except strip
from xmltree import escape
import packedjson
import types, utils, formatters

const
  unicodeOpen = "\uFFFA"
  unicodeClose = "\uFFFB"
  xmlOpen = escape("<")
  xmlClose = escape(">")

let
  unRegex = re"(^|[^A-z0-9-_./?])@([A-z0-9_]{1,15})"
  unReplace = "$1<a href=\"/$2\">@$2</a>"

  htRegex = re"(^|[^\w-_./?])([#$]|＃)([\w_]+)"
  htReplace = "$1<a href=\"/search?f=tweets&q=%23$3\">$2$3</a>"

type
  ReplaceSliceKind = enum
    rkRemove, rkUrl, rkHashtag, rkMention

  ReplaceSlice = object
    slice: Slice[int]
    kind: ReplaceSliceKind
    url, display: string

template isNull*(js: JsonNode): bool = js.kind == JNull
template notNull*(js: JsonNode): bool = js.kind != JNull

template `?`*(js: JsonNode): untyped =
  let j = js
  if j.isNull: return
  j

template select*(a, b: JsonNode): untyped =
  if a.notNull: a else: b

template select*(a, b, c: JsonNode): untyped =
  if a.notNull: a elif b.notNull: b else: c

template with*(ident, value, body): untyped =
  if true:
    let ident {.inject.} = value
    if ident != nil: body

template with*(ident; value: JsonNode; body): untyped =
  if true:
    let ident {.inject.} = value
    if value.notNull: body

template getCursor*(js: JsonNode): string =
  js{"content", "operation", "cursor", "value"}.getStr

template getError*(js: JsonNode): Error =
  if js.kind != JArray or js.len == 0: null
  else: Error(js[0]{"code"}.getInt)

proc getTweetResult*(js: JsonNode; root="content"): JsonNode =
  select(
    js{root, "content", "tweet_results", "result"},
    js{root, "itemContent", "tweet_results", "result"},
    js{root, "content", "tweetResult", "result"}
  )

template getTypeName*(js: JsonNode): string =
  js{"__typename"}.getStr(js{"type"}.getStr)

template getEntryId*(e: JsonNode): string =
  e{"entryId"}.getStr(e{"entry_id"}.getStr)

template parseTime(time: string; f: static string; flen: int): DateTime =
  if time.len != flen: return
  parse(time, f, utc())

proc getDateTime*(js: JsonNode): DateTime =
  parseTime(js.getStr, "yyyy-MM-dd\'T\'HH:mm:ss\'Z\'", 20)

proc getTime*(js: JsonNode): DateTime =
  parseTime(js.getStr, "ddd MMM dd hh:mm:ss \'+0000\' yyyy", 30)

proc getTimeFromMs*(js: JsonNode): DateTime =
  let ms = js.getInt(0)
  if ms == 0: return
  let seconds = ms div 1000
  return fromUnix(seconds).utc()

proc getTimeFromMsStr*(js: JsonNode): DateTime =
  var ms: int64
  try: ms = parseBiggestInt(js.getStr("0"))
  except ValueError: return
  if ms == 0: return
  let seconds = ms div 1000
  return fromUnix(seconds).utc()

proc getId*(id: string): int64 {.inline.} =
  let start = id.rfind("-")
  if start < 0:
    return parseBiggestInt(id)
  return parseBiggestInt(id[start + 1 ..< id.len])

proc getId*(js: JsonNode): int64 {.inline.} =
  case js.kind
  of JString: return js.getStr("0").getId
  of JInt: return js.getBiggestInt()
  else: return 0

template getStrVal*(js: JsonNode; default=""): string =
  js{"string_value"}.getStr(default)

proc getImageStr*(js: JsonNode): string =
  result = js.getStr
  result.removePrefix(https)
  result.removePrefix(twimg)

template getImageVal*(js: JsonNode): string =
  js{"image_value", "url"}.getImageStr

template getExpandedUrl*(js: JsonNode; fallback=""): string =
  js{"expanded_url"}.getStr(js{"url"}.getStr(fallback))

proc getCardUrl*(js: JsonNode; kind: CardKind): string =
  result = js{"website_url"}.getStrVal
  if kind == promoVideoConvo:
    result = js{"thank_you_url"}.getStrVal(result)
  if result.startsWith("card://"):
    result = ""

proc getCardDomain*(js: JsonNode; kind: CardKind): string =
  result = js{"vanity_url"}.getStrVal(js{"domain"}.getStr)
  if kind == promoVideoConvo:
    result = js{"thank_you_vanity_url"}.getStrVal(result)

proc getCardTitle*(js: JsonNode; kind: CardKind): string =
  result = js{"title"}.getStrVal
  if kind == promoVideoConvo:
    result = js{"thank_you_text"}.getStrVal(result)
  elif kind == liveEvent:
    result = js{"event_category"}.getStrVal
  elif kind in {videoDirectMessage, imageDirectMessage}:
    result = js{"cta1"}.getStrVal

proc getBanner*(js: JsonNode): string =
  let url = js{"profile_banner_url"}.getImageStr
  if url.len > 0:
    return url & "/1500x500"

  let color = js{"profile_link_color"}.getStr
  if color.len > 0:
    return '#' & color

  # use primary color from profile picture color histogram
  with p, js{"profile_image_extensions", "mediaColor", "r", "ok", "palette"}:
    if p.len > 0:
      let pal = p[0]{"rgb"}
      result = "#"
      result.add toHex(pal{"red"}.getInt, 2)
      result.add toHex(pal{"green"}.getInt, 2)
      result.add toHex(pal{"blue"}.getInt, 2)
      return

proc getTombstone*(js: JsonNode): string =
  result = js{"text"}.getStr
  result.removeSuffix(" Learn more")

proc getMp4Resolution*(url: string): int =
  # parses the height out of a URL like this one:
  # https://video.twimg.com/ext_tw_video/<tweet-id>/pu/vid/720x1280/<random>.mp4
  const vidSep = "/vid/"
  let
    vidIdx = url.find(vidSep) + vidSep.len
    resIdx = url.find('x', vidIdx) + 1
    res = url[resIdx ..< url.find("/", resIdx)]

  try:
    return parseInt(res)
  except ValueError:
    # cannot determine resolution (e.g. m3u8/non-mp4 video)
    return 0

proc extractSlice(js: JsonNode): Slice[int] =
  result = js["indices"][0].getInt ..< js["indices"][1].getInt

proc extractUrls(result: var seq[ReplaceSlice]; js: JsonNode;
                 textLen: int; hideTwitter = false;
                 hideArticle = false) =
  let
    url = js.getExpandedUrl
    slice = js.extractSlice

  if hideArticle and url.isTwitterUrl and "/article/" in url:
    if slice.a < textLen:
      result.add ReplaceSlice(kind: rkRemove, slice: slice)
  elif hideTwitter and slice.b.succ >= textLen and url.isTwitterUrl:
    if slice.a < textLen:
      result.add ReplaceSlice(kind: rkRemove, slice: slice)
  else:
    result.add ReplaceSlice(kind: rkUrl, url: url,
                            display: url.shortLink, slice: slice)

proc extractHashtags(result: var seq[ReplaceSlice]; js: JsonNode) =
  result.add ReplaceSlice(kind: rkHashtag, slice: js.extractSlice)

proc replacedWith(runes: seq[Rune]; repls: openArray[ReplaceSlice];
                  textSlice: Slice[int]): string =
  let
    runeLen = runes.len
    safeStart = max(0, textSlice.a)
    safeEnd = min(runeLen, textSlice.b)

  var validRepls: seq[ReplaceSlice]
  for rep in repls:
    if rep.slice.a >= 0 and rep.slice.b >= 0 and rep.slice.b < runeLen and rep.slice.a <= rep.slice.b:
      validRepls.add rep

  template extractLowerBound(i: int; idx): int =
    if i > 0: min(validRepls[idx].slice.b.succ, runeLen) else: safeStart

  result = newStringOfCap(runes.len)

  for i, rep in validRepls:
    let lower = extractLowerBound(i, i - 1)
    if lower < rep.slice.a:
      result.add $runes[lower ..< rep.slice.a]
    case rep.kind
    of rkHashtag:
      if rep.slice.a.succ <= rep.slice.b:
        let
          name = $runes[rep.slice.a.succ .. rep.slice.b]
          symbol = $runes[rep.slice.a]
        result.add a(symbol & name, href = "/search?f=tweets&q=%23" & name)
    of rkMention:
      result.add a($runes[rep.slice], href = rep.url, title = rep.display)
    of rkUrl:
      result.add a(rep.display, href = rep.url)
    of rkRemove:
      discard

  let rest = extractLowerBound(validRepls.len, ^1) ..< safeEnd
  if rest.a >= 0 and rest.a <= rest.b and rest.b <= runeLen:
    result.add $runes[rest]

proc deduplicate(s: var seq[ReplaceSlice]) =
  var
    len = s.len
    i = 0
  while i < len:
    var j = i + 1
    while j < len:
      if s[i].slice.a == s[j].slice.a:
        s.del j
        dec len
      else:
        inc j
    inc i

proc cmp(x, y: ReplaceSlice): int = cmp(x.slice.a, y.slice.b)

proc expandUserEntities*(user: var User; js: JsonNode) =
  let
    orig = user.bio.toRunes
    ent = ? js{"entities"}

  with urls, ent{"url", "urls"}:
    user.website = urls[0].getExpandedUrl

  var replacements = newSeq[ReplaceSlice]()

  with urls, ent{"description", "urls"}:
    for u in urls:
      replacements.extractUrls(u, orig.high)

  replacements.deduplicate
  replacements.sort(cmp)

  user.bio = orig.replacedWith(replacements, 0 .. orig.len)
  user.bio = user.bio.replacef(unRegex, unReplace)
                     .replacef(htRegex, htReplace)

proc expandTextEntities(tweet: Tweet; entities: JsonNode; text: string; textSlice: Slice[int];
                        replyTo=""; hasRedundantLink=false) =
  let hasCard = tweet.card.isSome

  var replacements = newSeq[ReplaceSlice]()

  with urls, entities{"urls"}:
    for u in urls:
      let urlStr = u["url"].getStr
      if urlStr.len == 0 or urlStr notin text:
        continue

      replacements.extractUrls(u, textSlice.b, hideTwitter = hasRedundantLink)

      if hasCard and u{"url"}.getStr == get(tweet.card).url:
        get(tweet.card).url = u.getExpandedUrl

  with media, entities{"media"}:
    for m in media:
      replacements.extractUrls(m, textSlice.b, hideTwitter = true)

  if "hashtags" in entities:
    for hashtag in entities["hashtags"]:
      replacements.extractHashtags(hashtag)

  if "symbols" in entities:
    for symbol in entities["symbols"]:
      replacements.extractHashtags(symbol)

  if "user_mentions" in entities:
    for mention in entities["user_mentions"]:
      let
        name = mention{"screen_name"}.getStr
        slice = mention.extractSlice
        idx = tweet.reply.find(name)

      if slice.a >= textSlice.a:
        replacements.add ReplaceSlice(kind: rkMention, slice: slice,
          url: "/" & name, display: mention["name"].getStr)
        if idx > -1 and name != replyTo:
          tweet.reply.delete idx
      elif idx == -1 and tweet.replyId != 0:
        tweet.reply.add name

  replacements.deduplicate
  replacements.sort(cmp)

  tweet.text = text.toRunes.replacedWith(replacements, textSlice).strip(leading=false)

proc expandTweetEntities*(tweet: Tweet; js: JsonNode) =
  let
    entities = ? js{"entities"}
    textRange = js{"display_text_range"}
    textSlice = textRange{0}.getInt .. textRange{1}.getInt
    hasQuote = js{"is_quote_status"}.getBool
    hasJobCard = tweet.card.isSome and get(tweet.card).kind == jobDetails

  var replyTo = ""
  if tweet.replyId != 0:
    with reply, js{"in_reply_to_screen_name"}:
      replyTo = reply.getStr
      tweet.reply.add replyTo

  tweet.expandTextEntities(entities, tweet.text, textSlice, replyTo,
                           hasQuote or hasJobCard)

proc expandTextEntitiesV2(tweet: Tweet; js: JsonNode; text: string; textSlice: Slice[int];
                          hasRedundantLink=false; hasArticle=false) =
  let hasCard = tweet.card.isSome

  var replacements = newSeq[ReplaceSlice]()

  with urls, js{"url_entities"}:
    for u in urls:
      let urlStr = u["url"].getStr
      if urlStr.len == 0 or urlStr notin text:
        continue

      replacements.extractUrls(u, textSlice.b, hideTwitter = hasRedundantLink,
                               hideArticle = hasArticle)

      if hasCard and u{"url"}.getStr == get(tweet.card).url:
        get(tweet.card).url = u.getExpandedUrl

  with hashtags, js{"details", "hashtag_entities"}:
    for hashtag in hashtags:
      replacements.extractHashtags(hashtag)

  with cashtags, js{"details", "cashtag_entities"}:
    for cashtag in cashtags:
      replacements.extractHashtags(cashtag)

  with mentions, js{"mention_entities"}:
    for mention in mentions:
      let
        name = mention{"screen_name"}.getStr
        slice = mention.extractSlice
        idx = tweet.reply.find(name)

      if slice.a >= textSlice.a:
        replacements.add ReplaceSlice(kind: rkMention, slice: slice,
          url: "/" & name, display: mention["name"].getStr)
      elif idx == -1 and tweet.replyId != 0:
        tweet.reply.add name

  replacements.deduplicate
  replacements.sort(cmp)

  tweet.text = text.toRunes.replacedWith(replacements, textSlice).strip(leading=false)

proc expandTweetEntitiesV2*(tweet: Tweet; js: JsonNode; hasArticle=false) =
  let
    textRange = js{"details", "display_text_range"}
    textSlice = textRange{0}.getInt .. textRange{1}.getInt
    hasQuote = "quoted_tweet_results" in js
    hasJobCard = tweet.card.isSome and get(tweet.card).kind == jobDetails
    hasAttribution = tweet.attribution.isSome

  tweet.expandTextEntitiesV2(js, tweet.text, textSlice,
                             hasQuote or hasJobCard or hasAttribution,
                             hasArticle)

proc expandNoteTweetEntities*(tweet: Tweet; js: JsonNode) =
  let
    entities = ? js{"entity_set"}
    text = js{"text"}.getStr.multiReplace(("<", unicodeOpen), (">", unicodeClose))
    textSlice = 0..text.runeLen
    hasAttribution = tweet.attribution.isSome

  tweet.expandTextEntities(entities, text, textSlice, hasRedundantLink=hasAttribution)

  tweet.text = tweet.text.multiReplace((unicodeOpen, xmlOpen), (unicodeClose, xmlClose))

proc expandBirdwatchEntities*(text: string; entities: JsonNode): string =
  let runes = text.toRunes
  var replacements: seq[ReplaceSlice]

  for entity in entities:
    let
      fromIdx = entity{"from_index"}.getInt
      toIdx = entity{"to_index"}.getInt
      url = entity{"ref", "url"}.getStr
    if url.len > 0:
      replacements.add ReplaceSlice(
        kind: rkUrl,
        slice: fromIdx ..< toIdx,
        url: url,
        display: $runes[fromIdx ..< min(toIdx, runes.len)]
      )

  replacements.sort(cmp)
  result = runes.replacedWith(replacements, 0 ..< runes.len)

proc extractGalleryPhoto*(t: Tweet): GalleryPhoto =
  let url =
    if t.media.len > 0: t.media[0].getThumb
    elif t.card.isSome: get(t.card).image
    else: ""

  result = GalleryPhoto(url: url, tweetId: $t.id)



================================================
FILE: src/prefs.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import tables, strutils
import types, prefs_impl
from config import get
from parsecfg import nil

export genUpdatePrefs, genResetPrefs, genApplyPrefs

var defaultPrefs*: Prefs

proc updateDefaultPrefs*(cfg: parsecfg.Config) =
  genDefaultPrefs()

proc getPrefs*(cookies, params: Table[string, string]): Prefs =
  result = defaultPrefs
  genParsePrefs(cookies)
  genParsePrefs(params)

proc encodePrefs*(prefs: Prefs): string =
  var encPairs: seq[string]
  genEncodePrefs(prefs)
  encPairs.join(",")



================================================
FILE: src/prefs_impl.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import macros, tables, strutils, xmltree

type
  PrefKind* = enum
    checkbox, select, input

  Pref* = object
    name*: string
    label*: string
    kind*: PrefKind
    # checkbox
    defaultState*: bool
    # select
    defaultOption*: string
    options*: seq[string]
    # input
    defaultInput*: string
    placeholder*: string

  PrefList* = OrderedTable[string, seq[Pref]]

macro genPrefs*(prefDsl: untyped) =
  var table = nnkTableConstr.newTree()
  for category in prefDsl:
    table.add nnkExprColonExpr.newTree(newLit($category[0]))
    table[^1].add nnkPrefix.newTree(newIdentNode("@"), nnkBracket.newTree())
    for pref in category[1]:
      let
        name = newLit($pref[0])
        kind = pref[1]
        label = pref[3][0]
        default = pref[2]
        defaultField =
          case parseEnum[PrefKind]($kind)
          of checkbox: ident("defaultState")
          of select: ident("defaultOption")
          of input: ident("defaultInput")

      var newPref = quote do:
        Pref(kind: `kind`, name: `name`, label: `label`, `defaultField`: `default`)

      for node in pref[3]:
        if node.kind == nnkCall:
          newPref.add nnkExprColonExpr.newTree(node[0], node[1][0])
      table[^1][1][1].add newPref

  let name = ident("prefList")
  result = quote do:
    const `name`*: PrefList = toOrderedTable(`table`)

genPrefs:
  Display:
    theme(select, "Nitter"):
      "Theme"

    infiniteScroll(checkbox, false):
      "Infinite scrolling (experimental, requires JavaScript)"

    stickyProfile(checkbox, true):
      "Make profile sidebar stick to top"

    stickyNav(checkbox, true):
      "Keep navbar fixed to top"

    bidiSupport(checkbox, false):
      "Support bidirectional text (makes clicking on tweets harder)"

    hideTweetStats(checkbox, false):
      "Hide tweet stats (replies, retweets, likes)"

    hideBanner(checkbox, false):
      "Hide profile banner"

    hidePins(checkbox, false):
      "Hide pinned tweets"

    hideReplies(checkbox, false):
      "Hide tweet replies"

    hideCommunityNotes(checkbox, false):
      "Hide community notes"

    squareAvatars(checkbox, false):
      "Square profile pictures"

  Media:
    mp4Playback(checkbox, true):
      "Enable mp4 video playback (only for gifs)"

    hlsPlayback(checkbox, false):
      "Enable HLS video streaming (requires JavaScript)"

    proxyVideos(checkbox, true):
      "Proxy video streaming through the server (might be slow)"

    muteVideos(checkbox, false):
      "Mute videos by default"

    autoplayGifs(checkbox, true):
      "Autoplay gifs"

    compactGallery(checkbox, false):
      "Compact media gallery (no profile info or text)"

    gallerySize(select, "Medium"):
      "Gallery column size"
      options: @["Small", "Medium", "Large"]

    mediaView(select, "Timeline"):
      "Default media view"
      options: @["Timeline", "Grid", "Gallery"]

  "Link replacements (blank to disable)":
    replaceTwitter(input, ""):
      "Twitter -> Nitter"
      placeholder: "Nitter hostname"

    replaceYouTube(input, ""):
      "YouTube -> Piped/Invidious"
      placeholder: "Piped hostname"

    replaceReddit(input, ""):
      "Reddit -> Teddit/Libreddit"
      placeholder: "Teddit hostname"

iterator allPrefs*(): Pref =
  for k, v in prefList:
    for pref in v:
      yield pref

macro genDefaultPrefs*(): untyped =
  result = nnkStmtList.newTree()
  for pref in allPrefs():
    let
      ident = ident(pref.name)
      name = newLit(pref.name)
      default =
        case pref.kind
        of checkbox: newLit(pref.defaultState)
        of select: newLit(pref.defaultOption)
        of input: newLit(pref.defaultInput)

    result.add quote do:
      defaultPrefs.`ident` = cfg.get("Preferences", `name`, `default`)

macro genParsePrefs*(prefs): untyped =
  result = nnkStmtList.newTree()
  for pref in allPrefs():
    let
      name = pref.name
      ident = ident(pref.name)
      kind = newLit(pref.kind)
      options = pref.options

    result.add quote do:
      if `name` in `prefs`:
        when `kind` == input or `name` == "theme":
          result.`ident` = `prefs`[`name`]
        elif `kind` == checkbox:
          result.`ident` = `prefs`[`name`] == "on" or 
                           `prefs`[`name`] == "true" or
                           `prefs`[`name`] == "1"
        else:
          let value = `prefs`[`name`]
          if value in `options`: result.`ident` = value

macro genUpdatePrefs*(): untyped =
  result = nnkStmtList.newTree()
  let req = ident("request")
  for pref in allPrefs():
    let
      name = newLit(pref.name)
      kind = newLit(pref.kind)
      options = newLit(pref.options)
      default = nnkDotExpr.newTree(ident("defaultPrefs"), ident(pref.name))

    result.add quote do:
      let val = @`name`
      let isDefault =
        when `kind` == input or `name` == "theme":
          if `default`.len != val.len: false
          else: val == `default`
        elif `kind` == checkbox:
          (val == "on") == `default`
        else:
          val notin `options` or val == `default`

      if isDefault:
        savePref(`name`, "", `req`, expire=true)
      else:
        savePref(`name`, val, `req`)

macro genResetPrefs*(): untyped =
  result = nnkStmtList.newTree()
  let req = ident("request")
  for pref in allPrefs():
    let name = newLit(pref.name)
    result.add quote do:
      savePref(`name`, "", `req`, expire=true)

macro genEncodePrefs*(prefs): untyped =
  result = nnkStmtList.newTree()
  for pref in allPrefs():
    let
      name = newLit(pref.name)
      ident = ident(pref.name)
      kind = newLit(pref.kind)
      defaultIdent = nnkDotExpr.newTree(ident("defaultPrefs"), ident(pref.name))

    result.add quote do:
      when `kind` == checkbox:
        if `prefs`.`ident` != `defaultIdent`:
          if `prefs`.`ident`:
            encPairs.add `name` & "=on"
          else:
            encPairs.add `name` & "="
      else:
        if `prefs`.`ident` != `defaultIdent`:
          encPairs.add `name` & "=" & `prefs`.`ident`

macro genApplyPrefs*(params, req): untyped =
  result = nnkStmtList.newTree()
  for pref in allPrefs():
    let name = newLit(pref.name)
    result.add quote do:
      if `name` in `params`:
        savePref(`name`, `params`[`name`], `req`)
      else:
        savePref(`name`, "", `req`, expire=true)

macro genPrefsType*(): untyped =
  let name = nnkPostfix.newTree(ident("*"), ident("Prefs"))
  result = quote do:
    type `name` = object
      discard

  for pref in allPrefs():
    result[0][2][2].add nnkIdentDefs.newTree(
      nnkPostfix.newTree(ident("*"), ident(pref.name)),
      (case pref.kind
       of checkbox: ident("bool")
       of input, select: ident("string")),
      newEmptyNode())



================================================
FILE: src/query.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, sequtils, tables, uri

import types, utils

const
  validFilters* = @[
    "media", "images", "twimg", "videos",
    "native_video", "consumer_video", "spaces",
    "links", "news", "quote", "mentions",
    "replies", "retweets", "nativeretweets"
  ]

  emptyQuery* = "include:nativeretweets"

template `@`(param: string): untyped =
  if param in pms: pms[param]
  else: ""

proc initQuery*(pms: Table[string, string]; name=""): Query =
  result = Query(
    kind: parseEnum[QueryKind](@"f", tweets),
    view: @"view",
    text: @"q",
    filters: validFilters.filterIt("f-" & it in pms),
    excludes: validFilters.filterIt("e-" & it in pms),
    since: @"since",
    until: @"until",
    minLikes: validateNumber(@"min_faves")
  )

  if name.len > 0:
    result.fromUser = name.split(",")

proc getMediaQuery*(name: string): Query =
  Query(
    kind: media,
    filters: @["twimg", "native_video"],
    fromUser: @[name],
    sep: "OR"
  )

proc getReplyQuery*(name: string): Query =
  Query(
    kind: replies,
    fromUser: @[name]
  )

proc genQueryParam*(query: Query; maxId=""): string =
  var
    filters: seq[string]
    param: string

  if query.kind == users:
    return query.text

  for i, user in query.fromUser:
    if i == 0:
      param = "("

    param &= &"from:{user}"
    if i < query.fromUser.high:
      param &= " OR "
    else:
      param &= ")"

  if query.fromUser.len > 0 and query.kind in {posts, media}:
    param &= " (filter:self_threads OR -filter:replies)"

  if "nativeretweets" notin query.excludes:
    param &= " include:nativeretweets"

  for f in query.filters:
    filters.add "filter:" & f
  for e in query.excludes:
    if e == "nativeretweets": continue
    filters.add "-filter:" & e
  for i in query.includes:
    filters.add "include:" & i

  if filters.len > 0:
    result = strip(param & " (" & filters.join(&" {query.sep} ") & ")")
  else:
    result = strip(param)

  if query.since.len > 0:
    result &= " since:" & query.since
  if query.until.len > 0 and maxId.len == 0:
    result &= " until:" & query.until
  if query.minLikes.len > 0:
    result &= " min_faves:" & query.minLikes
  if query.text.len > 0:
    if result.len > 0:
      result &= " " & query.text
    else:
      result = query.text

  if result.len > 0 and maxId.len > 0:
    result &= " max_id:" & maxId

proc genQueryUrl*(query: Query): string =
  var params: seq[string]

  if query.view.len > 0:
    params.add "view=" & encodeUrl(query.view)

  if query.kind in {tweets, users}:
    params.add &"f={query.kind}"
    if query.text.len > 0:
      params.add "q=" & encodeUrl(query.text)
    for f in query.filters:
      params.add &"f-{f}=on"
    for e in query.excludes:
      params.add &"e-{e}=on"
    for i in query.includes.filterIt(it != "nativeretweets"):
      params.add &"i-{i}=on"

    if query.since.len > 0:
      params.add "since=" & query.since
    if query.until.len > 0:
      params.add "until=" & query.until
    if query.minLikes.len > 0:
      params.add "min_faves=" & query.minLikes

  if params.len > 0:
    result &= params.join("&")



================================================
FILE: src/redis_cache.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, times, strformat, strutils, tables, hashes
import redis, redpool, flatty, supersnappy

import types, api

const
  redisNil = "\0\0"
  baseCacheTime = 60 * 60

var
  pool: RedisPool
  rssCacheTime: int
  listCacheTime*: int

template dawait(future) =
  discard await future

# flatty can't serialize DateTime, so we need to define this
proc toFlatty*(s: var string, x: DateTime) =
  s.toFlatty(x.toTime().toUnix())

proc fromFlatty*(s: string, i: var int, x: var DateTime) =
  var unix: int64
  s.fromFlatty(i, unix)
  x = fromUnix(unix).utc()

proc setCacheTimes*(cfg: Config) =
  rssCacheTime = cfg.rssCacheTime * 60
  listCacheTime = cfg.listCacheTime * 60

proc migrate*(key, match: string) {.async.} =
  pool.withAcquire(r):
    let hasKey = await r.get(key)
    if hasKey == redisNil:
      let list = await r.scan(newCursor(0), match, 100000)
      r.startPipelining()
      for item in list:
        dawait r.del(item)
      await r.setk(key, "true")
      dawait r.flushPipeline()

proc initRedisPool*(cfg: Config) {.async.} =
  try:
    pool = await newRedisPool(cfg.redisConns, cfg.redisMaxConns,
                              host=cfg.redisHost, port=cfg.redisPort,
                              password=cfg.redisPassword)

    await migrate("flatty", "*:*")
    await migrate("snappyRss", "rss:*")
    await migrate("userBuckets", "p:*")
    await migrate("profileDates", "p:*")
    await migrate("profileStats", "p:*")
    await migrate("userType", "p:*")
    await migrate("verifiedType", "p:*")

    pool.withAcquire(r):
      # optimize memory usage for user ID buckets
      await r.configSet("hash-max-ziplist-entries", "1000")

  except OSError:
    stdout.write "Failed to connect to Redis.\n"
    stdout.flushFile
    quit(1)

template uidKey(name: string): string = "pid:" & $(hash(name) div 1_000_000)
template userKey(name: string): string = "p:" & name
template listKey(l: List): string = "l:" & l.id
template tweetKey(id: int64): string = "t:" & $id

proc get(query: string): Future[string] {.async.} =
  pool.withAcquire(r):
    result = await r.get(query)

proc setEx(key: string; time: int; data: string) {.async.} =
  pool.withAcquire(r):
    dawait r.setEx(key, time, data)

proc cacheUserId(username, id: string) {.async.} =
  if username.len == 0 or id.len == 0: return
  let name = toLower(username)
  pool.withAcquire(r):
    dawait r.hSet(name.uidKey, name, id)

proc cache*(data: List) {.async.} =
  await setEx(data.listKey, listCacheTime, compress(toFlatty(data)))

proc cache*(data: PhotoRail; name: string) {.async.} =
  await setEx("pr2:" & toLower(name), baseCacheTime * 2, compress(toFlatty(data)))

proc cache*(data: User) {.async.} =
  if data.username.len == 0: return
  let name = toLower(data.username)
  await cacheUserId(name, data.id)
  pool.withAcquire(r):
    dawait r.setEx(name.userKey, baseCacheTime, compress(toFlatty(data)))

proc cache*(data: Tweet) {.async.} =
  if data.isNil or data.id == 0: return
  pool.withAcquire(r):
    dawait r.setEx(data.id.tweetKey, baseCacheTime, compress(toFlatty(data)))

proc cacheRss*(query: string; rss: Rss) {.async.} =
  let key = "rss:" & query
  pool.withAcquire(r):
    dawait r.hSet(key, "min", rss.cursor)
    if rss.cursor != "suspended":
      dawait r.hSet(key, "rss", compress(rss.feed))
    dawait r.expire(key, rssCacheTime)

template deserialize(data, T) =
  try:
    result = fromFlatty(uncompress(data), T)
  except:
    echo "Decompression failed($#): '$#'" % [astToStr(T), data]

proc getUserId*(username: string): Future[string] {.async.} =
  let name = toLower(username)
  pool.withAcquire(r):
    result = await r.hGet(name.uidKey, name)
    if result == redisNil:
      let user = await getGraphUser(username)
      if user.suspended:
        return "suspended"
      else:
        await all(cacheUserId(name, user.id), cache(user))
        return user.id

proc getCachedUser*(username: string; fetch=true): Future[User] {.async.} =
  let prof = await get("p:" & toLower(username))
  if prof != redisNil:
    prof.deserialize(User)
  elif fetch:
    result = await getGraphUser(username)
    await cache(result)

proc getCachedUsername*(userId: string): Future[string] {.async.} =
  let
    key = "i:" & userId
    username = await get(key)

  if username != redisNil:
    result = username
  else:
    let user = await getGraphUserById(userId)
    result = user.username
    if result.len > 0:
      await setEx(key, baseCacheTime, result)
      if user.id.len > 0:
        await all(cacheUserId(result, user.id), cache(user))

# proc getCachedTweet*(id: int64): Future[Tweet] {.async.} =
#   if id == 0: return
#   let tweet = await get(id.tweetKey)
#   if tweet != redisNil:
#     tweet.deserialize(Tweet)
#   else:
#     result = await getGraphTweetResult($id)
#     if not result.isNil:
#       await cache(result)

proc cache*(data: Broadcast) {.async.} =
  if data.id.len == 0: return
  await setEx("bc:" & data.id, baseCacheTime, compress(toFlatty(data)))

proc getCachedBroadcast*(id: string): Future[Broadcast] {.async.} =
  if id.len == 0: return
  let cached = await get("bc:" & id)
  if cached != redisNil:
    cached.deserialize(Broadcast)
  else:
    result = await getBroadcastInfo(id)
    await cache(result)
  result.m3u8Url = await fetchBroadcastStream(result.mediaKey)

proc cache*(data: AudioSpace) {.async.} =
  if data.id.len == 0: return
  let ttl = if data.state == "RUNNING": baseCacheTime div 6 else: baseCacheTime
  await setEx("sp:" & data.id, ttl, compress(toFlatty(data)))

proc getCachedAudioSpace*(id: string): Future[AudioSpace] {.async.} =
  if id.len == 0: return
  let cached = await get("sp:" & id)
  if cached != redisNil:
    cached.deserialize(AudioSpace)
  else:
    result = await getAudioSpace(id)
    await cache(result)
  result.m3u8Url = await fetchBroadcastStream(result.mediaKey)

proc cache*(data: AccountInfo; name: string) {.async.} =
  await setEx("ai:" & toLower(name), baseCacheTime * 24, compress(toFlatty(data)))

proc getCachedAccountInfo*(username: string; fetch=true): Future[AccountInfo] {.async.} =
  if username.len == 0: return
  let name = toLower(username)
  let cached = await get("ai:" & name)
  if cached != redisNil:
    cached.deserialize(AccountInfo)
  elif fetch:
    result = await getAboutAccount(username)
    await cache(result, name)

proc getCachedPhotoRail*(id: string): Future[PhotoRail] {.async.} =
  if id.len == 0: return
  let rail = await get("pr2:" & toLower(id))
  if rail != redisNil:
    rail.deserialize(PhotoRail)
  else:
    result = await getPhotoRail(id)
    await cache(result, id)

proc cache*(data: Community) {.async.} =
  if data.id.len == 0: return
  await setEx("cm:" & data.id, listCacheTime, compress(toFlatty(data)))

proc getCachedCommunity*(id: string): Future[Community] {.async.} =
  if id.len == 0: return
  let cached = await get("cm:" & id)
  if cached != redisNil:
    cached.deserialize(Community)
  else:
    result = await getGraphCommunity(id)
    await cache(result)

proc getCachedCommunityModerators*(id: string): Future[seq[User]] {.async.} =
  if id.len == 0: return
  let cached = await get("cmm:" & id)
  if cached != redisNil:
    cached.deserialize(seq[User])
  else:
    let mods = await getGraphCommunityModerators(id)
    result = mods.content
    await setEx("cmm:" & id, listCacheTime, compress(toFlatty(result)))

proc getCachedList*(username=""; slug=""; id=""): Future[List] {.async.} =
  let list = if id.len == 0: redisNil
             else: await get("l:" & id)

  if list != redisNil:
    list.deserialize(List)
  else:
    if id.len > 0:
      result = await getGraphList(id)
    else:
      result = await getGraphListBySlug(username, slug)
    await cache(result)

proc getCachedRss*(key: string): Future[Rss] {.async.} =
  let k = "rss:" & key
  pool.withAcquire(r):
    result.cursor = await r.hGet(k, "min")
    if result.cursor.len > 2:
      if result.cursor != "suspended":
        let feed = await r.hGet(k, "rss")
        if feed.len > 0 and feed != redisNil:
          try: result.feed = uncompress feed
          except: echo "Decompressing RSS failed: ", feed
    else:
      result.cursor.setLen 0



================================================
FILE: src/tid.nim
================================================
import std/[asyncdispatch, base64, httpclient, random, strutils, sequtils, times]
import nimcrypto
import experimental/parser/tid

randomize()

const defaultKeyword = "obfiowerehiring";
const pairsUrl =
  "https://raw.githubusercontent.com/fa0311/x-client-transaction-id-pair-dict/refs/heads/main/pair.json";

var
  cachedPairs: seq[TidPair] = @[]
  lastCached = 0
  # refresh every hour
  ttlSec = 60 * 60

proc getPair(): Future[TidPair] {.async.} =
  if cachedPairs.len == 0 or int(epochTime()) - lastCached > ttlSec:
    lastCached = int(epochTime())

    let client = newAsyncHttpClient()
    defer: client.close()

    let resp = await client.get(pairsUrl)
    if resp.status == $Http200:
      cachedPairs = parseTidPairs(await resp.body)

  return sample(cachedPairs)

proc encodeSha256(text: string): array[32, byte] =
  let
    data = cast[ptr byte](addr text[0])
    dataLen = uint(len(text))
    digest = sha256.digest(data, dataLen)
  return digest.data

proc encodeBase64[T](data: T): string =
  return encode(data).replace("=", "")

proc decodeBase64(data: string): seq[byte] =
  return cast[seq[byte]](decode(data))

proc genTid*(path: string): Future[string] {.async.} =
  let 
    pair = await getPair()

    timeNow = int(epochTime() - 1682924400)
    timeNowBytes = @[
      byte(timeNow and 0xff),
      byte((timeNow shr 8) and 0xff),
      byte((timeNow shr 16) and 0xff),
      byte((timeNow shr 24) and 0xff)
    ]

    data = "GET!" & path & "!" & $timeNow & defaultKeyword & pair.animationKey
    hashBytes = encodeSha256(data)
    keyBytes = decodeBase64(pair.verification)
    bytesArr = keyBytes & timeNowBytes & hashBytes[0 ..< 16] & @[3'u8]
    randomNum = byte(rand(256))
    tid = @[randomNum] & bytesArr.mapIt(it xor randomNum)

  return encodeBase64(tid)



================================================
FILE: src/types.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import times, sequtils, options, tables
import prefs_impl

genPrefsType()

type
  RateLimitError* = object of CatchableError
  NoSessionsError* = object of CatchableError
  InternalError* = object of CatchableError
  BadClientError* = object of CatchableError

  TimelineKind* {.pure.} = enum
    tweets, replies, media

  ApiUrl* = object
    endpoint*: string
    params*: seq[(string, string)]
    skipTid*: bool

  ApiReq* = object
    oauth*: ApiUrl
    cookie*: ApiUrl

  RateLimit* = object
    limit*: int
    remaining*: int
    reset*: int

  SessionKind* = enum
    oauth
    cookie

  Session* = ref object
    id*: int64
    username*: string
    pending*: int
    limited*: bool
    limitedAt*: int
    apis*: Table[string, RateLimit]
    case kind*: SessionKind
    of oauth:
      oauthToken*: string
      oauthSecret*: string
    of cookie:
      authToken*: string
      ct0*: string

  Error* = enum
    null = 0
    noUserMatches = 17
    protectedUser = 22
    missingParams = 25
    timeout = 29
    couldntAuth = 32
    doesntExist = 34
    unauthorized = 37
    invalidParam = 47
    userNotFound = 50
    suspended = 63
    rateLimited = 88
    expiredToken = 89
    listIdOrSlug = 112
    timelineUnavailable = 131
    tweetNotFound = 144
    tweetNotAuthorized = 179
    forbidden = 200
    badRequest = 214
    badToken = 239
    locked = 326
    noCsrf = 353
    tweetUnavailable = 421
    tweetCensored = 422

  VerifiedType* = enum
    none = "None"
    blue = "Blue"
    business = "Business"
    government = "Government"

  User* = object
    id*: string
    username*: string
    fullname*: string
    location*: string
    website*: string
    bio*: string
    userPic*: string
    banner*: string
    pinnedTweet*: int64
    following*: int
    followers*: int
    tweets*: int
    likes*: int
    media*: int
    verifiedType*: VerifiedType
    protected*: bool
    suspended*: bool
    joinDate*: DateTime

  AccountInfo* = object
    username*: string
    fullname*: string
    userPic*: string
    joinDate*: DateTime
    verifiedType*: VerifiedType
    suspended*: bool
    basedIn*: string
    source*: string
    usernameChanges*: int
    lastUsernameChange*: DateTime
    affiliateUsername*: string
    affiliateLabel*: string
    isIdentityVerified*: bool
    verifiedSince*: DateTime
    overrideVerifiedYear*: int

  Broadcast* = object
    id*: string
    title*: string
    state*: string
    thumb*: string
    mediaKey*: string
    m3u8Url*: string
    totalWatched*: int
    startTime*: DateTime
    endTime*: DateTime
    replayStart*: int
    availableForReplay*: bool
    user*: User

  SpaceParticipant* = object
    userId*: string
    username*: string
    displayName*: string
    avatarUrl*: string
    isVerified*: bool

  AudioSpace* = object
    id*: string
    title*: string
    state*: string
    mediaKey*: string
    m3u8Url*: string
    totalLiveListeners*: int
    totalReplayWatched*: int
    startTime*: DateTime
    endTime*: DateTime
    availableForReplay*: bool
    creator*: User
    admins*: seq[SpaceParticipant]
    speakers*: seq[SpaceParticipant]

  VideoType* = enum
    m3u8 = "application/x-mpegURL"
    mp4 = "video/mp4"
    vmap = "video/vmap"

  VideoVariant* = object
    contentType*: VideoType
    url*: string
    bitrate*: int
    resolution*: int

  Video* = object
    durationMs*: int
    url*: string
    thumb*: string
    available*: bool
    reason*: string
    title*: string
    description*: string
    playbackType*: VideoType
    variants*: seq[VideoVariant]

  QueryKind* = enum
    posts, replies, media, users, tweets, userList, followers, following

  Query* = object
    kind*: QueryKind
    view*: string
    text*: string
    filters*: seq[string]
    includes*: seq[string]
    excludes*: seq[string]
    fromUser*: seq[string]
    since*: string
    until*: string
    minLikes*: string
    sep*: string

  Gif* = object
    url*: string
    thumb*: string
    altText*: string

  Photo* = object
    url*: string
    altText*: string

  MediaKind* = enum
    photoMedia
    videoMedia
    gifMedia

  Media* = object
    case kind*: MediaKind
    of photoMedia:
      photo*: Photo
    of videoMedia:
      video*: Video
    of gifMedia:
      gif*: Gif

  MediaEntities* = seq[Media]

  GalleryPhoto* = object
    url*: string
    tweetId*: string
    color*: string

  PhotoRail* = seq[GalleryPhoto]

  Article* = ref object
    title*: string
    coverImage*: string
    user*: User
    time*: DateTime
    stats*: TweetStats
    paragraphs*: seq[ArticleParagraph]
    entities*: Table[int, ArticleEntity]
    media*: Table[string, ArticleMedia]

  ArticleParagraph* = object
    text*: string
    kind*: string
    inlineStyles*: seq[ArticleStyle]
    entityRanges*: seq[ArticleEntityRange]

  ArticleStyle* = object
    offset*: int
    length*: int
    style*: string

  ArticleEntityRange* = object
    offset*: int
    length*: int
    key*: int

  ArticleEntity* = object
    kind*: string
    url*: string
    mediaIds*: seq[string]
    tweetId*: string
    markdown*: string

  ArticleMedia* = object
    kind*: string
    url*: string

  Poll* = object
    options*: seq[string]
    values*: seq[int]
    votes*: int
    leader*: int
    status*: string

  CardKind* = enum
    amplify = "amplify"
    app = "app"
    appPlayer = "appplayer"
    player = "player"
    summary = "summary"
    summaryLarge = "summary_large_image"
    promoWebsite = "promo_website"
    promoVideo = "promo_video_website"
    promoVideoConvo = "promo_video_convo"
    promoImageConvo = "promo_image_convo"
    promoImageApp = "promo_image_app"
    storeLink = "direct_store_link_app"
    liveEvent = "live_event"
    broadcast = "broadcast"
    periscope = "periscope_broadcast"
    unified = "unified_card"
    moment = "moment"
    messageMe = "message_me"
    videoDirectMessage = "video_direct_message"
    imageDirectMessage = "image_direct_message"
    audiospace = "audiospace"
    newsletterPublication = "newsletter_publication"
    jobDetails = "job_details"
    hidden
    unknown

  Card* = object
    kind*: CardKind
    url*: string
    title*: string
    dest*: string
    text*: string
    image*: string
    video*: Option[Video]

  TweetStats* = object
    replies*: int
    retweets*: int
    likes*: int
    views*: int

  ArticlePreview* = object
    title*: string
    previewText*: string
    coverImage*: string
    tweetId*: int64

  Tweet* = ref object
    id*: int64
    threadId*: int64
    replyId*: int64
    user*: User
    text*: string
    time*: DateTime
    reply*: seq[string]
    pinned*: bool
    hasThread*: bool
    available*: bool
    tombstone*: string
    location*: string
    # Unused, needed for backwards compat
    source*: string
    stats*: TweetStats
    retweet*: Option[Tweet]
    attribution*: Option[User]
    attributionLink*: string
    mediaTags*: seq[User]
    quote*: Option[Tweet]
    card*: Option[Card]
    poll*: Option[Poll]
    media*: MediaEntities
    history*: seq[int64]
    note*: string
    isAd*: bool
    isAI*: bool
    articlePreview*: Option[ArticlePreview]

  Tweets* = seq[Tweet]

  Result*[T] = object
    content*: seq[T]
    top*, bottom*: string
    beginning*: bool
    query*: Query

  Chain* = object
    content*: Tweets
    hasMore*: bool
    cursor*: string

  Conversation* = ref object
    tweet*: Tweet
    before*: Chain
    after*: Chain
    replies*: Result[Chain]

  EditHistory* = object
    latest*: Tweet
    history*: Tweets

  Timeline* = Result[Tweets]

  Profile* = object
    user*: User
    photoRail*: PhotoRail
    pinned*: Option[Tweet]
    tweets*: Timeline
    accountInfo*: AccountInfo

  List* = object
    id*: string
    name*: string
    userId*: string
    username*: string
    description*: string
    members*: int
    banner*: string

  CommunityRule* = object
    name*: string
    description*: string

  Community* = object
    id*: string
    name*: string
    description*: string
    memberCount*: int
    banner*: string
    creator*: User
    category*: string
    joinPolicy*: string
    createdAt*: DateTime
    rules*: seq[CommunityRule]
    hashtags*: seq[string]

  GlobalObjects* = ref object
    tweets*: Table[string, Tweet]
    users*: Table[string, User]

  Config* = ref object
    address*: string
    port*: int
    useHttps*: bool
    httpMaxConns*: int
    title*: string
    hostname*: string
    staticDir*: string

    hmacKey*: string
    base64Media*: bool
    minTokens*: int
    enableRSSUserTweets*: bool
    enableRSSUserReplies*: bool
    enableRSSUserMedia*: bool
    enableRSSSearch*: bool
    enableRSSList*: bool
    enableDebug*: bool
    proxy*: string
    proxyAuth*: string
    apiProxy*: string
    disableTid*: bool
    maxConcurrentReqs*: int
    maxRetries*: int
    retryDelayMs*: int

    rssCacheTime*: int
    listCacheTime*: int

    redisHost*: string
    redisPort*: int
    redisConns*: int
    redisMaxConns*: int
    redisPassword*: string

  Rss* = object
    feed*, cursor*: string

proc contains*(thread: Chain; tweet: Tweet): bool =
  thread.content.anyIt(it.id == tweet.id)

proc add*(timeline: var seq[Tweets]; tweet: Tweet) =
  timeline.add @[tweet]

proc getPhotos*(tweet: Tweet): seq[Photo] =
  tweet.media.filterIt(it.kind == photoMedia).mapIt(it.photo)

proc getVideos*(tweet: Tweet): seq[Video] =
  tweet.media.filterIt(it.kind == videoMedia).mapIt(it.video)

proc hasPhotos*(tweet: Tweet): bool =
  tweet.media.anyIt(it.kind == photoMedia)

proc hasVideos*(tweet: Tweet): bool =
  tweet.media.anyIt(it.kind == videoMedia)

proc hasGifs*(tweet: Tweet): bool =
  tweet.media.anyIt(it.kind == gifMedia)

proc getThumb*(media: Media): string =
  case media.kind
  of photoMedia: media.photo.url
  of videoMedia: media.video.thumb
  of gifMedia: media.gif.thumb



================================================
FILE: src/utils.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import sequtils, strutils, strformat, uri, tables, base64
import nimcrypto

var
  hmacKey: string
  base64Media = false

const
  https* = "https://"
  twimg* = "pbs.twimg.com/"
  nitterParams* = ["name", "tab", "id", "list", "referer", "scroll", "prefs"]
  twitterDomains = @[
    "twitter.com",
    "pic.twitter.com",
    "twimg.com",
    "abs.twimg.com",
    "pbs.twimg.com",
    "video.twimg.com",
    "x.com",
    "pscp.tv",
    "video.pscp.tv"
  ]

proc setHmacKey*(key: string) =
  hmacKey = key

proc setProxyEncoding*(state: bool) =
  base64Media = state

proc getHmac*(data: string): string =
  ($hmac(sha256, hmacKey, data))[0 .. 12]

proc getVidUrl*(link: string): string =
  if link.len == 0: return
  let sig = getHmac(link)
  if base64Media:
    &"/video/enc/{sig}/{encode(link, safe=true)}"
  else:
    &"/video/{sig}/{encodeUrl(link)}"

proc getPicUrl*(link: string): string =
  if link.len == 0: return
  if base64Media:
    &"/pic/enc/{encode(link, safe=true)}"
  else:
    &"/pic/{encodeUrl(link)}"

proc getOrigPicUrl*(link: string): string =
  if link.len == 0: return
  if base64Media:
    &"/pic/orig/enc/{encode(link, safe=true)}"
  else:
    &"/pic/orig/{encodeUrl(link)}"

proc filterParams*(params: Table): seq[(string, string)] =
  for p in params.pairs():
    if p[1].len > 0 and p[0] notin nitterParams:
      result.add p

proc isTwitterUrl*(uri: Uri): bool =
  uri.scheme in ["http", "https"] and
    (uri.hostname in twitterDomains or uri.hostname.endsWith(".video.pscp.tv"))

proc isTwitterUrl*(url: string): bool =
  isTwitterUrl(parseUri(url))

proc validateNumber*(value: string): string =
  if value.anyIt(not it.isDigit):
    return ""
  return value



================================================
FILE: src/experimental/parser.nim
================================================
import parser/[user, graphql, article]
export user, graphql, article



================================================
FILE: src/experimental/parser/article.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import std/[strutils, tables, times, options]
import jsony
import utils, graphql, ../types/article
from ../../types import Article, ArticleParagraph, ArticleEntity, ArticleMedia,
                        User, TweetStats

proc parseGraphArticle*(json: string): Article =
  if json.len == 0 or json[0] != '{':
    return

  var raw: GraphArticle
  try:
    raw = json.fromJson(GraphArticle)
  except CatchableError:
    return

  let
    tweet = raw.data.tweetResult.result
    article = tweet.article.articleResults.result

  if article.title.len == 0:
    return

  let publishedAt = article.metadata.firstPublishedAtSecs
  var articleTime: DateTime
  if publishedAt > 0:
    articleTime = publishedAt.int64.fromUnix.utc
  elif tweet.legacy.createdAt.len > 0:
    articleTime = parseTwitterDate(tweet.legacy.createdAt)

  result = Article(
    title: article.title,
    coverImage: getImageUrl(article.coverMedia.mediaInfo.originalImgUrl),
    time: articleTime,
    user: parseUserResult(tweet.core.userResults.result),
  )

  result.stats = TweetStats(
    replies: tweet.legacy.replyCount,
    retweets: tweet.legacy.retweetCount,
    likes: tweet.legacy.favoriteCount,
  )
  if tweet.views.count.len > 0:
    try: result.stats.views = parseInt(tweet.views.count)
    except ValueError: discard

  for blk in article.contentState.blocks:
    result.paragraphs.add ArticleParagraph(
      text: blk.text,
      kind: blk.blockKind,
      inlineStyles: blk.inlineStyleRanges,
      entityRanges: blk.entityRanges,
    )

  for entry in article.contentState.entityMap:
    let key = try: parseInt(entry.key) except ValueError: continue
    var entity = ArticleEntity(kind: entry.value.entityKind)
    case entity.kind
    of "LINK": entity.url = entry.value.data.url
    of "MEDIA":
      for mi in entry.value.data.mediaItems:
        entity.mediaIds.add mi.mediaId
    of "TWEET": entity.tweetId = entry.value.data.tweetId
    of "MARKDOWN": entity.markdown = entry.value.data.markdown
    else: discard
    result.entities[key] = entity

  for me in article.mediaEntities:
    let typeName = me.mediaInfo.typeName
    var media = ArticleMedia(kind: typeName)
    if me.mediaInfo.videoInfo.isSome:
      let variants = me.mediaInfo.videoInfo.get.variants
      case typeName
      of "ApiGif":
        if variants.len > 0:
          media.url = variants[0].url
      of "ApiVideo":
        var bestBitrate = -1
        for v in variants:
          if v.bitrate > bestBitrate:
            bestBitrate = v.bitrate
            media.url = v.url
      else: discard
    elif typeName == "ApiImage":
      media.url = getImageUrl(me.mediaInfo.originalImgUrl)
    result.media[me.mediaId] = media



================================================
FILE: src/experimental/parser/graphql.nim
================================================
import options, strutils
import jsony
import user, utils, ../types/[graphuser, graphlistmembers, graphfollowers]
from ../../types import User, VerifiedType, Result, Query, QueryKind

proc parseUserResult*(userResult: UserResult): User =
  result = userResult.legacy

  if result.verifiedType == none and userResult.isBlueVerified:
    result.verifiedType = blue

  if result.username.len == 0 and userResult.core.screenName.len > 0:
    result.id = userResult.restId
    result.username = userResult.core.screenName
    result.fullname = userResult.core.name
    result.userPic = userResult.avatar.imageUrl.replace("_normal", "")

    if userResult.privacy.isSome:
      result.protected = userResult.privacy.get.protected

    if userResult.location.isSome:
      result.location = userResult.location.get.location

    if userResult.core.createdAt.len > 0:
      result.joinDate = parseTwitterDate(userResult.core.createdAt)

    if userResult.verification.isSome:
      let v = userResult.verification.get
      if v.verifiedType != VerifiedType.none:
        result.verifiedType = v.verifiedType

    if userResult.profileBio.isSome and result.bio.len == 0:
      result.bio = userResult.profileBio.get.description

proc parseGraphUser*(json: string): User =
  if json.len == 0 or json[0] != '{':
    return

  let 
    raw = json.fromJson(GraphUser)
    userResult = 
      if raw.data.userResult.isSome: raw.data.userResult.get.result
      elif raw.data.user.isSome: raw.data.user.get.result
      else: UserResult()

  if userResult.unavailableReason.get("") == "Suspended" or
     userResult.reason.get("") == "Suspended":
    return User(suspended: true)

  result = parseUserResult(userResult)

proc parseGraphListMembers*(json, cursor: string): Result[User] =
  result = Result[User](
    beginning: cursor.len == 0,
    query: Query(kind: userList)
  )

  let raw = json.fromJson(GraphListMembers)
  for instruction in raw.data.list.membersTimeline.timeline.instructions:
    if instruction.kind == "TimelineAddEntries":
      for entry in instruction.entries:
        case entry.content.entryType
        of TimelineTimelineItem:
          let userResult = entry.content.itemContent.userResults.result
          if userResult.restId.len > 0:
            result.content.add parseUserResult(userResult)
        of TimelineTimelineCursor:
          if entry.content.cursorType == "Bottom":
            result.bottom = entry.content.value

proc parseGraphFollowers*(json, cursor: string; kind: QueryKind): Result[User] =
  result = Result[User](
    beginning: cursor.len == 0,
    query: Query(kind: kind)
  )

  if json.len == 0 or json[0] != '{':
    return

  let raw = json.fromJson(GraphFollowers)
  for instruction in raw.data.user.result.timeline.timeline.instructions:
    if instruction.kind == "TimelineAddEntries":
      for entry in instruction.entries:
        case entry.content.entryType
        of TimelineTimelineItem:
          let userResult = entry.content.itemContent.userResults.result
          if userResult.restId.len > 0:
            result.content.add parseUserResult(userResult)
        of TimelineTimelineCursor:
          if entry.content.cursorType == "Bottom":
            result.bottom = entry.content.value



================================================
FILE: src/experimental/parser/session.nim
================================================
import std/strutils
import jsony
import ../types/session
from ../../types import Session, SessionKind

proc parseSession*(raw: string): Session =
  let session = raw.fromJson(RawSession)
  let kind = if session.kind == "": "oauth" else: session.kind

  case kind
  of "oauth":
    let id = session.oauthToken[0 ..< session.oauthToken.find('-')]
    result = Session(
      kind: SessionKind.oauth,
      id: parseBiggestInt(id),
      username: session.username,
      oauthToken: session.oauthToken,
      oauthSecret: session.oauthTokenSecret
    )
  of "cookie":
    let id = if session.id.len > 0: parseBiggestInt(session.id) else: 0
    result = Session(
      kind: SessionKind.cookie,
      id: id,
      username: session.username,
      authToken: session.authToken,
      ct0: session.ct0
    )
  else:
    raise newException(ValueError, "Unknown session kind: " & kind)



================================================
FILE: src/experimental/parser/slices.nim
================================================
import std/[macros, htmlgen, unicode]
import ../types/common
import ".."/../[formatters, utils]

type
  ReplaceSliceKind = enum
    rkRemove, rkUrl, rkHashtag, rkMention

  ReplaceSlice* = object
    slice: Slice[int]
    kind: ReplaceSliceKind
    url, display: string

proc cmp*(x, y: ReplaceSlice): int = cmp(x.slice.a, y.slice.b)

proc dedupSlices*(s: var seq[ReplaceSlice]) =
  var
    len = s.len
    i = 0
  while i < len:
    var j = i + 1
    while j < len:
      if s[i].slice.a == s[j].slice.a:
        s.del j
        dec len
      else:
        inc j
    inc i

proc extractUrls*(result: var seq[ReplaceSlice]; url: Url;
                  textLen: int; hideTwitter = false) =
  let
    link = url.expandedUrl
    slice = url.indices[0] ..< url.indices[1]

  if hideTwitter and slice.b.succ >= textLen and link.isTwitterUrl:
    if slice.a < textLen:
      result.add ReplaceSlice(kind: rkRemove, slice: slice)
  else:
    result.add ReplaceSlice(kind: rkUrl, url: link,
                            display: link.shortLink, slice: slice)

proc replacedWith*(runes: seq[Rune]; repls: openArray[ReplaceSlice];
                   textSlice: Slice[int]): string =
  template extractLowerBound(i: int; idx): int =
    if i > 0: repls[idx].slice.b.succ else: textSlice.a

  result = newStringOfCap(runes.len)

  for i, rep in repls:
    result.add $runes[extractLowerBound(i, i - 1) ..< rep.slice.a]
    case rep.kind
    of rkHashtag:
      let
        name = $runes[rep.slice.a.succ .. rep.slice.b]
        symbol = $runes[rep.slice.a]
      result.add a(symbol & name, href = "/search?f=tweets&q=%23" & name)
    of rkMention:
      result.add a($runes[rep.slice], href = rep.url, title = rep.display)
    of rkUrl:
      result.add a(rep.display, href = rep.url)
    of rkRemove:
      discard

  let rest = extractLowerBound(repls.len, ^1) ..< textSlice.b
  if rest.a <= rest.b:
    result.add $runes[rest]



================================================
FILE: src/experimental/parser/tid.nim
================================================
import jsony
import ../types/tid
export TidPair

proc parseTidPairs*(raw: string): seq[TidPair] =
  result = raw.fromJson(seq[TidPair])
  if result.len == 0:
    raise newException(ValueError, "Parsing pairs failed: " & raw)



================================================
FILE: src/experimental/parser/unifiedcard.nim
================================================
import std/[options, tables, strutils, strformat, sugar]
import jsony
import user, ../types/unifiedcard
import ../../formatters
from ../../types import Card, CardKind, Video
from ../../utils import twimg, https

proc getImageUrl(entity: MediaEntity): string =
  entity.mediaUrlHttps.dup(removePrefix(twimg), removePrefix(https))

proc parseDestination(id: string; card: UnifiedCard; result: var Card) =
  let destination = card.destinationObjects[id].data
  result.dest = destination.urlData.vanity
  result.url = destination.urlData.url

proc parseDetails(data: ComponentData; card: UnifiedCard; result: var Card) =
  data.destination.parseDestination(card, result)

  result.text = data.title
  if result.text.len == 0:
    result.text = data.name

proc parseMediaDetails(data: ComponentData; card: UnifiedCard; result: var Card) =
  data.destination.parseDestination(card, result)

  result.kind = summary
  result.image = card.mediaEntities[data.mediaId].getImageUrl
  result.text = data.topicDetail.title
  result.dest = "Topic"

proc parseJobDetails(data: ComponentData; card: UnifiedCard; result: var Card) =
  data.destination.parseDestination(card, result)

  result.kind = CardKind.jobDetails
  result.title = data.title
  result.text = data.shortDescriptionText
  result.dest = &"@{data.profileUser.username} · {data.location}"

proc parseAppDetails(data: ComponentData; card: UnifiedCard; result: var Card) =
  let app = card.appStoreData[data.appId][0]

  case app.kind
  of androidApp:
    result.url = "http://play.google.com/store/apps/details?id=" & app.id
  of iPhoneApp, iPadApp:
    result.url = "https://itunes.apple.com/app/id" & app.id

  result.text = app.title
  result.dest = app.category

proc parseListDetails(data: ComponentData; result: var Card) =
  result.dest = &"List · {data.memberCount} Members"

proc parseCommunityDetails(data: ComponentData; result: var Card) =
  result.dest = &"Community · {data.memberCount} Members"

proc parseMedia(component: Component; card: UnifiedCard; result: var Card) =
  let mediaId =
    if component.kind == swipeableMedia:
      component.data.mediaList[0].id
    else:
      component.data.id

  let rMedia = card.mediaEntities[mediaId]
  case rMedia.kind:
  of photo:
    result.kind = summaryLarge
    result.image = rMedia.getImageUrl
  of video:
    let videoInfo = rMedia.videoInfo.get
    result.kind = promoVideo
    result.video = some Video(
      available: true,
      thumb: rMedia.getImageUrl,
      durationMs: videoInfo.durationMillis,
      variants: videoInfo.variants
    )
  of model3d:
    result.title = "Unsupported 3D model ad"

proc parseGrokShare(data: ComponentData; card: UnifiedCard; result: var Card) =
  result.kind = summaryLarge

  data.destination.parseDestination(card, result)
  result.dest = "Answer by Grok"

  for msg in data.conversationPreview:
    if msg.sender == "USER":
      result.title = msg.message.shorten(70)
    elif msg.sender == "AGENT":
      result.text = msg.message.shorten(500)

proc parseUnifiedCard*(json: string): Card =
  let card = json.fromJson(UnifiedCard)

  for component in card.componentObjects.values:
    case component.kind
    of details, communityDetails, twitterListDetails:
      component.data.parseDetails(card, result)
    of appStoreDetails:
      component.data.parseAppDetails(card, result)
    of mediaWithDetailsHorizontal:
      component.data.parseMediaDetails(card, result)
    of media, swipeableMedia:
      component.parseMedia(card, result)
    of buttonGroup:
      discard
    of grokShare:
      component.data.parseGrokShare(card, result)
    of ComponentType.jobDetails:
      component.data.parseJobDetails(card, result)
    of ComponentType.hidden:
      result.kind = CardKind.hidden
    of ComponentType.unknown:
      echo "ERROR: Unknown component type: ", json

    case component.kind
    of twitterListDetails:
      component.data.parseListDetails(result)
    of communityDetails:
      component.data.parseCommunityDetails(result)
    else: discard



================================================
FILE: src/experimental/parser/user.nim
================================================
import std/[algorithm, unicode, re, strutils, strformat, options, nre]
import jsony
import utils, slices
import ../types/user as userType
from ../../types import Result, User, Error

let
  unRegex = re.re"(^|[^A-z0-9-_./?])@([A-z0-9_]{1,15})"
  unReplace = "$1<a href=\"/$2\">@$2</a>"

  htRegex = nre.re"""(*U)(^|[^\w-_.?])([#＃$])([\w_]*+)(?!</a>|">|#)"""
  htReplace = "$1<a href=\"/search?f=tweets&q=%23$3\">$2$3</a>"

proc expandUserEntities(user: var User; raw: RawUser) =
  let
    orig = user.bio.toRunes
    ent = raw.entities

  if ent.url.urls.len > 0:
    user.website = ent.url.urls[0].expandedUrl

  var replacements = newSeq[ReplaceSlice]()

  for u in ent.description.urls:
    replacements.extractUrls(u, orig.high)

  replacements.dedupSlices
  replacements.sort(cmp)

  user.bio = orig.replacedWith(replacements, 0 .. orig.len)
                 .replacef(unRegex, unReplace)
                 .replace(htRegex, htReplace)

proc getBanner(user: RawUser): string =
  if user.profileBannerUrl.len > 0:
    return user.profileBannerUrl & "/1500x500"

  if user.profileLinkColor.len > 0:
    return '#' & user.profileLinkColor

  if user.profileImageExtensions.isSome:
    let ext = get(user.profileImageExtensions)
    if ext.mediaColor.r.ok.palette.len > 0:
      let color = ext.mediaColor.r.ok.palette[0].rgb
      return &"#{color.red:02x}{color.green:02x}{color.blue:02x}"

proc toUser*(raw: RawUser): User =
  result = User(
    id: raw.idStr,
    username: raw.screenName,
    fullname: raw.name,
    location: raw.location,
    bio: raw.description,
    following: raw.friendsCount,
    followers: raw.followersCount,
    tweets: raw.statusesCount,
    likes: raw.favouritesCount,
    media: raw.mediaCount,
    verifiedType: raw.verifiedType,
    protected: raw.protected,
    banner: getBanner(raw),
    userPic: getImageUrl(raw.profileImageUrlHttps).replace("_normal", "")
  )

  if raw.createdAt.len > 0:
    result.joinDate = parseTwitterDate(raw.createdAt)

  if raw.pinnedTweetIdsStr.len > 0:
    result.pinnedTweet = parseBiggestInt(raw.pinnedTweetIdsStr[0])

  result.expandUserEntities(raw)

proc parseHook*(s: string; i: var int; v: var User) =
  var u: RawUser
  parseHook(s, i, u)
  v = toUser u



================================================
FILE: src/experimental/parser/utils.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import std/[sugar, strutils, times]
import ../types/common
import ../../utils as uutils

template parseTime(time: string; f: static string; flen: int): DateTime =
  if time.len != flen: return
  parse(time, f, utc())

proc parseIsoDate*(date: string): DateTime =
  date.parseTime("yyyy-MM-dd\'T\'HH:mm:ss\'Z\'", 20)

proc parseTwitterDate*(date: string): DateTime =
  date.parseTime("ddd MMM dd hh:mm:ss \'+0000\' yyyy", 30)

proc getImageUrl*(url: string): string =
  url.dup(removePrefix(twimg), removePrefix(https))

template handleErrors*(body) =
  if json.startsWith("{\"errors"):
    for error {.inject.} in json.fromJson(Errors).errors:
      body



================================================
FILE: src/experimental/types/article.nim
================================================
import std/options
import graphuser
from ../../types import ArticleStyle, ArticleEntityRange

type
  GraphArticle* = object
    data*: tuple[tweetResult: tuple[result: TweetResultNode]]

  TweetResultNode* = object
    article*: tuple[articleResults: tuple[result: ArticleResultNode]]
    legacy*: TweetLegacy
    core*: tuple[userResults: UserData]
    views*: tuple[count: string]

  TweetLegacy* = object
    createdAt*: string
    replyCount*: int
    retweetCount*: int
    favoriteCount*: int

  ArticleResultNode* = object
    title*: string
    coverMedia*: tuple[mediaInfo: MediaInfoNode]
    contentState*: ContentState
    metadata*: tuple[firstPublishedAtSecs: int]
    mediaEntities*: seq[RawMediaEntity]

  ContentState* = object
    blocks*: seq[ContentBlock]
    entityMap*: seq[EntityMapEntry]

  ContentBlock* = object
    text*: string
    blockKind*: string
    inlineStyleRanges*: seq[ArticleStyle]
    entityRanges*: seq[ArticleEntityRange]

  EntityMapEntry* = object
    key*: string
    value*: EntityMapValue

  EntityMapValue* = object
    entityKind*: string
    data*: EntityDataNode

  EntityDataNode* = object
    url*: string
    mediaItems*: seq[tuple[mediaId: string]]
    tweetId*: string
    markdown*: string

  RawMediaEntity* = object
    mediaId*: string
    mediaInfo*: MediaInfoNode

  MediaInfoNode* = object
    typeName*: string
    originalImgUrl*: string
    videoInfo*: Option[VideoInfoNode]

  VideoInfoNode* = object
    variants*: seq[VideoVariant]

  VideoVariant* = object
    url*: string
    bitrate*: int

proc renameHook*(v: var ContentBlock; fieldName: var string) =
  if fieldName == "type":
    fieldName = "blockKind"

proc renameHook*(v: var EntityMapValue; fieldName: var string) =
  if fieldName == "type":
    fieldName = "entityKind"

proc renameHook*(v: var MediaInfoNode; fieldName: var string) =
  if fieldName == "__typename":
    fieldName = "typeName"



================================================
FILE: src/experimental/types/common.nim
================================================
from ../../types import Error

type
  Url* = object
    url*: string
    expandedUrl*: string
    displayUrl*: string
    indices*: array[2, int]

  ErrorObj* = object
    code*: Error
    message*: string

  Errors* = object
    errors*: seq[ErrorObj]

proc contains*(codes: set[Error]; errors: Errors): bool =
  for e in errors.errors:
    if e.code in codes:
      return true



================================================
FILE: src/experimental/types/graphfollowers.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import graphlistmembers

type
  GraphFollowers* = object
    data*: tuple[user: UserWrapper]

  UserWrapper = object
    result*: UserResultWrapper

  UserResultWrapper = object
    timeline*: tuple[timeline: graphlistmembers.Timeline]

# Hook to normalize snake_case field from API to camelCase used by shared types
proc renameHook*(v: var Content; fieldName: var string) =
  if fieldName == "user_results":
    fieldName = "userResults"



================================================
FILE: src/experimental/types/graphlistmembers.nim
================================================
import graphuser

type
  GraphListMembers* = object
    data*: tuple[list: List]

  List = object
    membersTimeline*: tuple[timeline: Timeline]

  Timeline* = object
    instructions*: seq[Instruction]

  Instruction* = object
    kind*: string
    entries*: seq[tuple[content: Content]]

  ContentEntryType* = enum
    TimelineTimelineItem
    TimelineTimelineCursor

  Content* = object
    case entryType*: ContentEntryType
    of TimelineTimelineItem:
      itemContent*: tuple[userResults: UserData]
    of TimelineTimelineCursor:
      value*: string
      cursorType*: string

proc renameHook*(v: var Instruction; fieldName: var string) =
  if fieldName == "type":
    fieldName = "kind"



================================================
FILE: src/experimental/types/graphuser.nim
================================================
import options, strutils
from ../../types import User, VerifiedType

type
  GraphUser* = object
    data*: tuple[userResult: Option[UserData], user: Option[UserData]]

  UserData* = object
    result*: UserResult

  UserCore* = object
    name*: string
    screenName*: string
    createdAt*: string

  UserBio* = object
    description*: string

  UserAvatar* = object
    imageUrl*: string

  Verification* = object
    verifiedType*: VerifiedType

  Location* = object
    location*: string

  Privacy* = object
    protected*: bool

  UserResult* = object
    legacy*: User
    restId*: string
    isBlueVerified*: bool
    core*: UserCore
    avatar*: UserAvatar
    unavailableReason*: Option[string]
    reason*: Option[string]
    privacy*: Option[Privacy]
    profileBio*: Option[UserBio]
    verification*: Option[Verification]
    location*: Option[Location]

proc enumHook*(s: string; v: var VerifiedType) =
  v = try:
    parseEnum[VerifiedType](s)
  except:
    VerifiedType.none



================================================
FILE: src/experimental/types/session.nim
================================================
type
  RawSession* = object
    kind*: string
    id*: string
    username*: string
    oauthToken*: string
    oauthTokenSecret*: string
    authToken*: string
    ct0*: string



================================================
FILE: src/experimental/types/tid.nim
================================================
type
  TidPair* = object
    animationKey*: string
    verification*: string



================================================
FILE: src/experimental/types/unifiedcard.nim
================================================
import std/[options, tables, times]
import jsony
from ../../types import VideoType, VideoVariant, User

type
  Text* = distinct string

  UnifiedCard* = object
    componentObjects*: Table[string, Component]
    destinationObjects*: Table[string, Destination]
    mediaEntities*: Table[string, MediaEntity]
    appStoreData*: Table[string, seq[AppStoreData]]

  ComponentType* = enum
    details
    media
    swipeableMedia
    buttonGroup
    jobDetails
    appStoreDetails
    twitterListDetails
    communityDetails
    mediaWithDetailsHorizontal
    hidden
    grokShare
    unknown

  Component* = object
    kind*: ComponentType
    data*: ComponentData

  ComponentData* = object
    id*: string
    appId*: string
    mediaId*: string
    destination*: string
    location*: string
    title*: Text
    subtitle*: Text
    name*: Text
    memberCount*: int
    mediaList*: seq[MediaItem]
    topicDetail*: tuple[title: Text]
    profileUser*: User
    shortDescriptionText*: string
    conversationPreview*: seq[GrokConversation]

  MediaItem* = object
    id*: string
    destination*: string

  Destination* = object
    kind*: string
    data*: tuple[urlData: UrlData]

  UrlData* = object
    url*: string
    vanity*: string

  MediaType* = enum
    photo, video, model3d

  MediaEntity* = object
    kind*: MediaType
    mediaUrlHttps*: string
    videoInfo*: Option[VideoInfo]

  VideoInfo* = object
    durationMillis*: int
    variants*: seq[VideoVariant]

  AppType* = enum
    androidApp, iPhoneApp, iPadApp

  AppStoreData* = object
    kind*: AppType
    id*: string
    title*: Text
    category*: Text

  GrokConversation* = object
    message*: string
    sender*: string

  TypeField = Component | Destination | MediaEntity | AppStoreData

converter fromText*(text: Text): string = string(text)

proc renameHook*(v: var TypeField; fieldName: var string) =
  if fieldName == "type":
    fieldName = "kind"

proc enumHook*(s: string; v: var ComponentType) =
  v = case s
      of "details": details
      of "media": media
      of "swipeable_media": swipeableMedia
      of "button_group": buttonGroup
      of "job_details": jobDetails
      of "app_store_details": appStoreDetails
      of "twitter_list_details": twitterListDetails
      of "community_details": communityDetails
      of "media_with_details_horizontal": mediaWithDetailsHorizontal
      of "commerce_drop_details": hidden
      of "grok_share": grokShare
      else: echo "ERROR: Unknown enum value (ComponentType): ", s; unknown

proc enumHook*(s: string; v: var AppType) =
  v = case s
      of "android_app": androidApp
      of "iphone_app": iPhoneApp
      of "ipad_app": iPadApp
      else: echo "ERROR: Unknown enum value (AppType): ", s; androidApp

proc enumHook*(s: string; v: var MediaType) =
  v = case s
      of "video": video
      of "photo": photo
      of "model3d": model3d
      else: echo "ERROR: Unknown enum value (MediaType): ", s; photo

proc parseHook*(s: string; i: var int; v: var DateTime) =
  var str: string
  parseHook(s, i, str)
  v = parse(str, "yyyy-MM-dd hh:mm:ss")

proc parseHook*(s: string; i: var int; v: var Text) =
  if s[i] == '"':
    var str: string
    parseHook(s, i, str)
    v = Text(str)
  else:
    var t: tuple[content: string]
    parseHook(s, i, t)
    v = Text(t.content)



================================================
FILE: src/experimental/types/user.nim
================================================
import options
import common
from ../../types import VerifiedType

type
  RawUser* = object
    idStr*: string
    name*: string
    screenName*: string
    location*: string
    description*: string
    entities*: Entities
    createdAt*: string
    followersCount*: int
    friendsCount*: int
    favouritesCount*: int
    statusesCount*: int
    mediaCount*: int
    verifiedType*: VerifiedType
    protected*: bool
    profileLinkColor*: string
    profileBannerUrl*: string
    profileImageUrlHttps*: string
    profileImageExtensions*: Option[ImageExtensions]
    pinnedTweetIdsStr*: seq[string]

  Entities* = object
    url*: Urls
    description*: Urls

  Urls* = object
    urls*: seq[Url]

  ImageExtensions = object
    mediaColor*: tuple[r: Ok]

  Ok = object
    ok*: Palette

  Palette = object
    palette*: seq[tuple[rgb: Color]]

  Color* = object
    red*, green*, blue*: int



================================================
FILE: src/routes/article.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, tables, strutils
import jester, karax/vdom
import ".."/[types, api]
import ../views/[article, general]
import router_utils

export api, article, vdom, general, router_utils

proc createArticleRouter*(cfg: Config) =
  router articleRoute:
    get "/i/article/@id":
      cond @"id".allCharsInSet(Digits)

      let article = await getGraphArticle(@"id")
      if article == nil:
        resp Http404, showError("Article not found", cfg)

      var tweetIds: seq[string]
      for e in article.entities.values:
        if e.kind == "TWEET":
          tweetIds.add e.tweetId

      var tweets = initTable[int64, Tweet]()
      if tweetIds.len > 0:
        try:
          for t in await getGraphTweetResults(tweetIds):
            tweets[t.id] = t
        except CatchableError:
          discard

      let
        prefs = requestPrefs()
        path = getPath()
        html = renderArticle(article, tweets, path, prefs, @"id")
        twitterUrl = "https://x.com/" & article.user.username & "/article/" & @"id"
      resp renderMain(html, request, cfg, prefs, titleText=article.title,
                      twitterLink=twitterUrl)

    get "/@name/article/@id/?":
      cond '.' notin @"name"
      cond @"id".allCharsInSet(Digits)
      redirect("/i/article/" & @"id")

    get "/@name/status/@id/article":
      cond '.' notin @"name"
      cond @"id".allCharsInSet(Digits)
      redirect("/i/article/" & @"id")



================================================
FILE: src/routes/broadcast.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, strutils
import jester

import router_utils
import ".."/[types, formatters, redis_cache]
import ../views/[general, broadcast]
import media

export broadcast

proc createBroadcastRouter*(cfg: Config) =
  router broadcastRoute:
    get "/i/broadcasts/@id":
      cond @"id".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9'})
      var bc: Broadcast
      try:
        bc = await getCachedBroadcast(@"id")
      except:
        discard

      if bc.id.len == 0:
        resp Http404, showError("Broadcast not found", cfg)

      let prefs = requestPrefs()
      resp renderMain(renderBroadcast(bc, prefs, request.path), request, cfg, prefs,
                      bc.title, ogTitle=bc.title)

    get "/i/broadcasts/@id/stream":
      cond @"id".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9'})
      var bc: Broadcast
      try:
        bc = await getCachedBroadcast(@"id")
      except:
        discard

      if bc.m3u8Url.len == 0:
        resp Http404

      let manifest = await safeFetch(bc.m3u8Url)
      if manifest.len == 0:
        resp Http502

      resp proxifyVideo(manifest, requestPrefs().proxyVideos, bc.m3u8Url), m3u8Mime



================================================
FILE: src/routes/community.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strformat

import jester

import router_utils
import ".."/[types, redis_cache, api]
import ../views/[general, timeline, community]

export community

template respCommunity*(cmty: Community; title: string; nav, vnode: typed) =
  if cmty.id.len == 0 or cmty.name.len == 0:
    resp Http404, showError(&"""Community "{@"id"}" not found""", cfg)

  let html = renderCommunity(vnode, nav, cmty)
  resp renderMain(html, request, cfg, prefs, titleText=title, banner=cmty.banner)

proc createCommunityRouter*(cfg: Config) =
  router community:
    get "/i/communities/@id/?":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        tl = await getGraphCommunityTweets(cmty.id, "Relevance", getCursor())
      respCommunity(cmty, cmty.name,
                     renderCommunityTabs(QueryKind.posts, cmty),
                     renderTimelineTweets(tl, prefs, request.path))

    get "/i/communities/@id/latest":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        tl = await getGraphCommunityTweets(cmty.id, "Recency", getCursor())
      respCommunity(cmty, cmty.name & " - Latest",
                     renderCommunityTabs(QueryKind.replies, cmty),
                     renderTimelineTweets(tl, prefs, request.path))

    get "/i/communities/@id/media":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        tl = await getGraphCommunityMedia(cmty.id, getCursor())
      respCommunity(cmty, cmty.name & " - Media",
                     renderCommunityTabs(QueryKind.media, cmty),
                     renderTimelineTweets(tl, prefs, request.path))

    get "/i/communities/@id/about":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        mods = await getCachedCommunityModerators(cmty.id)
      respCommunity(cmty, cmty.name & " - About",
                     renderCommunityTabs(QueryKind.userList, cmty),
                     renderCommunityAbout(cmty, mods))

    get "/i/communities/@id/members":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        members = await getGraphCommunityMembers(cmty.id, getCursor())
      respCommunity(cmty, cmty.name & " - Members",
                     renderMemberTabs(cmty, false),
                     renderTimelineUsers(members, prefs, request.path))

    get "/i/communities/@id/moderators":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        mods = await getCachedCommunityModerators(cmty.id)
      respCommunity(cmty, cmty.name & " - Moderators",
                     renderMemberTabs(cmty, true),
                     renderTimelineUsers(Result[User](content: mods), prefs, request.path))

    get "/i/communities/@id/hashtag/@tag":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        cmty = await getCachedCommunity(@"id")
        tl = await getGraphCommunityHashtags(cmty.id, @"tag", getCursor())
      respCommunity(cmty, cmty.name & " - #" & @"tag",
                     renderHashtagHeader(cmty, @"tag"),
                     renderTimelineTweets(tl, prefs, request.path))



================================================
FILE: src/routes/debug.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import jester
import router_utils
import ".."/[auth, types]

proc createDebugRouter*(cfg: Config) =
  router debug:
    get "/.health":
      respJson getSessionPoolHealth()

    get "/.sessions":
      cond cfg.enableDebug
      respJson getSessionPoolDebug()



================================================
FILE: src/routes/embed.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, strutils, strformat, options
import jester, karax/vdom
import ".."/[types, api]
import ../views/[embed, tweet, general]
import router_utils

export api, embed, vdom, tweet, general, router_utils

proc createEmbedRouter*(cfg: Config) =
  router embed:
    get "/i/videos/tweet/@id":
      let tweet = await getGraphTweetResult(@"id")
      if tweet == nil or not tweet.hasVideos:
        resp Http404

      resp renderVideoEmbed(tweet, cfg, request)

    get "/@user/status/@id/embed":
      let
        tweet = await getGraphTweetResult(@"id")
        prefs = requestPrefs()
        path = getPath()

      if tweet == nil:
        resp Http404

      resp renderTweetEmbed(tweet, path, prefs, cfg, request)

    get "/embed/Tweet.html":
      let id = @"id"

      if id.len > 0:
        redirect(&"/i/status/{id}/embed")
      else:
        resp Http404



================================================
FILE: src/routes/list.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, uri

import jester

import router_utils
import ".."/[types, redis_cache, api]
import ../views/[general, timeline, list]

template respList*(list, timeline, title, vnode: typed) =
  if list.id.len == 0 or list.name.len == 0:
    resp Http404, showError(&"""List "{@"id"}" not found""", cfg)

  let
    html = renderList(vnode, timeline.query, list)
    rss = if cfg.enableRSSList: &"""/i/lists/{@"id"}/rss""" else: ""

  resp renderMain(html, request, cfg, prefs, titleText=title, rss=rss, banner=list.banner)

proc title*(list: List): string =
  &"@{list.username}/{list.name}"

proc createListRouter*(cfg: Config) =
  router list:
    get "/@name/lists/@slug/?":
      cond '.' notin @"name"
      cond @"name" != "i"
      cond @"slug" != "memberships"
      let
        slug = decodeUrl(@"slug")
        list = await getCachedList(@"name", slug)
      if list.id.len == 0:
        resp Http404, showError(&"""List "{@"slug"}" not found""", cfg)
      redirect(&"/i/lists/{list.id}")

    get "/i/lists/@id/?":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        list = await getCachedList(id=(@"id"))
        timeline = await getGraphListTweets(list.id, getCursor())
        vnode = renderTimelineTweets(timeline, prefs, request.path)
      respList(list, timeline, list.title, vnode)

    get "/i/lists/@id/members":
      cond '.' notin @"id"
      let
        prefs = requestPrefs()
        list = await getCachedList(id=(@"id"))
        members = await getGraphListMembers(list, getCursor())
      respList(list, members, list.title, renderTimelineUsers(members, prefs, request.path))



================================================
FILE: src/routes/media.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import uri, strutils, httpclient, os, hashes, base64, re
import asynchttpserver, asyncstreams, asyncfile, asyncnet
import asyncdispatch

import jester

import router_utils
import ".."/[types, formatters, utils]

export asynchttpserver, asyncstreams, asyncfile, asyncnet
export httpclient, os, strutils, asyncstreams, base64, re

const
  m3u8Mime* = "application/vnd.apple.mpegurl"
  maxAge* = "max-age=604800"

proc safeFetch*(url: string): Future[string] {.async.} =
  # maxRedirects=0: the caller already validated the host, so never follow a
  # redirect off the allowlisted host (would re-open the #1411 SSRF).
  let client = newAsyncHttpClient(maxRedirects = 0)
  try: result = await client.getContent(url)
  except: discard
  finally: client.close()

template respond*(req: asynchttpserver.Request; headers) =
  var msg = "HTTP/1.1 200 OK\c\L"
  for k, v in headers:
    msg.add(k & ": " & v & "\c\L")

  msg.add "\c\L"
  yield req.client.send(msg)

proc proxyMedia*(req: jester.Request; url: string): Future[HttpCode] {.async.} =
  result = Http200
  let request = req.getNativeReq()
  var fetchUrl = url

  for attempt in 0 .. 2:
    let client = newAsyncHttpClient(maxRedirects = 0)
    var shouldRetry = false
    try:
      let resFut = client.get(fetchUrl)
      let completed = await withTimeout(resFut, 5000)
      if not completed:
        if attempt < 2:
          echo "[media] Retry $1/2, timeout after 5s, url: $2" % [$(attempt + 1), fetchUrl]
          shouldRetry = true
        else:
          echo "[media] Proxying timeout after 5s, url: $1" % [fetchUrl]
          return Http504
      else:
        let res = resFut.read()
        if res.status != "200 OK":
          if res.status == "404 Not Found":
            return Http404
          if res.status.startsWith("30") and res.headers.hasKey("location"):
            let location = res.headers["location", 0]
            if isTwitterUrl(location):
              fetchUrl = location
              shouldRetry = true
              continue
            else:
              return Http403
          if attempt < 2:
            echo "[media] Retry $1/2, status: $2, url: $3" % [$(attempt + 1), res.status, fetchUrl]
            shouldRetry = true
          else:
            echo "[media] Proxying failed, status: $1, url: $2" % [res.status, fetchUrl]
            return Http404
        else:
          let hashed = $hash(url)
          if request.headers.getOrDefault("If-None-Match") == hashed:
            return Http304

          let contentLength =
            if res.headers.hasKey("content-length"):
              res.headers["content-length", 0]
            else:
              ""

          let headers = newHttpHeaders({
            "content-type": res.headers["content-type", 0],
            "content-length": contentLength,
            "cache-control": maxAge,
            "etag": hashed
          })

          respond(request, headers)

          var (hasValue, data) = (true, "")
          while hasValue:
            (hasValue, data) = await res.bodyStream.read()
            if hasValue:
              await request.client.send(data)
          data.setLen 0
          return Http200
    except CatchableError:
      if attempt < 2:
        echo "[media] Retry $1/2, error: $2, url: $3" % [$(attempt + 1), getCurrentExceptionMsg(), fetchUrl]
        shouldRetry = true
      else:
        echo "[media] Proxying exception, error: $1, url: $2" % [getCurrentExceptionMsg(), fetchUrl]
        result = Http404
    finally:
      client.close()
    if not shouldRetry:
      break

template check*(code): untyped =
  if code != Http200:
    resp code
  else:
    enableRawMode()
    break route

proc decoded*(req: jester.Request; index: int): string =
  let
    based = req.matches[0].len > 1
    encoded = req.matches[index]
  if based: decode(encoded)
  else: decodeUrl(encoded)

proc normalizeImgUrl*(url: var string) =
  if not url.startsWith("http"):
    if "twimg.com" notin url:
      url.insert(twimg)
    url.insert(https)

proc createMediaRouter*(cfg: Config) =
  router media:
    get "/pic/?":
      resp Http404

    get re"^\/pic\/orig\/(enc)?\/?(.+)":
      var url = decoded(request, 1)
      cond "/amplify_video/" notin url
      normalizeImgUrl(url)
      url.add("?name=orig")

      let uri = parseUri(url)
      cond isTwitterUrl(uri) == true

      let code = await proxyMedia(request, url)
      check code

    get re"^\/pic\/(enc)?\/?(.+)":
      var url = decoded(request, 1)
      cond "/amplify_video/" notin url
      normalizeImgUrl(url)

      let uri = parseUri(url)
      cond isTwitterUrl(uri) == true

      let code = await proxyMedia(request, url)
      check code

    get re"^\/video\/(enc)?\/?(.+)\/(.+)$":
      let url = decoded(request, 2)
      cond isTwitterUrl(url)

      if getHmac(url) != request.matches[1]:
        resp Http403, showError("Failed to verify signature", cfg)

      if ".mp4" in url or ".ts" in url or ".m4s" in url or ".aac" in url:
        let code = await proxyMedia(request, url)
        check code

      var content: string
      if ".vmap" in url:
        let m3u8 = getM3u8Url(await safeFetch(url))
        if m3u8.len > 0:
          content = await safeFetch(url)
        else:
          resp Http404

      if ".m3u8" in url:
        let vid = await safeFetch(url)
        content = proxifyVideo(vid, requestPrefs().proxyVideos, url)

      resp content, m3u8Mime



================================================
FILE: src/routes/preferences.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, uri, os, algorithm

import jester

import router_utils
import ".."/[types, formatters]
import ../views/[general, preferences]

export preferences

proc findThemes*(dir: string): seq[string] =
  for kind, path in walkDir(dir / "css" / "themes"):
    let theme = path.splitFile.name
    result.add theme.replace("_", " ").titleize
  sort(result)

proc createPrefRouter*(cfg: Config) =
  router preferences:
    get "/settings":
      let
        prefs = requestPrefs()
        prefsCode = encodePrefs(prefs)
        prefsUrl = getUrlPrefix(cfg) & "/?prefs=" & prefsCode
        html = renderPreferences(prefs, refPath(), findThemes(cfg.staticDir), prefsUrl)
      resp renderMain(html, request, cfg, prefs, "Preferences")

    get "/settings/@i?":
      redirect("/settings")

    post "/saveprefs":
      genUpdatePrefs()
      redirect(refPath())

    post "/resetprefs":
      genResetPrefs()
      redirect("/settings?referer=" & encodeUrl(refPath()))

    post "/enablehls":
      savePref("hlsPlayback", "on", request)
      redirect(refPath())

    post "/enablemp4":
      savePref("mp4Playback", "on", request)
      redirect(refPath())



================================================
FILE: src/routes/resolver.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils

import jester

import router_utils
import ".."/[types, api]
import ../views/general

template respResolved*(url, kind: string): untyped =
  let u = url
  if u.len == 0:
    resp showError("Invalid $1 link" % kind, cfg)
  else:
    redirect(u)

proc createResolverRouter*(cfg: Config) =
  router resolver:
    get "/cards/@card/@id":
      let url = "https://cards.twitter.com/cards/$1/$2" % [@"card", @"id"]
      respResolved(await resolve(url, requestPrefs()), "card")

    get "/t.co/@url":
      let url = "https://t.co/" & @"url"
      respResolved(await resolve(url, requestPrefs()), "t.co")



================================================
FILE: src/routes/router_utils.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, sequtils, uri, tables, json
from jester import Request, cookies

import ../views/general
import ".."/[utils, prefs, types]
export utils, prefs, types, uri

template savePref*(pref, value: string; req: Request; expire=false) =
  if not expire or pref in cookies(req):
    let sameSite = if cfg.useHttps: None else: Lax
    setCookie(pref, value, daysForward(when expire: -10 else: 360),
              httpOnly=true, secure=cfg.useHttps, sameSite=sameSite, path="/")

template requestPrefs*(): untyped {.dirty.} =
  getPrefs(cookies(request), params(request))

template showError*(error: string; cfg: Config): string =
  renderMain(renderError(error), request, cfg, requestPrefs(), "Error")

template getPath*(): untyped {.dirty.} =
  $(parseUri(request.path) ? filterParams(request.params))

template refPath*(): untyped {.dirty.} =
  if @"referer".len > 0: @"referer" else: "/"

template getCursor*(): string =
  let cursor = @"cursor"
  decodeUrl(if cursor.len > 0: cursor else: @"max_position", false)

template getCursor*(req: Request): string =
  let cursor = req.params.getOrDefault("cursor")
  decodeUrl(if cursor.len > 0: cursor
            else: req.params.getOrDefault("max_position"), false)

proc getNames*(name: string): seq[string] =
  name.strip(chars={'/'}).split(",").filterIt(it.len > 0)

template applyUrlPrefs*() {.dirty.} =
  if @"prefs".len > 0:
    var prefParams = initTable[string, string]()
    for pair in @"prefs".split(','):
      let kv = pair.split('=', maxsplit=1)
      if kv.len == 2:
        prefParams[kv[0]] = kv[1]
      elif kv.len == 1 and kv[0].len > 0:
        prefParams[kv[0]] = ""
    genApplyPrefs(prefParams, request)

    # Rebuild URL without prefs param
    var params: seq[(string, string)]
    for k, v in request.params:
      if k != "prefs":
        params.add (k, v)

    if params.len > 0:
      let cleanUrl = request.getNativeReq.url ? params
      redirect($cleanUrl)
    else:
      redirect(request.path)

template respJson*(node: JsonNode) =
  resp $node, "application/json"



================================================
FILE: src/routes/rss.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, tables, times, hashes, uri

import jester

import router_utils, timeline
import ../query

include "../views/rss.nimf"

export times, hashes

proc redisKey*(page, name, cursor: string): string =
  result = page & ":" & name
  if cursor.len > 0:
    result &= ":" & cursor

proc timelineRss*(req: Request; cfg: Config; query: Query; prefs: Prefs): Future[Rss] {.async.} =
  var profile: Profile
  let
    name = req.params.getOrDefault("name")
    after = getCursor(req)
    names = getNames(name)

  if names.len == 1:
    profile = await fetchProfile(after, query, skipRail=true)
  else:
    var q = query
    q.fromUser = names
    profile.tweets = await getGraphTweetSearch(q, after)
    # this is kinda dumb
    profile.user = User(
      username: name,
      fullname: names.join(" | "),
      userpic: "https://abs.twimg.com/sticky/default_profile_images/default_profile.png"
    )

  if profile.user.suspended:
    return Rss(feed: profile.user.username, cursor: "suspended")

  if profile.user.fullname.len > 0:
    let rss = renderTimelineRss(profile, cfg, prefs, multi=(names.len > 1))
    return Rss(feed: rss, cursor: profile.tweets.bottom)

template respRss*(rss, page) =
  if rss.cursor.len == 0:
    let info = case page
               of "User": " \"" & @"name" & "\" "
               of "List": " \"" & @"id" & "\" "
               else: " "

    resp Http404, showError(page & info & "not found", cfg)
  elif rss.cursor.len == 9 and rss.cursor == "suspended":
    resp Http404, showError(getSuspended(@"name"), cfg)

  let headers = {"Content-Type": "application/rss+xml; charset=utf-8",
                 "Min-Id": rss.cursor}
  resp Http200, headers, rss.feed

proc createRssRouter*(cfg: Config) =
  router rss:
    get "/search/rss":
      if not cfg.enableRSSSearch:
        resp Http403, showError("RSS feed is disabled", cfg)
      if @"q".len > 200:
        resp Http400, showError("Search input too long.", cfg)

      let
        prefs = requestPrefs()
        query = initQuery(params(request))
      if query.kind != tweets:
        resp Http400, showError("Only Tweet searches are allowed for RSS feeds.", cfg)

      let
        cursor = getCursor()
        key = redisKey("search", $hash(genQueryUrl(query)), cursor)

      var rss = await getCachedRss(key)
      if rss.cursor.len > 0:
        respRss(rss, "Search")

      let tweets = await getGraphTweetSearch(query, cursor)
      rss.cursor = tweets.bottom
      rss.feed = renderSearchRss(tweets.content, query.text, genQueryUrl(query), cfg, prefs)

      await cacheRss(key, rss)
      respRss(rss, "Search")

    get "/@name/rss":
      cond '.' notin @"name"
      if not cfg.enableRSSUserTweets:
        resp Http403, showError("RSS feed is disabled", cfg)
      let
        prefs = requestPrefs()
        name = @"name"
        key = redisKey("twitter", name, getCursor())

      var rss = await getCachedRss(key)
      if rss.cursor.len > 0:
        respRss(rss, "User")

      rss = await timelineRss(request, cfg, Query(fromUser: @[name]), prefs)

      await cacheRss(key, rss)
      respRss(rss, "User")

    get "/@name/@tab/rss":
      cond '.' notin @"name"
      cond @"tab" in ["with_replies", "media", "search"]
      let rssEnabled = case @"tab"
        of "with_replies": cfg.enableRSSUserReplies
        of "media": cfg.enableRSSUserMedia
        of "search": cfg.enableRSSSearch
        else: false
      if not rssEnabled:
        resp Http403, showError("RSS feed is disabled", cfg)
      let
        prefs = requestPrefs()
        name = @"name"
        tab = @"tab"
        query =
          case tab
          of "with_replies": getReplyQuery(name)
          of "media": getMediaQuery(name)
          of "search": initQuery(params(request), name=name)
          else: Query(fromUser: @[name])

      let searchKey = if tab != "search": ""
                      else: ":" & $hash(genQueryUrl(query))

      let key = redisKey(tab, name & searchKey, getCursor())

      var rss = await getCachedRss(key)
      if rss.cursor.len > 0:
        respRss(rss, "User")

      rss = await timelineRss(request, cfg, query, prefs)

      await cacheRss(key, rss)
      respRss(rss, "User")

    get "/@name/lists/@slug/rss":
      cond @"name" != "i"
      if not cfg.enableRSSList:
        resp Http403, showError("RSS feed is disabled", cfg)
      let
        slug = decodeUrl(@"slug")
        list = await getCachedList(@"name", slug)
        cursor = getCursor()

      if list.id.len == 0:
        resp Http404, showError("List \"" & @"slug" & "\" not found", cfg)

      let url = "/i/lists/" & list.id & "/rss"
      if cursor.len > 0:
        redirect(url & "?cursor=" & encodeUrl(cursor, false))
      else:
        redirect(url)

    get "/i/lists/@id/rss":
      if not cfg.enableRSSList:
        resp Http403, showError("RSS feed is disabled", cfg)
      let
        prefs = requestPrefs()
        id = @"id"
        cursor = getCursor()
        key = redisKey("lists", id, cursor)

      var rss = await getCachedRss(key)
      if rss.cursor.len > 0:
        respRss(rss, "List")

      let
        list = await getCachedList(id=id)
        timeline = await getGraphListTweets(list.id, cursor)
      rss.cursor = timeline.bottom
      rss.feed = renderListRss(timeline.content, list, cfg, prefs)

      await cacheRss(key, rss)
      respRss(rss, "List")



================================================
FILE: src/routes/search.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, uri

import jester

import router_utils
import ".."/[query, types, api, formatters]
import ../views/[general, search]

include "../views/opensearch.nimf"

export search

proc createSearchRouter*(cfg: Config) =
  router search:
    get "/search/?":
      let q = @"q"
      if q.len > 500:
        resp Http400, showError("Search input too long.", cfg)

      let
        prefs = requestPrefs()
        query = initQuery(params(request))
        title = "Search" & (if q.len > 0: " (" & q & ")" else: "")

      case query.kind
      of users:
        if "," in q:
          redirect("/" & q)
        var users: Result[User]
        try:
          users = await getGraphUserSearch(query, getCursor())
        except InternalError:
          users = Result[User](beginning: true, query: query)
        resp renderMain(renderUserSearch(users, prefs), request, cfg, prefs, title)
      of tweets:
        let
          tweets = await getGraphTweetSearch(query, getCursor())
          rss = if cfg.enableRSSSearch: "/search/rss?" & genQueryUrl(query) else: ""
        resp renderMain(renderTweetSearch(tweets, prefs, getPath()),
                        request, cfg, prefs, title, rss=rss)
      else:
        resp Http404, showError("Invalid search", cfg)

    get "/hashtag/@hash":
      redirect("/search?f=tweets&q=" & encodeUrl("#" & @"hash"))

    get "/opensearch":
      let
        url = getUrlPrefix(cfg) & "/search?f=tweets&q="
        headers = {"Content-Type": "application/opensearchdescription+xml"}
      resp Http200, headers, generateOpenSearchXML(cfg.title, cfg.hostname, url)



================================================
FILE: src/routes/space.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, strutils
import jester

import router_utils
import ".."/[types, formatters, redis_cache]
import ../views/[general, space]
import media

export space

proc createSpaceRouter*(cfg: Config) =
  router spaceRoute:
    get "/i/spaces/@id":
      cond @"id".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9'})
      let sp = await getCachedAudioSpace(@"id")

      if sp.id.len == 0:
        resp Http404, showError("Space not found", cfg)

      let prefs = requestPrefs()
      resp renderMain(renderSpace(sp, prefs, request.path), request, cfg, prefs,
                      sp.title, ogTitle=sp.title)

    get "/i/spaces/@id/stream":
      cond @"id".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9'})
      let sp = await getCachedAudioSpace(@"id")

      if sp.m3u8Url.len == 0:
        resp Http404

      let manifest = await safeFetch(sp.m3u8Url)
      if manifest.len == 0:
        resp Http502

      resp proxifyVideo(manifest, requestPrefs().proxyVideos, sp.m3u8Url), m3u8Mime



================================================
FILE: src/routes/status.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, strutils, sequtils, uri, options, sugar

import jester, karax/vdom

import router_utils
import ".."/[types, formatters, api]
import ../views/[general, status]

export uri, sequtils, options, sugar
export router_utils
export api, formatters
export status

proc createStatusRouter*(cfg: Config) =
  router status:
    get "/@name/status/@id/?":
      cond '.' notin @"name"
      let id = @"id"

      if id.len > 19 or id.any(c => not c.isDigit):
        resp Http404, showError("Invalid tweet ID", cfg)

      let prefs = requestPrefs()

      # used for the infinite scroll feature
      if @"scroll".len > 0:
        let replies = await getReplies(id, getCursor())
        if replies.content.len == 0:
          resp Http204
        resp $renderReplies(replies, prefs, getPath())

      let conv = await getTweet(id, getCursor())

      if conv == nil or conv.tweet == nil or conv.tweet.id == 0:
        var error = "Tweet not found"
        if conv != nil and conv.tweet != nil and conv.tweet.tombstone.len > 0:
          error = conv.tweet.tombstone
        resp Http404, showError(error, cfg)

      let
        title = pageTitle(conv.tweet)
        ogTitle = pageTitle(conv.tweet.user)
        desc = conv.tweet.text

      var
        images = conv.tweet.getPhotos.mapIt(it.url)
        video = ""

      let
        firstMediaKind = if conv.tweet.media.len > 0: conv.tweet.media[0].kind
                         else: photoMedia

      if firstMediaKind == videoMedia:
        images = @[conv.tweet.media[0].getThumb]
        video = getVideoEmbed(cfg, conv.tweet.id)
      elif firstMediaKind == gifMedia:
        images = @[conv.tweet.media[0].getThumb]
        video = getPicUrl(conv.tweet.media[0].gif.url)
      elif conv.tweet.card.isSome():
        let card = conv.tweet.card.get()
        if card.image.len > 0:
          images = @[card.image]
        elif card.video.isSome():
          images = @[card.video.get().thumb]

      let html = renderConversation(conv, prefs, getPath() & "#m")
      resp renderMain(html, request, cfg, prefs, title, desc, ogTitle,
                      images=images, video=video)

    get "/@name/status/@id/history/?":
      cond '.' notin @"name"
      let id = @"id"

      if id.len > 19 or id.any(c => not c.isDigit):
        resp Http404, showError("Invalid tweet ID", cfg)

      let edits = await getGraphEditHistory(id)
      if edits.latest == nil or edits.latest.id == 0:
        resp Http404, showError("Tweet history not found", cfg)

      let
        prefs = requestPrefs()
        title = "History for " & pageTitle(edits.latest)
        ogTitle = "Edit History for " & pageTitle(edits.latest.user)
        desc = edits.latest.text

      let html = renderEditHistory(edits, prefs, getPath())
      resp renderMain(html, request, cfg, prefs, title, desc, ogTitle)

    get "/@name/@s/@id/@m/?@i?":
      cond @"s" in ["status", "statuses"]
      cond @"m" in ["video", "photo"]
      redirect("/$1/status/$2" % [@"name", @"id"])

    get "/@name/statuses/@id/?":
      redirect("/$1/status/$2" % [@"name", @"id"])

    get "/i/web/status/@id":
      redirect("/i/status/" & @"id")

    get "/@name/thread/@id/?":
      redirect("/$1/status/$2" % [@"name", @"id"])



================================================
FILE: src/routes/timeline.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import asyncdispatch, strutils, sequtils, uri, options, times
import jester, karax/vdom

import router_utils
import ".."/[types, redis_cache, formatters, query, api]
import ../views/[general, profile, timeline, status, search, about_account]

export vdom
export uri, sequtils
export router_utils
export redis_cache, formatters, query, api
export profile, timeline, status, about_account

proc getQuery*(request: Request; tab, name: string; prefs: Prefs): Query =
  let view = request.params.getOrDefault("view")
  case tab
  of "with_replies":
    result = getReplyQuery(name)
  of "media":
    result = getMediaQuery(name)
    result.view =
      if view in ["timeline", "grid", "gallery"]: view
      else: prefs.mediaView.toLowerAscii
  of "search":
    result = initQuery(params(request), name=name)
  else:
    result = Query(fromUser: @[name])

template skipIf[T](cond: bool; default; body: Future[T]): Future[T] =
  if cond:
    let fut = newFuture[T]()
    fut.complete(default)
    fut
  else:
    body

proc fetchProfile*(after: string; query: Query; skipRail=false): Future[Profile] {.async.} =
  let
    name = query.fromUser[0]
    userId = await getUserId(name)

  if userId.len == 0:
    return Profile(user: User(username: name))
  elif userId == "suspended":
    return Profile(user: User(username: name, suspended: true))

  # temporary fix to prevent errors from people browsing
  # timelines during/immediately after deployment
  var after = after
  if query.kind in {posts, replies} and after.startsWith("scroll"):
    after.setLen 0

  let
    rail =
      skipIf(skipRail or query.kind == media, @[]):
        getCachedPhotoRail(userId)

    user = getCachedUser(name)
    info = getCachedAccountInfo(name, fetch=false)

  result =
    case query.kind
    of posts: await getGraphUserTweets(userId, TimelineKind.tweets, after)
    of replies: await getGraphUserTweets(userId, TimelineKind.replies, after)
    of media: await getGraphUserTweets(userId, TimelineKind.media, after)
    else: Profile(tweets: await getGraphTweetSearch(query, after))

  result.user = await user
  result.photoRail = await rail
  result.accountInfo = await info

  result.tweets.query = query

proc showTimeline*(request: Request; query: Query; cfg: Config; prefs: Prefs;
                   rss, after: string): Future[string] {.async.} =
  if query.fromUser.len != 1:
    let
      timeline = await getGraphTweetSearch(query, after)
      html = renderTweetSearch(timeline, prefs, getPath())
    return renderMain(html, request, cfg, prefs, "Multi", rss=rss)

  var profile = await fetchProfile(after, query)
  template u: untyped = profile.user

  if u.suspended:
    return showError(getSuspended(u.username), cfg)

  if profile.user.id.len == 0: return

  let pHtml = renderProfile(profile, prefs, getPath())
  result = renderMain(pHtml, request, cfg, prefs, pageTitle(u), pageDesc(u),
                      rss=rss, images = @[u.getUserPic("_400x400")],
                      banner=u.banner)

template respTimeline*(timeline: typed) =
  let t = timeline
  if t.len == 0:
    resp Http404, showError("User \"" & @"name" & "\" not found", cfg)
  resp t

template respUserId*() =
  cond @"user_id".len > 0
  let username = await getCachedUsername(@"user_id")
  if username.len > 0:
    redirect("/" & username)
  else:
    resp Http404, showError("User not found", cfg)

proc createTimelineRouter*(cfg: Config) =
  router timeline:
    get "/i/user/@user_id":
      respUserId()

    get "/intent/user":
      respUserId()

    get "/intent/follow/?":
      let username = request.params.getOrDefault("screen_name")
      if username.len == 0:
        resp Http400, showError("Missing screen_name parameter", cfg)
      redirect("/" & username)

    get "/@name/about/?":
      cond @"name".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9', '_'})
      let
        prefs = requestPrefs()
        name = @"name"
        info = await getCachedAccountInfo(name)
      if info.suspended:
        resp showError(getSuspended(name), cfg)
      if info.username.len == 0:
        resp Http404, showError("User \"" & name & "\" not found", cfg)
      let aboutHtml = renderAboutAccount(info)
      resp renderMain(aboutHtml, request, cfg, prefs,
                      "About @" & info.username)

    get "/@name/@kind/?":
      cond @"kind" in ["followers", "following"]
      cond '.' notin @"name"
      cond @"name".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9', '_'})
      let
        prefs = requestPrefs()
        name = @"name"
        userId = await getUserId(name)

      if userId.len == 0:
        resp Http404, showError("User \"" & name & "\" not found", cfg)
      if userId == "suspended":
        resp showError(getSuspended(name), cfg)

      let
        cursor = getCursor()
        isFollowers = @"kind" == "followers"
        user = await getCachedUser(name)
        results = if isFollowers: await getGraphFollowers(userId, cursor)
                  else: await getGraphFollowing(userId, cursor)

      if user.protected:
        resp renderMain(renderProtected(user.username), request, cfg, prefs,
                        "Protected account @" & name)

      let
        tab = if isFollowers: "Followers" else: "Following"
        title = (if isFollowers: "People following @" else: "People followed by @") & name
        html = renderUserList(user, results, prefs, request.path, tab)

      resp renderMain(html, request, cfg, prefs, title,
                      images = @[user.getUserPic("_400x400")])

    get "/@name/?@tab?/?":
      cond '.' notin @"name"
      cond @"name" notin ["pic", "gif", "video", "search", "settings", "login", "intent", "i"]
      cond @"name".allCharsInSet({'a'..'z', 'A'..'Z', '0'..'9', '_', ','})
      cond @"tab" in ["with_replies", "media", "search", ""]
      let
        prefs = requestPrefs()
        after = getCursor()
        names = getNames(@"name")

      var query = request.getQuery(@"tab", @"name", prefs)
      if names.len != 1:
        query.fromUser = names

      # used for the infinite scroll feature
      if @"scroll".len > 0:
        if query.fromUser.len != 1:
          var timeline = await getGraphTweetSearch(query, after)
          if timeline.content.len == 0: 
            resp Http204
          timeline.beginning = true
          resp $renderTweetSearch(timeline, prefs, getPath())
        else:
          var profile = await fetchProfile(after, query, skipRail=true)
          if profile.tweets.content.len == 0: resp Http404
          profile.tweets.beginning = true
          resp $renderTimelineTweets(profile.tweets, prefs, getPath())

      let rssEnabled =
        if @"tab".len == 0: cfg.enableRSSUserTweets
        elif @"tab" == "with_replies": cfg.enableRSSUserReplies
        elif @"tab" == "media": cfg.enableRSSUserMedia
        elif @"tab" == "search": cfg.enableRSSSearch
        else: false

      let rss =
        if not rssEnabled: 
          ""
        elif @"tab".len == 0:
          "/$1/rss" % @"name"
        elif @"tab" == "search":
          "/$1/search/rss?$2" % [@"name", genQueryUrl(query)]
        else:
          "/$1/$2/rss" % [@"name", @"tab"]

      respTimeline(await showTimeline(request, query, cfg, prefs, rss, after))



================================================
FILE: src/routes/unsupported.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import jester

import router_utils
import ../types
import ../views/[general, feature]

export feature

proc createUnsupportedRouter*(cfg: Config) =
  router unsupported:
    template feature {.dirty.} =
      resp renderMain(renderFeature(), request, cfg, requestPrefs())

    get "/about/feature": feature()
    get "/login/?@i?": feature()
    get "/@name/lists/?": feature()

    get "/intent/?@i?": 
      cond @"i" notin ["user", "follow"]
      feature()

    get "/i/@i?/?@j?":
      cond @"i" notin ["status", "lists" , "user"]
      feature()



================================================
FILE: src/sass/_article.scss
================================================
.article-page {
  max-width: 700px;
  margin: 0 auto 20px;
  background-color: var(--bg_panel);

  > .top-ref {
    padding-top: 20px;
  }

  .article-cover {
    width: 100%;
    display: block;
  }

  .article-body {
    padding: 20px;

    > :last-child {
      margin-bottom: 0;
    }

    .article-title {
      display: block;
      font-size: 2rem;
      line-height: 1.3;
      margin: 0 0 10px;
      color: var(--fg_color);
    }

    .article-author {
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border_grey);
      font-size: 14px;

      .article-author-row {
        display: flex;
        align-items: center;
        gap: 8px;
      }

      .article-avatar {
        display: flex;
      }

      .avatar {
        width: 40px;
        height: 40px;
      }

      .article-author-name {
        display: flex;
        align-items: center;
        margin-bottom: 2px;

        .fullname {
          font-size: 15px;
        }

        .verified-icon {
          margin-left: 2px;
        }
      }

      .article-author-meta {
        display: flex;
        align-items: center;
      }

      .fullname {
        font-weight: 700;
        color: var(--fg_color);
        max-width: unset;
        text-overflow: unset;
        overflow: visible;
        white-space: normal;
      }

      .username,
      .article-date-sep,
      .article-date {
        color: var(--fg_dark);
      }

      .username {
        margin-left: 0;
      }

      .article-date-sep {
        margin: 0 4px;
      }

      .article-date {
        text-decoration: none;

        &:hover {
          text-decoration: underline;
        }
      }

      .tweet-stats {
        margin-top: 6px;

        .tweet-stat {
          padding-top: 0;
        }
      }
    }

    > h1 {
      display: block;
      font-size: 1.8rem;
      margin: 25px 0 15px;
    }

    > h2 {
      font-size: 1.4rem;
      font-weight: bold;
      margin: 20px 0 12px;
    }

    > h3 {
      font-size: 1.2rem;
      font-weight: bold;
      margin: 18px 0 10px;
    }

    > p {
      font-size: 16px;
      line-height: 1.7;
      margin: 16px 0;
      word-wrap: break-word;
    }

    .blockquote-attribution {
      display: block;
      margin-top: 0.5em;
    }

    > blockquote {
      border-left: 3px solid var(--accent);
      padding-left: 16px;
      margin: 16px 0;
      color: var(--fg_faded);
      font-size: 16px;
      line-height: 1.7;
    }

    > pre {
      background-color: var(--bg_elements);
      padding: 12px 16px;
      border-radius: 6px;
      overflow-x: auto;
      margin: 16px 0;

      code {
        font-family: monospace;
        font-size: 14px;
        color: var(--fg_color);
      }
    }

    code {
      background-color: var(--bg_elements);
      padding: 2px 5px;
      border-radius: 3px;
      font-family: monospace;
      font-size: 0.9em;
    }

    > ul,
    > ol {
      margin: 16px 0;
      padding-left: 2em;

      li {
        font-size: 16px;
        line-height: 1.7;
        margin: 6px 0;
      }
    }

    .article-media {
      text-align: center;
      margin: 20px 0;

      img,
      video {
        max-width: 100%;
        border-radius: 12px;
      }
    }

    > a,
    > p a,
    > h1 a,
    > h2 a,
    > h3 a,
    > blockquote a,
    > ul a,
    > ol a {
      color: var(--accent);
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }

    .article-divider {
      border: none;
      border-top: 1px solid var(--border_grey);
      margin: 30px 0;
    }

    .timeline-item {
      margin: 20px 0;
      border: 1px solid var(--border_grey);
      border-radius: 12px;
      overflow: hidden;
    }
  }
}

.conversation .article-page {
  max-width: 100%;
  margin-bottom: 0;
}

.article-card {
  .card-image-container {
    position: relative;
  }

  .card-image img {
    height: auto;
  }

  .article-card-badge {
    position: absolute;
    bottom: 8px;
    left: 8px;
    background: rgba(0, 0, 0, 0.75);
    color: #fff;
    font-size: 13px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
  }
}

.quote .article-card {
  margin: 0;

  .card-container {
    border: none;
    border-radius: 0;
    border-top: solid 1px var(--dark_grey);
  }
}

@media (max-width: 700px) {
  .article-page {
    .article-body {
      padding: 12px 15px 25px;

      .article-title {
        font-size: 1.6rem;
      }
    }
  }
}



================================================
FILE: src/sass/_broadcast.scss
================================================
.broadcast-page {
  max-width: 800px;
  width: 100%;
  margin: 20px auto 0;
}

.broadcast-panel {
  background-color: var(--bg_panel);
  border: 1px solid var(--border_grey);
  border-radius: 8px;
  overflow: hidden;
}

.broadcast-player {
  position: relative;
  background: black;

  video,
  img {
    display: block;
    width: 100%;
  }
}

.broadcast-info {
  padding: 14px 16px;
}

.broadcast-title {
  font-size: 18px;
  font-weight: bold;
  margin: 0 0 12px;
}

.broadcast-user-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.broadcast-user {
  display: flex;
  align-items: center;
  gap: 10px;
  color: var(--fg_color);

  img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
  }
}

.broadcast-username {
  color: var(--fg_dark);
}

.broadcast-meta {
  color: var(--fg_faded);
  font-size: 14px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  flex-shrink: 0;
  line-height: 1.5em;
}

.broadcast-live {
  background: #e0245e;
  color: white;
  padding: 1px 6px;
  border-radius: 3px;
  font-weight: bold;
  font-size: 12px;
}



================================================
FILE: src/sass/_space.scss
================================================
.space-page {
  max-width: 800px;
  width: 100%;
  margin: 20px auto 0;
}

.space-panel {
  background-color: var(--bg_panel);
  border: 1px solid var(--border_grey);
  border-radius: 8px;
  overflow: hidden;
}

.space-player {
  position: relative;
  background: linear-gradient(135deg, #7b2a8c 0%, #9b3ab1 100%);
  min-height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;

  audio {
    width: 100%;
    padding: 15px;
    box-sizing: border-box;

    &:not([controls]) {
      display: none;
    }
  }

  .video-overlay {
    background-color: transparent;
  }
}

.space-live {
  background: #e0245e;
  color: white;
  padding: 3px 8px;
  border-radius: 4px;
  font-weight: bold;
  font-size: 12px;
  text-transform: uppercase;
  position: absolute;
  top: 8px;
  right: 8px;
}

.space-info {
  padding: 16px;
}

.space-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 16px;
}

.space-title {
  font-size: 18px;
  font-weight: bold;
  margin: 0;
  line-height: 1.3;
  flex: 1;
}

.space-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
  flex-shrink: 0;
  font-size: 14px;
  color: var(--fg_faded);
}

.listener-count {
  color: var(--fg_color);
}

.space-state {
  color: var(--fg_dark);
}

.space-participants {
  border-top: 1px solid var(--border_grey);
  padding-top: 12px;
}

.space-participant {
  margin-bottom: 10px;

  a {
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--fg_color);
    padding: 6px 0;
  }

  img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    flex-shrink: 0;
  }
}

.participant-info {
  min-width: 0;
}

.participant-name {
  display: flex;
  align-items: center;
  gap: 4px;

  strong {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .verified-icon {
    margin-bottom: 0;
    position: relative;
    top: -2px;
  }
}

.host-badge {
  background: var(--accent);
  color: white;
  padding: 2px 7px;
  border-radius: 3px;
  font-size: 11px;
  font-weight: 600;
  line-height: 1;
  position: relative;
  top: 1px;
}

.participant-username {
  color: var(--fg_dark);
  font-size: 13px;
}



================================================
FILE: src/sass/general.scss
================================================
@import "_variables";
@import "_mixins";

.panel-container {
  margin: auto;
  font-size: 130%;
}

.error-panel {
  @include center-panel(var(--error_red));
  text-align: center;
}

.search-bar > form {
  @include center-panel(var(--darkest_grey));

  button {
    background: var(--bg_elements);
    color: var(--fg_color);
    border: 0;
    border-radius: 3px;
    cursor: pointer;
    font-weight: bold;
    width: 30px;
    height: 30px;
    padding: 0px 5px 1px 8px;
  }

  input {
    font-size: 16px;
    width: 100%;
    background: var(--bg_elements);
    color: var(--fg_color);
    border: 0;
    border-radius: 4px;
    padding: 4px;
    margin-right: 8px;
    height: unset;
  }
}



================================================
FILE: src/sass/index.scss
================================================
@import "_variables";

@import "tweet/_base";
@import "profile/_base";
@import "general";
@import "navbar";
@import "inputs";
@import "timeline";
@import "search";
@import "broadcast";
@import "space";
@import "_article";

body {
  // colors
  --bg_color: #{$bg_color};
  --fg_color: #{$fg_color};
  --fg_faded: #{$fg_faded};
  --fg_dark: #{$fg_dark};
  --fg_nav: #{$fg_nav};

  --bg_panel: #{$bg_panel};
  --bg_elements: #{$bg_elements};
  --bg_overlays: #{$bg_overlays};
  --bg_hover: #{$bg_hover};

  --grey: #{$grey};
  --dark_grey: #{$dark_grey};
  --darker_grey: #{$darker_grey};
  --darkest_grey: #{$darkest_grey};
  --border_grey: #{$border_grey};

  --accent: #{$accent};
  --accent_light: #{$accent_light};
  --accent_dark: #{$accent_dark};
  --accent_border: #{$accent_border};

  --play_button: #{$play_button};
  --play_button_hover: #{$play_button_hover};

  --more_replies_dots: #{$more_replies_dots};
  --error_red: #{$error_red};

  --verified_blue: #{$verified_blue};
  --verified_business: #{$verified_business};
  --verified_government: #{$verified_government};
  --icon_text: #{$icon_text};

  --tab: #{$fg_color};
  --tab_selected: #{$accent};

  --profile_stat: #{$fg_color};

  background-color: var(--bg_color);
  color: var(--fg_color);
  font-family: $font_0, $font_1;
  font-size: 15px;
  line-height: 1.3;
  margin: 0;
}

* {
  outline: unset;
  margin: 0;
  text-decoration: none;
}

img {
  dynamic-range-limit: standard;
}

h1 {
  display: inline;
}

h2,
h3 {
  font-weight: normal;
}

p {
  margin: 14px 0;
}

a {
  color: var(--accent);

  &:hover {
    text-decoration: underline;
  }
}

fieldset {
  border: 0;
  padding: 0;
  margin-top: -0.6em;
}

legend {
  width: 100%;
  padding: 0.6em 0 0.3em 0;
  border: 0;
  font-size: 16px;
  font-weight: 600;
  border-bottom: 1px solid var(--border_grey);
  margin-bottom: 8px;
}

.preferences {
  .note {
    border-top: 1px solid var(--border_grey);
    border-bottom: 1px solid var(--border_grey);
    padding: 6px 0 8px 0;
    margin-bottom: 8px;
    margin-top: 16px;
  }

  .bookmark-note {
    margin: 0;
    margin-bottom: 10px;
  }
}

ul {
  padding-left: 1.3em;
}

.container {
  display: flex;
  flex-wrap: wrap;
  box-sizing: border-box;
  margin: auto;
  min-height: 100vh;
}

body.fixed-nav .container {
  padding-top: 50px;
}

.icon-container {
  display: inline;
}

.overlay-panel {
  max-width: 600px;
  width: 100%;
  margin: 0 auto;
  margin-top: 10px;
  background-color: var(--bg_overlays);
  padding: 10px 15px;
  align-self: start;

  ul {
    margin-bottom: 14px;
  }

  p {
    word-break: break-word;
  }
}

.verified-icon {
  display: inline-block;
  position: relative;
  width: 14px;
  height: 14px;
  margin-bottom: 2px;

  .verified-icon-circle {
    position: absolute;
    font-size: 15px;
  }

  .verified-icon-check {
    position: absolute;
    font-size: 9px;
    margin: 5px 3px;
  }

  &.blue {
    .verified-icon-circle {
      color: var(--verified_blue);
    }

    .verified-icon-check {
      color: var(--icon_text);
    }
  }

  &.business {
    .verified-icon-circle {
      color: var(--verified_business);
    }

    .verified-icon-check {
      color: var(--bg_panel);
    }
  }

  &.government {
    .verified-icon-circle {
      color: var(--verified_government);
    }

    .verified-icon-check {
      color: var(--bg_panel);
    }
  }
}

@media (max-width: 600px) {
  .preferences-container {
    max-width: 95vw;
  }

  .nav-item,
  .nav-item .icon-container {
    font-size: 16px;
  }
}



================================================
FILE: src/sass/inputs.scss
================================================
@import "_variables";
@import "_mixins";

button {
  @include input-colors;
  background-color: var(--bg_elements);
  color: var(--fg_color);
  border: 1px solid var(--accent_border);
  padding: 3px 6px;
  font-size: 14px;
  cursor: pointer;
  float: right;
}

input[type="text"],
input[type="date"],
input[type="number"],
select {
  @include input-colors;
  background-color: var(--bg_elements);
  padding: 1px 4px;
  color: var(--fg_color);
  border: 1px solid var(--accent_border);
  border-radius: 0;
  font-size: 14px;
}

input[type="number"] {
  -moz-appearance: textfield;
}

input[type="text"],
input[type="number"] {
  height: 16px;
}

select {
  height: 20px;
  padding: 0 2px;
  line-height: 1;
}

input[type="date"]::-webkit-inner-spin-button {
  display: none;
}

input[type="number"] {
  -moz-appearance: textfield;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  display: none;
  -webkit-appearance: none;
  margin: 0;
}

input[type="date"]::-webkit-clear-button {
  margin-left: 17px;
  filter: grayscale(100%);
  filter: hue-rotate(120deg);
}

input::-webkit-calendar-picker-indicator {
  opacity: 0;
}

input::-webkit-datetime-edit-day-field:focus,
input::-webkit-datetime-edit-month-field:focus,
input::-webkit-datetime-edit-year-field:focus {
  background-color: var(--accent);
  color: var(--fg_color);
  outline: none;
}

.date-range {
  .date-input {
    display: inline-block;
    position: relative;
  }

  .icon-container {
    pointer-events: none;
    position: absolute;
    top: 2px;
    right: 5px;
  }

  .search-title {
    margin: 0 2px;
  }
}

.icon-button button {
  color: var(--accent);
  text-decoration: none;
  background: none;
  border: none;
  float: none;
  padding: unset;
  padding-left: 4px;

  &:hover {
    color: var(--accent_light);
  }
}

.checkbox {
  position: absolute;
  top: 1px;
  right: 0;
  height: 17px;
  width: 17px;
  background-color: var(--bg_elements);
  border: 1px solid var(--accent_border);

  &:after {
    content: "";
    position: absolute;
    display: none;
  }
}

.checkbox-container {
  display: block;
  position: relative;
  margin-bottom: 5px;
  cursor: pointer;
  user-select: none;
  padding-right: 22px;

  input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;

    &:checked ~ .checkbox:after {
      display: block;
    }
  }

  &:hover input ~ .checkbox {
    border-color: var(--accent);
  }

  &:active input ~ .checkbox {
    border-color: var(--accent_light);
  }

  .checkbox:after {
    left: 2px;
    bottom: 0;
    font-size: 13px;
    font-family: $font_1;
    content: "\e811";
  }
}

.pref-group {
  display: inline;
}

.preferences {
  button {
    margin: 6px 0 3px 0;
  }

  label {
    padding-right: 150px;
  }

  select {
    position: absolute;
    top: 0;
    right: 0;
    display: block;
    -moz-appearance: none;
    -webkit-appearance: none;
    appearance: none;
    min-width: 100px;
  }

  input[type="text"],
  input[type="number"] {
    position: absolute;
    right: 0;
    max-width: 140px;
  }

  .pref-group {
    display: block;
  }

  .pref-input {
    position: relative;
    margin-bottom: 6px;
  }

  .pref-reset {
    float: left;
  }

  .prefs-code {
    background-color: var(--bg_elements);
    border: 1px solid var(--accent_border);
    color: var(--fg_color);
    font-size: 13px;
    padding: 6px 8px;
    margin: 4px 0;
    word-break: break-all;
    white-space: pre-wrap;
    user-select: all;
  }
}



================================================
FILE: src/sass/navbar.scss
================================================
@import "_variables";

nav {
  display: flex;
  align-items: center;
  background-color: var(--bg_overlays);
  box-shadow: 0 0 4px $shadow;
  padding: 0;
  width: 100%;
  height: 50px;
  z-index: 1000;
  font-size: 16px;

  a,
  .icon-button button {
    color: var(--fg_nav);
  }

  body.fixed-nav & {
    position: fixed;
  }
}

.inner-nav {
  margin: auto;
  box-sizing: border-box;
  padding: 0 10px;
  display: flex;
  align-items: center;
  flex-basis: 920px;
  height: 50px;
}

.site-name {
  font-size: 15px;
  font-weight: 600;
  line-height: 1;

  &:hover {
    color: var(--accent_light);
    text-decoration: unset;
  }
}

.site-logo {
  display: block;
  width: 35px;
  height: 35px;
}

.nav-item {
  display: flex;
  flex: 1;
  line-height: 50px;
  height: 50px;
  overflow: hidden;
  flex-wrap: wrap;
  align-items: center;

  &.right {
    text-align: right;
    justify-content: flex-end;
  }

  &.right a:hover {
    color: var(--accent_light);
    text-decoration: unset;
  }
}

.lp {
  height: 14px;
  display: inline-block;
  position: relative;
  top: 2px;
  fill: var(--fg_nav);

  &:hover {
    fill: var(--accent_light);
  }
}

.icon-info {
  margin: 0 -3px;
}

.icon-cog {
  font-size: 15px;
  padding-left: 0 !important;
}



================================================
FILE: src/sass/search.scss
================================================
@import "_variables";
@import "_mixins";

.search-title {
  font-weight: bold;
  display: inline-block;
  margin-top: 4px;
}

.search-field {
  display: flex;
  flex-wrap: wrap;

  button {
    margin: 0 2px 0 0;
    padding: 0px 1px 1px 4px;
    height: 23px;
    display: flex;
    align-items: center;
  }

  .pref-input {
    margin: 0 4px 0 0;
    flex-grow: 1;
    height: 23px;
  }

  input[type="text"],
  input[type="number"] {
    height: calc(100% - 4px);
    width: calc(100% - 8px);
  }

  > label {
    display: inline;
    background-color: var(--bg_elements);
    color: var(--fg_color);
    border: 1px solid var(--accent_border);
    padding: 1px 1px 2px 4px;
    font-size: 14px;
    cursor: pointer;
    margin-bottom: 2px;

    @include input-colors;
  }

  @include create-toggle(search-panel, 380px);
}

.search-panel {
  width: 100%;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s;

  flex-grow: 1;
  font-weight: initial;
  text-align: left;

  .checkbox-container {
    display: inline;
    padding-right: unset;
    margin-bottom: 5px;
    margin-left: 23px;
  }

  .checkbox {
    right: unset;
    left: -22px;
    line-height: 1.6em;
  }

  .checkbox-container .checkbox:after {
    top: -4px;
  }
}

.search-row {
  display: flex;
  flex-wrap: wrap;
  line-height: unset;

  > div {
    flex-grow: 1;
    flex-shrink: 1;
  }

  input {
    height: 21px;
  }

  .pref-input {
    display: block;
    padding-bottom: 5px;

    input {
      height: 21px;
      margin-top: 1px;
    }
  }
}

.search-toggles {
  flex-grow: 1;
  display: grid;
  grid-template-columns: repeat(5, auto);
  grid-column-gap: 10px;
}

.profile-tabs {
  @include search-resize(820px, 5);
  @include search-resize(715px, 4);
  @include search-resize(700px, 5);
  @include search-resize(485px, 4);
  @include search-resize(410px, 3);
}

@include search-resize(700px, 5);
@include search-resize(485px, 4);
@include search-resize(410px, 3);



================================================
FILE: src/sass/timeline.scss
================================================
@import "_variables";

.timeline-container {
  @include panel(100%, 600px);
}

.timeline > div:not(:first-child) {
  border-top: 1px solid var(--border_grey);
}

.timeline-header {
  width: 100%;
  background-color: var(--bg_panel);
  text-align: center;
  padding: 8px;
  display: block;
  font-weight: bold;
  margin-bottom: 4px;
  box-sizing: border-box;

  button {
    float: unset;
  }
}

.timeline-banner img {
  width: 100%;
}

.timeline-description {
  font-weight: normal;
}

.tab {
  align-items: center;
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0 0 4px 0;
  background-color: var(--bg_panel);
  padding: 0;
}

.tab-item {
  flex: 1 1 0;
  text-align: center;
  margin-top: 0;

  a {
    border-bottom: 0.1rem solid transparent;
    color: var(--tab);
    display: block;
    padding: 8px 0;
    text-decoration: none;
    font-weight: bold;

    &:hover {
      text-decoration: none;
    }

    &.active {
      border-bottom-color: var(--tab_selected);
      color: var(--tab_selected);
    }
  }

  &.active a {
    border-bottom-color: var(--tab_selected);
    color: var(--tab_selected);
  }

  &.wide {
    flex-grow: 1.2;
    flex-basis: 50px;
  }
}

.timeline-footer {
  background-color: var(--bg_panel);
  padding: 6px 0;
}

.timeline-protected {
  text-align: center;

  p {
    margin: 8px 0;
  }

  h2 {
    color: var(--accent);
    font-size: 20px;
    font-weight: 600;
  }
}

.timeline-none {
  color: var(--accent);
  font-size: 20px;
  font-weight: 600;
  text-align: center;
}

.timeline-end {
  background-color: var(--bg_panel);
  color: var(--accent);
  font-size: 16px;
  font-weight: 600;
  text-align: center;
}

.show-more {
  background-color: var(--bg_panel);
  text-align: center;
  padding: 0.75em 0;
  display: block !important;

  a {
    background-color: var(--darkest_grey);
    display: inline-block;
    height: 2em;
    padding: 0 2em;
    line-height: 2em;

    &:hover {
      background-color: var(--darker_grey);
    }
  }
}

.top-ref {
  background-color: var(--bg_color);
  border-top: none !important;

  .icon-down {
    font-size: 20px;
    display: flex;
    justify-content: center;
    text-decoration: none;

    &:hover {
      color: var(--accent_light);
    }

    &::before {
      transform: rotate(180deg) translateY(-1px);
    }
  }
}

.timeline-item {
  overflow-wrap: break-word;
  border-left-width: 0;
  min-width: 0;
  padding: 0.75em;
  display: flex;
  position: relative;
  background-color: var(--bg_panel);
}

.timeline.media-grid-view,
.timeline.media-gallery-view {
  > div:not(:first-child) {
    border-top: none;
  }

  .timeline-item::before {
    display: none;
  }
}

.timeline.media-grid-view,
.timeline.media-gallery-view .gallery-masonry.compact {
  .tweet-header,
  .replying-to,
  .retweet-header,
  .pinned,
  .tweet-stats,
  .attribution,
  .poll,
  .quote,
  .community-note,
  .media-tag-block,
  .tweet-content,
  .card-content {
    display: none;
  }

  .card {
    margin: unset;

    .card-container {
      border: unset;
      border-radius: unset;

      .card-image-container {
        width: 100%;
        min-height: 100%;
      }

      .card-content-container {
        display: none;
      }
    }
  }
}

.timeline.media-grid-view {
  display: grid;
  gap: 4px;
  grid-template-columns: repeat(3, minmax(0, 1fr));

  > div:not(:first-child) {
    margin-top: 0;
  }

  .timeline-item {
    padding: 0;
  }

  .tweet-link {
    z-index: 1000;

    &:hover {
      background-color: unset;
    }
  }

  > .show-more,
  > .top-ref,
  > .timeline-footer,
  > .timeline-header {
    grid-column: 1 / -1;
  }

  .tweet-body {
    height: 100%;
    margin-left: 0;
    padding: 0;
    position: relative;
    aspect-ratio: 1/1;
  }

  .gallery-row + .gallery-row {
    margin-top: 0.25em !important;
  }

  .attachments {
    background-color: var(--darkest_grey);
    border-radius: 0;
    margin: 0;
    max-height: none;
  }

  .attachments,
  .gallery-row,
  .still-image {
    height: 100%;
    width: 100%;
  }

  .still-image img,
  .attachment > video,
  .attachment > img {
    object-fit: cover;
    height: 100%;
    width: 100%;
  }

  .attachment {
    display: flex;
    align-items: center;
  }

  .gallery-video {
    height: 100%;
  }

  .media-gif {
    display: flex;
  }

  .timeline-item:hover {
    opacity: 0.85;
  }

  .alt-text {
    display: none;
  }
}

.timeline.media-gallery-view {
  .gallery-masonry {
    margin: 10px 0;
    column-gap: 10px;
    column-width: unquote("clamp(190px, 22vw, 350px)");

    &[data-col-size="small"] {
      column-width: unquote("max(130px, 11vw)");
    }

    &[data-col-size="large"] {
      column-width: unquote("clamp(350px, 22vw, 480px)");
    }

    &.masonry-active {
      column-width: unset;
      column-gap: unset;
      position: relative;

      .timeline-item {
        animation: none;
        position: absolute;
        box-sizing: border-box;
        margin-bottom: 0;
      }
    }

    &.compact {
      .tweet-body {
        padding: 0;

        > .attachments {
          margin: 0;
        }
      }

      .card-image-container img {
        max-height: unset;
      }
    }
  }

  @keyframes masonry-init {
    to {
      opacity: 1;
      pointer-events: auto;
    }
  }

  // Start hidden. CSS animation reveals after a delay as a no-JS fallback.
  // With JS, masonry-active cancels the animation and masonry-visible reveals.
  .gallery-masonry .timeline-item,
  > .show-more,
  > .top-ref,
  > .timeline-footer {
    opacity: 0;
    pointer-events: none;
    animation: masonry-init 0.2s 0.3s forwards;
  }

  .gallery-masonry.masonry-active .timeline-item.masonry-visible,
  > .show-more.masonry-visible,
  > .top-ref.masonry-visible,
  > .timeline-footer.masonry-visible {
    opacity: 1;
    pointer-events: auto;
    transition: opacity 0.15s ease;
    animation: none;
  }

  .timeline-item {
    margin-bottom: 10px;
    break-inside: avoid;
    flex-direction: column;
    padding: 0;
  }

  > .show-more,
  > .top-ref,
  > .timeline-footer,
  > .timeline-header {
    margin-left: auto;
    margin-right: auto;
    max-width: 900px;
  }

  > .show-more {
    padding: 0;
    margin-top: 8px;
    background-color: unset;
  }

  .tweet-content {
    margin: 3px 0;
  }

  .tweet-body {
    display: flex;
    flex-direction: column;
    height: 100%;
    margin-left: 0;
    padding: 10px;

    > .attachments {
      align-self: stretch;
      border-radius: 0;
      margin: -10px -10px 10px;
      max-height: none;
      order: -1;
      width: auto;
      background-color: var(--bg_elements);

      .gallery-row {
        max-height: none;
        max-width: none;
        align-items: center;
      }

      .still-image img,
      .attachment > video,
      .attachment > img {
        max-height: none;
        width: 100%;
      }

      .attachment:last-child {
        max-height: none;
      }

      .card-container {
        border: unset;
        border-radius: unset;
      }
    }

    .tweet-stat {
      padding-top: unset;
    }

    .quote {
      margin-bottom: 5px;
      margin-top: 5px;
    }

    .replying-to {
      margin: 0;
    }
  }

  .tweet-header {
    align-items: flex-start;
    display: flex;
    gap: 0.75em;
    margin-bottom: 0;

    .tweet-avatar {
      img {
        float: none;
        height: 42px;
        margin: 0;
        width: 42px;
      }
    }

    .tweet-name-row {
      flex: 1;
    }

    .fullname-and-username {
      flex-wrap: wrap;
    }

    .fullname {
      max-width: calc(100% - 18px);
    }

    .verified-icon {
      margin-left: 4px;
      margin-top: 1px;
    }

    .username {
      display: block;
      flex-basis: 100%;
      margin-left: 0;
    }
  }
}

@media (max-width: 520px) {
  .timeline.media-gallery-view {
    padding: 8px 0;
  }
}



================================================
FILE: src/sass/include/_mixins.css
================================================
@import '_variables';

@mixin panel($width, $max-width) {
    max-width: $max-width;
    margin: 0 auto;
    float: none;
    border-radius: 0;
    position: relative;
    width: $width;
}

@mixin play-button {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 1;

    &:hover {
        .overlay-circle {
            border-color: var(--play_button_hover);
        }

        .overlay-triangle {
            border-color: transparent transparent transparent var(--play_button_hover);
        }
    }
}

@mixin breakable {
    overflow: hidden;
    overflow-wrap: break-word;
}

@mixin ellipsis {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

@mixin center-panel($bg) {
    padding: 12px;
    border-radius: 4px;
    display: flex;
    background: $bg;
    box-shadow: 0 0 15px $shadow_dark;
    margin: auto;
    margin-top: -50px;
}

@mixin input-colors {
    &:hover {
        border-color: var(--accent);
    }

    &:active {
        border-color: var(--accent_light);
    }
}

@mixin search-resize($width, $rows) {
    @media(max-width: $width) {
        .search-toggles {
            grid-template-columns: repeat($rows, auto);
        }

        #search-panel-toggle:checked ~ .search-panel {
            max-height: 380px !important;
        }
    }
}

@mixin create-toggle($elem, $height) {
    ##{$elem}-toggle {
        display: none;

        &:checked ~ .#{$elem} {
            max-height: $height;
        }

        &:checked ~ label .icon-down:before {
            transform: rotate(180deg) translateY(-1px);
        }
    }
}



================================================
FILE: src/sass/include/_variables.scss
================================================
// colors
$bg_color: #0f0f0f;
$fg_color: #f8f8f2;
$fg_faded: #f8f8f2cf;
$fg_dark: #ff6c60;
$fg_nav: #ff6c60;

$bg_panel: #161616;
$bg_elements: #121212;
$bg_overlays: #1f1f1f;
$bg_hover: #1a1a1a;

$grey: #888889;
$dark_grey: #404040;
$darker_grey: #282828;
$darkest_grey: #222222;
$border_grey: #3e3e35;

$accent: #ff6c60;
$accent_light: #ffaca0;
$accent_dark: #8a3731;
$accent_border: #ff6c6091;

$play_button: #d8574d;
$play_button_hover: #ff6c60;

$more_replies_dots: #ad433b;
$error_red: #420a05;

$verified_blue: #1da1f2;
$verified_business: #fac82b;
$verified_government: #c1b6a4;
$icon_text: $fg_color;

$tab: $fg_color;
$tab_selected: $accent;

$shadow: rgba(0, 0, 0, 0.6);
$shadow_dark: rgba(0, 0, 0, 0.2);

//fonts
$font_0: sans-serif;
$font_1: fontello;



================================================
FILE: src/sass/profile/_base.scss
================================================
@import "_variables";
@import "_mixins";

@import "card";
@import "about-account";
@import "photo-rail";
@import "community";

.profile-tabs {
  @include panel(auto, 900px);

  .timeline-container {
    float: right;
    width: 68% !important;
    max-width: unset;
  }
}

.profile-banner {
  margin-bottom: 4px;
  background-color: var(--bg_panel);

  a {
    display: block;
    position: relative;
    padding: 33.34% 0 0 0;
  }

  img {
    max-width: 100%;
    position: absolute;
    top: 0;
  }
}

.profile-tab {
  padding: 0 4px 0 0;
  box-sizing: border-box;
  display: inline-block;
  font-size: 14px;
  text-align: left;
  vertical-align: top;
  max-width: 32%;
  top: 0;

  body.fixed-nav & {
    top: 50px;
  }
}

.profile-result {
  min-height: 54px;

  .username {
    margin: 0 !important;
  }

  .tweet-header {
    margin-bottom: unset;
  }
}

.profile-tabs.media-only {
  max-width: none;
  width: 100%;

  .timeline-container {
    float: none;
    width: 100% !important;
    max-width: none;
    padding: 0 10px;
    box-sizing: border-box;
  }

  .timeline-container > .tab {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
  }
}

@media (max-width: 700px) {
  .profile-tabs {
    width: 100vw;
    max-width: 600px;

    .timeline-container {
      width: 100% !important;

      .tab-item wide {
        flex-grow: 1.4;
      }
    }
  }

  .profile-tabs.media-only {
    width: 100%;
    max-width: none;

    .timeline-container {
      width: 100vw !important;
      padding: 0;
    }
  }

  .profile-tab {
    width: 100%;
    max-width: unset;
    position: initial !important;
    padding: 0;
  }
}

@media (min-height: 900px) {
  .profile-tab.sticky {
    position: sticky;
  }
}



================================================
FILE: src/sass/profile/_community.scss
================================================
.community-header {
  padding: 12px 15px;
  border-bottom: 1px solid var(--border_grey);
  background-color: var(--bg_panel);

  .community-name {
    font-size: 22px;
    margin-bottom: 6px;

    a {
      color: inherit;
    }
  }

  .community-category {
    display: inline-block;
    background-color: var(--bg_elements);
    border: 1px solid var(--border_grey);
    border-radius: 16px;
    padding: 2px 12px;
    font-size: 13px;
    color: var(--fg_faded);
    margin-bottom: 8px;
  }

  .community-description {
    color: var(--fg_faded);
    margin-bottom: 8px;
    line-height: 1.4;
  }

  .community-member-count {
    font-weight: bold;
    color: inherit;
  }

  .community-stats {
    color: var(--grey);
    font-size: 14px;
  }
}

.community-about {
  padding: 16px 15px 15px;
  background-color: var(--bg_panel);

  h2 {
    font-size: 18px;
    margin: 0 0 12px;
  }

  .community-info {
    border-bottom: 1px solid var(--border_grey);
    padding-bottom: 12px;
  }

  .community-info-item {
    display: flex;
    gap: 10px;
    padding: 8px 0;
    align-items: center;

    .verified-icon {
      margin-left: 2px;
    }

    > .icon-container {
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      color: var(--grey);
      flex-shrink: 0;
      width: 26px;
      height: 26px;
    }

    strong {
      color: var(--fg_color);
    }

    a {
      color: var(--accent);
    }
  }

  .community-rules {
    border-bottom: 1px solid var(--border_grey);
    padding: 16px 0 12px;
  }

  .community-rules-intro {
    color: var(--fg_faded);
    font-size: 14px;
    margin: 0 0 12px;
  }

  .community-rule {
    display: flex;
    gap: 10px;
    padding: 10px 0;
    align-items: flex-start;

    .community-rule-number {
      display: flex;
      align-items: center;
      justify-content: center;
      min-width: 26px;
      height: 26px;
      border-radius: 50%;
      background-color: var(--accent);
      color: var(--fg_color);
      font-weight: bold;
      font-size: 13px;
      flex-shrink: 0;
    }

    .community-rule-content p {
      margin: 4px 0 0;
      color: var(--fg_faded);
      font-size: 14px;
    }
  }

  .community-moderators {
    padding-top: 16px;

    h2 {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .community-mods-link {
      font-size: 14px;
      font-weight: normal;
      color: var(--accent);
    }
  }

  .community-moderator {
    display: flex;
    gap: 10px;
    padding: 8px 0;
    align-items: center;

    .community-mod-avatar {
      width: 40px;
      height: 40px;
      border-radius: 50%;
    }

    .community-mod-info {
      display: flex;
      flex-direction: column;
    }

    .community-mod-name {
      display: flex;
      align-items: center;
      font-weight: bold;
      color: var(--fg_color);

      .verified-icon {
        margin-left: 2px;
      }
    }

    .community-mod-username {
      color: var(--fg_faded);
      font-size: 14px;
    }
  }
}

.community-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 10px 15px;
  border-bottom: 1px solid var(--border_grey);

  .community-tag {
    display: inline-block;
    background-color: var(--bg_elements);
    border: 1px solid var(--border_grey);
    border-radius: 16px;
    padding: 4px 12px;
    font-size: 13px;
    color: var(--accent);
  }
}

.community-hashtag-header {
  padding: 12px 15px;
  border-bottom: 1px solid var(--border_grey);

  .community-hashtag-title {
    font-size: 20px;
    color: var(--accent);
    margin: 0;
  }
}



================================================
FILE: src/sass/profile/about-account.scss
================================================
@import '_variables';

.about-account {
    max-width: 500px;
    width: 100%;
    margin: 20px auto 0;
    align-self: flex-start;
    background: var(--bg_panel);
    border-radius: 4px;
    padding: 12px 20px 20px;
}

.about-account-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 16px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--border_grey);
}

.about-account-avatar img {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    margin-bottom: 4px;
}

.about-account-name {
    @include breakable;
    font-weight: bold;
}

.about-account-body {
    display: flex;
    flex-direction: column;
    gap: 14px;
}

.about-account-at {
    font-size: 18px;
    font-weight: bold;
}

.about-account-row {
    display: flex;
    align-items: center;
    gap: 10px;

    > span:first-child {
        color: var(--fg_faded);
        flex-shrink: 0;
    }

    > div {
        display: flex;
        flex-direction: column;
    }
}

.about-account-label {
    color: var(--fg_faded);
    font-size: 13px;
}

@media(max-width: 700px) {
    .about-account {
        max-width: none;
        margin: 10px;
    }
}



================================================
FILE: src/sass/profile/card.scss
================================================
@import '_variables';
@import '_mixins';

.profile-card {
    flex-wrap: wrap;
    background: var(--bg_panel);
    padding: 12px;
    display: flex;
}

.profile-card-info {
    @include breakable;
    width: 100%;
}

.profile-card-tabs-name {
    @include breakable;
    max-width: 100%;
}

.profile-card-username {
    @include breakable;
    color: var(--fg_color);
    font-size: 14px;
    display: block;
}

.profile-card-fullname {
    @include breakable;
    color: var(--fg_color);
    font-size: 16px;
    font-weight: bold;
    text-shadow: none;
    max-width: 100%;
}

.profile-card-avatar {
    display: inline-block;
    position: relative;
    width: 100%;
    margin-right: 4px;
    margin-bottom: 6px;

    &:after {
        content: '';
        display: block;
        margin-top: 100%;
    }

    img {
        box-sizing: border-box;
        position: absolute;
        width: 100%;
        height: 100%;
        border: 4px solid var(--darker_grey);
        background: var(--bg_panel);
    }
}

.profile-card-extra {
    display: contents;
    flex: 100%;
    margin-top: 7px;

    .profile-bio {
        @include breakable;
        width: 100%;
        margin: 4px -6px 6px 0;
        white-space: pre-wrap;

        p {
            margin: 0;
        }
    }

    .profile-joindate, .profile-location, .profile-website {
        color: var(--fg_faded);
        margin: 1px 0;
        width: 100%;
    }
}

.profile-card-extra-links {
    margin-top: 8px;
    font-size: 14px;
    width: 100%;
}

.profile-statlist {
    display: flex;
    flex-wrap: wrap;
    padding: 0;
    width: 100%;
    justify-content: space-between;

    li {
        display: table-cell;
        text-align: center;
    }
}

.profile-stat-header {
    font-weight: bold;
    color: var(--profile_stat);
}

.profile-stat-num {
    display: block;
    color: var(--profile_stat);
}

@media(max-width: 700px) {
    .profile-card-info {
        display: flex;
    }

    .profile-card-tabs-name {
        flex-shrink: 100;
    }

    .profile-card-avatar {
        width: 80px;
        height: 80px;

        img {
            border-width: 2px;
            width: unset;
        }
    }
}



================================================
FILE: src/sass/profile/photo-rail.scss
================================================
@import '_variables';

.photo-rail {
    &-card {
        float: left;
        background: var(--bg_panel);
        border-radius: 0 0 4px 4px;
        width: 100%;
        margin: 5px 0;
    }

    &-header {
        padding: 5px 12px 0;
    }

    &-header-mobile {
        display: none;
        box-sizing: border-box;
        padding: 5px 12px 0;
        width: 100%;
        float: unset;
        color: var(--accent);
        justify-content: space-between;
    }

    &-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        grid-gap: 3px 3px;
        padding: 5px 12px 12px;

        a {
            position: relative;
            border-radius: 5px;
            background-color: var(--darker_grey);

            &:before {
                content: "";
                display: block;
                padding-top: 100%;
            }
        }

        img {
            height: 100%;
            width: 100%;
            border-radius: 4px;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
        }
    }
}

@include create-toggle(photo-rail-grid, 640px);
#photo-rail-grid-toggle:checked ~ .photo-rail-grid {
    padding-bottom: 12px;
}

@media(max-width: 700px) {
    .photo-rail-header {
        display: none;
    }

    .photo-rail-header-mobile {
        display: flex;
    }

    .photo-rail-grid {
        max-height: 0;
        padding-bottom: 0;
        overflow: hidden;
        transition: max-height 0.4s;
    }

    .photo-rail-grid {
        grid-template-columns: repeat(6, 1fr);
    }

    #photo-rail-grid-toggle:checked ~ .photo-rail-grid {
        max-height: 300px;
    }
}

@media(max-width: 450px) {
    .photo-rail-grid {
        grid-template-columns: repeat(4, 1fr);
    }

    #photo-rail-grid-toggle:checked ~ .photo-rail-grid {
        max-height: 450px;
    }
}



================================================
FILE: src/sass/tweet/_base.scss
================================================
@import "_variables";
@import "_mixins";
@import "thread";
@import "media";
@import "video";
@import "embed";
@import "card";
@import "poll";
@import "quote";

.tweet-body {
  flex: 1;
  min-width: 0;
  margin-left: 58px;
  pointer-events: none;
  z-index: 1;
}

.tweet-content {
  line-height: 1.3em;
  pointer-events: all;
  display: inline;
}

.tweet-bidi {
  display: block !important;
}

.tweet-header {
  padding: 0;
  vertical-align: bottom;
  flex-basis: 100%;
  margin-bottom: 0.2em;

  a {
    display: inline-block;
    word-break: break-all;
    max-width: 100%;
    pointer-events: all;
  }
}

.tweet-name-row {
  padding: 0;
  display: flex;
  justify-content: space-between;

  .verified-icon {
    margin-left: 2px;
  }
}

.fullname-and-username {
  display: flex;
  min-width: 0;
}

.fullname {
  @include ellipsis;
  flex-shrink: 2;
  max-width: 80%;
  font-size: 14px;
  font-weight: 700;
  color: var(--fg_color);
}

.username {
  @include ellipsis;
  min-width: 1.6em;
  margin-left: 0.4em;
  word-wrap: normal;
}

.tweet-date {
  display: flex;
  flex-shrink: 0;
  margin-left: 4px;
}

.tweet-date a,
.username,
.show-more a {
  color: var(--fg_dark);
}

.tweet-published {
  margin-top: 6px;
  margin-bottom: 0px;
  color: var(--grey);
  pointer-events: all;
}

.tweet-avatar {
  display: contents !important;

  img {
    float: left;
    margin-top: 3px;
    margin-left: -58px;
    width: 48px;
    height: 48px;
  }
}

.avatar {
  &.round {
    border-radius: 50%;
    user-select: none;
    -webkit-user-select: none;
  }

  &.mini {
    position: unset;
    margin-right: 5px;
    margin-top: -1px;
    width: 20px;
    height: 20px;
  }
}

.tweet-embed {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  background-color: var(--bg_panel);

  .tweet-content {
    font-size: 18px;
  }

  .tweet-body {
    display: flex;
    flex-direction: column;
    max-height: calc(100vh - 0.75em * 2);
  }

  .card-image img {
    height: auto;
  }

  .avatar {
    position: absolute;
  }
}

.attribution {
  display: flex;
  pointer-events: all;
  margin: 5px 0;

  strong {
    color: var(--fg_color);
  }
}

.media-tag-block {
  padding-top: 5px;
  pointer-events: all;
  color: var(--fg_faded);

  .icon-container {
    padding-right: 2px;
  }

  .media-tag,
  .icon-container {
    color: var(--fg_faded);
  }
}

.timeline-container .media-tag-block {
  font-size: 13px;
}

.tweet-geo {
  color: var(--fg_faded);
}

.replying-to {
  color: var(--fg_faded);
  margin: -2px 0 4px;

  a {
    pointer-events: all;
  }
}

.retweet-header,
.pinned,
.tweet-stats {
  align-content: center;
  color: var(--grey);
  display: flex;
  flex-shrink: 0;
  flex-wrap: wrap;
  font-size: 14px;
  font-weight: 600;
  line-height: 22px;

  span {
    @include ellipsis;
  }
}

.retweet-header {
  margin-top: -5px !important;
}

.tweet-stats {
  margin-bottom: -3px;
  user-select: none;
  -webkit-user-select: none;
}

.tweet-stat {
  padding-top: 5px;
  min-width: 1em;
  margin-right: 0.8em;
}

.show-thread {
  display: block;
  pointer-events: all;
  padding-top: 2px;
}

.unavailable-box {
  width: 100%;
  height: 100%;
  padding: 12px;
  border: solid 1px var(--dark_grey);
  box-sizing: border-box;
  border-radius: 10px;
  background-color: var(--bg_color);
  z-index: 2;
}

.tweet-link {
  height: 100%;
  width: 100%;
  left: 0;
  top: 0;
  position: absolute;
  user-select: none;
  -webkit-user-select: none;

  &:hover {
    background-color: var(--bg_hover);
  }
}

.latest-post-version {
  border-bottom: 1px solid var(--dark_grey);
  border-top: 1px solid var(--dark_grey);
  padding: 01ch 0px;
  margin: 1ch 0px;
  color: var(--grey);

  a {
    pointer-events: all;
  }
}

.community-note {
  background-color: var(--bg_elements);
  margin-top: 10px;
  border: solid 1px var(--dark_grey);
  border-radius: 10px;
  overflow: hidden;
  pointer-events: all;

  &:hover {
    background-color: var(--bg_panel);
    border-color: var(--grey);
  }
}

.community-note-header {
  background-color: var(--bg_hover);
  font-weight: 700;
  padding: 8px 10px;
  padding-top: 6px;
  display: flex;
  align-items: center;
  gap: 2px;

  .icon-container {
    flex-shrink: 0;
    color: var(--accent);
  }
}

.community-note-text {
  white-space: pre-line;
  padding: 10px 10px;
  padding-top: 6px;
}

.disclosures {
  display: flex;
  flex-direction: column;
  color: var(--grey);
  font-size: 14px;
  margin-top: 4px;
  margin-bottom: -2px;

  .icon-attention-circled {
    margin-right: -3px;
  }
}



================================================
FILE: src/sass/tweet/card.scss
================================================
@import "_variables";
@import "_mixins";

.card {
  margin: 5px 0;
  pointer-events: all;
  max-height: unset;
}

.card-container {
  border: solid 1px var(--dark_grey);
  border-radius: 10px;
  background-color: var(--bg_elements);
  overflow: hidden;
  color: inherit;
  display: flex;
  flex-direction: row;
  text-decoration: none !important;

  &:hover {
    border-color: var(--grey);
  }

  .attachments {
    margin: 0;
    border-radius: 0;
  }
}

.card-content {
  padding: 0.5em;
}

.card-title {
  @include ellipsis;
  white-space: unset;
  font-weight: bold;
  font-size: 1.1em;
}

.card-description {
  margin: 0.3em 0;
  white-space: pre-wrap;
}

.card-destination {
  @include ellipsis;
  color: var(--grey);
  display: block;
}

.card-content-container {
  color: unset;
  overflow: auto;

  &:hover {
    text-decoration: none;
  }
}

.card-image-container {
  width: 98px;
  flex-shrink: 0;
  position: relative;
  overflow: hidden;

  &:before {
    content: "";
    display: block;
    padding-top: 100%;
  }
}

.card-image {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: var(--bg_overlays);

  img {
    width: 100%;
    height: 100%;
    max-height: 400px;
    display: block;
    object-fit: cover;
  }
}

.card-overlay {
  @include play-button;
  opacity: 0.8;
  display: flex;
  justify-content: center;
  align-items: center;
}

.large {
  .card-container {
    display: block;
  }

  .card-image-container {
    width: unset;

    &:before {
      display: none;
    }
  }

  .card-image {
    position: unset;
    border-style: solid;
    border-color: var(--dark_grey);
    border-width: 0;
    border-bottom-width: 1px;
  }
}



================================================
FILE: src/sass/tweet/embed.scss
================================================
@import "_variables";
@import "_mixins";

.embed-video {
  .gallery-video {
    width: 100%;
    height: 100%;
    position: absolute;
    background-color: black;
    top: 0%;
    left: 0%;
  }

  .gallery-video > .attachment {
    max-height: unset;
  }
}



================================================
FILE: src/sass/tweet/media.scss
================================================
@import "_variables";

.gallery-row {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  overflow: hidden;
  flex-grow: 1;
  max-height: 379.5px;
  max-width: 533px;
  pointer-events: all;

  &.mixed-row {
    .attachment {
      min-width: 0;
      min-height: 0;
      flex: 1 1 0;
      max-height: 379.5px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #101010;
    }

    .still-image,
    .still-image img,
    .attachment > video,
    .attachment > img {
      width: 100%;
      height: 100%;
      max-width: none;
      max-height: none;
    }

    .still-image {
      display: flex;
      align-self: stretch;
    }

    .still-image img {
      flex-basis: auto;
      flex-grow: 0;
      object-fit: cover;
    }

    .attachment > video,
    .attachment > img {
      object-fit: cover;
    }

    .attachment > video {
      object-fit: contain;
    }
  }
}

.attachments {
  margin-top: 0.35em;
  display: flex;
  flex-direction: row;
  width: 100%;
  max-height: 600px;
  border-radius: 7px;
  overflow: hidden;
  flex-flow: column;
  background-color: var(--bg_color);
  align-items: center;
  pointer-events: all;
}

.attachment {
  position: relative;
  line-height: 0;
  overflow: hidden;
  margin: 0 0.25em 0 0;
  flex-grow: 1;
  box-sizing: border-box;
  min-width: 2em;

  &:last-child {
    margin: 0;
    max-height: 530px;
  }
}

.media-gif {
  display: table;
  background-color: unset;
  width: unset;
  max-height: unset;
}

.media-gif video,
.media-gif img {
  width: 100%;
  height: 100%;
  max-height: 530px;
  background-color: #101010;
}

.still-image {
  max-height: 379.5px;
  max-width: 533px;

  img {
    object-fit: cover;
    max-width: 100%;
    max-height: 379.5px;
    flex-basis: 300px;
    flex-grow: 1;
  }
}

.alt-text {
  margin: 0px;
  padding: 11px 7px;
  box-sizing: border-box;
  position: absolute;
  bottom: 10px;
  left: 10px;
  width: 2.98em;
  max-height: 25px;
  white-space: pre;
  overflow: hidden;
  border-radius: 10px;
  color: var(--fg_color);
  font-size: 12px;
  font-weight: bold;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(12px);
}

.alt-text:hover {
  padding: 7px;
  width: Min(230px, calc(100% - 10px * 2));
  max-height: calc(100% - 10px);
  line-height: 1.2em;
  white-space: pre-wrap;
  transition-duration: 0.4s;
  transition-property: max-height;
}

.overlay-circle {
  border-radius: 50%;
  background-color: var(--dark_grey);
  width: 40px;
  height: 40px;
  align-items: center;
  display: flex;
  border-width: 5px;
  border-color: var(--play_button);
  border-style: solid;
}

.overlay-triangle {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 12px 0 12px 17px;
  border-color: transparent transparent transparent var(--play_button);
  margin-left: 14px;
}

.media-body {
  flex: 1;
  padding: 0;
  white-space: pre-wrap;
}



================================================
FILE: src/sass/tweet/poll.scss
================================================
@import "_variables";

.poll-meter {
  overflow: hidden;
  position: relative;
  margin: 6px 0;
  height: 26px;
  background: var(--bg_color);
  border-radius: 5px;
  display: flex;
  align-items: center;
}

.poll-choice-bar {
  height: 100%;
  position: absolute;
  background: var(--dark_grey);
}

.poll-choice-value {
  position: relative;
  font-weight: bold;
  margin-left: 5px;
  margin-right: 6px;
  min-width: 30px;
  text-align: right;
  pointer-events: all;
}

.poll-choice-option {
  position: relative;
  pointer-events: all;
}

.poll-info {
  color: var(--grey);
  pointer-events: all;
}

.leader .poll-choice-bar {
  background: var(--accent_dark);
}



================================================
FILE: src/sass/tweet/quote.scss
================================================
@import "_variables";

.quote {
  margin-top: 10px;
  border: solid 1px var(--dark_grey);
  border-radius: 10px;
  background-color: var(--bg_elements);
  overflow: hidden;
  pointer-events: all;
  position: relative;
  width: 100%;

  &:hover {
    border-color: var(--grey);
  }

  &.unavailable:hover {
    border-color: var(--dark_grey);
  }

  .tweet-name-row {
    padding: 8px 10px 6px 10px;
  }

  .quote-text {
    overflow: hidden;
    white-space: pre-wrap;
    word-wrap: break-word;
    padding: 10px;
    padding-top: 0;
  }

  .show-thread {
    padding: 0px 10px 6px 10px;
    margin-top: -6px;
  }

  .quote-latest {
    padding: 0px 10px 6px 10px;
    color: var(--grey);
  }

  .replying-to {
    padding: 0px 10px;
    padding-bottom: 4px;
    margin: unset;
  }

  .community-note {
    background-color: var(--bg_panel);
    border: unset;
    border-top: solid 1px var(--dark_grey);
    border-radius: unset;
    margin-top: 0;

    &:hover {
      border-top-color: var(--grey);
    }

    .community-note-header {
      background-color: var(--bg_panel);
      padding-bottom: 0;
    }
  }
}

.unavailable-quote {
  padding: 12px;
  display: block;
}

.quote-link {
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  position: absolute;
}

.quote-media-container {
  max-height: 300px;
  display: flex;

  .card {
    margin: unset;
  }

  .attachments {
    border-radius: 0;
  }

  .media-gif {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .media-gif > .attachment {
    display: flex;
    justify-content: center;
    background-color: var(--bg_color);

    video,
    img {
      height: unset;
      width: unset;
      max-height: 100%;
      max-width: 100%;
    }
  }

  .gallery-row .attachment,
  .gallery-row .attachment > video,
  .gallery-row .attachment > img {
    max-height: 300px;
  }

  .still-image img {
    max-height: 250px;
  }
}



================================================
FILE: src/sass/tweet/thread.scss
================================================
@import "_variables";
@import "_mixins";

.conversation,
.edit-history {
  @include panel(100%, 600px);

  .show-more {
    margin-bottom: 10px;
  }
}

.main-thread,
.latest-edit {
  margin-bottom: 20px;
}

.reply {
  margin-bottom: 10px;
}

.main-tweet,
.replies,
.edit-history > div {
  body.fixed-nav & {
    padding-top: 50px;
    margin-top: -50px;
  }
}

.edit-history-header {
  padding: 10px;
  margin-bottom: 5px;
  font-size: 16px;
  font-weight: bold;
  background-color: var(--bg_panel);
}

.tweet-edit {
  margin-bottom: 5px;
}

.main-tweet .tweet-content {
  font-size: 18px;
}

@media (max-width: 600px) {
  .main-tweet .tweet-content {
    font-size: 16px;
  }
}

.thread-line {
  .timeline-item::before,
  &.timeline-item::before {
    background: var(--accent_dark);
    content: "";
    position: relative;
    min-width: 3px;
    width: 3px;
    left: 26px;
    border-radius: 2px;
    margin-left: -3px;
    margin-bottom: 37px;
    top: 56px;
    z-index: 1;
    pointer-events: none;
  }

  .with-header:not(:first-child)::after {
    background: var(--accent_dark);
    content: "";
    position: relative;
    float: left;
    min-width: 3px;
    width: 3px;
    right: calc(100% - 26px);
    border-radius: 2px;
    margin-left: -3px;
    margin-bottom: 37px;
    bottom: 10px;
    height: 30px;
    z-index: 1;
    pointer-events: none;
  }

  .unavailable::before {
    top: 48px;
    margin-bottom: 28px;
  }

  .more-replies::before {
    content: "...";
    background: unset;
    color: var(--more_replies_dots);
    font-weight: bold;
    font-size: 20px;
    line-height: 0.25em;
    left: 1.2em;
    width: 5px;
    top: 2px;
    margin-bottom: 0;
    margin-left: -2.5px;
  }

  .earlier-replies {
    padding-bottom: 0;
    margin-bottom: -5px;
  }
}

.timeline-item.thread-last::before {
  background: unset;
  min-width: unset;
  width: 0;
  margin: 0;
}

.more-replies {
  padding-top: 0.3em !important;
}

.more-replies-text {
  @include ellipsis;
  display: block;
  margin-left: 58px;
  padding: 7px 0;
}

.timeline-item.thread.more-replies-thread {
  padding: 0 0.75em;

  &::before {
    top: 40px;
    margin-bottom: 31px;
  }

  .more-replies {
    display: flex;
    padding-top: unset !important;
    margin-top: 8px;

    &::before {
      display: inline-block;
      position: relative;
      top: -1px;
      line-height: 0.4em;
    }

    .more-replies-text {
      display: inline;
    }
  }
}



================================================
FILE: src/sass/tweet/video.scss
================================================
@import "_variables";
@import "_mixins";

video {
  height: 100%;
  width: 100%;
}

.gallery-video {
  display: flex;
  overflow: hidden;
  
  &.card-container {
    flex-direction: column;
    width: 100%;
  }

  > .attachment {
    min-height: 80px;
    min-width: 200px;
    max-height: 530px;
    margin: 0;

    img {
      max-height: 100%;
      max-width: 100%;
    }
  }
}

.video-download {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 2;
  color: var(--accent);
  text-decoration: none;
  opacity: 0;
  transition: opacity 0.2s;
  filter: drop-shadow(0 1px 2px rgba(0, 0, 0, 0.7));

  .icon-container {
    margin: 0;
  }

  .icon-download-alt {
    font-size: 18px;
  }
}

.attachment:hover .video-download {
  opacity: 1;

  &:hover {
    color: var(--fg_color);
  }
}

@media (hover: none) {
  .video-download {
    opacity: 1;
  }
}

.video-overlay {
  @include play-button;
  background-color: $shadow;

  p {
    position: relative;
    z-index: 0;
    text-align: center;
    top: calc(50% - 20px);
    font-size: 20px;
    line-height: 1.3;
    margin: 0 20px;
  }

  .overlay-circle {
    position: relative;
    z-index: 0;
    top: calc(50% - 20px);
    margin: 0 auto;
    width: 40px;
    height: 40px;
  }

  .overlay-duration {
    position: absolute;
    bottom: 8px;
    left: 8px;
    background-color: #0000007a;
    line-height: 1em;
    padding: 4px 6px 4px 6px;
    border-radius: 5px;
    font-weight: bold;
  }

  form {
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
    display: flex;
  }

  button {
    padding: 5px 8px;
    font-size: 16px;
  }
}



================================================
FILE: src/views/about.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import os, strformat
import karax/[karaxdsl, vdom]

const
  date = staticExec("git show -s --format=\"%cd\" --date=format:\"%Y.%m.%d\"")
  hash = staticExec("git show -s --format=\"%h\"")
  link = "https://github.com/zedeus/nitter/commit/" & hash
  version = &"{date}-{hash}"

var aboutHtml: string

proc initAboutPage*(dir: string) =
  try:
    aboutHtml = readFile(dir/"md/about.html")
  except IOError:
    stderr.write (dir/"md/about.html") & " not found, please run `nimble md`\n"
    aboutHtml = "<h1>About page is missing</h1><br><br>"

proc renderAbout*(): VNode =
  buildHtml(tdiv(class="overlay-panel")):
    verbatim aboutHtml
    h2: text "Instance info"
    p:
      text "Version "
      a(href=link): text version



================================================
FILE: src/views/about_account.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, times
import karax/[karaxdsl, vdom]

import renderutils
import ".."/[types, formatters]

proc renderAboutAccount*(info: AccountInfo): VNode =
  let user = User(
    username: info.username,
    fullname: info.fullname,
    userPic: info.userPic,
    verifiedType: info.verifiedType
  )

  buildHtml(tdiv(class="about-account")):
    tdiv(class="about-account-header"):
      a(class="about-account-avatar", href=(&"/{info.username}")):
        genImg(getUserPic(info.userPic, "_200x200"))
      tdiv(class="about-account-name"):
        linkUser(user, class="profile-card-fullname")
        verifiedIcon(user)
      linkUser(user, class="profile-card-username")

    tdiv(class="about-account-body"):
      tdiv(class="about-account-row"):
        span: icon "calendar"
        tdiv:
          span(class="about-account-label"): text "Date joined"
          span(class="about-account-value"):
            text info.joinDate.format("MMMM YYYY")

      if info.basedIn.len > 0:
        tdiv(class="about-account-row"):
          span: icon "location"
          tdiv:
            span(class="about-account-label"): text "Account based in"
            span(class="about-account-value"): text info.basedIn

      if info.verifiedType != VerifiedType.none:
        if info.overrideVerifiedYear != 0:
          tdiv(class="about-account-row"):
            span: icon "ok"
            tdiv:
              span(class="about-account-label"): text "Verified"
              span(class="about-account-value"):
                let year = abs(info.overrideVerifiedYear)
                let era = if info.overrideVerifiedYear < 0: " BCE" else: ""
                text "Since " & $year & era
        elif info.verifiedSince.year > 0:
          tdiv(class="about-account-row"):
            span: icon "ok"
            tdiv:
              span(class="about-account-label"): text "Verified"
              span(class="about-account-value"):
                text "Since " & info.verifiedSince.format("MMMM YYYY")

        if info.isIdentityVerified:
          tdiv(class="about-account-row"):
            span: icon "ok"
            tdiv:
              span(class="about-account-label"): text "ID Verified"
              span(class="about-account-value"): text "Yes"

      if info.affiliateUsername.len > 0:
        tdiv(class="about-account-row"):
          span: icon "group"
          tdiv:
            span(class="about-account-label"): text "An affiliate of"
            span(class="about-account-value"):
              a(href=(&"/{info.affiliateUsername}")):
                if info.affiliateLabel.len > 0:
                  text info.affiliateLabel & " (@" & info.affiliateUsername & ")"
                else:
                  text "@" & info.affiliateUsername

      if info.usernameChanges > 0:
        tdiv(class="about-account-row"):
          span(class="about-account-at"): text "@"
          tdiv:
            span(class="about-account-label"):
              text $info.usernameChanges & " username change"
              if info.usernameChanges > 1: text "s"
            if info.lastUsernameChange.year > 0:
              span(class="about-account-value"):
                text "Last on " & info.lastUsernameChange.format("MMMM YYYY")

      if info.source.len > 0:
        tdiv(class="about-account-row"):
          span: icon "link"
          tdiv:
            span(class="about-account-label"): text "Connected via"
            span(class="about-account-value"): text info.source



================================================
FILE: src/views/article.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, tables, unicode, bitops, uri
import karax/[karaxdsl, vdom]

import renderutils, tweet, timeline
import ".."/[types, utils, formatters]

proc renderAtomicParagraph(paragraph: ArticleParagraph; article: Article;
                           tweets: Table[int64, Tweet]; path: string;
                           prefs: Prefs): VNode =
  if paragraph.entityRanges.len == 0:
    return text ""

  let er = paragraph.entityRanges[0]
  if er.key notin article.entities:
    return text ""

  let entity = article.entities[er.key]

  case entity.kind
  of "MEDIA":
    buildHtml(tdiv(class="article-media")):
      for id in entity.mediaIds:
        let media = article.media.getOrDefault(id)
        if media.url.len == 0:
          continue
        case media.kind
        of "ApiGif":
          video(src=getVidUrl(media.url), controls="", autoplay="", loop="",
                muted="")
        of "ApiVideo":
          video(src=getVidUrl(media.url), controls="")
        else:
          a(href=getOrigPicUrl(media.url), target="_blank"):
            img(src=getSmallPic(media.url), alt="", loading="lazy")
  of "TWEET":
    let tweet = tweets.getOrDefault(
      try: parseBiggestInt(entity.tweetId)
      except ValueError: 0, nil)
    if tweet != nil:
      renderTweet(tweet, prefs, path)
    else:
      text ""
  of "MARKDOWN":
    var content = entity.markdown
    if content.startsWith("```"):
      let firstNl = content.find('\n')
      if firstNl >= 0: content = content[firstNl + 1 .. ^1]
      if content.endsWith("```"): content = content[0 .. ^4]
      content = content.strip
    buildHtml(pre()):
      code(): text content
  of "DIVIDER":
    buildHtml(hr(class="article-divider"))
  else:
    text ""

proc wrapStyle(node: VNode; style: int): VNode =
  result = node
  if style.testBit(4): result = buildHtml(code()): result
  if style.testBit(0): result = buildHtml(strong()): result
  if style.testBit(1): result = buildHtml(em()): result
  if style.testBit(2): result = buildHtml(del()): result
  if style.testBit(3): result = buildHtml(underlined()): result

proc addContent(target: VNode; content: string; style = 0) =
  var first = true
  for line in content.split('\n'):
    if not first:
      target.add VNode(kind: VNodeKind.br)
    first = false
    var pos = 0
    while pos < line.len:
      let atPos = line.find('@', pos)
      if atPos == -1:
        target.add wrapStyle(text line[pos .. ^1], style)
        break
      if atPos > 0 and line[atPos - 1] in Letters + Digits + {'_'}:
        target.add wrapStyle(text line[pos .. atPos], style)
        pos = atPos + 1
        continue
      var j = atPos + 1
      while j < line.len and j - atPos - 1 < 15 and
            line[j] in Letters + Digits + {'_'}:
        inc j
      if j == atPos + 1:
        target.add wrapStyle(text line[pos .. atPos], style)
        pos = atPos + 1
        continue
      if atPos > pos:
        target.add wrapStyle(text line[pos ..< atPos], style)
      let username = line[atPos + 1 ..< j]
      let link = a.newVNode()
      link.setAttr("href", "/" & username)
      link.add wrapStyle(text ("@" & username), style)
      target.add link
      pos = j

proc applyInlineStyles(target: VNode; runes: seq[Rune]; start, length: int;
                       styles: seq[ArticleStyle]) =
  if styles.len == 0:
    target.addContent($runes[start ..< start + length])
    return

  var
    lastStyle = 0
    lastStart = start
  let endPos = start + length

  for i in start ..< endPos:
    var style = 0
    for sr in styles:
      let
        sStart = sr.offset
        sEnd = sStart + sr.length
      if sStart <= i and sEnd > i:
        case sr.style
        of "Bold": style.setBit(0)
        of "Italic": style.setBit(1)
        of "Strikethrough": style.setBit(2)
        of "Underline": style.setBit(3)
        of "Code": style.setBit(4)
        else: discard

    if style != lastStyle:
      if i > lastStart:
        addContent(target, $runes[lastStart ..< i], lastStyle)
      lastStyle = style
      lastStart = i

  if lastStart < endPos:
    addContent(target, $runes[lastStart ..< endPos], lastStyle)

proc renderTextParagraph(paragraph: ArticleParagraph; article: Article): VNode =
  let text = paragraph.text

  result = case paragraph.kind
    of "header-one": h1.newVNode()
    of "header-two": h2.newVNode()
    of "header-three": h3.newVNode()
    of "ordered-list-item", "unordered-list-item": li.newVNode()
    of "blockquote": VNode(kind: VNodeKind.blockquote)
    of "code-block":
      let pre = pre.newVNode()
      let code = code.newVNode()
      code.add text text
      pre.add code
      return pre
    else: p.newVNode()

  let
    runes = text.toRunes
    textLen = runes.len
  var last = 0
  for er in paragraph.entityRanges:
    if er.offset > last:
      applyInlineStyles(result, runes, last, er.offset - last,
                        paragraph.inlineStyles)

    last = er.offset + er.length

    var target = result
    if er.key in article.entities:
      let entity = article.entities[er.key]
      if entity.kind == "LINK":
        let parsed = parseUri(entity.url)
        if parsed.scheme in ["http", "https"]:
          target = a.newVNode()
          if parsed.isTwitterUrl:
            target.setAttr("href", parsed.path)
          else:
            target.setAttr("href", entity.url)

    applyInlineStyles(target, runes, er.offset, er.length,
                      paragraph.inlineStyles)
    if target != result:
      result.add target

  if last < textLen:
    applyInlineStyles(result, runes, last, textLen - last,
                      paragraph.inlineStyles)

  if paragraph.kind == "blockquote" and result.len > 0:
    let lastChild = result[result.len - 1]
    if lastChild.kind == VNodeKind.strong and lastChild.len > 0 and
       lastChild[0].kind == VNodeKind.text:
      lastChild.setAttr("class", "blockquote-attribution")

proc renderArticle*(article: Article; tweets: Table[int64, Tweet];
                    path: string; prefs: Prefs; tweetId=""): VNode =
  let author = article.user

  let main = buildHtml(article(class="article-body")):
    h1(class="article-title"): text article.title

    tdiv(class="article-author"):
      tdiv(class="article-author-row"):
        a(class="article-avatar", href=("/" & author.username)):
          genImg(author.getUserPic("_bigger"), class=prefs.getAvatarClass)
        tdiv(class="article-author-info"):
          tdiv(class="article-author-name"):
            linkUser(author, class="fullname")
            verifiedIcon(author)
          tdiv(class="article-author-meta"):
            linkUser(author, class="username")
            span(class="article-date-sep"): text " · "
            a(class="article-date",
              href=("/" & author.username & "/status/" & tweetId)):
              text article.time.getShortTime
      if not prefs.hideTweetStats:
        renderStats(article.stats)

  var listKind = ""
  var list: VNode = nil

  for paragraph in article.paragraphs:
    let isListItem = paragraph.kind in [
      "ordered-list-item", "unordered-list-item"]

    if not isListItem and list != nil:
      main.add list
      list = nil
      listKind = ""

    if paragraph.kind == "atomic":
      main.add renderAtomicParagraph(paragraph, article, tweets, path, prefs)
    elif isListItem:
      if paragraph.kind != listKind:
        if list != nil:
          main.add list
        list = if paragraph.kind == "ordered-list-item": ol.newVNode()
               else: ul.newVNode()
        listKind = paragraph.kind
      list.add renderTextParagraph(paragraph, article)
    else:
      main.add renderTextParagraph(paragraph, article)

  if list != nil:
    main.add list

  buildHtml(tdiv(class="article-page")):
    if article.coverImage.len > 0:
      a(href=getOrigPicUrl(article.coverImage), target="_blank"):
        img(class="article-cover", src=getSmallPic(article.coverImage), alt="")
    main
    renderToTop()



================================================
FILE: src/views/broadcast.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, times
import karax/[karaxdsl, vdom]

import renderutils
import ".."/[types, utils, formatters]

proc renderBroadcast*(bc: Broadcast; prefs: Prefs; path: string): VNode =
  let
    isLive = bc.state == "RUNNING"
    thumb = getPicUrl(bc.thumb)
    source = if prefs.proxyVideos and bc.m3u8Url.startsWith("http"):
               getVidUrl(bc.m3u8Url) else: bc.m3u8Url
    stateText =
      if isLive: "LIVE"
      elif bc.endTime.year > 1: "Ended " & bc.endTime.format("MMM d, YYYY")
      elif bc.state.len > 0: bc.state
      else: "Ended"
    durationMs =
      if bc.startTime.year > 1 and bc.endTime.year > 1:
        int((bc.endTime - bc.startTime).inMilliseconds) - bc.replayStart * 1000
      else: 0
    duration = if durationMs > 0: getDuration(durationMs) else: ""

  buildHtml(tdiv(class="broadcast-page")):
    tdiv(class="broadcast-panel"):
      tdiv(class="broadcast-player"):
        if bc.m3u8Url.len > 0 and prefs.hlsPlayback:
          video(poster=thumb, data-url=source, data-autoload="false",
                data-start=($bc.replayStart), muted=prefs.muteVideos)
          verbatim "<div class=\"video-overlay\" onclick=\"playVideo(this)\">"
          tdiv(class="overlay-circle"): span(class="overlay-triangle")
          if isLive:
            tdiv(class="broadcast-live"): text "LIVE"
          elif duration.len > 0:
            tdiv(class="overlay-duration"): text duration
          verbatim "</div>"
        elif bc.m3u8Url.len > 0:
          img(src=thumb, alt=bc.title)
          tdiv(class="video-overlay"):
            buttonReferer "/enablehls", "Enable hls playback", path
            if isLive:
              tdiv(class="broadcast-live"): text "LIVE"
            elif duration.len > 0:
              tdiv(class="overlay-duration"): text duration
        elif bc.thumb.len > 0:
          img(src=thumb, alt=bc.title)
          tdiv(class="video-overlay"):
            if bc.availableForReplay:
              p: text "Stream unavailable"
            else:
              p: text "Replay is not available"
        else:
          tdiv(class="video-overlay"):
            p: text "Broadcast not found"

      tdiv(class="broadcast-info"):
        h2(class="broadcast-title"): text bc.title

        tdiv(class="broadcast-user-row"):
          a(class="broadcast-user", href=("/" & bc.user.username)):
            genImg(getUserPic(bc.user.userPic, "_bigger"))
            tdiv:
              tdiv:
                strong: text bc.user.fullname
                verifiedIcon(bc.user)
              span(class="broadcast-username"): text "@" & bc.user.username

          tdiv(class="broadcast-meta"):
            if bc.totalWatched > 0: 
              span: text insertSep($bc.totalWatched, ',') & " views"
            if isLive:
              span(class="broadcast-live"): text stateText
            else:
              span: text stateText



================================================
FILE: src/views/community.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, times
import karax/[karaxdsl, vdom]

import renderutils
import ".."/[types, utils, formatters]

proc renderCommunityTabs*(kind: QueryKind; community: Community): VNode =
  let
    path = &"/i/communities/{community.id}"
    q = Query(kind: kind)
  buildHtml(tdiv):
    ul(class="tab"):
      li(class=q.getTabClass(posts)):
        a(href=path): text "Top"
      li(class=q.getTabClass(replies)):
        a(href=(path & "/latest")): text "Latest"
      li(class=q.getTabClass(media)):
        a(href=(path & "/media")): text "Media"
      li(class=q.getTabClass(userList)):
        a(href=(path & "/about")): text "About"
    if community.hashtags.len > 0:
      tdiv(class="community-tags"):
        for tag in community.hashtags:
          let bare = tag.strip(chars={'#'})
          a(class="community-tag",
            href=(&"/i/communities/{community.id}/hashtag/{bare}")):
            text tag

proc renderMemberTabs*(community: Community; isModerators: bool): VNode =
  let path = &"/i/communities/{community.id}"
  buildHtml(ul(class="tab")):
    li(class=(if not isModerators: "tab-item active" else: "tab-item")):
      a(href=(path & "/members")): text "All"
    li(class=(if isModerators: "tab-item active" else: "tab-item")):
      a(href=(path & "/moderators")): text "Moderators"

proc renderHashtagHeader*(community: Community; tag: string): VNode =
  buildHtml(tdiv(class="community-hashtag-header")):
    h2(class="community-hashtag-title"): text "#" & tag

proc renderCommunityAbout*(community: Community; moderators: seq[User]): VNode =
  buildHtml(tdiv(class="community-about")):
    tdiv(class="community-info"):
      h2: text "Community Info"
      tdiv(class="community-info-item"):
        icon "group"
        if community.joinPolicy == "Open":
          text "Anyone can join this Community."
        else:
          text "Membership is by approval only."

      tdiv(class="community-info-item"):
        icon "info"
        text "All Communities are publicly visible."

      tdiv(class="community-info-item"):
        icon "calendar"
        let
          date = community.createdAt.format("MMMM d, yyyy")
          creator = community.creator.username
        span:
          text &"Created {date} by "
          a(href=(&"/{creator}")): text &"@{creator}"
          if community.creator.verifiedType != none:
            verifiedIcon(community.creator)

    if community.rules.len > 0:
      tdiv(class="community-rules"):
        h2: text "Rules"
        p(class="community-rules-intro"):
          text "These are set and enforced by Community admins and are in addition to "
          a(href="https://help.x.com/rules-and-policies/x-rules"): text "X's rules"
          text "."

        for i, rule in community.rules:
          tdiv(class="community-rule"):
            span(class="community-rule-number"): text $(i + 1)
            tdiv(class="community-rule-content"):
              strong: text rule.name
              if rule.description.len > 0:
                p: text rule.description

    if moderators.len > 0:
      tdiv(class="community-moderators"):
        h2:
          text "Moderators"
          a(class="community-mods-link",
            href=(&"/i/communities/{community.id}/moderators")):
            text "See all"
        for user in moderators:
          tdiv(class="community-moderator"):
            a(href=(&"/{user.username}")):
              genImg(user.getUserPic("_bigger"), class="community-mod-avatar")
            tdiv(class="community-mod-info"):
              a(href=(&"/{user.username}"), class="community-mod-name"):
                text user.fullname
                if user.verifiedType != none:
                  verifiedIcon(user)
              a(href=(&"/{user.username}"), class="community-mod-username"):
                text &"@{user.username}"

proc renderCommunity*(body, nav: VNode; community: Community): VNode =
  buildHtml(tdiv(class="timeline-container")):
    if community.banner.len > 0:
      tdiv(class="timeline-banner"):
        a(href=getPicUrl(community.banner), target="_blank"):
          genImg(community.banner)

    tdiv(class="community-header"):
      h1(class="community-name"):
        a(href=(&"/i/communities/{community.id}")): text community.name

      if community.category.len > 0:
        span(class="community-category"): text community.category

      if community.description.len > 0:
        tdiv(class="community-description"):
          text community.description

      tdiv(class="community-stats"):
        a(class="community-member-count",
          href=(&"/i/communities/{community.id}/members")):
          text insertSep($community.memberCount, ',')
          text " Members"

    nav
    body



================================================
FILE: src/views/embed.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import options
import karax/[karaxdsl, vdom]
from jester import Request

import ".."/[types, formatters]
import general, tweet

const doctype = "<!DOCTYPE html>\n"

proc renderVideoEmbed*(tweet: Tweet; cfg: Config; req: Request): string =
  let 
    video = tweet.getVideos()[0]
    thumb = video.thumb
    vidUrl = getVideoEmbed(cfg, tweet.id)
    prefs = Prefs(hlsPlayback: true, mp4Playback: true)

  let node = buildHtml(html(lang="en")):
    renderHead(prefs, cfg, req, video=vidUrl, images=(@[thumb]))

    body:
      tdiv(class="embed-video"):
        renderVideo(video, prefs, "")

  result = doctype & $node



================================================
FILE: src/views/feature.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import karax/[karaxdsl, vdom]

proc renderFeature*(): VNode =
  buildHtml(tdiv(class="overlay-panel")):
    h1: text "Unsupported feature"
    p:
      text "Nitter doesn't support this feature yet, but it might in the future. "
      text "You can check for an issue and open one if needed here: "
      a(href="https://github.com/zedeus/nitter/issues"):
        text "https://github.com/zedeus/nitter/issues"
    p:
      text "To find out more about the Nitter project, see the "
      a(href="/about"): text "About page"



================================================
FILE: src/views/general.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import uri, strutils, strformat
import karax/[karaxdsl, vdom]

import renderutils
import ../utils, ../types, ../prefs, ../formatters

import jester

const
  doctype = "<!DOCTYPE html>\n"
  lp = readFile("public/lp.svg")

proc toTheme(theme: string): string =
  theme.toLowerAscii.replace(" ", "_")

proc renderNavbar(cfg: Config; req: Request; rss, canonical: string): VNode =
  var path = req.params.getOrDefault("referer")
  if path.len == 0:
    path = $(parseUri(req.path) ? filterParams(req.params))
    if "/status/" in path: path.add "#m"

  buildHtml(nav):
    tdiv(class="inner-nav"):
      tdiv(class="nav-item"):
        a(class="site-name", href="/"): text cfg.title

      a(href="/"): img(class="site-logo", src="/logo.png", alt="Logo")

      tdiv(class="nav-item right"):
        icon "search", title="Search", href="/search"
        if rss.len > 0:
          icon "rss", title="RSS Feed", href=rss
        icon "bird", title="Open in X", href=canonical
        a(href="https://liberapay.com/zedeus"): verbatim lp
        icon "info", title="About", href="/about"
        icon "cog", title="Preferences", href=("/settings?referer=" & encodeUrl(path))

proc renderHead*(prefs: Prefs; cfg: Config; req: Request; titleText=""; desc="";
                 video=""; images: seq[string] = @[]; banner=""; ogTitle="";
                 rss=""; alternate=""): VNode =
  let theme = prefs.theme.toTheme
    
  let ogType =
    if video.len > 0: "video"
    elif rss.len > 0: "object"
    elif images.len > 0: "photo"
    else: "article"

  let opensearchUrl = getUrlPrefix(cfg) & "/opensearch"

  buildHtml(head):
    link(rel="stylesheet", type="text/css", href="/css/style.css?v=44")
    link(rel="stylesheet", type="text/css", href="/css/fontello.css?v=7")

    if theme.len > 0:
      link(rel="stylesheet", type="text/css", href=(&"/css/themes/{theme}.css"))

    link(rel="apple-touch-icon", sizes="180x180", href="/apple-touch-icon.png")
    link(rel="icon", type="image/png", sizes="32x32", href="/favicon-32x32.png")
    link(rel="icon", type="image/png", sizes="16x16", href="/favicon-16x16.png")
    link(rel="manifest", href="/site.webmanifest")
    link(rel="mask-icon", href="/safari-pinned-tab.svg", color="#ff6c60")
    link(rel="search", type="application/opensearchdescription+xml", title=cfg.title,
                            href=opensearchUrl)

    if alternate.len > 0:
      link(rel="alternate", href=alternate, title="View on X")

    if rss.len > 0:
      link(rel="alternate", type="application/rss+xml", href=rss, title="RSS feed")

    if prefs.hlsPlayback:
      script(src="/js/hls.min.js", `defer`="")
      script(src="/js/hlsPlayback.js?v=1", `defer`="")

    if prefs.infiniteScroll:
      script(src="/js/infiniteScroll.js", `defer`="")

    title:
      if titleText.len > 0:
        text titleText & " | " & cfg.title
      else:
        text cfg.title

    meta(name="viewport", content="width=device-width, initial-scale=1.0")
    meta(name="referrer", content="same-origin")
    meta(name="theme-color", content="#1F1F1F")
    meta(property="og:type", content=ogType)
    meta(property="og:title", content=(if ogTitle.len > 0: ogTitle else: titleText))
    meta(property="og:description", content=stripHtml(desc))
    meta(property="og:site_name", content="Nitter")
    meta(property="og:locale", content="en_US")

    if banner.len > 0 and not banner.startsWith('#'):
      let bannerUrl = getPicUrl(banner)
      link(rel="preload", type="image/png", href=bannerUrl, `as`="image")

    for url in images:
      if url.len == 0: continue
      let preloadUrl = if "400x400" in url: getPicUrl(url)
                       else: getSmallPic(url)
      link(rel="preload", type="image/png", href=preloadUrl, `as`="image")

      let image = getUrlPrefix(cfg) & getPicUrl(url)
      meta(property="og:image", content=image)
      meta(property="twitter:image:src", content=image)

      if rss.len > 0:
        meta(property="twitter:card", content="summary")
      else:
        meta(property="twitter:card", content="summary_large_image")

    if video.len > 0:
      meta(property="og:video:url", content=video)
      meta(property="og:video:secure_url", content=video)
      meta(property="og:video:type", content="text/html")

    # this is last so images are also preloaded
    # if this is done earlier, Chrome only preloads one image for some reason
    link(rel="preload", type="font/woff2", `as`="font",
         href="/fonts/fontello.woff2?59696369", crossorigin="anonymous")

proc renderMain*(body: VNode; req: Request; cfg: Config; prefs=defaultPrefs;
                 titleText=""; desc=""; ogTitle=""; rss=""; video="";
                 images: seq[string] = @[]; banner="";
                 twitterLink=""): string =

  let twitterLink =
    if twitterLink.len > 0: twitterLink
    else: getTwitterLink(req.path, req.params)

  let node = buildHtml(html(lang="en")):
    renderHead(prefs, cfg, req, titleText, desc, video, images, banner, ogTitle,
               rss, twitterLink)

    let bodyClass = if prefs.stickyNav: "fixed-nav" else: ""
    body(class=bodyClass):
      renderNavbar(cfg, req, rss, twitterLink)

      tdiv(class="container"):
        body

  result = doctype & $node

proc renderError*(error: string): VNode =
  buildHtml(tdiv(class="panel-container")):
    tdiv(class="error-panel"):
      span: verbatim error



================================================
FILE: src/views/list.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strformat
import karax/[karaxdsl, vdom]

import renderutils
import ".."/[types, utils]

proc renderListTabs*(query: Query; path: string): VNode =
  buildHtml(ul(class="tab")):
    li(class=query.getTabClass(posts)):
      a(href=(path)): text "Tweets"
    li(class=query.getTabClass(userList)):
      a(href=(path & "/members")): text "Members"

proc renderList*(body: VNode; query: Query; list: List): VNode =
  buildHtml(tdiv(class="timeline-container")):
    if list.banner.len > 0:
      tdiv(class="timeline-banner"):
        a(href=getPicUrl(list.banner), target="_blank"):
          genImg(list.banner)

    tdiv(class="timeline-header"):
      text &"\"{list.name}\" by @{list.username}"

      tdiv(class="timeline-description"):
        text list.description

    renderListTabs(query, &"/i/lists/{list.id}")
    body



================================================
FILE: src/views/opensearch.nimf
================================================
#? stdtmpl(subsChar = '$', metaChar = '#')
## SPDX-License-Identifier: AGPL-3.0-only
#proc generateOpenSearchXML*(name, hostname, url: string): string =
#  result = ""
<?xml version="1.0" encoding="UTF-8"?>
<OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/"
                       xmlns:moz="http://www.mozilla.org/2006/browser/search/">
  <ShortName>${name}</ShortName>
  <Description>Twitter search via ${hostname}</Description>
  <InputEncoding>UTF-8</InputEncoding>
  <Url type="text/html" template="${url}{searchTerms}" />
</OpenSearchDescription>
#end proc



================================================
FILE: src/views/preferences.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import tables, macros, strutils
import karax/[karaxdsl, vdom]

import renderutils
import ../types, ../prefs_impl

macro renderPrefs*(): untyped =
  result = nnkCall.newTree(
    ident("buildHtml"), ident("tdiv"), nnkStmtList.newTree())

  for header, options in prefList:
    result[2].add nnkCall.newTree(
      ident("legend"),
      nnkStmtList.newTree(
        nnkCommand.newTree(ident("text"), newLit(header))))

    for pref in options:
      let procName = ident("gen" & capitalizeAscii($pref.kind))
      let state = nnkDotExpr.newTree(ident("prefs"), ident(pref.name))
      var stmt = nnkStmtList.newTree(
        nnkCall.newTree(procName, newLit(pref.name), newLit(pref.label), state))

      case pref.kind
      of checkbox: discard
      of input: stmt[0].add newLit(pref.placeholder)
      of select:
        if pref.name == "theme":
          stmt[0].add ident("themes")
        else:
          stmt[0].add newLit(pref.options)

      result[2].add stmt

proc renderPreferences*(prefs: Prefs; path: string; themes: seq[string];
                        prefsUrl: string): VNode =
  buildHtml(tdiv(class="overlay-panel")):
    fieldset(class="preferences"):
      form(`method`="post", action="/saveprefs", autocomplete="off"):
        refererField path

        renderPrefs()

        legend: text "Bookmark"
        p(class="bookmark-note"):
          text "Save this URL to restore your preferences (?prefs works on all pages)"
        pre(class="prefs-code"):
          text prefsUrl
        p(class="bookmark-note"):
          verbatim "You can override preferences with query parameters (e.g. <code>?hlsPlayback=on</code>). These overrides aren't saved to cookies, and links won't retain the parameters. Intended for configuring RSS feeds and other cookieless environments. Hover over a preference to see its name."

        h4(class="note"):
          text "Preferences are stored client-side using cookies without any personal information."

        button(`type`="submit", class="pref-submit"):
          text "Save preferences"

      buttonReferer "/resetprefs", "Reset preferences", path, class="pref-reset"



================================================
FILE: src/views/profile.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat
import karax/[karaxdsl, vdom, vstyles]

import renderutils, search, timeline
import ".."/[types, utils, formatters]

proc renderStat(num: int; class: string; text=""): VNode =
  let t = if text.len > 0: text else: class
  buildHtml(li(class=class)):
    span(class="profile-stat-header"): text capitalizeAscii(t)
    span(class="profile-stat-num"):
      text insertSep($num, ',')

proc renderStatLink(num: int; class, href: string): VNode =
  buildHtml(li(class=class)):
    a(href=href):
      span(class="profile-stat-header"): text capitalizeAscii(class)
      span(class="profile-stat-num"):
        text insertSep($num, ',')

proc renderUserCard*(user: User; prefs: Prefs; info: AccountInfo): VNode =
  buildHtml(tdiv(class="profile-card")):
    tdiv(class="profile-card-info"):
      let
        url = getPicUrl(user.getUserPic())
        size =
          if prefs.autoplayGifs and user.userPic.endsWith("gif"): ""
          else: "_400x400"

      a(class="profile-card-avatar", href=url, target="_blank"):
        genImg(user.getUserPic(size))

      tdiv(class="profile-card-tabs-name"):
        linkUser(user, class="profile-card-fullname")
        verifiedIcon(user)
        linkUser(user, class="profile-card-username")

    tdiv(class="profile-card-extra"):
      if user.bio.len > 0:
        tdiv(class="profile-bio"):
          p(dir="auto"):
            verbatim replaceUrls(user.bio, prefs)

      if user.location.len > 0:
        tdiv(class="profile-location"):
          span: icon "location"
          let (place, url) = getLocation(user)
          if url.len > 1:
            a(href=url): text place
          elif "://" in place:
            a(href=place): text place
          else:
            span: text place

      if info.basedIn.len > 0:
        tdiv(class="profile-location"):
          span: icon "location"
          span: text "Based in " & info.basedIn

      if user.website.len > 0:
        tdiv(class="profile-website"):
          span:
            let url = replaceUrls(user.website, prefs)
            icon "link"
            a(href=url): text url.shortLink

      tdiv(class="profile-joindate"):
        a(href=(&"/{user.username}/about"), title=getJoinDateFull(user)):
          icon "calendar", getJoinDate(user)

      tdiv(class="profile-card-extra-links"):
        ul(class="profile-statlist"):
          renderStat(user.tweets, "posts", text="Tweets")
          renderStatLink(user.following, "following", &"/{user.username}/following")
          renderStatLink(user.followers, "followers", &"/{user.username}/followers")
          renderStat(user.likes, "likes")

proc renderPhotoRail(profile: Profile): VNode =
  let count = insertSep($profile.user.media, ',')
  buildHtml(tdiv(class="photo-rail-card")):
    tdiv(class="photo-rail-header"):
      a(href=(&"/{profile.user.username}/media")):
        icon "picture", count & " Photos and videos"

    input(id="photo-rail-grid-toggle", `type`="checkbox")
    label(`for`="photo-rail-grid-toggle", class="photo-rail-header-mobile"):
      icon "picture", count & " Photos and videos"
      icon "down"

    tdiv(class="photo-rail-grid"):
      for i, photo in profile.photoRail:
        if i == 16: break
        let photoSuffix =
          if "format" in photo.url or "placeholder" in photo.url: ""
          else: ":thumb"
        a(href=(&"/{profile.user.username}/status/{photo.tweetId}#m")):
          genImg(photo.url & photoSuffix)

proc renderBanner(banner: string): VNode =
  buildHtml():
    if banner.len == 0:
      a()
    elif banner.startsWith('#'):
      a(style={backgroundColor: banner})
    else:
      a(href=getPicUrl(banner), target="_blank"): genImg(banner)

proc renderProtected*(username: string): VNode =
  buildHtml(tdiv(class="timeline-container")):
    tdiv(class="timeline-header timeline-protected"):
      h2: text "This account's tweets are protected."
      p: text &"Only confirmed followers have access to @{username}'s tweets."

proc renderProfile*(profile: var Profile; prefs: Prefs; path: string): VNode =
  profile.tweets.query.fromUser = @[profile.user.username]
  let
    isGalleryView = profile.tweets.query.kind == media and
      profile.tweets.query.view == "gallery"
    viewClass = if isGalleryView: " media-only" else: ""

  buildHtml(tdiv(class=("profile-tabs" & viewClass))):
    if not isGalleryView and not prefs.hideBanner:
      tdiv(class="profile-banner"):
        renderBanner(profile.user.banner)

    if not isGalleryView:
      let sticky = if prefs.stickyProfile: " sticky" else: ""
      tdiv(class=("profile-tab" & sticky)):
        renderUserCard(profile.user, prefs, profile.accountInfo)
        if profile.photoRail.len > 0:
          renderPhotoRail(profile)

    if profile.user.protected:
      renderProtected(profile.user.username)
    else:
      renderTweetSearch(profile.tweets, prefs, path, profile.pinned)

proc renderFollowTabs(user: User; activeTab: string): VNode =
  buildHtml(ul(class="tab")):
    for tab in ["Following", "Followers"]:
      li(class=(if activeTab == tab: "tab-item active" else: "tab-item")):
        a(href=(&"/{user.username}/{tab.toLowerAscii()}")): text tab

proc renderUserList*(user: User; results: Result[User]; prefs: Prefs;
                     path, activeTab: string): VNode =
  # Check if we've loaded all results (for page 1)
  var displayResults = results
  if results.beginning:
    let expectedCount = if activeTab == "Followers": user.followers else: user.following
    if results.content.len >= expectedCount:
      displayResults.bottom = ""

  buildHtml(tdiv(class="profile-tabs")):
    if not prefs.hideBanner:
      tdiv(class="profile-banner"):
        renderBanner(user.banner)

    let sticky = if prefs.stickyProfile: " sticky" else: ""
    tdiv(class=("profile-tab" & sticky)):
      renderUserCard(user, prefs, AccountInfo())

    tdiv(class="timeline-container"):
      renderFollowTabs(user, activeTab)
      renderTimelineUsers(displayResults, prefs, path)



================================================
FILE: src/views/renderutils.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat
import karax/[karaxdsl, vdom, vstyles]
import ".."/[types, utils]

const smallWebp* = "?name=small&format=webp"
const mediumWebp* = "?name=medium&format=webp"

proc getSmallPic*(url: string): string =
  if url.len == 0: return
  result = url
  if "?" notin url and not url.endsWith("placeholder.png"):
    result &= smallWebp
  result = getPicUrl(result)

proc getMediumPic*(url: string): string =
  if url.len == 0: return
  result = url
  if "?" notin url and not url.endsWith("placeholder.png"):
    result &= mediumWebp
  result = getPicUrl(result)

proc icon*(icon: string; label=""; title=""; class=""; href=""): VNode =
  var c = "icon-" & icon
  if class.len > 0: c = &"{c} {class}"
  buildHtml(tdiv(class="icon-container")):
    if href.len > 0:
      a(class=c, title=title, href=href)
    else:
      span(class=c, title=title)

    if label.len > 0:
      text " " & label

template verifiedIcon*(user: User): untyped {.dirty.} =
  if user.verifiedType != VerifiedType.none:
    let lower = ($user.verifiedType).toLowerAscii()
    buildHtml(tdiv(class=(&"verified-icon {lower}"))):
      icon "circle", class="verified-icon-circle", title=(&"Verified {lower} account")
      icon "ok", class="verified-icon-check", title=(&"Verified {lower} account")
  else:
    text ""

proc linkUser*(user: User, class=""): VNode =
  let
    isName = "username" notin class
    href = "/" & user.username
    nameText = if isName: user.fullname
               else: "@" & user.username

  buildHtml(a(href=href, class=class, title=nameText)):
    text nameText
    if isName:
      if user.protected:
        text " "
        icon "lock", title="Protected account"

proc linkText*(text: string; class=""): VNode =
  let url = if "http" notin text: https & text else: text
  buildHtml():
    a(href=url, class=class): text text

proc hiddenField*(name, value: string): VNode =
  buildHtml():
    input(name=name, style={display: "none"}, value=value)

proc refererField*(path: string): VNode =
  hiddenField("referer", path)

proc buttonReferer*(action, text, path: string; class=""; `method`="post"): VNode =
  buildHtml(form(`method`=`method`, action=action, class=class)):
    refererField path
    button(`type`="submit"):
      text text

proc genCheckbox*(pref, label: string; state: bool): VNode =
  buildHtml(label(class="pref-group checkbox-container", title=pref)):
    text label
    input(name=pref, `type`="checkbox", checked=state)
    span(class="checkbox")

proc genInput*(pref, label, state, placeholder: string; class=""; autofocus=true): VNode =
  let p = placeholder
  buildHtml(tdiv(class=("pref-group pref-input " & class), title=pref)):
    if label.len > 0:
      label(`for`=pref): text label
    input(name=pref, `type`="text", placeholder=p, value=state, autofocus=(autofocus and state.len == 0))

proc genSelect*(pref, label, state: string; options: seq[string]): VNode =
  buildHtml(tdiv(class="pref-group pref-input", title=pref)):
    label(`for`=pref): text label
    select(name=pref):
      for opt in options:
        option(value=opt, selected=(opt == state)):
          text opt

proc genDate*(pref, state: string): VNode =
  buildHtml(span(class="date-input")):
    input(name=pref, `type`="date", value=state)
    icon "calendar"

proc genNumberInput*(pref, label, state, placeholder: string; class=""; autofocus=true; min="0"): VNode =
  let p = placeholder
  buildHtml(tdiv(class=("pref-group pref-input " & class))):
    if label.len > 0:
      label(`for`=pref): text label
    input(name=pref, `type`="number", placeholder=p, value=state, autofocus=(autofocus and state.len == 0), min=min, step="1")

proc genImg*(url: string; class=""; alt=""): VNode =
  buildHtml():
    img(src=getPicUrl(url), class=class, alt=alt, loading="lazy")

proc getTabClass*(query: Query; tab: QueryKind): string =
  if query.kind == tab: "tab-item active"
  else: "tab-item"

proc getAvatarClass*(prefs: Prefs): string =
  if prefs.squareAvatars: "avatar"
  else: "avatar round"



================================================
FILE: src/views/rss.nimf
================================================
#? stdtmpl(subsChar = '$', metaChar = '#')
## SPDX-License-Identifier: AGPL-3.0-only
#import strutils, sequtils, xmltree, strformat, options, unicode
#import ../types, ../utils, ../formatters, ../prefs
## Snowflake ID cutoff for RSS GUID format transition
## Corresponds to approximately December 14, 2025 UTC
#const guidCutoff = 2000000000000000000'i64
#
#proc getTitle(tweet: Tweet; retweet: string): string =
#var prefix = ""
#if tweet.pinned: prefix = "Pinned: "
#elif retweet.len > 0: prefix = &"RT by @{retweet}: "
#elif tweet.reply.len > 0: prefix = &"R to @{tweet.reply[0]}: "
#end if
#var text = strutils.splitWhitespace(stripHtml(tweet.text)).join(" ")
##if unicode.runeLen(text) > 32:
##  text = unicode.runeSubStr(text, 0, 32) & "..."
##end if
#text = xmltree.escape(text)
#if text.len > 0:
#  result = prefix & text
#  return
#end if
#if tweet.media.len > 0:
#  result = prefix
#  let firstKind = tweet.media[0].kind
#  if tweet.media.anyIt(it.kind != firstKind):
#    result &= "Media"
#  else:
#    case firstKind
#    of photoMedia: result &= "Image"
#    of videoMedia: result &= "Video"
#    of gifMedia:   result &= "Gif"
#    end case
#  end if
#end if
#if result.len == 0 and tweet.articlePreview.isSome:
#  let art = tweet.articlePreview.get()
#  if art.title.len > 0:
#    result = prefix & xmltree.escape(art.title)
#  end if
#end if
#if result.len == 0 and tweet.card.isSome:
#  let card = tweet.card.get()
#  if card.kind notin {hidden, unknown} and card.title.len > 0:
#    result = prefix & xmltree.escape(card.title)
#  end if
#end if
#end proc
#
#proc getDescription(desc: string; cfg: Config): string =
Twitter feed for: ${desc}. Generated by ${getUrlPrefix(cfg)}
#end proc
#
#proc renderRssMedia(media: Media; tweet: Tweet; urlPrefix: string): string =
#case media.kind
#of photoMedia:
#  let photo = media.photo
<img src="${urlPrefix}${getPicUrl(photo.url)}" style="max-width:250px;" />
#of videoMedia:
#  let video = media.video
<a href="${urlPrefix}${tweet.getLink}">
<br>Video<br>
  <img src="${urlPrefix}${getPicUrl(video.thumb)}" style="max-width:250px;" />
</a>
#of gifMedia:
#  let gif = media.gif
#  let thumb = &"{urlPrefix}{getPicUrl(gif.thumb)}"
#  let url = &"{urlPrefix}{getPicUrl(gif.url)}"
<video poster="${thumb}" autoplay muted loop style="max-width:250px;">
  <source src="${url}" type="video/mp4"></video>
#end case
#end proc
#
#proc renderRssCard(card: Card; prefs: Prefs; urlPrefix: string): string =
#let cardLink = if card.url.startsWith("/"): urlPrefix & card.url else: replaceUrls(card.url, prefs)
#let title = xmltree.escape(card.title)
<hr/>
<b>Link</b><br>
#if cardLink.len > 0:
<a href="${xmltree.escape(cardLink)}">
#end if
#if card.image.len > 0:
<img src="${urlPrefix}${getPicUrl(card.image)}" style="max-width:250px;" />
#end if
#if title.len > 0:
#  if card.image.len > 0:
<br>
#  end if
<b>${title}</b>
#end if
#if cardLink.len > 0:
</a>
#end if
#if card.text.len > 0:
<p>${xmltree.escape(card.text)}</p>
#end if
#if cardLink.len > 0:
#  let destText = if card.dest.len > 0: xmltree.escape(card.dest) else: xmltree.escape(cardLink)
<small><a href="${xmltree.escape(cardLink)}">${destText}</a></small>
#elif card.dest.len > 0:
<small>${xmltree.escape(card.dest)}</small>
#end if
#end proc
#
#proc renderRssArticle(article: ArticlePreview; urlPrefix: string): string =
#let link = urlPrefix & "/i/article/" & $article.tweetId
<hr/>
<b>Article</b><br>
<a href="${link}">
#if article.coverImage.len > 0:
<img src="${urlPrefix}${getPicUrl(article.coverImage)}" style="max-width:250px;" />
#end if
#if article.title.len > 0:
#  if article.coverImage.len > 0:
<br>
#  end if
<b>${xmltree.escape(article.title)}</b>
#end if
</a>
#if article.previewText.len > 0:
<p>${xmltree.escape(article.previewText)}</p>
#end if
#end proc
#
#proc renderRssPoll(poll: Poll): string =
<hr/>
<b>Poll</b>
<p>
#for i in 0 ..< poll.options.len:
#  let perc = if poll.votes > 0: poll.values[i] / poll.votes * 100 else: 0.0
#  let pct = (&"{perc:.0f}").strip(chars={'.'})
#  let line = pct & "% — " & xmltree.escape(poll.options[i])
${line}<br>
#end for
#let votesStr = insertSep($poll.votes, ',')
<i>${votesStr} votes • ${xmltree.escape(poll.status)}</i>
</p>
#end proc
#
#proc getTweetsWithPinned(profile: Profile): seq[Tweets] =
#result = profile.tweets.content
#if profile.pinned.isSome and result.len > 0:
#  let pinnedTweet = profile.pinned.get
#  var inserted = false
#  for threadIdx in 0 ..< result.len:
#    if not inserted:
#      for tweetIdx in 0 ..< result[threadIdx].len:
#        if result[threadIdx][tweetIdx].id < pinnedTweet.id:
#          result[threadIdx].insert(pinnedTweet, tweetIdx)
#          inserted = true
#        end if
#      end for
#    end if
#  end for
#end if
#end proc
#
#proc renderRssTweet(tweet: Tweet; cfg: Config; prefs: Prefs): string =
#let tweet = tweet.retweet.get(tweet)
#let urlPrefix = getUrlPrefix(cfg)
#let text = replaceUrls(tweet.text, prefs, absolute=urlPrefix)
#if text.len > 0:
<p>${text.replace("\n", "<br>\n")}</p>
#end if
#if tweet.media.len > 0:
#  for media in tweet.media:
${renderRssMedia(media, tweet, urlPrefix)}
#  end for
#elif tweet.card.isSome and tweet.card.get().kind notin {hidden, unknown}:
${renderRssCard(tweet.card.get(), prefs, urlPrefix)}
#end if
#if tweet.articlePreview.isSome:
${renderRssArticle(tweet.articlePreview.get(), urlPrefix)}
#end if
#if tweet.poll.isSome:
${renderRssPoll(tweet.poll.get())}
#end if
#if tweet.note.len > 0 and not prefs.hideCommunityNotes:
<p><b>Community note:</b> ${replaceUrls(tweet.note, prefs, absolute=urlPrefix)}</p>
#end if
#if tweet.quote.isSome and get(tweet.quote).available:
#  let quoteTweet = get(tweet.quote)
#  let quoteLink = urlPrefix & getLink(quoteTweet)
<hr/>
<blockquote>
<b>${quoteTweet.user.fullname} (@${quoteTweet.user.username})</b>
<p>
${renderRssTweet(quoteTweet, cfg, prefs)}
</p>
<footer>
— <cite><a href="${quoteLink}">${quoteLink}</a>
</footer>
</blockquote>
#end if
#end proc
#
#proc renderRssTweets(tweets: seq[Tweets]; cfg: Config; prefs: Prefs; userId=""): string =
#let urlPrefix = getUrlPrefix(cfg)
#var links: seq[string]
#for thread in tweets:
#  for tweet in thread:
#    if userId.len > 0 and tweet.user.id != userId: continue
#    end if
#
#    let retweet = if tweet.retweet.isSome: tweet.user.username else: ""
#    let tweet = if retweet.len > 0: tweet.retweet.get else: tweet
#    let link = getLink(tweet)
#    if link in links: continue
#    end if
#    links.add link
#    let useGlobalGuid = tweet.id >= guidCutoff
      <item>
        <title>${getTitle(tweet, retweet)}</title>
        <dc:creator>@${tweet.user.username}</dc:creator>
        <description><![CDATA[${renderRssTweet(tweet, cfg, prefs).strip(chars={'\n'})}]]></description>
        <pubDate>${getRfc822Time(tweet)}</pubDate>
#if useGlobalGuid:
        <guid isPermaLink="false">${tweet.id}</guid>
#else:
        <guid>${urlPrefix & link}</guid>
#end if
        <link>${urlPrefix & link}</link>
      </item>
#  end for
#end for
#end proc
#
#proc renderTimelineRss*(profile: Profile; cfg: Config; prefs: Prefs; multi=false): string =
#let urlPrefix = getUrlPrefix(cfg)
#result = ""
#let handle = (if multi: "" else: "@") & profile.user.username
#var title = profile.user.fullname
#if not multi: title &= " / " & handle
#end if
#title = xmltree.escape(title).sanitizeXml
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel>
    <atom:link href="${urlPrefix}/${profile.user.username}/rss" rel="self" type="application/rss+xml" />
    <title>${title}</title>
    <link>${urlPrefix}/${profile.user.username}</link>
    <description>${getDescription(handle, cfg)}</description>
    <language>en-us</language>
    <ttl>40</ttl>
    <image>
      <title>${title}</title>
      <link>${urlPrefix}/${profile.user.username}</link>
      <url>${urlPrefix}${getPicUrl(profile.user.getUserPic(style="_400x400"))}</url>
      <width>128</width>
      <height>128</height>
    </image>
#let tweetsList = getTweetsWithPinned(profile)
#if tweetsList.len > 0:
${renderRssTweets(tweetsList, cfg, prefs, userId=profile.user.id)}
#end if
  </channel>
</rss>
#end proc
#
#proc renderListRss*(tweets: seq[Tweets]; list: List; cfg: Config; prefs: Prefs): string =
#let link = &"{getUrlPrefix(cfg)}/i/lists/{list.id}"
#result = ""
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel>
    <atom:link href="${link}" rel="self" type="application/rss+xml" />
    <title>${xmltree.escape(list.name)} / @${list.username}</title>
    <link>${link}</link>
    <description>${getDescription(&"{list.name} by @{list.username}", cfg)}</description>
    <language>en-us</language>
    <ttl>40</ttl>
${renderRssTweets(tweets, cfg, prefs)}
 </channel>
</rss>
#end proc
#
#proc renderSearchRss*(tweets: seq[Tweets]; name, param: string; cfg: Config; prefs: Prefs): string =
#let link = &"{getUrlPrefix(cfg)}/search"
#let escName = xmltree.escape(name)
#result = ""
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0">
  <channel>
    <atom:link href="${link}" rel="self" type="application/rss+xml" />
    <title>Search results for "${escName}"</title>
    <link>${link}</link>
    <description>${getDescription(&"Search \"{escName}\"", cfg)}</description>
    <language>en-us</language>
    <ttl>40</ttl>
${renderRssTweets(tweets, cfg, prefs)}
  </channel>
</rss>
#end proc



================================================
FILE: src/views/search.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, sequtils, unicode, tables, options
import karax/[karaxdsl, vdom]

import renderutils, timeline
import ".."/[types, query]

const toggles = {
  "nativeretweets": "Retweets",
  "media": "Media",
  "videos": "Videos",
  "news": "News",
  "native_video": "Native videos",
  "replies": "Replies",
  "links": "Links",
  "images": "Images",
  "quote": "Quotes",
  "spaces": "Spaces"
}.toOrderedTable

proc renderSearch*(): VNode =
  buildHtml(tdiv(class="panel-container")):
    tdiv(class="search-bar"):
      form(`method`="get", action="/search", autocomplete="off"):
        hiddenField("f", "tweets")
        input(`type`="text", name="q", autofocus="",
              placeholder="Search...", dir="auto")
        button(`type`="submit"): icon "search"

proc renderProfileTabs*(query: Query; username: string): VNode =
  let link = "/" & username
  buildHtml(ul(class="tab")):
    li(class=query.getTabClass(posts)):
      a(href=link): text "Tweets"
    li(class=(query.getTabClass(replies) & " wide")):
      a(href=(link & "/with_replies")): text "Tweets & Replies"
    li(class=query.getTabClass(media)):
      a(href=(link & "/media")): text "Media"
    li(class=query.getTabClass(tweets)):
      a(href=(link & "/search")): text "Search"

proc renderMediaViewTabs*(query: Query; username: string): VNode =
  let currentView = if query.view.len > 0: query.view else: "timeline"
  let base = "/" & username & "/media?view="
  func cls(view: string): string =
    if currentView == view: "tab-item active" else: "tab-item"
  buildHtml(ul(class="tab media-view-tabs")):
    li(class=cls("timeline")):
      a(href=(base & "timeline")): text "Timeline"
    li(class=cls("grid")):
      a(href=(base & "grid")): text "Grid"
    li(class=cls("gallery")):
      a(href=(base & "gallery")): text "Gallery"

proc renderSearchTabs*(query: Query): VNode =
  var q = query
  buildHtml(ul(class="tab")):
    li(class=query.getTabClass(tweets)):
      q.kind = tweets
      a(href=("?" & genQueryUrl(q))): text "Tweets"
    li(class=query.getTabClass(users)):
      q.kind = users
      a(href=("?" & genQueryUrl(q))): text "Users"

proc isPanelOpen(q: Query): bool =
  q.fromUser.len == 0 and (q.filters.len > 0 or q.excludes.len > 0 or
  @[q.minLikes, q.until, q.since].anyIt(it.len > 0))

proc renderSearchPanel*(query: Query): VNode =
  let user = query.fromUser.join(",")
  let action = if user.len > 0: &"/{user}/search" else: "/search"
  buildHtml(form(`method`="get", action=action,
                 class="search-field", autocomplete="off")):
    hiddenField("f", "tweets")
    genInput("q", "", query.text, "Enter search...", class="pref-inline")
    button(`type`="submit"): icon "search"

    input(id="search-panel-toggle", `type`="checkbox", checked=isPanelOpen(query))
    label(`for`="search-panel-toggle"): icon "down"

    tdiv(class="search-panel"):
      for f in @["filter", "exclude"]:
        span(class="search-title"): text capitalize(f)
        tdiv(class="search-toggles"):
          for k, v in toggles:
            let state =
              if f == "filter": k in query.filters
              else: k in query.excludes
            genCheckbox(&"{f[0]}-{k}", v, state)

      tdiv(class="search-row"):
        tdiv:
          span(class="search-title"): text "Time range"
          tdiv(class="date-range"):
            genDate("since", query.since)
            span(class="search-title"): text "-"
            genDate("until", query.until)
        tdiv:
          span(class="search-title"): text "Minimum likes"
          genNumberInput("min_faves", "", query.minLikes, "Number...", autofocus=false)

proc renderTweetSearch*(results: Timeline; prefs: Prefs; path: string;
                        pinned=none(Tweet)): VNode =
  let query = results.query
  buildHtml(tdiv(class="timeline-container")):
    if query.fromUser.len > 1:
      tdiv(class="timeline-header"):
        text query.fromUser.join(" | ")

    if query.fromUser.len > 0:
      if query.kind != media or query.view != "gallery":
        renderProfileTabs(query, query.fromUser.join(","))
      if query.kind == media and query.fromUser.len == 1:
        renderMediaViewTabs(query, query.fromUser[0])

    if query.fromUser.len == 0 or query.kind == tweets:
      tdiv(class="timeline-header"):
        renderSearchPanel(query)

    if query.fromUser.len == 0:
      renderSearchTabs(query)

    renderTimelineTweets(results, prefs, path, pinned)

proc renderUserSearch*(results: Result[User]; prefs: Prefs): VNode =
  buildHtml(tdiv(class="timeline-container")):
    tdiv(class="timeline-header"):
      form(`method`="get", action="/search", class="search-field", autocomplete="off"):
        hiddenField("f", "users")
        genInput("q", "", results.query.text, "Enter username...", class="pref-inline")
        button(`type`="submit"): icon "search"

    renderSearchTabs(results.query)
    renderTimelineUsers(results, prefs)



================================================
FILE: src/views/space.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, times
import karax/[karaxdsl, vdom]

import renderutils
import ".."/[types, utils, formatters]

proc renderParticipant(p: SpaceParticipant; role: string): VNode =
  buildHtml(tdiv(class="space-participant")):
    a(href=("/" & p.username)):
      genImg(p.avatarUrl.replace("_normal", "_bigger"))
      tdiv(class="participant-info"):
        tdiv(class="participant-name"):
          strong: text p.displayName
          if p.isVerified:
            tdiv(class="verified-icon blue"):
              icon "circle", class="verified-icon-circle", title="Verified account"
              icon "ok", class="verified-icon-check", title="Verified account"
          if role.len > 0:
            span(class="host-badge"): text role
        span(class="participant-username"): text "@" & p.username

proc renderSpace*(sp: AudioSpace; prefs: Prefs; path: string): VNode =
  let
    isLive = sp.state == "RUNNING"
    source = if prefs.proxyVideos and sp.m3u8Url.startsWith("http"):
               getVidUrl(sp.m3u8Url) else: sp.m3u8Url
    stateText =
      if isLive: "LIVE"
      elif sp.endTime.year > 1: "Ended " & sp.endTime.format("MMM d, YYYY")
      elif sp.state.len > 0: sp.state
      else: "Ended"
    durationMs =
      if sp.startTime.year > 1 and sp.endTime.year > 1:
        int((sp.endTime - sp.startTime).inMilliseconds)
      else: 0
    duration = if durationMs > 0: getDuration(durationMs) else: ""
    totalListeners =
      if sp.totalReplayWatched > 0: sp.totalReplayWatched
      else: sp.totalLiveListeners

  buildHtml(tdiv(class="space-page")):
    tdiv(class="space-panel"):
      tdiv(class="space-player"):
        if sp.m3u8Url.len > 0 and prefs.hlsPlayback:
          audio(data-url=source, data-autoload="false")
          verbatim "<div class=\"video-overlay\" onclick=\"playAudio(this)\">"
          tdiv(class="overlay-circle"): span(class="overlay-triangle")
          if isLive:
            tdiv(class="space-live"): text "LIVE"
          elif duration.len > 0:
            tdiv(class="overlay-duration"): text duration
          verbatim "</div>"
        elif sp.m3u8Url.len > 0:
          tdiv(class="video-overlay"):
            buttonReferer "/enablehls", "Enable hls playback", path
            if isLive:
              tdiv(class="space-live"): text "LIVE"
            elif duration.len > 0:
              tdiv(class="overlay-duration"): text duration
        elif sp.availableForReplay:
          tdiv(class="video-overlay"):
            p: text "Audio stream unavailable"
        else:
          tdiv(class="video-overlay"):
            p: text "Replay is not available"

      tdiv(class="space-info"):
        tdiv(class="space-header"):
          h2(class="space-title"): text sp.title
          tdiv(class="space-meta"):
            if totalListeners > 0:
              span(class="listener-count"): text insertSep($totalListeners, ',') & " listeners"
            if isLive:
              span(class="space-live"): text stateText
            else:
              span(class="space-state"): text stateText

        if sp.admins.len > 0 or sp.speakers.len > 0:
          tdiv(class="space-participants"):
            for admin in sp.admins:
              let role = if admin.username == sp.creator.username: "Host"
                         else: "Co-host"
              renderParticipant(admin, role)
            for speaker in sp.speakers:
              renderParticipant(speaker, "")



================================================
FILE: src/views/status.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import karax/[karaxdsl, vdom]

import ".."/[types, formatters]
import tweet, timeline

proc renderEarlier(thread: Chain): VNode =
  buildHtml(tdiv(class="timeline-item more-replies earlier-replies")):
    a(class="more-replies-text", href=getLink(thread.content[0])):
      text "earlier replies"

proc renderMoreReplies(thread: Chain): VNode =
  let link = getLink(thread.content[^1])
  buildHtml(tdiv(class="timeline-item more-replies")):
    if thread.content[^1].available:
      a(class="more-replies-text", href=link):
        text "more replies"
    else:
      a(class="more-replies-text"):
        text "more replies"

proc renderReplyThread(thread: Chain; prefs: Prefs; path: string): VNode =
  buildHtml(tdiv(class="reply thread thread-line")):
    for i, tweet in thread.content:
      let last = (i == thread.content.high and not thread.hasMore)
      renderTweet(tweet, prefs, path, index=i, last=last)

    if thread.hasMore:
      renderMoreReplies(thread)

proc renderReplies*(replies: Result[Chain]; prefs: Prefs; path: string; tweet: Tweet = nil): VNode =
  buildHtml(tdiv(class="replies", id="r")):
    var hasReplies = false
    var replyCount = 0
    for thread in replies.content:
      if thread.content.len == 0: continue
      hasReplies = true
      replyCount += thread.content.len
      renderReplyThread(thread, prefs, path)

    if hasReplies and replies.bottom.len > 0:
      if tweet == nil or not replies.beginning or replyCount < tweet.stats.replies:
        renderMore(Query(), replies.bottom, focus="#r")

proc renderConversation*(conv: Conversation; prefs: Prefs; path: string): VNode =
  let hasAfter = conv.after.content.len > 0
  let threadId = conv.tweet.threadId
  buildHtml(tdiv(class="conversation")):
    tdiv(class="main-thread"):
      if conv.before.content.len > 0:
        tdiv(class="before-tweet thread-line"):
          let first = conv.before.content[0]
          if threadId != first.id and (first.replyId > 0 or not first.available):
            renderEarlier(conv.before)
          for i, tweet in conv.before.content:
            renderTweet(tweet, prefs, path, index=i)

      tdiv(class="main-tweet", id="m"):
        let afterClass = if hasAfter: "thread thread-line" else: ""
        renderTweet(conv.tweet, prefs, path, class=afterClass, mainTweet=true)

      if hasAfter:
        tdiv(class="after-tweet thread-line"):
          let
            total = conv.after.content.high
            hasMore = conv.after.hasMore
          for i, tweet in conv.after.content:
            renderTweet(tweet, prefs, path, index=i,
                        last=(i == total and not hasMore), afterTweet=true)

          if hasMore:
            renderMoreReplies(conv.after)

    if not prefs.hideReplies:
      if not conv.replies.beginning:
        renderNewer(Query(), getLink(conv.tweet), focus="#r")
      if conv.replies.content.len > 0 or conv.replies.bottom.len > 0:
        renderReplies(conv.replies, prefs, path, conv.tweet)

    renderToTop(focus="#m")

proc renderEditHistory*(edits: EditHistory; prefs: Prefs; path: string): VNode =
  buildHtml(tdiv(class="edit-history")):
    tdiv(class="latest-edit"):
      tdiv(class="edit-history-header"): 
        text "Latest post"
      renderTweet(edits.latest, prefs, path)

    tdiv(class="previous-edits"):
      tdiv(class="edit-history-header"): 
        text "Version history"
      for tweet in edits.history:
        tdiv(class="tweet-edit"):
          renderTweet(tweet, prefs, path)



================================================
FILE: src/views/timeline.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, strformat, algorithm, uri, options
import karax/[karaxdsl, vdom]

import ".."/[types, query, formatters]
import tweet, renderutils

proc timelineViewClass(query: Query): string =
  if query.kind != media:
    return "timeline"

  case query.view
  of "grid": "timeline media-grid-view"
  of "gallery": "timeline media-gallery-view"
  else: "timeline"

proc getQuery(query: Query): string =
  if query.kind != posts:
    result = genQueryUrl(query)
  if result.len > 0:
    result &= "&"

proc getSearchMaxId(results: Timeline; path: string): string =
  if results.query.kind != tweets or results.content.len == 0 or
     results.query.until.len == 0:
    return

  let lastThread = results.content[^1]
  if lastThread.len == 0 or lastThread[^1].id == 0:
    return

  # 2000000 is the minimum decrement to guarantee no result overlap
  var maxId = lastThread[^1].id - 2_000_000'i64
  if maxId <= 0:
    maxId = lastThread[^1].id - 1

  if maxId > 0:
    return "maxid:" & $maxId

proc renderToTop*(focus="#"): VNode =
  buildHtml(tdiv(class="top-ref")):
    icon "down", href=focus

proc renderNewer*(query: Query; path: string; focus=""): VNode =
  let
    q = genQueryUrl(query)
    url = if q.len > 0: "?" & q else: ""
    p = if focus.len > 0: path.replace("#m", focus) else: path
  buildHtml(tdiv(class="timeline-item show-more")):
    a(href=(p & url)):
      text "Load newest"

proc renderMore*(query: Query; cursor: string; focus=""): VNode =
  buildHtml(tdiv(class="show-more")):
    a(href=(&"?{getQuery(query)}cursor={encodeUrl(cursor, usePlus=false)}{focus}")):
      text "Load more"

proc renderNoMore(): VNode =
  buildHtml(tdiv(class="timeline-footer")):
    h2(class="timeline-end"):
      text "No more items"

proc renderNoneFound(): VNode =
  buildHtml(tdiv(class="timeline-header")):
    h2(class="timeline-none"):
      text "No items found"

proc renderThread(thread: Tweets; prefs: Prefs; path: string; bigThumb=false): VNode =
  buildHtml(tdiv(class="thread-line")):
    let sortedThread = thread.sortedByIt(it.id)
    for i, tweet in sortedThread:
      # thread has a gap, display "more replies" link
      if i > 0 and tweet.replyId != sortedThread[i - 1].id:
        tdiv(class="timeline-item thread more-replies-thread"):
          tdiv(class="more-replies"):
            a(class="more-replies-text", href=getLink(tweet)):
              text "more replies"

      let show = i == thread.high and sortedThread[0].id != tweet.threadId
      let header = if tweet.pinned or tweet.retweet.isSome: "with-header " else: ""
      renderTweet(tweet, prefs, path, class=(header & "thread"),
                  index=i, last=(i == thread.high), bigThumb=bigThumb)

proc renderUser(user: User; prefs: Prefs): VNode =
  buildHtml(tdiv(class="timeline-item", data-username=user.username)):
    a(class="tweet-link", href=("/" & user.username))
    tdiv(class="tweet-body profile-result"):
      tdiv(class="tweet-header"):
        a(class="tweet-avatar", href=("/" & user.username)):
          genImg(user.getUserPic("_bigger"), class=prefs.getAvatarClass)

        tdiv(class="tweet-name-row"):
          tdiv(class="fullname-and-username"):
            linkUser(user, class="fullname")
            verifiedIcon(user)
        linkUser(user, class="username")

      tdiv(class="tweet-content media-body", dir="auto"):
        verbatim replaceUrls(user.bio, prefs)

proc renderTimelineUsers*(results: Result[User]; prefs: Prefs; path=""): VNode =
  buildHtml(tdiv(class="timeline")):
    if not results.beginning:
      renderNewer(results.query, path)

    if results.content.len > 0:
      for user in results.content:
        renderUser(user, prefs)
      if results.bottom.len > 0:
        renderMore(results.query, results.bottom)
      renderToTop()
    elif results.beginning:
      renderNoneFound()
    else:
      renderNoMore()

proc filterThreads(threads: seq[Tweets]; prefs: Prefs): seq[Tweets] =
  var retweets: seq[int64]
  for thread in threads:
    if thread.len == 1:
      let tweet = thread[0]
      let retweetId = if tweet.retweet.isSome: get(tweet.retweet).id else: 0
      if retweetId in retweets or tweet.id in retweets or
         tweet.pinned and prefs.hidePins:
        continue
      if retweetId != 0 and tweet.retweet.isSome:
        retweets &= retweetId
    result.add(thread)

proc renderTimelineTweets*(results: Timeline; prefs: Prefs; path: string;
                           pinned=none(Tweet)): VNode =
  buildHtml(tdiv(class=results.query.timelineViewClass)):
    if not results.beginning:
      renderNewer(results.query, parseUri(path).path)

    if not prefs.hidePins and pinned.isSome:
      let tweet = get pinned
      renderTweet(tweet, prefs, path)

    if results.content.len == 0:
      if not results.beginning:
        renderNoMore()
      else:
        renderNoneFound()
    else:
      let filtered = filterThreads(results.content, prefs)

      if results.query.view == "gallery":
        let bigThumb = prefs.gallerySize == "Large"
        let galClass = if prefs.compactGallery: "gallery-masonry compact" else: "gallery-masonry"
        tdiv(class=galClass, `data-col-size`=prefs.gallerySize.toLowerAscii):
          for thread in filtered:
            if thread.len == 1: renderTweet(thread[0], prefs, path, bigThumb=bigThumb)
            else: renderThread(thread, prefs, path, bigThumb)
      else:
        for thread in filtered:
          if thread.len == 1:
            renderTweet(thread[0], prefs, path)
          else: renderThread(thread, prefs, path)

      var cursor = getSearchMaxId(results, path)
      if cursor.len > 0:
        renderMore(results.query, cursor)
      elif results.bottom.len > 0:
        renderMore(results.query, results.bottom)
      renderToTop()



================================================
FILE: src/views/tweet.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
import strutils, sequtils, strformat, options, algorithm
import karax/[karaxdsl, vdom, vstyles]
from jester import Request

import renderutils
import ".."/[types, utils, formatters]
import general

const doctype = "<!DOCTYPE html>\n"

proc renderMiniAvatar*(user: User; prefs: Prefs): VNode =
  genImg(user.getUserPic("_mini"), class=(prefs.getAvatarClass & " mini"))

proc renderArticleCard(preview: ArticlePreview; prefs: Prefs): VNode =
  let url = "/i/article/" & $preview.tweetId
  buildHtml(tdiv(class="article-card card large")):
    a(class="card-container", href=url):
      if preview.coverImage.len > 0:
        tdiv(class="card-image-container"):
          tdiv(class="card-image"):
            genImg(preview.coverImage)
          span(class="article-card-badge"): text "Article"
      tdiv(class="card-content-container"):
        tdiv(class="card-content"):
          h2(class="card-title"): text preview.title
          if preview.previewText.len > 0:
            p(class="card-description"): text preview.previewText

proc renderHeader(tweet: Tweet; retweet: string; pinned: bool; prefs: Prefs;
                   path = ""): VNode =
  buildHtml(tdiv):
    if pinned:
      let pinnedLabel =
        if "/i/communities/" in path: "Pinned by Community mods"
        else: "Pinned Tweet"
      tdiv(class="pinned"):
        span: icon("pin", pinnedLabel)
    elif retweet.len > 0:
      tdiv(class="retweet-header"):
        span: icon("retweet", retweet & " retweeted")

    tdiv(class="tweet-header"):
      a(class="tweet-avatar", href=("/" & tweet.user.username)):
        var size = "_bigger"
        if not prefs.autoplayGifs and tweet.user.userPic.endsWith("gif"):
          size = "_400x400"
        genImg(tweet.user.getUserPic(size), class=prefs.getAvatarClass)

      tdiv(class="tweet-name-row"):
        tdiv(class="fullname-and-username"):
          linkUser(tweet.user, class="fullname")
          verifiedIcon(tweet.user)
          linkUser(tweet.user, class="username")

        span(class="tweet-date"):
          a(href=getLink(tweet), title=tweet.getTime):
            text tweet.getShortTime

proc renderAltText(altText: string): VNode =
  buildHtml(p(class="alt-text")):
    text "ALT  " & altText

proc renderPhotoAttachment(photo: Photo; bigThumb=false): VNode =
  buildHtml(tdiv(class="attachment")):
    let
      named = "name=" in photo.url
      thumb = if named: photo.url
              elif bigThumb: photo.url & mediumWebp
              else: photo.url & smallWebp
    a(href=getOrigPicUrl(photo.url), class="still-image", target="_blank"):
      genImg(thumb, alt=photo.altText)
    if photo.altText.len > 0:
      renderAltText(photo.altText)

proc isPlaybackEnabled(prefs: Prefs; playbackType: VideoType): bool =
  case playbackType
  of mp4: prefs.mp4Playback
  of m3u8, vmap: prefs.hlsPlayback

proc hasMp4Url(video: Video): bool =
  video.variants.anyIt(it.contentType == mp4)

proc renderVideoDisabled(playbackType: VideoType; path=""): VNode =
  buildHtml(tdiv(class="video-overlay")):
    case playbackType
    of mp4:
      buttonReferer "/enablemp4", "Enable mp4 playback", path
    of m3u8, vmap:
      buttonReferer "/enablehls", "Enable hls playback", path

proc renderVideoUnavailable(video: Video): VNode =
  buildHtml(tdiv(class="video-overlay")):
    case video.reason
    of "dmcaed":
      p: text "This media has been disabled in response to a report by the copyright owner"
    else:
      p: text "This media is unavailable"

proc getVideoDownloadUrl(videoData: Video): string =
  let mp4Vars = videoData.variants.filterIt(it.contentType == mp4)
  if mp4Vars.len == 0: return ""
  let best = mp4Vars.sortedByIt(it.bitrate)[^1].url
  if best.startsWith("http"): getVidUrl(best) else: best

proc renderVideoAttachment(videoData: Video; prefs: Prefs; path=""; bigThumb=false): VNode =
  let
    playbackType = if not prefs.proxyVideos and videoData.hasMp4Url: mp4
                   else: videoData.playbackType
    thumb = if bigThumb: getMediumPic(videoData.thumb) else: getSmallPic(videoData.thumb)

  buildHtml(tdiv(class="attachment")):
    if not videoData.available:
      img(src=thumb, loading="lazy")
      renderVideoUnavailable(videoData)
    elif not prefs.isPlaybackEnabled(playbackType):
      img(src=thumb, loading="lazy")
      renderVideoDisabled(playbackType, path)
    else:
      let
        vars = videoData.variants.filterIt(it.contentType == playbackType)
        vidUrl = vars.sortedByIt(it.resolution)[^1].url
        source = if prefs.proxyVideos and vidUrl.startsWith("http"):
                   getVidUrl(vidUrl) else: vidUrl
      case playbackType
      of mp4:
        video(poster=thumb, controls="", muted=prefs.muteVideos):
          source(src=source, `type`="video/mp4")
      of m3u8, vmap:
        video(poster=thumb, data-url=source, data-autoload="false", muted=prefs.muteVideos)
        verbatim "<div class=\"video-overlay\" onclick=\"playVideo(this)\">"
        tdiv(class="overlay-circle"): span(class="overlay-triangle")
        if videoData.durationMs > 0:
          tdiv(class="overlay-duration"): text getDuration(videoData)
        verbatim "</div>"
    if videoData.available:
      let dlUrl = getVideoDownloadUrl(videoData)
      if dlUrl.len > 0:
        a(class="video-download", href=dlUrl, download="",
          title="Download video"): icon "download-alt"

proc renderVideo*(video: Video; prefs: Prefs; path: string; bigThumb=false): VNode =
  let hasCardContent = video.description.len > 0 or video.title.len > 0

  buildHtml(tdiv(class="attachments card")):
    tdiv(class=("gallery-video" & (if hasCardContent: " card-container" else: ""))):
      renderVideoAttachment(video, prefs, path, bigThumb)
      if hasCardContent:
        tdiv(class="card-content"):
          h2(class="card-title"): text video.title
          if video.description.len > 0:
            p(class="card-description"): text video.description

proc renderGifAttachment(gif: Gif; prefs: Prefs; path=""): VNode =
  let thumb = getSmallPic(gif.thumb)

  buildHtml(tdiv(class="attachment")):
    if not prefs.mp4Playback:
      img(src=thumb, loading="lazy")
      renderVideoDisabled(mp4, path)
    elif prefs.autoplayGifs:
      video(class="gif", poster=thumb, autoplay="", muted="", loop=""):
        source(src=getPicUrl(gif.url), `type`="video/mp4")
    else:
      video(class="gif", poster=thumb, controls="", muted="", loop=""):
        source(src=getPicUrl(gif.url), `type`="video/mp4")
    if gif.altText.len > 0:
      renderAltText(gif.altText)

proc renderGif(gif: Gif; prefs: Prefs; path=""): VNode =
  buildHtml(tdiv(class="attachments media-gif")):
    renderGifAttachment(gif, prefs, path)

proc renderMedia(media: seq[Media]; prefs: Prefs; path: string; bigThumb=false): VNode =
  if media.len == 0:
    return nil

  if media.len == 1:
    let item = media[0]
    if item.kind == videoMedia:
      return renderVideo(item.video, prefs, path, bigThumb)
    if item.kind == gifMedia:
      return renderGif(item.gif, prefs, path)

  let
    groups = if media.len < 3: @[media]
             else: media.distribute(2)

  buildHtml(tdiv(class="attachments")):
    for i, mediaGroup in groups:
      let margin = if i > 0: ".25em" else: ""
      let rowClass = "gallery-row" &
                     (if mediaGroup.allIt(it.kind == photoMedia): "" else: " mixed-row")
      tdiv(class=rowClass, style={marginTop: margin}):
        for mediaItem in mediaGroup:
          case mediaItem.kind
          of photoMedia:
            renderPhotoAttachment(mediaItem.photo, bigThumb)
          of videoMedia:
            renderVideoAttachment(mediaItem.video, prefs, path, bigThumb)
          of gifMedia:
            renderGifAttachment(mediaItem.gif, prefs, path)

proc renderPoll(poll: Poll): VNode =
  buildHtml(tdiv(class="poll")):
    for i in 0 ..< poll.options.len:
      let
        leader = if poll.leader == i: " leader" else: ""
        val = poll.values[i]
        perc = if val > 0: val / poll.votes * 100 else: 0
        percStr = (&"{perc:>3.0f}").strip(chars={'.'}) & '%'
      tdiv(class=("poll-meter" & leader)):
        span(class="poll-choice-bar", style={width: percStr})
        span(class="poll-choice-value"): text percStr
        span(class="poll-choice-option"): text poll.options[i]
    span(class="poll-info"):
      text &"{insertSep($poll.votes, ',')} votes • {poll.status}"

proc renderCardImage(card: Card): VNode =
  buildHtml(tdiv(class="card-image-container")):
    tdiv(class="card-image"):
      genImg(card.image)
      if card.kind == player:
        tdiv(class="card-overlay"):
          tdiv(class="overlay-circle"):
            span(class="overlay-triangle")

proc renderCardContent(card: Card): VNode =
  buildHtml(tdiv(class="card-content")):
    h2(class="card-title"): text card.title
    if card.text.len > 0:
      p(class="card-description"): text card.text
    if card.dest.len > 0:
      span(class="card-destination"): text card.dest

proc renderCard(card: Card; prefs: Prefs; path: string): VNode =
  const smallCards = {app, player, summary, storeLink}
  let large = if card.kind notin smallCards: " large" else: ""
  let url = replaceUrls(card.url, prefs)

  buildHtml(tdiv(class=("card" & large))):
    if card.video.isSome:
      tdiv(class="card-container"):
        renderVideo(get(card.video), prefs, path)
        a(class="card-content-container", href=url):
          renderCardContent(card)
    else:
      a(class="card-container", href=url):
        if card.image.len > 0:
          renderCardImage(card)
        tdiv(class="card-content-container"):
          renderCardContent(card)

func formatStat(stat: int): string =
  if stat > 0: insertSep($stat, ',')
  else: ""

proc renderStats*(stats: TweetStats): VNode =
  buildHtml(tdiv(class="tweet-stats")):
    span(class="tweet-stat"): icon "comment", formatStat(stats.replies)
    span(class="tweet-stat"): icon "retweet", formatStat(stats.retweets)
    span(class="tweet-stat"): icon "heart", formatStat(stats.likes)
    span(class="tweet-stat"): icon "views", formatStat(stats.views)

proc renderReply(tweet: Tweet): VNode =
  buildHtml(tdiv(class="replying-to")):
    text "Replying to "
    for i, u in tweet.reply:
      if i > 0: text " "
      a(href=("/" & u)): text "@" & u

proc renderAttribution(user: User; prefs: Prefs; link = ""): VNode =
  let href = if link.len > 0: link else: "/" & user.username
  buildHtml(a(class="attribution", href=href)):
    renderMiniAvatar(user, prefs)
    strong: text user.fullname
    verifiedIcon(user)

proc renderMediaTags(tags: seq[User]): VNode =
  buildHtml(tdiv(class="media-tag-block")):
    icon "user"
    for i, p in tags:
      a(class="media-tag", href=("/" & p.username), title=p.username):
        text p.fullname
      if i < tags.high:
        text ", "

proc renderLatestPost(username: string; id: int64): VNode =
  buildHtml(tdiv(class="latest-post-version")):
    text "There's a new version of this post. "
    a(href=getLink(id, username)):
      text "See the latest post"

proc renderCommunityNote(note: string; prefs: Prefs): VNode =
  buildHtml(tdiv(class="community-note")):
    tdiv(class="community-note-header"):
      icon "group"
      span: text "Community note"
    tdiv(class="community-note-text", dir="auto"):
      verbatim replaceUrls(note, prefs)

proc renderQuoteMedia(quote: Tweet; prefs: Prefs; path: string): VNode =
  buildHtml(tdiv(class="quote-media-container")):
    renderMedia(quote.media, prefs, path)

proc renderQuote(quote: Tweet; prefs: Prefs; path: string): VNode =
  if not quote.available:
    return buildHtml(tdiv(class="quote unavailable")):
      a(class="unavailable-quote", href=getLink(quote, focus=false)):
        if quote.tombstone.len > 0:
          text quote.tombstone
        elif quote.text.len > 0:
          text quote.text
        else:
          text "This tweet is unavailable"

  buildHtml(tdiv(class="quote quote-big")):
    a(class="quote-link", href=getLink(quote))

    tdiv(class="tweet-name-row"):
      tdiv(class="fullname-and-username"):
        renderMiniAvatar(quote.user, prefs)
        linkUser(quote.user, class="fullname")
        verifiedIcon(quote.user)
        linkUser(quote.user, class="username")

      span(class="tweet-date"):
        a(href=getLink(quote), title=quote.getTime):
          text quote.getShortTime

    if quote.reply.len > 0:
      renderReply(quote)

    if quote.text.len > 0:
      tdiv(class="quote-text", dir="auto"):
        verbatim replaceUrls(quote.text, prefs)

    if quote.media.len > 0:
      renderQuoteMedia(quote, prefs, path)

    if quote.articlePreview.isSome:
      renderArticleCard(quote.articlePreview.get(), prefs)

    if quote.note.len > 0 and not prefs.hideCommunityNotes:
      renderCommunityNote(quote.note, prefs)

    if quote.hasThread:
      a(class="show-thread", href=getLink(quote)):
        text "Show this thread"

    if quote.history.len > 0 and quote.id != max(quote.history):
      tdiv(class="quote-latest"):
        text "There's a new version of this post"

proc renderDisclosures*(tweet: Tweet): VNode =
  buildHtml(tdiv(class="disclosures")):
    if tweet.isAI:
      span(data-disclosure="ai"):
        icon "attention-circled", "Made with AI"
    if tweet.isAd:
      span(data-disclosure="ad"):
        icon "attention-circled", "Paid partnership (ad)"

proc renderLocation*(tweet: Tweet): string =
  let (place, url) = tweet.getLocation()
  if place.len == 0: return
  let node = buildHtml(span(class="tweet-geo")):
    text " – at "
    if url.len > 1:
      a(href=url): text place
    else:
      text place
  return $node

proc renderTweet*(tweet: Tweet; prefs: Prefs; path: string; class=""; index=0;
                  last=false; mainTweet=false; afterTweet=false;
                  bigThumb=false): VNode =
  var divClass = class
  if index == -1 or last:
    divClass = "thread-last " & class

  if not tweet.available:
    return buildHtml(tdiv(class=divClass & "unavailable timeline-item", data-username=tweet.user.username)):
      a(class="unavailable-box", href=getLink(tweet)):
        if tweet.tombstone.len > 0:
          text tweet.tombstone
        elif tweet.text.len > 0:
          text tweet.text
        else:
          text "This tweet is unavailable"

      if tweet.quote.isSome:
        renderQuote(tweet.quote.get(), prefs, path)

  let
    fullTweet = tweet
    pinned = tweet.pinned

  var retweet: string
  var tweet = fullTweet
  if tweet.retweet.isSome:
    tweet = tweet.retweet.get
    retweet = fullTweet.user.fullname

  buildHtml(tdiv(class=("timeline-item " & divClass), data-username=tweet.user.username)):
    if not mainTweet:
      a(class="tweet-link", href=getLink(tweet))

    tdiv(class="tweet-body"):
      renderHeader(tweet, retweet, pinned, prefs, path)

      if not afterTweet and index == 0 and tweet.reply.len > 0 and
         (tweet.reply.len > 1 or tweet.reply[0] != tweet.user.username or pinned):
        renderReply(tweet)

      var tweetClass = "tweet-content media-body"
      if prefs.bidiSupport:
        tweetClass &= " tweet-bidi"

      tdiv(class=tweetClass, dir="auto"):
        verbatim replaceUrls(tweet.text, prefs) & renderLocation(tweet)

      if tweet.attribution.isSome:
        renderAttribution(tweet.attribution.get(), prefs, tweet.attributionLink)

      if tweet.card.isSome and tweet.card.get().kind != hidden:
        renderCard(tweet.card.get(), prefs, path)

      if tweet.articlePreview.isSome:
        renderArticleCard(tweet.articlePreview.get(), prefs)

      if tweet.media.len > 0:
        renderMedia(tweet.media, prefs, path, bigThumb)

      if tweet.poll.isSome:
        renderPoll(tweet.poll.get())

      if tweet.quote.isSome:
        renderQuote(tweet.quote.get(), prefs, path)

      if tweet.note.len > 0 and not prefs.hideCommunityNotes:
        renderCommunityNote(tweet.note, prefs)

      if tweet.isAI or tweet.isAd:
        renderDisclosures(tweet)

      let
        hasEdits = tweet.history.len > 1
        isLatest = hasEdits and tweet.id == max(tweet.history)

      if mainTweet:
        p(class="tweet-published"): 
          if hasEdits and isLatest:
            a(href=(getLink(tweet, focus=false) & "/history")):
              text &"Last edited {getTime(tweet)}"
          else:
            text &"{getTime(tweet)}"

        if hasEdits and not isLatest:
          renderLatestPost(tweet.user.username, max(tweet.history))

      if tweet.mediaTags.len > 0:
        renderMediaTags(tweet.mediaTags)

      if not prefs.hideTweetStats:
        renderStats(tweet.stats)

proc renderTweetEmbed*(tweet: Tweet; path: string; prefs: Prefs; cfg: Config; req: Request): string =
  let node = buildHtml(html(lang="en")):
    renderHead(prefs, cfg, req)

    body:
      tdiv(class="tweet-embed"):
        renderTweet(tweet, prefs, path, mainTweet=true)

  result = doctype & $node



================================================
FILE: tests/base.py
================================================
from seleniumbase import BaseCase


class Card(object):
    def __init__(self, tweet=''):
        card = tweet + '.card '
        self.link = card + 'a'
        self.title = card + '.card-title'
        self.description = card + '.card-description'
        self.destination = card + '.card-destination'
        self.image = card + '.card-image'


class Quote(object):
    def __init__(self, tweet=''):
        quote = tweet + '.quote '
        namerow = quote + '.fullname-and-username '
        self.link = quote + '.quote-link'
        self.fullname = namerow + '.fullname'
        self.username = namerow + '.username'
        self.text = quote + '.quote-text'
        self.media = quote + '.quote-media-container'
        self.unavailable = quote + '.quote.unavailable'


class Tweet(object):
    def __init__(self, tweet=''):
        namerow = tweet + '.tweet-header '
        self.fullname = namerow + '.fullname'
        self.username = namerow + '.username'
        self.date = namerow + '.tweet-date'
        self.text = tweet + '.tweet-content.media-body'
        self.retweet = tweet + '.retweet-header'
        self.reply = tweet + '.replying-to'


class Profile(object):
    fullname = '.profile-card-fullname'
    username = '.profile-card-username'
    protected = '.icon-lock'
    verified = '.verified-icon'
    banner = '.profile-banner'
    bio = '.profile-bio'
    location = '.profile-location'
    website = '.profile-website'
    joinDate = '.profile-joindate'
    mediaCount = '.photo-rail-header'


class Timeline(object):
    newest = 'div[class="timeline-item show-more"]'
    older = 'div[class="show-more"]'
    end = '.timeline-end'
    none = '.timeline-none'
    protected = '.timeline-protected'
    photo_rail = '.photo-rail-grid'
    media_view_tabs = '.media-view-tabs'
    media_view_timeline = '.media-view-tabs a[href$="media?view=timeline"]'
    media_view_grid = '.media-view-tabs a[href$="media?view=grid"]'
    media_view_gallery = '.media-view-tabs a[href$="media?view=gallery"]'
    media_view_active = '.media-view-tabs .tab-item.active a'
    grid_view = '.timeline.media-grid-view'
    gallery_view = '.timeline.media-gallery-view'


class Conversation(object):
    main = '.main-tweet'
    before = '.before-tweet'
    after = '.after-tweet'
    replies = '.replies'
    thread = '.reply'
    tweet = '.timeline-item'
    tweet_text = '.tweet-content'


class Poll(object):
    votes = '.poll-info'
    choice = '.poll-meter'
    value = 'poll-choice-value'
    option = 'poll-choice-option'
    leader = 'leader'


class Media(object):
    container = '.attachments'
    row = '.gallery-row'
    image = '.still-image'
    video = '.gallery-video'
    gif = '.media-gif'


class BaseTestCase(BaseCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()

    def tearDown(self):
        super(BaseTestCase, self).tearDown()

    def open_nitter(self, page=''):
        self.open(f'http://localhost:8080/{page}')

    def search_username(self, username):
        self.open_nitter()
        self.update_text('.search-bar input[type=text]', username)
        self.submit('.search-bar form')


def get_timeline_tweet(num=1):
    return Tweet(f'.timeline > div:nth-child({num}) ')



================================================
FILE: tests/poetry.toml
================================================
[virtualenvs]
in-project = true



================================================
FILE: tests/pyproject.toml
================================================
[tool.poetry]
name = "nitter-tests"
version = "0.0.0"
package-mode = false

[tool.poetry.dependencies]
python = "^3.14"
seleniumbase = "4.46.5"



================================================
FILE: tests/requirements.txt
================================================
seleniumbase==4.46.5



================================================
FILE: tests/test_about_account.py
================================================
from base import BaseTestCase, Profile
from parameterized import parameterized


class AboutAccount(object):
    header = '.about-account-header'
    name = '.about-account-name'
    body = '.about-account-body'
    row = '.about-account-row'
    label = '.about-account-label'
    value = '.about-account-value'


# (username, expected_labels)
# Each label is checked for presence in the page text
about_data = [
    ['jack', ['Date joined', 'Account based in', 'Connected via']],
    ['NASA', ['Date joined']],
    ['elonmusk', ['Date joined']],
]

about_verified = [
    ['jack', 'Verified', 'Since '],
]

about_affiliate = [
    ['jack', 'An affiliate of', 'Square'],
    ['elonmusk', 'An affiliate of', 'X'],
]


class AboutAccountTest(BaseTestCase):
    @parameterized.expand(about_data)
    def test_about_page_has_labels(self, username, expected_labels):
        """About page shows expected info labels"""
        self.open_nitter(f'{username}/about')
        self.assert_element_visible(AboutAccount.header)
        self.assert_element_visible(AboutAccount.body)
        for label in expected_labels:
            self.assert_text(label, AboutAccount.body)

    @parameterized.expand(about_verified)
    def test_about_verified(self, username, label, value_prefix):
        """About page shows verification info for verified accounts"""
        self.open_nitter(f'{username}/about')
        self.assert_text(label, AboutAccount.body)
        self.assert_text(value_prefix, AboutAccount.body)

    @parameterized.expand(about_affiliate)
    def test_about_affiliate(self, username, label, affiliate):
        """About page shows affiliate info"""
        self.open_nitter(f'{username}/about')
        self.assert_text(label, AboutAccount.body)
        self.assert_text(f'@{affiliate}', AboutAccount.body)

    def test_about_page_title(self):
        """Title contains account name"""
        self.open_nitter('jack/about')
        self.assert_text('jack', AboutAccount.name)

    def test_about_join_date(self):
        """About page always shows join date"""
        self.open_nitter('jack/about')
        self.assert_text('Date joined', AboutAccount.body)
        self.assert_text('March 2006', AboutAccount.body)

    def test_about_invalid_user(self):
        """About page for non-existent user shows error"""
        self.open_nitter('thisprofiledoesntexist/about')
        self.assert_text('User "thisprofiledoesntexist" not found')

    def test_joindate_links_to_about(self):
        """Join date on profile page links to about page"""
        self.open_nitter('jack')
        link = self.find_element(Profile.joinDate + ' a')
        self.assertIn('/jack/about', link.get_attribute('href'))



================================================
FILE: tests/test_article.py
================================================
from base import BaseTestCase
from parameterized import parameterized


class ArticleSelectors:
    page = '.article-page'
    cover = '.article-cover'
    body = '.article-body'
    title = '.article-title'
    author = '.article-author'
    fullname = '.article-author .fullname'
    username = '.article-author .username'
    date = '.article-author .article-date'
    avatar = '.article-author img.avatar'
    verified = '.article-author .verified-icon'
    media = '.article-media'
    divider = '.article-divider'


articles = [
    ['2064166507438059759',
     '1s，秒杀一切，开源一个 X 文章发布 Skill【重磅升级】',
     'punk2898', 'Punk'],

    ['2064689664213041529',
     'SpaceX Thesis & Valuation Memorandum',
     'Dialectic_Group', 'Dialectic'],

    ['2064691088636424322',
     'Consciousness and AI: The Problem of Inner Experience',
     'CosmicOrFun', 'Cosmic Orphan'],

    ['2064696491948777658',
     'NC Push for Data Centers + Stablecoin Crypto= Data Centers are defacto BAILOUT OF Fed Reserve System',
     'June_12_1776', 'June_12_1776'],

    ['2064755789391110154',
     'DeFi Markets Update 2026-06-10',
     'SteakhouseFi', 'Steakhouse Financial'],

    ['2064755231901319527',
     'The machine economy has a killswitch and somebody just pulled it.',
     '1914ad', 'Justin Bechler HMP-028'],

    ['2062858677149675788',
     'Yakshinis',
     'CosmicOrFun', 'Cosmic Orphan'],
]

articles_with_media = [
    ['2064166507438059759', 6],
    ['2064689664213041529', 11],
    ['2064755789391110154', 5],
]

articles_with_dividers = [
    ['2064166507438059759', 1],
    ['2064689664213041529', 6],
]


class ArticleBasicTest(BaseTestCase):
    @parameterized.expand(articles)
    def test_article_loads(self, tweet_id, title, username, fullname):
        self.open_nitter(f'i/article/{tweet_id}')
        self.assert_element_visible(ArticleSelectors.page)
        self.assert_element_visible(ArticleSelectors.body)
        self.assert_text(title, ArticleSelectors.title)

    @parameterized.expand(articles)
    def test_article_author(self, tweet_id, title, username, fullname):
        self.open_nitter(f'i/article/{tweet_id}')
        self.assert_element_visible(ArticleSelectors.author)
        self.assert_text(f'@{username}', ArticleSelectors.username)

    @parameterized.expand(articles)
    def test_article_has_cover(self, tweet_id, title, username, fullname):
        self.open_nitter(f'i/article/{tweet_id}')
        self.assert_element_visible(ArticleSelectors.cover)
        src = self.get_attribute(ArticleSelectors.cover, 'src')
        self.assertIn('/pic/', src)

    @parameterized.expand(articles)
    def test_article_has_date(self, tweet_id, title, username, fullname):
        self.open_nitter(f'i/article/{tweet_id}')
        date_text = self.get_text(ArticleSelectors.date)
        self.assertTrue(len(date_text) > 3)

    @parameterized.expand(articles)
    def test_article_author_avatar(self, tweet_id, title, username, fullname):
        self.open_nitter(f'i/article/{tweet_id}')
        self.assert_element_visible(ArticleSelectors.avatar)
        src = self.get_attribute(ArticleSelectors.avatar, 'src')
        self.assertIn('/pic/', src)
        self.assertGreater(len(src), len('/pic/'))

    @parameterized.expand(articles)
    def test_article_author_verified(self, tweet_id, title, username, fullname):
        self.open_nitter(f'i/article/{tweet_id}')
        self.assert_element_visible(ArticleSelectors.verified)

    def test_article_author_verified_business(self):
        self.open_nitter('i/article/2064755789391110154')
        self.assert_element_visible('.article-author .verified-icon.business')


class ArticleContentTest(BaseTestCase):
    def test_article_has_paragraphs(self):
        self.open_nitter('i/article/2064689664213041529')
        paragraphs = self.find_elements('.article-body p')
        self.assertGreater(len(paragraphs), 10)

    def test_article_has_headers(self):
        self.open_nitter('i/article/2064689664213041529')
        headers = self.find_elements('.article-body h1, .article-body h2')
        self.assertGreater(len(headers), 5)

    def test_article_has_bold_text(self):
        self.open_nitter('i/article/2064166507438059759')
        bold = self.find_elements('.article-body strong')
        self.assertGreater(len(bold), 0)

    def test_article_has_italic_text(self):
        self.open_nitter('i/article/2064166507438059759')
        italic = self.find_elements('.article-body em')
        self.assertGreater(len(italic), 0)

    def test_article_has_blockquotes(self):
        self.open_nitter('i/article/2064696491948777658')
        self.assert_element_visible('.article-body blockquote')

    def test_article_has_lists(self):
        self.open_nitter('i/article/2064696491948777658')
        self.assert_element_visible('.article-body ul')

    def test_article_has_emoji_text(self):
        self.open_nitter('i/article/2064166507438059759')
        body = self.get_text(ArticleSelectors.body)
        self.assertTrue(any(ord(c) > 0x1F000 for c in body))

    def test_article_has_links(self):
        self.open_nitter('i/article/2064691088636424322')
        links = self.find_elements('.article-body a[href]')
        self.assertGreater(len(links), 0)

    def test_article_twitter_links_localized(self):
        self.open_nitter('i/article/2064755789391110154')
        links = self.find_elements('.article-body a[href^="https://x.com"]')
        self.assertEqual(len(links), 0, 'x.com links should be converted to local paths')

    @parameterized.expand(articles_with_media)
    def test_article_media_count(self, tweet_id, expected_count):
        self.open_nitter(f'i/article/{tweet_id}')
        media = self.find_elements(ArticleSelectors.media)
        self.assertEqual(len(media), expected_count)

    @parameterized.expand(articles_with_dividers)
    def test_article_divider_count(self, tweet_id, expected_count):
        self.open_nitter(f'i/article/{tweet_id}')
        dividers = self.find_elements(ArticleSelectors.divider)
        self.assertEqual(len(dividers), expected_count)


class ArticleMediaTest(BaseTestCase):
    def test_media_images_proxied(self):
        self.open_nitter('i/article/2064689664213041529')
        self.assert_element_visible(ArticleSelectors.media)
        img = self.find_element(f'{ArticleSelectors.media} img')
        src = img.get_attribute('src')
        self.assertIn('/pic/', src)
        self.assertFalse(src.startswith('https://pbs.twimg.com'))

    def test_cover_image_proxied(self):
        self.open_nitter('i/article/2064689664213041529')
        self.assert_element_visible(ArticleSelectors.cover)
        src = self.get_attribute(ArticleSelectors.cover, 'src')
        self.assertIn('/pic/', src)
        self.assertFalse(src.startswith('https://pbs.twimg.com'))

    def test_embedded_tweet(self):
        self.open_nitter('i/article/2064755789391110154')
        self.assert_element_visible('.article-body .timeline-item')

    def test_multiple_embedded_tweets(self):
        self.open_nitter('i/article/2064755231901319527')
        tweets = self.find_elements('.article-body .timeline-item')
        self.assertGreaterEqual(len(tweets), 3)


class ArticleMentionTest(BaseTestCase):
    def test_mention_linkified(self):
        self.open_nitter('i/article/2064755231901319527')
        link = self.find_element('.article-body a[href="/ZachXBT"]')
        self.assertEqual(link.text, '@ZachXBT')

    def test_multiple_mentions_linkified(self):
        self.open_nitter('i/article/2064755231901319527')
        links = self.find_elements('.article-body a[href^="/"]')
        mention_hrefs = [l.get_attribute('href') for l in links
                         if l.text.startswith('@')]
        usernames = [h.split('/')[-1] for h in mention_hrefs]
        self.assertIn('ZachXBT', usernames)
        self.assertIn('River', usernames)

    def test_mention_in_different_article(self):
        self.open_nitter('i/article/2064689664213041529')
        link = self.find_element('.article-body a[href="/FutureJurvetson"]')
        self.assertEqual(link.text, '@FutureJurvetson')

    def test_no_spurious_whitespace_in_styled_paragraph(self):
        """Styled paragraphs should not have extra whitespace from VNode serialization."""
        self.open_nitter('i/article/2064696491948777658')
        source = self.get_page_source()
        self.assertNotIn('white-space: pre-wrap', source)
        self.assertNotIn('white-space:pre-wrap', source)


class ArticleCardTest(BaseTestCase):
    @parameterized.expand(articles)
    def test_status_page_shows_article_card(self, tweet_id, title, username, fullname):
        self.open_nitter(f'{username}/status/{tweet_id}')
        self.assert_element_visible('.article-card')
        self.assert_text(title, '.article-card .card-title')

    def test_article_card_has_cover_image(self):
        self.open_nitter('Dialectic_Group/status/2064689664213041529')
        self.assert_element_visible('.article-card .card-image img')
        src = self.get_attribute('.article-card .card-image img', 'src')
        self.assertIn('/pic/', src)

    def test_article_card_has_badge(self):
        self.open_nitter('Dialectic_Group/status/2064689664213041529')
        self.assert_element_visible('.article-card-badge')
        self.assert_text('Article', '.article-card-badge')

    def test_article_card_has_preview_text(self):
        self.open_nitter('CosmicOrFun/status/2064691088636424322')
        self.assert_element_visible('.article-card .card-description')

    def test_article_card_links_to_article(self):
        self.open_nitter('punk2898/status/2064166507438059759')
        href = self.get_attribute('.article-card .card-container', 'href')
        self.assertIn('/article/', href)

    def test_article_url_stripped_from_tweet_text(self):
        self.open_nitter('punk2898/status/2064166507438059759')
        self.assert_element_visible('.article-card')
        source = self.get_page_source()
        # Main tweet text should not contain article URL
        import re
        main = re.search(r'id="m".*?tweet-content[^>]*>(.*?)</div>', source, re.DOTALL)
        self.assertIsNotNone(main)
        self.assertNotIn('/article/', main.group(1))


class ArticleQuotedCardTest(BaseTestCase):
    """Article cards inside quoted tweets (1914ad quoting own article)."""
    quoted_tweet = '1914ad/status/2064789532071891085'
    quoted_article_id = '2063677483548102688'

    def test_quoted_card_visible(self):
        self.open_nitter(self.quoted_tweet)
        self.assert_element_visible('.quote .article-card')

    def test_quoted_card_has_title(self):
        self.open_nitter(self.quoted_tweet)
        self.assert_text('David Bailey Already Won', '.quote .article-card .card-title')

    def test_quoted_card_has_badge(self):
        self.open_nitter(self.quoted_tweet)
        self.assert_element_visible('.quote .article-card-badge')
        self.assert_text('Article', '.quote .article-card-badge')

    def test_quoted_card_has_cover_image(self):
        self.open_nitter(self.quoted_tweet)
        self.assert_element_visible('.quote .article-card .card-image img')
        src = self.get_attribute('.quote .article-card .card-image img', 'src')
        self.assertIn('/pic/', src)

    def test_quoted_card_has_description(self):
        self.open_nitter(self.quoted_tweet)
        self.assert_element_visible('.quote .article-card .card-description')

    def test_quoted_card_links_to_article(self):
        self.open_nitter(self.quoted_tweet)
        href = self.get_attribute('.quote .article-card .card-container', 'href')
        self.assertIn(f'/article/{self.quoted_article_id}', href)


class ArticleRoutingTest(BaseTestCase):
    def test_username_article_route_redirects(self):
        self.open_nitter('punk2898/article/2064166507438059759')
        self.assert_element_visible(ArticleSelectors.page)
        self.assert_text('1s', ArticleSelectors.title)

    def test_status_article_route_redirects(self):
        self.open_nitter('punk2898/status/2064166507438059759/article')
        self.assert_element_visible(ArticleSelectors.page)
        self.assert_text('1s', ArticleSelectors.title)

    def test_invalid_id_returns_404(self):
        self.open_nitter('i/article/notanumber')
        self.assert_element_not_visible(ArticleSelectors.page)

    def test_nonexistent_article(self):
        self.open_nitter('i/article/1')
        self.assert_element_visible('.error-panel')



================================================
FILE: tests/test_card.py
================================================
from base import BaseTestCase, Card, Conversation
from parameterized import parameterized


card = [
    ['nim_lang/status/1136652293510717440',
     'Version 0.20.0 released',
     'We are very proud to announce Nim version 0.20. This is a massive release, both literally and figuratively. It contains more than 1,000 commits and it marks our release candidate for version 1.0!',
     'nim-lang.org', True],

    ['voidtarget/status/1094632512926605312',
     'Basic OBS Studio plugin, written in nim, supporting C++ (C fine too)',
     'Basic OBS Studio plugin, written in nim, supporting C++ (C fine too) - obsplugin.nim',
     'gist.github.com', True],

    ['NASA/status/2061872347477418301',
     'Nancy Grace Roman Space Telescope - NASA Science',
     'The Nancy Grace Roman Space Telescope will settle essential questions in the areas of dark energy, exoplanets, and astrophysics.',
     'science.nasa.gov', True]
]

no_thumb = [
    ['Thom_Wolf/status/1122466524860702729',
     'GitHub - facebookresearch/XLM: PyTorch original implementation of Cross-lingual Language Model',
     'PyTorch original implementation of Cross-lingual Language Model Pretraining.',
     'github.com'],

    ['brent_p/status/1088857328680488961',
     'GitHub - brentp/hts-nim: nim wrapper for htslib for parsing genomics data files',
     '',
     'github.com'],

    ['voidtarget/status/1133028231672582145',
     'sinkingsugar/nimqt-example',
     'A sample of a Qt app written using mostly nim. Contribute to sinkingsugar/nimqt-example development by creating an account on GitHub.',
     'github.com']
]

playable = [
    ['NASA/status/2047048645845897398',
     'NASA\'s Artemis II News Conference with Moon Astronauts',
     'Live from NASA\'s Johnson Space Center in Houston',
     'youtube.com']
]

class CardTest(BaseTestCase):
    @parameterized.expand(card)
    def test_card(self, tweet, title, description, destination, large):
        self.open_nitter(tweet)
        c = Card(Conversation.main + " ")
        self.assert_text(title, c.title)
        self.assert_text(destination, c.destination)
        self.assertIn('/pic/', self.get_image_url(c.image + ' img'))
        if len(description) > 0:
            self.assert_text(description, c.description)
        if large:
            self.assert_element_visible('.card.large')
        else:
            self.assert_element_not_visible('.card.large')

    @parameterized.expand(no_thumb)
    def test_card_no_thumb(self, tweet, title, description, destination):
        self.open_nitter(tweet)
        c = Card(Conversation.main + " ")
        self.assert_text(title, c.title)
        self.assert_text(destination, c.destination)
        if len(description) > 0:
            self.assert_text(description, c.description)

    @parameterized.expand(playable, skip_on_empty=True)
    def test_card_playable(self, tweet, title, description, destination):
        self.open_nitter(tweet)
        c = Card(Conversation.main + " ")
        self.assert_text(title, c.title)
        self.assert_text(destination, c.destination)
        self.assertIn('/pic/', self.get_image_url(c.image + ' img'))
        self.assert_element_visible('.card-overlay')
        if len(description) > 0:
            self.assert_text(description, c.description)



================================================
FILE: tests/test_community.py
================================================
from base import BaseTestCase
from parameterized import parameterized


COMMUNITY_ID = '1493446837214187523'
COMMUNITY_PATH = f'i/communities/{COMMUNITY_ID}'


class CommunityTest(BaseTestCase):
    def test_top_page_loads(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.community-header')
        self.assert_text('Build in Public', '.community-name')

    def test_banner_visible(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.timeline-banner img')

    def test_member_count(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.community-member-count')
        self.assert_text('Members', '.community-member-count')

    def test_description_visible(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.community-description')

    def test_tabs_present(self):
        self.open_nitter(COMMUNITY_PATH)
        tabs = self.find_elements('.tab a')
        labels = [t.text for t in tabs]
        self.assertEqual(labels, ['Top', 'Latest', 'Media', 'About'])

    def test_top_tab_active(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.tab .active a[href$="/' + COMMUNITY_ID + '"]')

    def test_top_has_tweets(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.timeline-item .tweet-body')

    def test_top_has_pagination(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.show-more')
        self.assert_text('Load more', '.show-more')

    def test_latest_has_tweets(self):
        self.open_nitter(f'{COMMUNITY_PATH}/latest')
        self.assert_element_visible('.timeline-item .tweet-body')

    def test_latest_tab_active(self):
        self.open_nitter(f'{COMMUNITY_PATH}/latest')
        self.assert_element_visible('.tab .active a[href$="/latest"]')

    def test_media_has_tweets(self):
        self.open_nitter(f'{COMMUNITY_PATH}/media')
        self.assert_element_visible('.timeline-item .tweet-body')

    def test_media_tab_active(self):
        self.open_nitter(f'{COMMUNITY_PATH}/media')
        self.assert_element_visible('.tab .active a[href$="/media"]')

    def test_about_page(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_element_visible('.community-about')
        self.assert_text('Community Info', '.community-info h2')

    def test_about_rules(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_element_visible('.community-rules')
        self.assert_text('Rules', '.community-rules h2')
        rules = self.find_elements('.community-rule')
        self.assertGreater(len(rules), 0)

    def test_about_creator(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_text('Created', '.community-info')
        link = self.find_element('.community-info-item a')
        self.assertTrue(link.text.startswith('@'))
        self.assertGreater(len(link.text), 1)

    def test_about_tab_active(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_element_visible('.tab .active a[href$="/about"]')

    def test_about_moderators(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_element_visible('.community-moderators')
        self.assert_text('Moderators', '.community-moderators h2')
        mods = self.find_elements('.community-moderator')
        self.assertGreater(len(mods), 0)

    def test_about_moderators_have_avatars(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        avatars = self.find_elements('.community-mod-avatar')
        self.assertGreater(len(avatars), 0)

    def test_about_moderators_link_to_profiles(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        links = self.find_elements('.community-mod-username')
        self.assertGreater(len(links), 0)
        for link in links:
            self.assertTrue(link.text.startswith('@'))
            self.assertTrue(link.get_attribute('href').startswith('http'))

    def test_about_see_all_link(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        link = self.find_element('.community-mods-link')
        self.assertEqual(link.text, 'See all')
        self.assertIn('/moderators', link.get_attribute('href'))

    def test_members_page(self):
        self.open_nitter(f'{COMMUNITY_PATH}/members')
        self.assert_element_visible('.timeline-item')
        users = self.find_elements('.timeline-item .username')
        self.assertGreater(len(users), 0)

    def test_members_has_member_tabs(self):
        self.open_nitter(f'{COMMUNITY_PATH}/members')
        tabs = self.find_elements('.tab a')
        labels = [t.text for t in tabs]
        self.assertEqual(labels, ['All', 'Moderators'])

    def test_members_all_tab_active(self):
        self.open_nitter(f'{COMMUNITY_PATH}/members')
        self.assert_element_visible('.tab .active a[href$="/members"]')

    def test_members_count_is_link(self):
        self.open_nitter(COMMUNITY_PATH)
        link = self.find_element('.community-member-count')
        self.assertIn('Members', link.text)
        self.assertIn('/members', link.get_attribute('href'))

    def test_moderators_page(self):
        self.open_nitter(f'{COMMUNITY_PATH}/moderators')
        self.assert_element_visible('.timeline-item')
        users = self.find_elements('.timeline-item .username')
        self.assertGreater(len(users), 0)

    def test_moderators_tab_active(self):
        self.open_nitter(f'{COMMUNITY_PATH}/moderators')
        self.assert_element_visible('.tab .active a[href$="/moderators"]')

    def test_moderators_has_member_tabs(self):
        self.open_nitter(f'{COMMUNITY_PATH}/moderators')
        tabs = self.find_elements('.tab a')
        labels = [t.text for t in tabs]
        self.assertEqual(labels, ['All', 'Moderators'])

    def test_pinned_tweet_label(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.pinned')
        self.assert_text('Pinned by Community mods', '.pinned')

    def test_hashtags_visible(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.community-tags')
        tags = self.find_elements('.community-tag')
        self.assertGreater(len(tags), 0)

    def test_hashtags_are_links(self):
        self.open_nitter(COMMUNITY_PATH)
        tags = self.find_elements('.community-tag')
        for tag in tags:
            href = tag.get_attribute('href')
            self.assertIn('/hashtag/', href)
            self.assertTrue(tag.text.startswith('#'))

    def test_hashtag_page(self):
        self.open_nitter(f'{COMMUNITY_PATH}/hashtag/buildinpublic')
        self.assert_element_visible('.timeline-item .tweet-body')

    def test_hashtag_shows_header(self):
        self.open_nitter(f'{COMMUNITY_PATH}/hashtag/buildinpublic')
        self.assert_element_visible('.community-header')
        self.assert_text('Build in Public', '.community-name')

    def test_hashtag_shows_tag_title(self):
        self.open_nitter(f'{COMMUNITY_PATH}/hashtag/buildinpublic')
        self.assert_element_visible('.community-hashtag-header')
        self.assert_text('#buildinpublic', '.community-hashtag-title')

    def test_hashtag_no_main_tabs(self):
        self.open_nitter(f'{COMMUNITY_PATH}/hashtag/buildinpublic')
        tabs = self.find_elements('.tab a')
        tab_labels = [t.text for t in tabs]
        self.assertNotIn('Top', tab_labels)
        self.assertNotIn('About', tab_labels)

    def test_category_visible(self):
        self.open_nitter(COMMUNITY_PATH)
        self.assert_element_visible('.community-category')

    def test_about_join_policy(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_text('Anyone can join', '.community-info')

    def test_about_visibility_note(self):
        self.open_nitter(f'{COMMUNITY_PATH}/about')
        self.assert_text('publicly visible', '.community-info')

    def test_404_invalid_id(self):
        self.open_nitter('i/communities/999')
        self.assert_element_visible('.error-panel')
        self.assert_text('not found', '.error-panel')

    @parameterized.expand(['', '/latest', '/media', '/about',
                           '/members', '/moderators'])
    def test_page_no_error(self, suffix):
        self.open_nitter(f'{COMMUNITY_PATH}{suffix}')
        self.assert_element_not_visible('.error-panel')



================================================
FILE: tests/test_followers.py
================================================
# SPDX-License-Identifier: AGPL-3.0-only
from base import BaseTestCase, Timeline


class FollowersTest(BaseTestCase):
    """Tests for followers and following pages"""

    def test_followers_page_loads(self):
        """Test that followers page loads and shows users"""
        self.open_nitter('jack/followers')
        self.assert_title_contains('following @jack')
        # Check for user list
        self.assert_element('.timeline-item')

    def test_following_page_loads(self):
        """Test that following page loads and shows users"""
        self.open_nitter('jack/following')
        self.assert_title_contains('followed by @jack')
        # Check for user list
        self.assert_element('.timeline-item')

    def test_followers_has_navigation_tabs(self):
        """Test that followers page has following/followers tabs"""
        self.open_nitter('jack/followers')
        self.assert_element('.profile-statlist')
        # Check for Following and Followers links
        self.assert_element('a[href="/jack/following"]')
        self.assert_element('a[href="/jack/followers"]')

    def test_following_pagination(self):
        """Test that following page has load more button or scroll-to-top"""
        self.open_nitter('jack/following')
        # Should have either more button or top-ref (scroll to top arrow)
        try:
            self.assert_element('.show-more')
        except:
            self.assert_element('.top-ref')

    def test_nonexistent_user_followers(self):
        """Test 404 for non-existent user"""
        self.open_nitter('this_user_definitely_does_not_exist_12345/followers')
        self.assert_element('.error-panel')
        self.assert_text_visible('not found')



================================================
FILE: tests/test_profile.py
================================================
from base import BaseTestCase, Profile
from parameterized import parameterized

profiles = [
        ['mobile_test', 'Test account',
         'Test Account. test test Testing username with @mobile_test_2 and a #hashtag',
         'San Francisco, CA', 'example.com/foobar', 'Joined October 2009', '97'],
        ['mobile_test_2', 'mobile test 2', '', '', '', 'Joined January 2011', '13']
]

verified = [['jack'], ['elonmusk']]

protected = [
    ['mobile_test_7', 'mobile test 7', ''],
    ['Poop', 'Randy', 'Social media fanatic.']
]

invalid = [['thisprofiledoesntexist']]

malformed = [
    ['${userId}'],
    ['$%7BuserId%7D'],  # URL encoded version
    ['%'],  # Percent sign is invalid
    ['user@name'],
    ['user.name'],
    ['user-name'],
    ['user$name'],
    ['user{name}'],
    ['user name'],  # space
]

banner_image = [
    ['mobile_test', 'profile_banners%2F82135242%2F1384108037%2F1500x500']
]


class ProfileTest(BaseTestCase):
    @parameterized.expand(profiles)
    def test_data(self, username, fullname, bio, location, website, joinDate, mediaCount):
        self.open_nitter(username)
        self.assert_exact_text(fullname, Profile.fullname)
        self.assert_exact_text(f'@{username}', Profile.username)

        tests = [
            (bio, Profile.bio),
            (location, Profile.location),
            (website, Profile.website),
            (joinDate, Profile.joinDate),
            (mediaCount + " Photos and videos", Profile.mediaCount)
        ]

        for text, selector in tests:
            if len(text) > 0:
                self.assert_exact_text(text, selector)
            else:
                self.assert_element_absent(selector)

    @parameterized.expand(verified)
    def test_verified(self, username):
        self.open_nitter(username)
        self.assert_element_visible(Profile.verified)

    @parameterized.expand(protected)
    def test_protected(self, username, fullname, bio):
        self.open_nitter(username)
        self.assert_element_visible(Profile.protected)
        self.assert_exact_text(fullname, Profile.fullname)
        self.assert_exact_text(f'@{username}', Profile.username)

        if len(bio) > 0:
            self.assert_text(bio, Profile.bio)
        else:
            self.assert_element_absent(Profile.bio)

    @parameterized.expand(invalid)
    def test_invalid_username(self, username):
        self.open_nitter(username)
        self.assert_text(f'User "{username}" not found')

    @parameterized.expand(malformed)
    def test_malformed_username(self, username):
        """Test that malformed usernames (with invalid characters) return 404"""
        self.open_nitter(username)
        # Malformed usernames should return 404 page not found, not try to fetch from Twitter
        self.assert_text('Page not found')

    def test_suspended(self):
        self.open_nitter('suspendme')
        self.assert_text('User "suspendme" has been suspended')

    @parameterized.expand(banner_image)
    def test_banner_image(self, username, url):
        self.open_nitter(username)
        banner = self.find_element(Profile.banner + ' img')
        self.assertIn(url, banner.get_attribute('src'))



================================================
FILE: tests/test_quote.py
================================================
from base import BaseTestCase, Quote, Conversation
from parameterized import parameterized

text = [
    ['nim_lang/status/1491461266849808397#m',
     'Nim', '@nim_lang',
     """What's better than Nim 1.6.0?

Nim 1.6.2 :)

nim-lang.org/blog/2021/12/17…"""]
]

image = [
    ['elonmusk/status/1138827760107790336', 'D83h6Y8UIAE2Wlz'],
    ['SpaceX/status/1067155053461426176', 'Ds9EYfxXoAAPNmx']
]

gif = [
    ['SpaceX/status/747497521593737216', 'Cl-R5yFWkAA_-3X'],
    ['nim_lang/status/1068099315074248704', 'DtJSqP9WoAAKdRC']
]

video = [
    ['bkuensting/status/1067316003200217088', 'IyCaQlzF0q8u9vBd']
]


class QuoteTest(BaseTestCase):
    @parameterized.expand(text)
    def test_text(self, tweet, fullname, username, text):
        self.open_nitter(tweet)
        quote = Quote(Conversation.main + " ")
        self.assert_text(fullname, quote.fullname)
        self.assert_text(username, quote.username)
        self.assert_text(text, quote.text)

    @parameterized.expand(image)
    def test_image(self, tweet, url):
        self.open_nitter(tweet)
        quote = Quote(Conversation.main + " ")
        self.assert_element_visible(quote.media)
        self.assertIn(url, self.get_image_url(quote.media + ' img'))

    @parameterized.expand(gif)
    def test_gif(self, tweet, url):
        self.open_nitter(tweet)
        quote = Quote(Conversation.main + " ")
        self.assert_element_visible(quote.media)
        self.assertIn(url, self.get_attribute(quote.media + ' source', 'src'))

    @parameterized.expand(video)
    def test_video(self, tweet, url):
        self.open_nitter(tweet)
        quote = Quote(Conversation.main + " ")
        self.assert_element_visible(quote.media)
        self.assertIn(url, self.get_image_url(quote.media + ' img'))



================================================
FILE: tests/test_search.py
================================================
from base import BaseTestCase
from parameterized import parameterized


#class SearchTest(BaseTestCase):
    #@parameterized.expand([['@mobile_test'], ['@mobile_test_2']])
    #def test_username_search(self, username):
        #self.search_username(username)
        #self.assert_text(f'{username}')



================================================
FILE: tests/test_security.py
================================================
import subprocess
from parameterized import parameterized

BASE_URL = 'http://localhost:8080'


def curl_status(url):
    """Get HTTP status code using curl to avoid URL normalization by Python libs."""
    result = subprocess.run(
        ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url],
        capture_output=True, text=True, timeout=10
    )
    return int(result.stdout)


class TestMalformedPaths:
    """Test that malformed paths don't crash the server.

    URLs like //foo are parsed as having 'foo' as the authority (host),
    resulting in an empty path. Empty paths previously crashed jester's
    static file handler. Now they return 400.

    URLs like //foo/bar are parsed as authority='foo', path='/bar',
    so they route normally (not empty path).
    """

    @parameterized.expand([
        # These parse to empty paths -> 400
        ('//lefty_rae', 400),
        ('//test', 400),
        ('//anyuser', 400),
    ])
    def test_empty_path_returns_400(self, path, expected_status):
        """URLs that parse to empty paths should return 400, not crash."""
        status = curl_status(f'{BASE_URL}{path}')
        assert status == expected_status, \
            f'Expected {expected_status} for {path}, got {status}'

    @parameterized.expand([
        ('/jack', 200),
        ('/about', 200),
        ('/', 200),
    ])
    def test_normal_paths_work(self, path, expected_status):
        """Normal paths should still work."""
        status = curl_status(f'{BASE_URL}{path}')
        assert status == expected_status, \
            f'Expected {expected_status} for {path}, got {status}'

    def test_server_survives_malformed_requests(self):
        """Server should handle malformed requests without crashing."""
        # These all parse to empty paths
        malformed_paths = ['//a', '//b', '//c', '//user', '//test']
        for path in malformed_paths:
            status = curl_status(f'{BASE_URL}{path}')
            assert status == 400, f'Expected 400 for {path}, got {status}'

        # Verify server is still responding after malformed requests
        status = curl_status(f'{BASE_URL}/')
        assert status == 200, 'Server should still be alive'



================================================
FILE: tests/test_space.py
================================================
# SPDX-License-Identifier: AGPL-3.0-only
"""Integration tests for Twitter Spaces support."""
import pytest
from seleniumbase import BaseCase


class TestSpacePage(BaseCase):
    """Tests for /i/spaces/@id route."""

    SPACE_ID = "1mxPaaRAwYjKN"
    SPACE_URL = f"http://localhost:8080/i/spaces/{SPACE_ID}"

    def test_space_page_loads(self):
        """Space page should load with title."""
        self.open(self.SPACE_URL)
        self.assert_element(".space-page")
        self.assert_element(".space-panel")
        self.assert_text_visible("INTEL WILL MOON NEXT WEEK", ".space-title")

    def test_space_host_info(self):
        """Space should display host in participants."""
        self.open(self.SPACE_URL)
        self.assert_element(".space-participants")
        self.assert_text_visible("bubble boi")
        self.assert_element(".host-badge")

    def test_space_metadata(self):
        """Space should display listener count and state."""
        self.open(self.SPACE_URL)
        self.assert_element(".space-meta")
        # Should show listener count (number format)
        meta_text = self.get_text(".space-meta")
        assert any(c.isdigit() for c in meta_text), "Should show listener count"
        # Should show ended state
        assert "Ended" in meta_text or "Jun" in meta_text, "Should show ended state"

    def test_space_participants(self):
        """Space should display host and speakers."""
        self.open(self.SPACE_URL)
        self.assert_element(".space-participants")
        # Host should have badge
        self.assert_element(".host-badge")
        self.assert_text_visible("Host", ".host-badge")
        # Should show speakers
        self.assert_text_visible("CANTELOPEPEEL")
        self.assert_text_visible("Based Burner Account")
        self.assert_text_visible("anon invests")

    def test_space_participant_avatars(self):
        """Participant avatars should load correctly."""
        self.open(self.SPACE_URL)
        # Check avatars in participants section
        avatars = self.find_elements(".space-participant img")
        assert len(avatars) >= 4, "Should have at least 4 participant avatars"
        for avatar in avatars:
            src = avatar.get_attribute("src")
            # Should NOT be double-encoded
            assert "%2Fpic%2F" not in src, f"Avatar URL double-encoded: {src}"
            # Should have valid path
            assert "/pic/" in src, f"Avatar URL missing /pic/: {src}"

    def test_space_player_hls_disabled(self):
        """Without HLS, should show enable button with video-overlay style."""
        self.open(self.SPACE_URL)
        self.assert_element(".space-player")
        self.assert_element(".video-overlay")
        # Should show duration in overlay-duration
        self.assert_element(".overlay-duration")
        # Should have enable button
        source = self.get_page_source()
        assert "Enable hls playback" in source

    def test_space_player_hls_enabled(self):
        """With HLS enabled, should have audio element in DOM."""
        self.open(self.SPACE_URL)
        # Set HLS preference via cookie
        self.add_cookie({"name": "hlsPlayback", "value": "on"})
        self.refresh()
        # Check page source for audio element (hidden until play clicked)
        source = self.get_page_source()
        assert '<audio data-url="' in source, "Should have audio element"
        assert "playAudio(this)" in source, "Should have play handler"
        # Overlay should be visible (uses video-overlay class)
        self.assert_element(".video-overlay")

    def test_space_stream_endpoint(self):
        """Stream endpoint should return HLS manifest."""
        import requests
        resp = requests.get(f"{self.SPACE_URL}/stream")
        assert resp.status_code == 200
        assert "#EXTM3U" in resp.text
        assert "#EXT-X-TARGETDURATION" in resp.text


class TestSpaceCard(BaseCase):
    """Tests for Space cards in tweets."""

    def test_space_card_in_tweet(self):
        """Tweet with Space should show card linking to Space page."""
        self.open("http://localhost:8080/bubbleboi/status/2065299704808960482")
        self.assert_element(".card")
        # Card should link to Space
        card_link = self.find_element(".card-container")
        href = card_link.get_attribute("href")
        assert "/i/spaces/" in href

    def test_space_card_title(self):
        """Space card should have title."""
        self.open("http://localhost:8080/bubbleboi/status/2065299704808960482")
        self.assert_text_visible("Twitter Space", ".card-title")


class TestSpaceNotFound(BaseCase):
    """Tests for error handling."""

    def test_invalid_space_id(self):
        """Invalid Space ID should show error."""
        self.open("http://localhost:8080/i/spaces/invalid123")
        self.assert_text_visible("Space not found")



================================================
FILE: tests/test_ssrf_1411.nim
================================================
# SPDX-License-Identifier: AGPL-3.0-only
# Reproduction + regression test for issue #1411:
# SSRF via /video proxy with default HMAC key and missing host validation.
import std/[unittest, uri]
import ".."/src/utils

suite "issue #1411 SSRF via /video proxy":
  setup:
    # The default key shipped in nitter.example.conf / config.nim.
    setHmacKey("secretkey")

  test "HMAC for arbitrary SSRF URLs is forgeable with the default key":
    # These signatures were independently computed (Python hmac-sha256, uppercase
    # hex, first 13 chars) and observed live in the issue report.
    check getHmac("http://172.17.0.1:19999/secret_data.m3u8") == "BBD19ACC6C012"
    check getHmac("http://172.17.0.1:19999/secret_data.mp4")  == "0780F00DDF3E7"

  test "isTwitterUrl rejects SSRF targets (the guard /video is missing)":
    # Internal / metadata hosts an attacker would target.
    check isTwitterUrl(parseUri("http://172.17.0.1:19999/secret_data.m3u8")) == false
    check isTwitterUrl(parseUri("http://169.254.169.254/latest/meta-data/x.m3u8")) == false
    check isTwitterUrl(parseUri("http://localhost/x.mp4")) == false
    check isTwitterUrl(parseUri("http://[::1]/x.mp4")) == false

  test "isTwitterUrl rejects userinfo / look-alike host bypass attempts":
    check isTwitterUrl(parseUri("http://video.twimg.com@169.254.169.254/x.mp4")) == false
    check isTwitterUrl(parseUri("http://video.twimg.com.evil.com/x.mp4")) == false
    check isTwitterUrl(parseUri("http://evilvideo.twimg.com.attacker/x.mp4")) == false

  test "isTwitterUrl rejects non-http schemes even on a Twitter host":
    check isTwitterUrl(parseUri("gopher://video.twimg.com/x.mp4")) == false
    check isTwitterUrl(parseUri("file:///etc/passwd")) == false
    check isTwitterUrl(parseUri("ftp://video.twimg.com/x.mp4")) == false

  test "isTwitterUrl still allows legitimate Twitter video hosts":
    check isTwitterUrl(parseUri("https://video.twimg.com/ext_tw_video/1/pu/pl/x.m3u8")) == true
    check isTwitterUrl(parseUri("https://video.twimg.com/amplify_video/1/vid/x.mp4")) == true
    check isTwitterUrl(parseUri("https://prod-fastly-us-east-1.video.pscp.tv/x.m3u8")) == true



================================================
FILE: tests/test_thread.py
================================================
from parameterized import parameterized
import pytest

from base import BaseTestCase, Conversation

thread = [
    [
        "octonion/status/975253897697611777",
        [],
        "Based",
        ["Crystal", "Julia"],
        [["For", "Then"], ["yeah,"]],
    ],
    ["octonion/status/975254452625002496", ["Based"], "Crystal", ["Julia"], []],
    ["octonion/status/975256058384887808", ["Based", "Crystal"], "Julia", [], []],
    [
        "d0m96/status/1141811379407425537",
        [],
        "I'm",
        ["The", "The", "Today", "Some", "If", "There", "Above"],
        [["Thank", "Also,"]],
    ],
    [
        "gmpreussner/status/999766552546299904",
        [],
        "A",
        [],
        [["I", "Especially"], ["I"]],
    ],
]


class ThreadTest(BaseTestCase):
    def find_tweets(self, selector):
        return self.find_elements(f"{selector} {Conversation.tweet_text}")

    def compare_first_word(self, tweets, selector):
        if len(tweets) > 0:
            self.assert_element_visible(selector)
            for i, tweet in enumerate(self.find_tweets(selector)):
                text = tweet.text.split(" ")[0]
                self.assert_equal(tweets[i], text)

    @parameterized.expand(thread)
    @pytest.mark.flaky(reruns=3)
    def test_thread(self, tweet, before, main, after, replies):
        self.open_nitter(tweet)
        self.assert_element_visible(Conversation.main)

        self.assert_text(main, Conversation.main)
        self.assert_text(main, Conversation.main)

        self.compare_first_word(before, Conversation.before)
        self.compare_first_word(after, Conversation.after)

        for i, reply in enumerate(self.find_elements(Conversation.thread)):
            selector = Conversation.replies + f" > div:nth-child({i + 1})"
            self.compare_first_word(replies[i], selector)



================================================
FILE: tests/test_timeline.py
================================================
from base import BaseTestCase, Timeline
from parameterized import parameterized

normal = [['jack'], ['elonmusk']]

after = [['jack', '1681686036294803456'],
         ['elonmusk', '1681686036294803456']]

no_more = [['mobile_test_8?cursor=DAABCgABF4YVAqN___kKAAICNn_4msIQAAgAAwAAAAIAAA']]

empty = [['emptyuser'], ['mobile_test_10']]

protected = [['mobile_test_7'], ['Empty_user']]

photo_rail = [['mobile_test', ['Bo0nDsYIYAIjqVn', 'BoQbwJAIUAA0QCY', 'BoQbRQxIIAA3FWD', 'Bn8Qh8iIIAABXrG']]]


class TweetTest(BaseTestCase):
    @parameterized.expand(normal)
    def test_timeline(self, username):
        self.open_nitter(username)
        self.assert_element_present(Timeline.older)
        self.assert_element_absent(Timeline.newest)
        self.assert_element_absent(Timeline.end)
        self.assert_element_absent(Timeline.none)

    @parameterized.expand(after)
    def test_after(self, username, cursor):
        self.open_nitter(f'{username}?cursor={cursor}')
        self.assert_element_present(Timeline.newest)
        self.assert_element_present(Timeline.older)
        self.assert_element_absent(Timeline.end)
        self.assert_element_absent(Timeline.none)

    @parameterized.expand(no_more)
    def test_no_more(self, username):
        self.open_nitter(username)
        self.assert_text('No more items', Timeline.end)
        self.assert_element_present(Timeline.newest)
        self.assert_element_absent(Timeline.older)

    @parameterized.expand(empty)
    def test_empty(self, username):
        self.open_nitter(username)
        self.assert_text('No items found', Timeline.none)
        self.assert_element_absent(Timeline.newest)
        self.assert_element_absent(Timeline.older)
        self.assert_element_absent(Timeline.end)

    @parameterized.expand(protected)
    def test_protected(self, username):
        self.open_nitter(username)
        self.assert_text('This account\'s tweets are protected.', Timeline.protected)
        self.assert_element_absent(Timeline.newest)
        self.assert_element_absent(Timeline.older)
        self.assert_element_absent(Timeline.end)

    def test_media_view_tabs(self):
        self.open_nitter('mobile_test/media')
        self.assert_element_present(Timeline.media_view_tabs)
        self.assert_text('Timeline', Timeline.media_view_timeline)
        self.assert_text('Grid', Timeline.media_view_grid)
        self.assert_text('Gallery', Timeline.media_view_gallery)
        self.assert_text('Timeline', Timeline.media_view_active)

    def test_media_view_grid_tab(self):
        self.open_nitter('mobile_test/media?view=grid')
        self.assert_element_present(Timeline.grid_view)
        self.assert_text('Grid', Timeline.media_view_active)

    def test_media_view_gallery_tab(self):
        self.open_nitter('mobile_test/media?view=gallery')
        self.assert_element_present(Timeline.gallery_view)
        self.assert_text('Gallery', Timeline.media_view_active)

    def test_media_view_tabs_not_on_posts(self):
        self.open_nitter('mobile_test')
        self.assert_element_absent(Timeline.media_view_tabs)

    #@parameterized.expand(photo_rail)
    #def test_photo_rail(self, username, images):
        #self.open_nitter(username)
        #self.assert_element_visible(Timeline.photo_rail)
        #for i, url in enumerate(images):
            #img = self.get_attribute(Timeline.photo_rail + f' a:nth-child({i + 1}) img', 'src')
            #self.assertIn(url, img)



================================================
FILE: tests/test_tweet.py
================================================
from base import BaseTestCase, Tweet, Conversation, get_timeline_tweet
from parameterized import parameterized

# image = tweet + 'div.attachments.media-body > div > div > a > div > img'
# self.assert_true(self.get_image_url(image).split('/')[0] == 'http')

timeline = [
    [1, 'Test account', 'mobile_test', '10 Aug 2016', '763483571793174528',
     '.'],

    [3, 'Test account', 'mobile_test', '3 Mar 2016', '705522133443571712',
     'LIVE on #Periscope pscp.tv/w/aadiTzF6dkVOTXZSbX…'],

    [6, 'mobile test 2', 'mobile_test_2', '1 Oct 2014', '517449200045277184',
     'Testing. One two three four. Test.']
]

status = [
    [20, 'jack', 'jack', '21 Mar 2006', 'just setting up my twttr'],
    [134849778302464000, 'The Twoffice', 'TheTwoffice', '11 Nov 2011', 'test'],
    [105685475985080322, 'The Twoffice', 'TheTwoffice', '22 Aug 2011', 'regular tweet'],
    [572593440719912960, 'Test account', 'mobile_test', '3 Mar 2015', 'testing test']
]

invalid = [
    ['mobile_test/status/120938109238'],
    ['TheTwoffice/status/8931928312']
]

multiline = [
    [1718660434457239868, 'WebDesignMuseum',
     """
Happy 32nd Birthday HTML tags! 

On October 29, 1991, the internet pioneer, Tim Berners-Lee, published a document entitled HTML Tags. 

The document contained a description of the first 18 HTML tags: <title>, <nextid>, <a>, <isindex>, <plaintext>, <listing>, <p>, <h1>…<h6>, <address>, <hp1>, <hp2>…, <dl>, <dt>, <dd>, <ul>, <li>,<menu> and <dir>. The design of the first version of HTML language was influenced by the SGML universal markup language.

#WebDesignHistory"""]
]

link = [
    ['nim_lang/status/1110499584852353024', [
        'nim-lang.org/araq/ownedrefs.…',
        'news.ycombinator.com/item?id…',
        'teddit.net/r/programming…'
    ]],
    ['nim_lang/status/1125887775151140864', [
        'en.wikipedia.org/wiki/Nim_(p…'
    ]],
    ['hiankun_taioan/status/1086916335215341570', [
        '(hackernoon.com/interview-wit…)'
    ]],
    ['archillinks/status/1146302618223951873', [
        'flickr.com/photos/87101284@N…',
        'hisafoto.tumblr.com/post/176…'
    ]],
    ['archillinks/status/1146292551936335873', [
        'flickr.com/photos/michaelrye…',
        'furtho.tumblr.com/post/16618…'
    ]]
]

username = [
    ['Bountysource/status/1094803522053320705', ['nim_lang']],
    ['leereilly/status/1058464250098704385', ['godotengine', 'unity3d', 'nim_lang']]
]

emoji = [
    ['Tesla/status/1134850442511257600', '🌈❤️🧡💛💚💙💜']
]

retweet = [
    [7, 'mobile_test_2', 'mobile test 2', 'Test account', '@mobile_test',
     'Testing. 1234.']
]


class TweetTest(BaseTestCase):
    @parameterized.expand(timeline)
    def test_timeline(self, index, fullname, username, date, tid, text):
        self.open_nitter(username)
        tweet = get_timeline_tweet(index)
        self.assert_exact_text(fullname, tweet.fullname)
        self.assert_exact_text('@' + username, tweet.username)
        self.assert_exact_text(date, tweet.date)
        self.assert_text(text, tweet.text)
        permalink = self.find_element(tweet.date + ' a')
        self.assertIn(tid, permalink.get_attribute('href'))

    @parameterized.expand(status)
    def test_status(self, tid, fullname, username, date, text):
        tweet = Tweet()
        self.open_nitter(f'{username}/status/{tid}')
        self.assert_exact_text(fullname, tweet.fullname)
        self.assert_exact_text('@' + username, tweet.username)
        self.assert_exact_text(date, tweet.date)
        self.assert_text(text, tweet.text)

    @parameterized.expand(multiline)
    def test_multiline_formatting(self, tid, username, text):
        self.open_nitter(f'{username}/status/{tid}')
        self.assert_text(text.strip('\n'), Conversation.main)

    @parameterized.expand(emoji)
    def test_emoji(self, tweet, text):
        self.open_nitter(tweet)
        self.assert_text(text, Conversation.main)

    @parameterized.expand(link)
    def test_link(self, tweet, links):
        self.open_nitter(tweet)
        for link in links:
            self.assert_text(link, Conversation.main)

    @parameterized.expand(username)
    def test_username(self, tweet, usernames):
        self.open_nitter(tweet)
        for un in usernames:
            link = self.find_link_text(f'@{un}')
            self.assertIn(f'/{un}', link.get_property('href'))

    @parameterized.expand(retweet, skip_on_empty=True)
    def test_retweet(self, index, url, retweet_by, fullname, username, text):
        self.open_nitter(url)
        tweet = get_timeline_tweet(index)
        self.assert_text(f'{retweet_by} retweeted', tweet.retweet)
        self.assert_text(text, tweet.text)
        self.assert_exact_text(fullname, tweet.fullname)
        self.assert_exact_text(username, tweet.username)

    @parameterized.expand(invalid)
    def test_invalid_id(self, tweet):
        self.open_nitter(tweet)
        self.assert_text('Tweet not found', '.error-panel')

    #@parameterized.expand(reply)
    #def test_thread(self, tweet, num):
        #self.open_nitter(tweet)
        #thread = self.find_element(f'.timeline > div:nth-child({num})')
        #self.assertIn(thread.get_attribute('class'), 'thread-line')



================================================
FILE: tests/test_tweet_media.py
================================================
from base import BaseTestCase, Poll, Media
from parameterized import parameterized
from selenium.webdriver.common.by import By
import pytest

poll = [
    ['nim_lang/status/1064219801499955200', 'Style insensitivity', '91', 1, [
        ('47%', 'Yay'), ('53%', 'Nay')
    ]],

    ['polls/status/1031986180622049281', 'What Tree Is Coolest?', '3,322', 1, [
        ('30%', 'Oak'), ('42%', 'Bonsai'), ('5%', 'Hemlock'), ('23%', 'Apple')
    ]]
]

image = [
    ['mobile_test/status/519364660823207936', 'BzUnaDFCUAAmrjs'],
    #['mobile_test_2/status/324619691039543297', 'BIFH45vCUAAQecj']
]

gif = [
    ['elonmusk/status/1141367104702038016', 'D9bzUqoUcAAfUgf'],
    ['Proj_Borealis/status/1136595194621677568', 'D8X_PJAXUAAavPT']
]

video_m3u8 = [
    ['d0m96/status/1078373829917974528', '9q1-v9w8-ft3awgD.jpg'],
    ['SpaceX/status/1138474014152712192', 'ocJJj2uu4n1kyD2Y.jpg']
]

gallery = [
    ['mobile_test/status/451108446603980803', [
        ['BkKovdrCUAAEz79', 'BkKovdcCEAAfoBO']
    ]],

    ['mobile_test/status/471539824713691137', [
        ['Bos--KNIQAAA7Li', 'Bos--FAIAAAWpah'],
        ['Bos--IqIQAAav23']
    ]],

    ['mobile_test/status/469530783384743936', [
        ['BoQbwJAIUAA0QCY', 'BoQbwN1IMAAuTiP'],
        ['BoQbwarIAAAlaE-', 'BoQbwh_IEAA27ef']
    ]]
]


class MediaTest(BaseTestCase):
    @parameterized.expand(poll)
    def test_poll(self, tweet, text, votes, leader, choices):
        self.open_nitter(tweet)
        self.assert_text(text, '.main-tweet')
        self.assert_text(votes, Poll.votes)

        poll_choices = self.find_elements(Poll.choice)
        for i, (v, o) in enumerate(choices):
            choice = poll_choices[i]
            value = choice.find_element(By.CLASS_NAME, Poll.value)
            option = choice.find_element(By.CLASS_NAME, Poll.option)
            choice_class = choice.get_attribute('class')

            self.assert_equal(v, value.text)
            self.assert_equal(o, option.text)

            if i == leader:
                self.assertIn(Poll.leader, choice_class)
            else:
                self.assertNotIn(Poll.leader, choice_class)

    @parameterized.expand(image)
    def test_image(self, tweet, url):
        self.open_nitter(tweet)
        self.assert_element_visible(Media.container)
        self.assert_element_visible(Media.image)

        image_url = self.get_image_url(Media.image + ' img')
        self.assertIn(url, image_url)

    @parameterized.expand(gif)
    def test_gif(self, tweet, gif_id):
        self.open_nitter(tweet)
        self.assert_element_visible(Media.container)
        self.assert_element_visible(Media.gif)

        url = self.get_attribute('.main-tweet source', 'src')
        thumb = self.get_attribute('.main-tweet video', 'poster')
        self.assertIn(gif_id + '.mp4', url)
        self.assertIn(gif_id + '.jpg', thumb)

    @parameterized.expand(video_m3u8)
    def test_video_m3u8(self, tweet, thumb):
        self.open_nitter(tweet)
        self.driver.delete_cookie("hlsPlayback")
        self.refresh()
        self.assert_element_visible('.main-tweet ' + Media.container)
        self.assert_element_visible('.main-tweet ' + Media.video)

        video_thumb = self.get_attribute('.main-tweet ' + Media.video + ' img', 'src')
        self.assertIn(thumb, video_thumb)

    @parameterized.expand(gallery)
    def test_gallery(self, tweet, rows):
        self.open_nitter(tweet)
        self.assert_element_visible(Media.container)
        self.assert_element_visible(Media.row)
        self.assert_element_visible(Media.image)

        gallery_rows = self.find_elements(Media.row)
        self.assert_equal(len(rows), len(gallery_rows))

        for i, row in enumerate(gallery_rows):
            images = row.find_elements(By.CSS_SELECTOR, 'img')
            self.assert_equal(len(rows[i]), len(images))
            for j, image in enumerate(images):
                self.assertIn(rows[i][j], image.get_attribute('src'))



================================================
FILE: tools/create_session_browser.py
================================================
#!/usr/bin/env python3
"""
Requirements:
  pip install -r tools/requirements.txt

Usage:
  python3 tools/create_session_browser.py <username> <password> [totp_seed] [--append sessions.jsonl] [--headless]

Examples:
  # Output to terminal
  python3 tools/create_session_browser.py myusername mypassword TOTP_SECRET

  # Append to sessions.jsonl
  python3 tools/create_session_browser.py myusername mypassword TOTP_SECRET --append sessions.jsonl

  # Headless mode (may increase detection risk)
  python3 tools/create_session_browser.py myusername mypassword TOTP_SECRET --headless

Output:
  {"kind": "cookie", "username": "...", "id": "...", "auth_token": "...", "ct0": "..."}
"""

import asyncio
import json
import os
import sys

import nodriver as uc
import pyotp


async def login_and_get_cookies(username, password, totp_seed=None, headless=False):
    """Authenticate with X.com and extract session cookies"""
    # Note: headless mode may increase detection risk from bot-detection systems
    browser = await uc.start(headless=headless)
    tab = await browser.get("https://x.com/i/flow/login")

    try:
        # Enter username
        print(f"[*] Entering username {username}...", file=sys.stderr)

        retry = 0
        while retry < 5:
            username_input = await tab.find(
                'input[autocomplete="username"]', timeout=10
            )

            pos = await username_input.get_position()
            await tab.mouse_move(pos.x, pos.y, steps=50, flash=True)
            await asyncio.sleep(0.1)

            await username_input.click()
            await asyncio.sleep(0.5)
            await username_input.send_keys(username)
            await asyncio.sleep(0.2)
            await username_input.send_keys("\n")
            await asyncio.sleep(2)

            page_content = await tab.get_content()
            if "Could not log you in" in page_content:
                retry += 1
                wait = retry * 10
                print(f"Retrying in {wait} seconds...")
                await asyncio.sleep(wait)
            else:
                break

        # Enter password
        print("[*] Entering password...", file=sys.stderr)
        pretry = 0
        while pretry < 5:
            password_input = await tab.find(
                'input[autocomplete="current-password"]', timeout=15
            )
            await password_input.click()
            await asyncio.sleep(0.5)
            await password_input.send_keys(password)
            await asyncio.sleep(0.2)
            await password_input.send_keys("\n")
            await asyncio.sleep(2)

            page_content = await tab.get_content()
            if "Could not log you in" in page_content:
                pretry += 1
                wait = pretry * 10
                print(f"Retrying in {wait} seconds...")
                await asyncio.sleep(wait)
            else:
                break

        # Handle 2FA if needed
        page_content = await tab.get_content()
        if "verification code" in page_content or "Enter code" in page_content:
            if not totp_seed:
                raise Exception("2FA required but no TOTP seed provided")

            print("[*] 2FA detected, entering code...", file=sys.stderr)
            totp_code = pyotp.TOTP(totp_seed).now()
            code_input = await tab.select('input[type="text"]')
            await code_input.send_keys(totp_code + "\n")
            await asyncio.sleep(3)

        # Get cookies
        print("[*] Retrieving cookies...", file=sys.stderr)
        for _ in range(20):  # 20 second timeout
            cookies = await browser.cookies.get_all()
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}

            if "auth_token" in cookies_dict and "ct0" in cookies_dict:
                # Extract ID from twid cookie (may be URL-encoded)
                user_id = None
                if "twid" in cookies_dict:
                    twid = cookies_dict["twid"]
                    # Try to extract the ID from twid (format: u%3D<id> or u=<id>)
                    if "u%3D" in twid:
                        user_id = twid.split("u%3D")[1].split("&")[0].strip('"')
                    elif "u=" in twid:
                        user_id = twid.split("u=")[1].split("&")[0].strip('"')

                cookies_dict["username"] = username
                if user_id:
                    cookies_dict["id"] = user_id

                return cookies_dict

            await asyncio.sleep(1)

        raise Exception("Timeout waiting for cookies")

    finally:
        browser.stop()


async def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python3 create_session_browser.py username password [totp_seed] [--append file.jsonl] [--headless]"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    totp_seed = None
    append_file = None
    headless = False

    # Parse optional arguments
    i = 3
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--append":
            if i + 1 < len(sys.argv):
                append_file = sys.argv[i + 1]
                i += 2  # Skip '--append' and filename
            else:
                print("[!] Error: --append requires a filename", file=sys.stderr)
                sys.exit(1)
        elif arg == "--headless":
            headless = True
            i += 1
        elif not arg.startswith("--"):
            if totp_seed is None:
                totp_seed = arg
            i += 1
        else:
            # Unkown args
            print(f"[!] Warning: Unknown argument: {arg}", file=sys.stderr)
            i += 1

    try:
        cookies = await login_and_get_cookies(username, password, totp_seed, headless)
        session = {
            "kind": "cookie",
            "username": cookies["username"],
            "id": cookies.get("id"),
            "auth_token": cookies["auth_token"],
            "ct0": cookies["ct0"],
        }
        output = json.dumps(session)

        if append_file:
            with open(append_file, "a") as f:
                f.write(output + "\n")
            print(f"✓ Session appended to {append_file}", file=sys.stderr)
        else:
            print(output)

        os._exit(0)

    except Exception as error:
        print(f"[!] Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())



================================================
FILE: tools/create_session_curl.py
================================================
#!/usr/bin/env python3
"""
Requirements:
  pip install curl_cffi pyotp

Usage:
  python3 tools/create_session_curl.py <username> <password> [totp_seed] [--append sessions.jsonl]

Examples:
  # Output to terminal
  python3 tools/create_session_curl.py myusername mypassword TOTP_SECRET

  # Append to sessions.jsonl
  python3 tools/create_session_curl.py myusername mypassword TOTP_SECRET --append sessions.jsonl

Output:
  {"kind": "cookie", "username": "...", "id": "...", "auth_token": "...", "ct0": "..."}
"""

import sys
import json
import pyotp
from curl_cffi import requests

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFQODgEAAAAAVHTp76lzh3rFzcHbmHVvQxYYpTw%3DckAlMINMjmCwxUcaXbAN4XqJVdgMJaHqNOFgPMK0zN1qLqLQCF"
BASE_URL = "https://api.x.com/1.1/onboarding/task.json"
GUEST_ACTIVATE_URL = "https://api.x.com/1.1/guest/activate.json"

# Subtask versions required by API
SUBTASK_VERSIONS = {
    "action_list": 2, "alert_dialog": 1, "app_download_cta": 1,
    "check_logged_in_account": 2, "choice_selection": 3,
    "contacts_live_sync_permission_prompt": 0, "cta": 7, "email_verification": 2,
    "end_flow": 1, "enter_date": 1, "enter_email": 2, "enter_password": 5,
    "enter_phone": 2, "enter_recaptcha": 1, "enter_text": 5, "generic_urt": 3,
    "in_app_notification": 1, "interest_picker": 3, "js_instrumentation": 1,
    "menu_dialog": 1, "notifications_permission_prompt": 2, "open_account": 2,
    "open_home_timeline": 1, "open_link": 1, "phone_verification": 4,
    "privacy_options": 1, "security_key": 3, "select_avatar": 4,
    "select_banner": 2, "settings_list": 7, "show_code": 1, "sign_up": 2,
    "sign_up_review": 4, "tweet_selection_urt": 1, "update_users": 1,
    "upload_media": 1, "user_recommendations_list": 4,
    "user_recommendations_urt": 1, "wait_spinner": 3, "web_modal": 1
}


def get_base_headers(guest_token=None):
    """Build base headers for API requests."""
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Language": "en-US",
        "X-Twitter-Client-Language": "en-US",
        "Origin": "https://x.com",
        "Referer": "https://x.com/",
    }
    if guest_token:
        headers["X-Guest-Token"] = guest_token
    return headers


def get_cookies_dict(session):
    """Extract cookies from session."""
    return session.cookies.get_dict() if hasattr(session.cookies, 'get_dict') else dict(session.cookies)


def make_request(session, headers, flow_token, subtask_data, print_msg):
    """Generic request handler for flow steps."""
    print(f"[*] {print_msg}...", file=sys.stderr)

    payload = {
        "flow_token": flow_token,
        "subtask_inputs": [subtask_data] if isinstance(subtask_data, dict) else subtask_data
    }

    response = session.post(BASE_URL, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    new_flow_token = data.get('flow_token')
    if not new_flow_token:
        raise Exception(f"Failed to get flow token: {print_msg}")

    return new_flow_token, data


def get_guest_token(session):
    """Get guest token for unauthenticated requests."""
    print("[*] Getting guest token...", file=sys.stderr)
    response = session.post(GUEST_ACTIVATE_URL, headers={"Authorization": f"Bearer {BEARER_TOKEN}"})
    response.raise_for_status()

    guest_token = response.json().get('guest_token')
    if not guest_token:
        raise Exception("Failed to obtain guest token")

    print(f"[*] Got guest token: {guest_token}", file=sys.stderr)
    return guest_token


def init_flow(session, guest_token):
    """Initialize the login flow."""
    print("[*] Initializing login flow...", file=sys.stderr)

    headers = get_base_headers(guest_token)
    payload = {
        "input_flow_data": {
            "flow_context": {
                "debug_overrides": {},
                "start_location": {"location": "manual_link"}
            },
            "subtask_versions": SUBTASK_VERSIONS
        }
    }

    response = session.post(f"{BASE_URL}?flow_name=login", json=payload, headers=headers)
    response.raise_for_status()

    flow_token = response.json().get('flow_token')
    if not flow_token:
        raise Exception("Failed to get initial flow token")

    print("[*] Got initial flow token", file=sys.stderr)
    return flow_token, headers


def submit_username(session, flow_token, headers, guest_token, username):
    """Submit username."""
    headers = headers.copy()
    headers["X-Guest-Token"] = guest_token

    subtask = {
        "subtask_id": "LoginEnterUserIdentifierSSO",
        "settings_list": {
            "setting_responses": [{
                "key": "user_identifier",
                "response_data": {"text_data": {"result": username}}
            }],
            "link": "next_link"
        }
    }

    flow_token, data = make_request(session, headers, flow_token, subtask, "Submitting username")

    # Check for denial (suspicious activity)
    if data.get('subtasks') and 'cta' in data['subtasks'][0]:
        error_msg = data['subtasks'][0]['cta'].get('primary_text', {}).get('text')
        if error_msg:
            raise Exception(f"Login denied: {error_msg}")

    return flow_token


def submit_password(session, flow_token, headers, guest_token, password):
    """Submit password and detect if 2FA is needed."""
    headers = headers.copy()
    headers["X-Guest-Token"] = guest_token

    subtask = {
        "subtask_id": "LoginEnterPassword",
        "enter_password": {"password": password, "link": "next_link"}
    }

    flow_token, data = make_request(session, headers, flow_token, subtask, "Submitting password")

    needs_2fa = any(s.get('subtask_id') == 'LoginTwoFactorAuthChallenge' for s in data.get('subtasks', []))
    if needs_2fa:
        print("[*] 2FA required", file=sys.stderr)

    return flow_token, needs_2fa


def submit_2fa(session, flow_token, headers, guest_token, totp_seed):
    """Submit 2FA code."""
    if not totp_seed:
        raise Exception("2FA required but no TOTP seed provided")

    code = pyotp.TOTP(totp_seed).now()
    print("[*] Generating 2FA code...", file=sys.stderr)

    headers = headers.copy()
    headers["X-Guest-Token"] = guest_token

    subtask = {
        "subtask_id": "LoginTwoFactorAuthChallenge",
        "enter_text": {"text": code, "link": "next_link"}
    }

    flow_token, _ = make_request(session, headers, flow_token, subtask, "Submitting 2FA code")
    return flow_token


def submit_js_instrumentation(session, flow_token, headers, guest_token):
    """Submit JS instrumentation response."""
    headers = headers.copy()
    headers["X-Guest-Token"] = guest_token

    subtask = {
        "subtask_id": "LoginJsInstrumentationSubtask",
        "js_instrumentation": {
            "response": '{"rf":{"a4fc506d24bb4843c48a1966940c2796bf4fb7617a2d515ad3297b7df6b459b6":121,"bff66e16f1d7ea28c04653dc32479cf416a9c8b67c80cb8ad533b2a44fee82a3":-1,"ac4008077a7e6ca03210159dbe2134dea72a616f03832178314bb9931645e4f7":-22,"c3a8a81a9b2706c6fec42c771da65a9597c537b8e4d9b39e8e58de9fe31ff239":-12},"s":"ZHYaDA9iXRxOl2J3AZ9cc23iJx-Fg5E82KIBA_fgeZFugZGYzRtf8Bl3EUeeYgsK30gLFD2jTQx9fAMsnYCw0j8ahEy4Pb5siM5zD6n7YgOeWmFFaXoTwaGY4H0o-jQnZi5yWZRAnFi4lVuCVouNz_xd2BO2sobCO7QuyOsOxQn2CWx7bjD8vPAzT5BS1mICqUWyjZDjLnRZJU6cSQG5YFIHEPBa8Kj-v1JFgkdAfAMIdVvP7C80HWoOqYivQR7IBuOAI4xCeLQEdxlGeT-JYStlP9dcU5St7jI6ExyMeQnRicOcxXLXsan8i5Joautk2M8dAJFByzBaG4wtrPhQ3QAAAZEi-_t7"}',
            "link": "next_link"
        }
    }

    flow_token, _ = make_request(session, headers, flow_token, subtask, "Submitting JS instrumentation")
    return flow_token


def complete_flow(session, flow_token, headers):
    """Complete the login flow."""
    cookies = get_cookies_dict(session)

    headers = headers.copy()
    headers["X-Twitter-Auth-Type"] = "OAuth2Session"
    if cookies.get('ct0'):
        headers["X-Csrf-Token"] = cookies['ct0']

    subtask = {
        "subtask_id": "AccountDuplicationCheck",
        "check_logged_in_account": {"link": "AccountDuplicationCheck_false"}
    }

    make_request(session, headers, flow_token, subtask, "Completing login flow")


def extract_user_id(cookies_dict):
    """Extract user ID from twid cookie."""
    twid = cookies_dict.get('twid', '').strip('"')

    for prefix in ['u=', 'u%3D']:
        if prefix in twid:
            return twid.split(prefix)[1].split('&')[0].strip('"')

    return None


def login_and_get_cookies(username, password, totp_seed=None):
    """Authenticate with X.com and extract session cookies."""
    session = requests.Session(impersonate="chrome")

    try:
        guest_token = get_guest_token(session)
        flow_token, headers = init_flow(session, guest_token)
        flow_token = submit_js_instrumentation(session, flow_token, headers, guest_token)
        flow_token = submit_username(session, flow_token, headers, guest_token, username)
        flow_token, needs_2fa = submit_password(session, flow_token, headers, guest_token, password)

        if needs_2fa:
            flow_token = submit_2fa(session, flow_token, headers, guest_token, totp_seed)

        complete_flow(session, flow_token, headers)

        cookies_dict = get_cookies_dict(session)
        cookies_dict['username'] = username

        user_id = extract_user_id(cookies_dict)
        if user_id:
            cookies_dict['id'] = user_id

        print("[*] Successfully authenticated", file=sys.stderr)
        return cookies_dict

    finally:
        session.close()


def main():
    if len(sys.argv) < 3:
        print('Usage: python3 create_session_curl.py username password [totp_seed] [--append sessions.jsonl]', file=sys.stderr)
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    totp_seed = None
    append_file = None

    # Parse optional arguments
    i = 3
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--append':
            if i + 1 < len(sys.argv):
                append_file = sys.argv[i + 1]
                i += 2
            else:
                print('[!] Error: --append requires a filename', file=sys.stderr)
                sys.exit(1)
        elif not arg.startswith('--'):
            if totp_seed is None:
                totp_seed = arg
            i += 1
        else:
            print(f'[!] Warning: Unknown argument: {arg}', file=sys.stderr)
            i += 1

    try:
        cookies = login_and_get_cookies(username, password, totp_seed)

        session = {
            'kind': 'cookie',
            'username': cookies['username'],
            'id': cookies.get('id'),
            'auth_token': cookies['auth_token'],
            'ct0': cookies['ct0']
        }

        output = json.dumps(session)

        if append_file:
            with open(append_file, 'a') as f:
                f.write(output + '\n')
            print(f'✓ Session appended to {append_file}', file=sys.stderr)
        else:
            print(output)

        sys.exit(0)

    except Exception as error:
        print(f'[!] Error: {error}', file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()



================================================
FILE: tools/create_sessions_browser.py
================================================
#!/usr/bin/env python3
"""
Requirements:
  pip install -r tools/requirements.txt

Usage:
  python3 tools/create_sessions_browser.py <accounts_file> [--append sessions.jsonl] [--headless] [--delay]

Examples:
  # Output to terminal
  python3 tools/create_sessions_browser.py <accounts_file>

  # Append to sessions.jsonl
  python3 tools/create_sessions_browser.py <accounts_file> --append sessions.jsonl

  # Add 5 second delay between sessions (default: 1)
  python3 tools/create_sessions_browser.py <accounts_file> --delay 5

  # Headless mode (may increase detection risk)
  python3 tools/create_sessions_browser.py <accounts_file> --headless

Input (accounts_file):
  [{"username": "user", "password": "pass", "totp": "totp_code"}, {...}, ...]

Output:
  {"kind": "cookie", "username": "...", "id": "...", "auth_token": "...", "ct0": "..."}
  {"kind": "cookie", "username": "...", "id": "...", "auth_token": "...", "ct0": "..."}
  ...
"""

import asyncio
import json
import sys
from time import sleep

import nodriver as uc
import pyotp


async def login_and_get_cookies(account, headless=False):
    """Authenticate with X.com and extract session cookies"""
    # Note: headless mode may increase detection risk from bot-detection systems
    browser = await uc.start(headless=headless)
    tab = await browser.get("https://x.com/i/flow/login")

    username = account["username"]
    password = account["password"]
    totp_seed = account["totp"]

    try:
        # Enter username
        print(f"[*] Entering username {username}...", file=sys.stderr)

        retry = 0
        while retry < 5:
            username_input = await tab.find(
                'input[autocomplete="username"]', timeout=10
            )

            pos = await username_input.get_position()
            await tab.mouse_move(pos.x, pos.y, steps=50, flash=True)
            await asyncio.sleep(0.1)

            await username_input.click()
            await asyncio.sleep(0.5)
            await username_input.send_keys(username)
            await asyncio.sleep(0.2)
            await username_input.send_keys("\n")
            await asyncio.sleep(2)

            page_content = await tab.get_content()
            if "Could not log you in" in page_content:
                retry += 1
                wait = retry * 10
                print(f"Retrying in {wait} seconds...")
                await asyncio.sleep(wait)
            else:
                break

        # Enter password
        print("[*] Entering password...", file=sys.stderr)
        pretry = 0
        while pretry < 5:
            password_input = await tab.find(
                'input[autocomplete="current-password"]', timeout=15
            )
            await password_input.click()
            await asyncio.sleep(0.5)
            await password_input.send_keys(password)
            await asyncio.sleep(0.2)
            await password_input.send_keys("\n")
            await asyncio.sleep(2)

            page_content = await tab.get_content()
            if "Could not log you in" in page_content:
                pretry += 1
                wait = pretry * 10
                print(f"Retrying in {wait} seconds...")
                await asyncio.sleep(wait)
            else:
                break

        # Handle 2FA if needed
        page_content = await tab.get_content()
        if "verification code" in page_content or "Enter code" in page_content:
            if not totp_seed:
                raise Exception("2FA required but no TOTP seed provided")

            print("[*] 2FA detected, entering code...", file=sys.stderr)
            totp_code = pyotp.TOTP(totp_seed).now()
            code_input = await tab.select('input[type="text"]')
            await code_input.send_keys(totp_code + "\n")
            await asyncio.sleep(3)

        # Get cookies
        print("[*] Retrieving cookies...", file=sys.stderr)
        for _ in range(20):  # 20 second timeout
            cookies = await browser.cookies.get_all()
            cookies_dict = {cookie.name: cookie.value for cookie in cookies}

            if "auth_token" in cookies_dict and "ct0" in cookies_dict:
                # Extract ID from twid cookie (may be URL-encoded)
                user_id = None
                if "twid" in cookies_dict:
                    twid = cookies_dict["twid"]
                    # Try to extract the ID from twid (format: u%3D<id> or u=<id>)
                    if "u%3D" in twid:
                        user_id = twid.split("u%3D")[1].split("&")[0].strip('"')
                    elif "u=" in twid:
                        user_id = twid.split("u=")[1].split("&")[0].strip('"')

                cookies_dict["username"] = username
                if user_id:
                    cookies_dict["id"] = user_id

                return cookies_dict

            await asyncio.sleep(1)

        raise Exception("Timeout waiting for cookies")

    finally:
        browser.stop()


async def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python3 create_sessions_browser.py <accounts_file> [--append sessions.jsonl] [--headless]"
        )
        sys.exit(1)

    input = sys.argv[1]
    append_file = None
    headless = False
    delay = 1

    # Parse optional arguments
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--append":
            if i + 1 < len(sys.argv):
                append_file = sys.argv[i + 1]
                i += 2  # Skip '--append' and filename
            else:
                print("[!] Error: --append requires a filename", file=sys.stderr)
                sys.exit(1)
        elif arg == "--headless":
            headless = True
            i += 1
        elif arg == "--delay":
            delay = int(sys.argv[i + 1])
            i += 2
        else:
            # Unkown args
            print(f"[!] Warning: Unknown argument: {arg}", file=sys.stderr)
            i += 1

    accounts = []
    with open(input) as f:
        accounts = json.load(f)

    if len(accounts) == 0:
        print("no accounts in file")
        sys.exit(0)

    sessions = 0
    for acc in accounts:
        sessions += 1
        try:
            cookies = await login_and_get_cookies(acc, headless)
            session = {
                "kind": "cookie",
                "username": cookies["username"],
                "id": cookies.get("id"),
                "auth_token": cookies["auth_token"],
                "ct0": cookies["ct0"],
            }

            if append_file:
                with open(append_file, "a") as f:
                    f.write(json.dumps(session) + "\n")
            else:
                print(json.dumps(session))

            print(f"Progress: {sessions} / {len(accounts)}")
            if sessions < len(accounts):
                print("Waiting", delay, "seconds")
                sleep(delay)
        except Exception as error:
            print(
                f"[!] Error getting session for {acc["username"]}, skipping: {error}",
                file=sys.stderr,
            )


if __name__ == "__main__":
    asyncio.run(main())



================================================
FILE: tools/gencss.nim
================================================
import sass

compileFile("src/sass/index.scss",
            outputPath = "public/css/style.css",
            includePaths = @["src/sass/include"])

echo "Compiled to public/css/style.css"



================================================
FILE: tools/get_session.py
================================================
#!/usr/bin/env python3
import requests
import json
import sys
import pyotp
import cloudscraper

# NOTE: pyotp, requests and cloudscraper are dependencies
# > pip install pyotp requests cloudscraper

TW_CONSUMER_KEY = '3nVuSoBZnx6U4vzUxf5w'
TW_CONSUMER_SECRET = 'Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys'

def auth(username, password, otp_secret):
    bearer_token_req = requests.post("https://api.twitter.com/oauth2/token",
        auth=(TW_CONSUMER_KEY, TW_CONSUMER_SECRET),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data='grant_type=client_credentials'
    ).json()
    bearer_token = ' '.join(str(x) for x in bearer_token_req.values())

    guest_token = requests.post(
        "https://api.twitter.com/1.1/guest/activate.json",
        headers={
            'Authorization': bearer_token,
             "User-Agent": "TwitterAndroid/10.21.0-release.0 (310210000-r-0) ONEPLUS+A3010/9"
        }
    ).json().get('guest_token')

    if not guest_token:
        print("Failed to obtain guest token.")
        sys.exit(1)

    twitter_header = {
        'Authorization': bearer_token,
        "Content-Type": "application/json",
        "User-Agent": "TwitterAndroid/10.21.0-release.0 (310210000-r-0) ONEPLUS+A3010/9 (OnePlus;ONEPLUS+A3010;OnePlus;OnePlus3;0;;1;2016)",
        "X-Twitter-API-Version": '5',
        "X-Twitter-Client": "TwitterAndroid",
        "X-Twitter-Client-Version": "10.21.0-release.0",
        "OS-Version": "28",
        "System-User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ONEPLUS A3010 Build/PKQ1.181203.001)",
        "X-Twitter-Active-User": "yes",
        "X-Guest-Token": guest_token,
        "X-Twitter-Client-DeviceID": ""
    }

    scraper = cloudscraper.create_scraper()
    scraper.headers = twitter_header

    task1 = scraper.post(
        'https://api.twitter.com/1.1/onboarding/task.json',
        params={
            'flow_name': 'login',
            'api_version': '1',
            'known_device_token': '',
            'sim_country_code': 'us'
        },
        json={
            "flow_token": None,
            "input_flow_data": {
                "country_code": None,
                "flow_context": {
                    "referrer_context": {
                        "referral_details": "utm_source=google-play&utm_medium=organic",
                        "referrer_url": ""
                    },
                    "start_location": {
                        "location": "deeplink"
                    }
                },
                "requested_variant": None,
                "target_user_id": 0
            }
        }
    )

    scraper.headers['att'] = task1.headers.get('att')

    task2 = scraper.post(
        'https://api.twitter.com/1.1/onboarding/task.json',
        json={
            "flow_token": task1.json().get('flow_token'),
            "subtask_inputs": [{
                "enter_text": {
                    "suggestion_id": None,
                    "text": username,
                    "link": "next_link"
                },
                "subtask_id": "LoginEnterUserIdentifier"
            }]
        }
    )

    task3 = scraper.post(
        'https://api.twitter.com/1.1/onboarding/task.json',
        json={
            "flow_token": task2.json().get('flow_token'),
            "subtask_inputs": [{
                "enter_password": {
                    "password": password,
                    "link": "next_link"
                },
                "subtask_id": "LoginEnterPassword"
            }],
        }
    )

    for t3_subtask in task3.json().get('subtasks', []):
        if "open_account" in t3_subtask:
            return t3_subtask["open_account"]
        elif "enter_text" in t3_subtask:
            response_text = t3_subtask["enter_text"]["hint_text"]
            totp = pyotp.TOTP(otp_secret)
            generated_code = totp.now()
            task4resp = scraper.post(
                "https://api.twitter.com/1.1/onboarding/task.json",
                json={
                    "flow_token": task3.json().get("flow_token"),
                    "subtask_inputs": [
                        {
                            "enter_text": {
                                "suggestion_id": None,
                                "text": generated_code,
                                "link": "next_link",
                            },
                            "subtask_id": "LoginTwoFactorAuthChallenge",
                        }
                    ],
                }
            )
            task4 = task4resp.json()
            for t4_subtask in task4.get("subtasks", []):
                if "open_account" in t4_subtask:
                    return t4_subtask["open_account"]

    return None

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 get_session.py <username> <password> <2fa secret> <path>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    otp_secret = sys.argv[3]
    path = sys.argv[4]

    result = auth(username, password, otp_secret)
    if result is None:
        print("Authentication failed.")
        sys.exit(1)

    session_entry = {
        "oauth_token": result.get("oauth_token"),
        "oauth_token_secret": result.get("oauth_token_secret")
    }

    try:
        with open(path, "a") as f:
            f.write(json.dumps(session_entry) + "\n")
        print("Authentication successful. Session appended to", path)
    except Exception as e:
        print(f"Failed to write session information: {e}")
        sys.exit(1)



================================================
FILE: tools/rendermd.nim
================================================
import std/[os, strutils]
import markdown

for file in walkFiles("public/md/*.md"):
  let
    html = markdown(readFile(file))
    output = file.replace(".md", ".html")

  output.writeFile(html)
  echo "Rendered ", output



================================================
FILE: tools/requirements.txt
================================================
nodriver>=0.48.0
pyotp
curl_cffi



================================================
FILE: .github/FUNDING.yml
================================================
github: zedeus
liberapay: zedeus
patreon: nitter



================================================
FILE: .github/workflows/build-docker.yml
================================================
name: Docker

on:
  push:
    paths-ignore:
      - "README.md"
    branches:
      - master

concurrency:
  group: docker-publish-${{ github.ref }}
  cancel-in-progress: true

env:
  IMAGE: zedeus/nitter

jobs:
  tests:
    uses: ./.github/workflows/run-tests.yml
    secrets: inherit

  build:
    needs: [tests]
    strategy:
      fail-fast: false
      matrix:
        include:
          - runner: ubuntu-24.04
            platform: linux/amd64
          - runner: ubuntu-24.04-arm
            platform: linux/arm64
    runs-on: ${{ matrix.runner }}
    steps:
      - name: Prepare platform name
        run: echo "PLATFORM_PAIR=${platform//\//-}" >> "$GITHUB_ENV"
        env:
          platform: ${{ matrix.platform }}

      - uses: actions/checkout@v6

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        with:
          version: latest

      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Build and push by digest
        id: build
        uses: docker/build-push-action@v6
        with:
          context: .
          file: ./Dockerfile
          platforms: ${{ matrix.platform }}
          outputs: type=image,name=${{ env.IMAGE }},push-by-digest=true,name-canonical=true,push=true
          provenance: false
          sbom: false

      - name: Export digest
        run: |
          mkdir -p "${{ runner.temp }}/digests"
          digest="${{ steps.build.outputs.digest }}"
          touch "${{ runner.temp }}/digests/${digest#sha256:}"

      - name: Upload digest
        uses: actions/upload-artifact@v4
        with:
          name: digests-${{ env.PLATFORM_PAIR }}
          path: ${{ runner.temp }}/digests/*
          if-no-files-found: error
          retention-days: 1

  # Combine the per-arch digests into one multi-arch manifest so that
  # `docker pull zedeus/nitter:latest` serves the right image on any CPU.
  merge:
    needs: [build]
    runs-on: ubuntu-24.04
    steps:
      - name: Download digests
        uses: actions/download-artifact@v4
        with:
          path: ${{ runner.temp }}/digests
          pattern: digests-*
          merge-multiple: true

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
        with:
          version: latest

      - name: Login to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}

      - name: Create manifest list and push
        working-directory: ${{ runner.temp }}/digests
        run: |
          docker buildx imagetools create \
            -t ${{ env.IMAGE }}:latest \
            -t ${{ env.IMAGE }}:latest-arm64 \
            -t ${{ env.IMAGE }}:${{ github.sha }} \
            $(printf '${{ env.IMAGE }}@sha256:%s ' *)

      - name: Inspect image
        run: docker buildx imagetools inspect ${{ env.IMAGE }}:${{ github.sha }}



================================================
FILE: .github/workflows/run-tests.yml
================================================
name: Tests

on:
  push:
    paths-ignore:
      - "*.md"
    branches-ignore:
      - master
  workflow_call:

# Ensure that multiple runs on the same branch do not overlap.
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

defaults:
  run:
    shell: bash

jobs:
  build-test:
    name: Build and test
    runs-on: ubuntu-24.04
    strategy:
      matrix:
        nim: ["2.0.x", "2.2.x", "devel"]
    steps:
      - name: Checkout Code
        uses: actions/checkout@v6

      - name: Cache Nimble Dependencies
        id: cache-nimble
        uses: actions/cache@v5
        with:
          path: |
            ~/.nimble/pkgcache
            ~/.nimble/packages_official.json
          key: ${{ matrix.nim }}-nimble-v6-${{ hashFiles('*.nimble') }}
          restore-keys: |
            ${{ matrix.nim }}-nimble-v6-

      - name: Setup Nim
        uses: jiro4989/setup-nim-action@v2
        with:
          nim-version: ${{ matrix.nim }}
          use-nightlies: true
          repo-token: ${{ secrets.GITHUB_TOKEN }}

      - name: Build Project
        run: nimble build -Y

      - name: Upload 2.2.x build artifact
        if: matrix.nim == '2.2.x'
        uses: actions/upload-artifact@v6
        with:
          name: nitter-linux-nim-2.2.x-${{ github.sha }}
          path: |
            ./nitter
          if-no-files-found: error

  integration-test:
    needs: [build-test]
    name: Integration test
    runs-on: ubuntu-24.04

    services:
      redis:
        image: redis:7
        ports:
          - 6379:6379

    steps:
      - name: Install runtime deps
        run: |
          sudo apt-get install -y --no-install-recommends libsass-dev libpcre3

      - name: Checkout code
        uses: actions/checkout@v6

      - name: Cache pipx (poetry)
        uses: actions/cache@v5
        with:
          path: |
            ~/.local/pipx
            ~/.local/bin
          key: pipx-poetry-${{ runner.os }}

      - name: Install poetry
        env:
          PIPX_HOME: ~/.local/pipx
          PIPX_BIN_DIR: ~/.local/bin
        run: command -v poetry >/dev/null 2>&1 || pipx install poetry

      - name: Setup Python (3.14) with Poetry cache
        uses: actions/setup-python@v6
        with:
          python-version: "3.14"
          cache: poetry
          cache-dependency-path: tests/poetry.lock

      - name: Install Python deps
        working-directory: tests
        run: poetry sync

      - name: Cache Nimble Dependencies
        uses: actions/cache@v5
        with:
          path: |
            ~/.nimble/pkgcache
            ~/.nimble/packages_official.json
          key: 2.2.x-nimble-v6-${{ hashFiles('*.nimble') }}
          restore-keys: |
            2.2.x-nimble-v6-

      - name: Setup Nim
        uses: jiro4989/setup-nim-action@v2
        with:
          nim-version: 2.2.x
          use-nightlies: true
          repo-token: ${{ secrets.GITHUB_TOKEN }}

      - name: Install Nimble dependencies
        run: nimble install -y --depsOnly

      - name: Download 2.2.x build artifact
        uses: actions/download-artifact@v4
        with:
          name: nitter-linux-nim-2.2.x-${{ github.sha }}
          path: .

      - name: Make nitter binary executable
        run: chmod +x ./nitter

      - name: Prepare Nitter Environment
        run: |
          cp nitter.example.conf nitter.conf
          sed -i 's/enableDebug = false/enableDebug = true/g' nitter.conf
          sed -i 's/maxRetries = 1/maxRetries = 10/g' nitter.conf

          nim r tools/rendermd.nim
          nim r tools/gencss.nim

          echo '${{ secrets.SESSIONS }}' | head -n1
          echo '${{ secrets.SESSIONS }}' > ./sessions.jsonl

      - name: Run Tests
        run: |
          ./nitter &
          cd tests
          poetry run pytest -n3 --reruns=5 --rs .


