# IPView

A simple Python library for IP lookup and analysis.
It provides geolocation, ISP, ASN, and usage type information in an easy-to-use Python interface.

---

## Description

IPView is a lightweight Python tool that allows developers to quickly retrieve detailed information about an IP address, including:

* Country and city location
* ISP (Internet Service Provider)
* ASN (Autonomous System Number)
* Usage type (hosting, residential, etc.)
* And more

It is designed to be simple, fast, and easy to integrate into other Python projects.

---

## Getting Started

### Dependencies

Before installing IPView, ensure you have:

* Python 3.8+
* requests library
* Internet connection (for API requests)

Compatible with:

* Windows 10/11
* Linux
* macOS

---

## Features

IPView combines multiple data sources to provide IP intelligence.

### Geolocation and Network Info (no API key required)

* Country, city, region, timezone
* ISP, ASN, organization
* Latitude and longitude
* Hostname resolution

### Privacy and Threat Intelligence (API key required)

Powered by IPLocate:

* VPN detection
* Proxy detection
* Tor detection
* Hosting / datacenter detection
* Anonymous / abuse indicators
* Satellite and anycast detection

### IP Utilities

* IPv4 to IPv6 conversion
* IPv6 to IPv4 conversion
* Hotspot detection (iPhone / Android)
* Basic datacenter detection heuristic

---

## API Providers

IPView uses multiple external services:

### Requires API Key (iplocate.io)

The following functions require an API key from [https://iplocate.io/](https://iplocate.io/)

* get_usage_type(ip, api_key)
* is_anycast(ip, api_key)
* is_satellite(ip, api_key)
* is_vpn(ip, api_key)
* is_proxy(ip, api_key)
* is_tor(ip, api_key)
* is_abuser(ip, api_key)
* is_anonymous(ip, api_key)
* is_bogon(ip, api_key)
* is_hosting(ip, api_key)
* is_icloud_relay(ip, api_key)
* get_abuse_score(ip, api_key)

### No API Key Required

These functions use public APIs or local system data:

* get_country(ip)
* get_country_code(ip)
* get_region_code(ip)
* get_region_name(ip)
* get_city(ip)
* get_timezone(ip)
* get_isp(ip)
* get_asn(ip)
* get_org(ip)
* get_latitude(ip)
* get_longitude(ip)
* get_hostname(ip)

---

## Installation

```bash
pip install ipview
```

---

## Usage Examples

### Basic usage

```python
from ipview import get_country, get_isp

print(get_country("8.8.8.8"))
print(get_isp("8.8.8.8"))
```

---

### Privacy checks (requires API key)

```python
from ipview import is_vpn, is_proxy

api_key = "YOUR_API_KEY"

print(is_vpn("8.8.8.8", api_key))
print(is_proxy("8.8.8.8", api_key))
```

---

### Hostname and utilities

```python
from ipview import get_hostname, ipv4_to_ipv6

print(get_hostname("8.8.8.8"))
print(ipv4_to_ipv6("192.168.0.1"))
```

---

## Notes

* Some functions depend on external APIs and may be rate limited
* IPLocate features require a valid API key
* Accuracy depends on third-party data providers

---

## Architecture

IPView combines multiple providers:

* IPLocate → privacy and threat intelligence
* ip-api.com → ISP, ASN, and geolocation
* geolocation-db → coordinate lookup
* Python standard library → IP utilities and hostname resolution

---

## License

MIT License

---

## Links

* GitHub: [https://github.com/ribsremoved/ipview](https://github.com/ribsremoved/ipview)
* PyPI: [https://pypi.org/project/ipview/](https://pypi.org/project/ipview/)
