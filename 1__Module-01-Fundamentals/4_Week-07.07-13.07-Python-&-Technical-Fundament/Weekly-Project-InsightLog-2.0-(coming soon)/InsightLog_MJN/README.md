# InsightLog

InsightLog is a Python script for extracting and analyzing data from server log files (Nginx, Apache2, and Auth logs). It provides tools to filter, parse, and analyze common server log formats.

## Features

- Filter log files by date, IP, or custom patterns
- Extract web requests and authentication attempts from logs
- Analyze logs from Nginx, Apache2, and system Auth logs

## Installation

Clone this repository:
```bash
git clone https://github.com/CyberstepsDE/insightlog.git
cd insightlog
```

You are ready to go!

## Command Line Usage

You can run the analyzer from the CLI:

```bash
python3 insightlog.py --service nginx --logfile logs-samples/nginx1.sample --filter 192.10.1.1
```

More examples:

- Analyze Apache2 logs for a specific IP:
  ```bash
  python3 insightlog.py --service apache2 --logfile logs-samples/apache1.sample --filter 127.0.1.1
  ```

- Analyze Auth logs for a specific string:
  ```bash
  python3 insightlog.py --service auth --logfile logs-samples/auth.sample --filter root
  ```

- Analyze all Nginx log entries (no filter):
  ```bash
  python3 insightlog.py --service nginx --logfile logs-samples/nginx1.sample
  ```

## Known Bugs

See [KNOWN_BUGS.md](KNOWN_BUGS.md) for a list of current bugs and how to replicate them.

## Planned Features

See [ROADMAP.md](0__Workspace/0__Karriere/cybersteps-edu-paths/1_Module-01-Fundamentals/4_Week-07.07-13.07-Python-&-Technical-Fundament/Weekly-Project-InsightLog-2.0-(coming%20soon)/InsightLog_MJN/ROADMAP.md) for planned features and improvements.

## Running Tests

We use Python's built-in `unittest` module for testing. To run the tests:

```bash
python3 -m unittest discover -s tests -v
```

## License

This project is licensed under the MIT License. See [LICENSE](0__Workspace/0__Karriere/Projekte-Cybersteps/cybersteps-security-meeting-distributor-to-googlecalender/DE/meetup-calendar-sync/venv/Lib/site-packages/pip/_vendor/idna/LICENSE.md) for details.