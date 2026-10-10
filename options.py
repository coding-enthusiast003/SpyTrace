import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers.phonenumberutil import NumberParseException
import requests
from rich.console import Console  # For rich console output
from rich.text import Text # For rich text formatting
import json
import time

console = Console()

def phone(): #for phone number information
    number_input = console.input("[bold green]Enter phone number (+country code)[/bold green]: ")

    
    parsed_number = phonenumbers.parse(number_input, None)

    
    console.print(f"[bold green]National Format:[/bold green] {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}")

    console.print(f"[bold green]E.164 Format:[/bold green] {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")

    console.print(f"[bold green]Country Code:[/bold green] {parsed_number.country_code}")

    console.print(f"[bold green]Region Code:[/bold green] {phonenumbers.region_code_for_number(parsed_number)}")

    console.print(f"[bold green]Country / Location:[/bold green] {geocoder.description_for_number(parsed_number, "en") or "Unavailable"}")

    console.print(f"[bold green]Carrier:[/bold green] {carrier.name_for_number(parsed_number, "en") or "Unavailable"}")
        

    console.print(f"[bold green]Time Zones:[/bold green] {', '.join(timezone.time_zones_for_number(parsed_number)) or 'Unavailable'}")

    number_types = {
    phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
    phonenumbers.PhoneNumberType.MOBILE: "Mobile",
    phonenumbers.PhoneNumberType.VOIP: "VoIP",
    phonenumbers.PhoneNumberType.UNKNOWN: "Unknown"
}

    # 3. Ask the library to identify the type
    number_type = phonenumbers.number_type(parsed_number)

    # 4. Find the matching label in the dictionary
    readable_type = number_types.get(number_type, "Other / Unknown")

    # 5. Display the result
    console.print(f"[bold green]Number Type:[/bold green] {readable_type}")


def ip_trace(): # for ip information
    ip = console.input("[bold green]Enter IP address: [/bold green] ")
    print()
    console.print(f"[bold green]Tracing IP info....: {ip}[/bold green]")
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text) #json.loads() for converting JSON string to Python dictionary
    time.sleep(2)

    console.print("\n========== IP INTELLIGENCE ==========" , style="bold blue")
    console.print(f"IP Address       : {ip_data.get('ip')}" , style="bold green") 
    console.print(f"Status           : {ip_data.get('success')}" , style="bold green")
    console.print(f"IP Type          : {ip_data.get('type')}" , style="bold green")

    console.print("\n========== LOCATION DETAILS ==========" , style="bold blue")
    console.print(f"Continent        : {ip_data.get('continent')}" , style="bold green")
    console.print(f"Country          : {ip_data.get('country')} ({ip_data.get('country_code')})" , style="bold green")
    console.print(f"Region           : {ip_data.get('region')}" , style="bold green")
    console.print(f"City             : {ip_data.get('city')}" , style="bold green")
    console.print(f"Postal Code      : {ip_data.get('postal')}" , style="bold green")
    console.print(f"Latitude         : {ip_data.get('latitude')}" , style="bold green")
    console.print(f"Longitude        : {ip_data.get('longitude')}" , style="bold green")

    console.print("\n========== NETWORK DETAILS ==========" , style="bold blue")
    connection = ip_data.get("connection", {})
    console.print(f"ASN              : {connection.get('asn')}" , style="bold green")
    console.print(f"Organization     : {connection.get('org')}" , style="bold green")
    console.print(f"ISP              : {connection.get('isp')}" , style="bold green")
    console.print(f"Domain           : {connection.get('domain')}" , style="bold green")

    console.print("\n========== TIMEZONE DETAILS ==========" , style="bold blue")
    timezone = ip_data.get("timezone", {})
    console.print(f"Timezone         : {timezone.get('id')}" , style="bold green")
    console.print(f"Abbreviation     : {timezone.get('abbr')}" , style="bold green")
    console.print(f"UTC Offset       : {timezone.get('utc')}" , style="bold green")
    console.print(f"Current Time     : {timezone.get('current_time')}" , style="bold green")

    console.print("\n========== SECURITY CHECK ==========" , style="bold blue")
    security = ip_data.get("security", {})
    console.print(f"Anonymous        : {security.get('anonymous')}" , style="bold green")
    console.print(f"Proxy            : {security.get('proxy')}" , style="bold green")
    console.print(f"VPN              : {security.get('vpn')}" , style="bold green")
    console.print(f"Tor              : {security.get('tor')}" , style="bold green")
    console.print(f"Hosting          : {security.get('hosting')}" , style="bold green")
    console.print(f"Relay            : {security.get('relay')}" , style="bold green")
    console.print(f"Mobile Network   : {security.get('mobile')}" , style="bold green")

    console.print("\n========== ADDITIONAL DETAILS ==========" , style="bold blue")
    console.print(f"Capital          : {ip_data.get('capital')}" , style="bold green")
    console.print(f"Calling Code     : +{ip_data.get('calling_code')}" , style="bold green")

    currency = ip_data.get("currency", {})
    console.print(f"Currency         : {currency.get('name')}" , style="bold green")
    console.print(f"Currency Code    : {currency.get('code')}" , style="bold green")
    console.print(f"Currency Symbol  : {currency.get('symbol')}" , style="bold green")

    flag = ip_data.get("flag", {})
    console.print(f"Country Flag     : {flag.get('emoji')}" , style="bold green")

    rate = ip_data.get("rate", {})
    console.print(f"API Limit        : {rate.get('limit')}" , style="bold green")
    console.print(f"Requests Left    : {rate.get('remaining')}" , style="bold green")

    console.print("\n=====================================")
