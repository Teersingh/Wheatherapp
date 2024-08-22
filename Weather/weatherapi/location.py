import requests

def get_location_from_ip(ip_address):
    # You can use a service like ipinfo.io or similar
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        data = response.json()
        city = data.get('city', '')
        region = data.get('region', '')
        country = data.get('country', '')
        return city, region, country
    except Exception as e:
        print(f"Error getting location from IP: {e}")
        return None, None, None

def get_client_ip(request):
    """Helper function to get client IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
        print(ip)
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

get_client_ip()

