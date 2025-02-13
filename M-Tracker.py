import os
import time
import subprocess
import requests
from colorama import Fore, Style
from googlesearch import search
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# List of platforms with username URL patterns
platforms = {
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "GitHub": "https://github.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Medium": "https://medium.com/@{}",
    "Stack Overflow": "https://stackoverflow.com/users/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Tumblr": "https://{}.tumblr.com",
    "Flickr": "https://www.flickr.com/photos/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Goodreads": "https://www.goodreads.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "VK": "https://vk.com/{}",
    "Weibo": "https://weibo.com/{}",
    "Xing": "https://www.xing.com/profile/{}",
    "AngelList": "https://angel.co/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "CNET Forums": "https://forums.cnet.com/profile/{}",
    "ResearchGate": "https://www.researchgate.net/profile/{}"
}

# Run Hollywood with subprocess
def run_hollywood():
    # Start Hollywood process
    process = subprocess.Popen(["hollywood"])
    time.sleep(15)  # Run it for 15 seconds
    process.terminate()  # Terminate the process

# Clear the screen and print the banner
os.system("clear")
run_hollywood()

# After terminating Hollywood, clear the screen and show banner
os.system("clear")
print(f"{Fore.GREEN}")

# Display banner
os.system("figlet M-Tracker") 
print(f"{Fore.YELLOW}made by A23y{Style.RESET_ALL}")

# Function to check accounts on platforms
def search_accounts(username):
    print(f"{Fore.GREEN}Searching accounts for username: {username}{Style.RESET_ALL}\n")
    for platform, url_pattern in platforms.items():
        url = url_pattern.format(username)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{Fore.YELLOW}[FOUND] {platform}: {url}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[NOT FOUND] {platform}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] {platform}: {e}{Style.RESET_ALL}")

# Google search fallback
def search_on_google(username):
    print(f"\n{Fore.GREEN}Searching Google for '{username}' profiles...{Style.RESET_ALL}\n")
    query = f"{username} site:linkedin.com OR site:github.com OR site:reddit.com OR site:twitter.com"
    for result in search(query, num_results=10):
        print(f"{Fore.YELLOW}[GOOGLE RESULT]: {result}{Style.RESET_ALL}")

# IP Lookup using ipinfo.io
def lookup_ip(ip_address):
    print(f"\n{Fore.GREEN}Looking up IP address: {ip_address}{Style.RESET_ALL}")
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            print(f"{Fore.YELLOW}[IP INFO]{Style.RESET_ALL}")
            print(f"  IP: {data.get('ip')}")
            print(f"  City: {data.get('city')}")
            print(f"  Region: {data.get('region')}")
            print(f"  Country: {data.get('country')}")
            print(f"  ISP: {data.get('org')}")
            print(f"  Location: {data.get('loc')}")
            print(f"  Timezone: {data.get('timezone')}\n")
        else:
            print(f"{Fore.RED}Unable to fetch IP info!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

# Phone number validation
def validate_phone_number(phone_number):
    print(f"\n{Fore.GREEN}Validating phone number: {phone_number}{Style.RESET_ALL}")
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if phonenumbers.is_valid_number(parsed_number):
            print(f"{Fore.YELLOW}[PHONE INFO]{Style.RESET_ALL}")
            print(f"  Country: {geocoder.description_for_number(parsed_number, 'en')}")
            print(f"  Carrier: {carrier.name_for_number(parsed_number, 'en')}")
            print(f"  Timezones: {timezone.time_zones_for_number(parsed_number)}")
        else:
            print(f"{Fore.RED}Invalid phone number!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

# Main function
def main():
    print(f"{Fore.CYAN}Choose an option (1: Username, 2: IP, 3: Phone): {Style.RESET_ALL}")
    choice = input()
    
    if choice == "1":
        username = input(f"{Fore.CYAN}Enter a username to search for: {Style.RESET_ALL}")
        search_accounts(username)
        search_on_google(username)
    elif choice == "2":
        ip_address = input(f"{Fore.CYAN}Enter an IP address to lookup: {Style.RESET_ALL}")
        lookup_ip(ip_address)
    elif choice == "3":
        phone_number = input(f"{Fore.CYAN}Enter a phone number to validate (with country code): {Style.RESET_ALL}")
        validate_phone_number(phone_number)
    else:
        print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()