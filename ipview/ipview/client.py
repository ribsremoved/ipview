import requests as r
import socket as s
import ipaddress




def fetch(url, params=None):
    return r.get(url, params=params, timeout=5).json()

"""
Basic Information

"""

def get_usage_type(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["company"]["type"]


def get_hostname(ip: str):
    return s.gethostbyaddr(ip)[0]


def is_anycast(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["is_anycast"]


def is_satellite(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["is_satellite"]


def get_isp(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "isp"})
    return data["isp"]


def get_asn(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "asn"})
    return data["connection"]["asn"]


def get_org(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "org"})
    return data["org"]

"""

Geographical Information

"""

def get_timezone(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "timezone"})
    return data["timezone"]


def get_country(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "country"})
    return data["country"]


def get_country_code(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "countryCode"})
    return data["countryCode"]


def get_region_code(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "region"})
    return data["region"]


def get_region_name(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "regionName"})
    return data["regionName"]


def get_city(ip: str):
    data = fetch("http://ip-api.com/json/" + ip, params={"fields": "city"})
    return data["city"]


def get_longitude(ip: str):
    data = fetch(f"https://geolocation-db.com/json/{ip}")
    return data.get("longitude")


def get_latitude(ip: str):
    data = fetch(f"https://geolocation-db.com/json/{ip}")
    return data.get("latitude")

def is_likely_datacenter(ip: str):
    hostname = get_hostname(ip).lower()
    keywords = ["amazon", "google", "azure", "digitalocean", "linode", "ovh"]
    return any(k in hostname for k in keywords)

"""

Privacy / Evasion / Threat intel:

"""


def is_abuser(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_abuser"]


def is_anonymous(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_anonymous"]


def is_bogon(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_bogon"]


def is_hosting(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_hosting"]


def is_icloud_relay(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_icloud_relay"]


def is_proxy(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_proxy"]


def is_tor(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_tor"]


def is_vpn(ip: str, api_key: str):
    data = fetch(f"https://iplocate.io/api/lookup/{ip}?apikey={api_key}")
    return data["privacy"]["is_vpn"]

def get_abuse_score(ip: str, api_key: str):
    pass 


""""

IP Manipulation
"""

def ipv6_to_ipv4(ip: str):
    try:
        ipv6 = ipaddress.IPv6Address(ip)

        if not ipv6.ipv4_mapped:
            return "Not a valid IPv4-mapped IPv6 address."

        ipv4_int = int(ipv6) & 0xFFFFFFFF
        return str(ipaddress.IPv4Address(ipv4_int))

    except ValueError as e:
        return f"Error: {e}"


def ipv4_to_ipv6(ip: str):
    try:
        ipv4 = ipaddress.IPv4Address(ip)

        parts = list(map(int, str(ipv4).split(".")))

        hex_part1 = (parts[0] << 8) + parts[1]
        hex_part2 = (parts[2] << 8) + parts[3]

        return f"0:0:0:0:0:ffff:{hex_part1:04x}:{hex_part2:04x}"

    except ValueError as e:
        return f"Error: {e}"
    
""""

Edge Cases

"""

def is_iphone_hotspot(ip: str):
    try:
        addr = ipaddress.ip_address(ip)

        if isinstance(addr, ipaddress.IPv6Address):
            if addr.ipv4_mapped:
                ip = str(addr.ipv4_mapped)
            else:
                return False

        return ip.startswith("172.20.10.")

    except ValueError:
        return False


def is_android_hotspot(ip: str):
    try:
        addr = ipaddress.ip_address(ip)

        if isinstance(addr, ipaddress.IPv6Address):
            if addr.ipv4_mapped:
                ip = str(addr.ipv4_mapped)
            else:
                return False

        return ip.startswith("192.168.43.")

    except ValueError:
        return False