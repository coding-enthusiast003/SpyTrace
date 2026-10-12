import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from phonenumbers.phonenumberutil import NumberParseException
import requests
from rich.console import Console  # For rich console output
from rich.text import Text # For rich text formatting
import json
import time
from xposedornot import XposedOrNot #xposedornot library to check email exposed in data breaches

console = Console()

# Initialize the client
xon = XposedOrNot()


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





def track_user():
    username = console.input("[bold green]enter the user name: [/bold green]")
    console.print("searching user name...." ,  style="bold green")
    print()
    time.sleep(2)
    platforms = {
    # Mainstream social media
    "Instagram": "https://www.instagram.com/{username}/",
    "Facebook": "https://www.facebook.com/{username}",
    "X (Twitter)": "https://x.com/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "YouTube": "https://www.youtube.com/@{username}",
    "Threads": "https://www.threads.net/@{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Pinterest": "https://www.pinterest.com/{username}/",

    # Professional networking
    "LinkedIn": "https://www.linkedin.com/in/{username}/",

    # Communities and discussion
    "Reddit": "https://www.reddit.com/user/{username}/",
    "Quora": "https://www.quora.com/profile/{username}",
    "Telegram": "https://t.me/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Discord": "https://discord.com/users/{user_id}",

    # Developer platforms
    "GitHub": "https://github.com/{username}",
    "GitLab": "https://gitlab.com/{username}",

    # Content and creative platforms
    "Medium": "https://medium.com/@{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "Spotify": "https://open.spotify.com/user/{user_id}",
    "Behance": "https://www.behance.net/{username}",
    "Dribbble": "https://dribbble.com/{username}",

    # Streaming and gaming
    "Kick": "https://kick.com/{username}",
    "Roblox": "https://www.roblox.com/users/profile?username={username}",
}
    for key, values in platforms.items():
        if "{user_id}" in values: #used to check if the platform requires a user ID instead of a username
            console.print(
                f"{key}: Requires a user ID; skipped",
                style="bold yellow"
            )
            continue

        try:
            url = values.format(username=username)
            response = requests.get(url, timeout=10) #timeout to avoid waiting tool long for a response

            if response.status_code == 200:
                console.print(key, ":", url, style="bold green")
            elif response.status_code == 404:
                console.print(key, ": Not found", style="bold red")
            else:
                console.print(
                    f"{key}: Inconclusive (HTTP {response.status_code})",
                    style="bold yellow"
                )

        except requests.RequestException as e:
            console.print(f"{key}: Request error - {e}", style="bold red")

def email_check(): #for email breach check
    mail = console.input("[bold green]enter the email id : [/bold green]")
    time.sleep(1)

    # Check if an email has been exposed (returns breach names only)
    result = xon.check_email(mail)
    if result.breaches:
        console.print(f"[bold red]Found in {len(result.breaches)} breaches: [/bold red]")
        for i in result.breaches:
             console.print( i, style="bold red")

        # Get detailed breach analytics
        analytics = xon.breach_analytics(mail)
        console.print(f"[bold red]Total exposures: {analytics.exposures_count}[/bold red]")
        console.print(f"[bold red]First breach: {analytics.first_breach}[/bold red]")

        for breach in analytics.breaches_details:
            console.print(f"  - {breach.breach}: {breach.xposed_records} records")

            # Get all known breaches
        breaches = xon.get_breaches()
        console.print(f"[bold red]Total breaches in database: {len(breaches)}[/bold red]")

    else:
        console.print( "[bold green]No known breaches found for this email.[/bold green]")

     
