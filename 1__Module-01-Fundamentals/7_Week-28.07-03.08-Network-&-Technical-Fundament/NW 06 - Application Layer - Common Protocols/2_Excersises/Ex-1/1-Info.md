# Banner Grabbing Bonanza

_Knock, knock. Who's there? (Let's ask the server!)_

**Goal**

Use the `telnet` command-line tool to manually connect to various standard and non-standard service ports on different servers and observe the initial server responses ("banners") to identify potential services.

**Instructions**

1. Open your Terminal application.
2. Use `telnet` to attempt connections to the following servers and ports. In case you don’t have telnet installed run `brew install telnet` Note down or screenshot the exact response (or connection failure) you get immediately after connecting.
    - `telnet ftp.dlptest.com 21` – FTP welcome banner.
    - `telnet smtp.googlemail.com 25` – SMTP greeting (plain‑text).
    - `telnet whois.iana.org 43` – WHOIS service banner (simple text).
    - `telnet dict.org 2628` – DICT protocol banner (dictionary server).
    - `telnet localhost 9999` – expected “connection refused” example.
3. To close a `telnet` session press `Ctrl + ]`, then type `quit` and hit `Enter`.
4. Review the banners you received. What information does each banner reveal about the server or service (e.g., server software name/version, welcome messages, protocol readiness)? How useful is this information for reconnaissance?

**Submission**

Submit one screenshot (or a collage) showing successful connections to:

- `google.com 80`
- `ftp.dlptest.com 21`
- `smtp.googlemail.com 25`
- `whois.iana.org 43`
- `dict.org 2628`

(Optional) include a refused‑connection example, e.g., `localhost 9999`.

Then add a brief note answering question 4 about what reconnaissance value these banners provide across _all_ your attempts.