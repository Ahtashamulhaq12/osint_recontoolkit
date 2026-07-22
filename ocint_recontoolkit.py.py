
import socket
import requests
import subprocess
import re

print("=" * 55)
print(" Cyber Information Gathering Tool")
print(" Developed by Ahtasham")
print("=" * 55)

target = input("\nEnter Website (example: google.com): ").strip()

# Remove http:// or https://
target = target.replace("http://", "").replace("https://", "").split("/")[0]

print("\nCollecting Information...\n")


try:
    ip = socket.gethostbyname(target)
    print("[+] IP Address :", ip)
except:
    print("[-] Unable to resolve IP")


print("\n========== WHOIS ==========")
try:
    subprocess.run(["whois", target])
except:
    print("whois is not installed.")


print("\n========== DNS Records ==========")
try:
    subprocess.run(["dig", target])
except:
    print("dig not installed.")


print("\n========== Server Information ==========")

try:
    r = requests.get("https://" + target, timeout=5)

    server = r.headers.get("Server", "Unknown")
    powered = r.headers.get("X-Powered-By", "Unknown")

    print("Server :", server)
    print("Powered By :", powered)

    banner = server.lower()

    if "apache" in banner:
        print("Possible OS : Linux/Unix")
    elif "iis" in banner:
        print("Possible OS : Windows")
    elif "nginx" in banner:
        print("Possible OS : Linux")
    else:
        print("Possible OS : Unknown")

except Exception:
    print("Unable to fetch headers.")


print("\n========== Public Emails ==========")

try:
    html = requests.get("https://" + target).text

    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html))

    if emails:
        for email in emails:
            print(email)
    else:
        print("No public email found on homepage.")

except:
    print("Unable to collect emails.")

print("\nFinished.")