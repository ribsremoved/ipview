# IPView

A simple Python library for IP lookup and analysis.  
It provides geolocation, ISP, ASN, and usage type information in an easy-to-use Python interface.

---

## Description

IPView is a lightweight Python tool that allows developers to quickly retrieve detailed information about an IP address, including:

- Country and city location
- ISP (Internet Service Provider)
- ASN (Autonomous System Number)
- Usage type (hosting, residential, etc.)
- And more 

It is designed to be simple, fast, and easy to integrate into other Python projects.

---

## Getting Started

### Dependencies

Before installing IPView, ensure you have:

- Python 3.8+
- `requests` library
- Internet connection (for API requests)

Compatible with:
- Windows 10/11
- Linux
- macOS

Features

IPView combines multiple data sources to provide IP intelligence.

Geolocation and Network Info (no API key required)
Country, city, region, timezone
ISP, ASN, organization
Latitude and longitude
Hostname resolution
Privacy and Threat Intelligence (API key required)

Powered by IPLocate:

VPN detection
Proxy detection
Tor detection
Hosting / datacenter detection
Anonymous / abuse indicators
Satellite and anycast detection
IP Utilities
IPv4 to IPv6 conversion
IPv6 to IPv4 conversion
Hotspot detection (iPhone / Android)
Basic datacenter detection heuristic
API Providers

IPView uses multiple external services:

Requires API Key (iplocate.io)

The following functions require an API key from https://iplocate.io/

get_usage_type(ip, api_key)
is_anycast(ip, api_key)
is_satellite(ip, api_key)
is_vpn(ip, api_key)
is_proxy(ip, api_key)
is_tor(ip, api_key)
is_abuser(ip, api_key)
is_anonymous(ip, api_key)
is_bogon(ip, api_key)
is_hosting(ip, api_key)
is_icloud_relay(ip, api_key)
get_abuse_score(ip, api_key)
No API Key Required

These functions use public APIs or local system data:

get_country(ip)
get_country_code(ip)
get_region_code(ip)
get_region_name(ip)
get_city(ip)
get_timezone(ip)
get_isp(ip)
get_asn(ip)
get_org(ip)
get_latitude(ip)
get_longitude(ip)
get_hostname(ip)
---

## Installing

Install via pip:

```bash
pip install ipview
