import requests
from Crypto.Hash import keccak
from colorama import Fore
b = Fore.LIGHTBLACK_EX
r = Fore.RED
keccak_hash = keccak.new(digest_bits=512)

def banner():
    print(r+"██"+b+"╗  "+r+"██"+b+"╗"+r+"██████"+b+"╗  "+r+"██████"+b+"╗ "+r+"███████"+b+"╗"+r+"███████"+b+"╗"+r+"██████"+b+"╗ ")
    print(b+"╚"+r+"██"+b+"╗"+r+"██"+b+"╔╝"+r+"██"+b+"╔══"+r+"██"+b+"╗"+r+"██"+b+"╔═══"+r+"██"+b+"╗"+r+"██"+b+"╔════╝"+r+"██"+b+"╔════╝"+r+"██"+b+"╔══"+r+"██"+b+"╗")
    print(b+" ╚"+r+"███"+b+"╔╝"+r+" ██████"+b+"╔╝"+r+"██"+b+"║   "+r+"██"+b+"║"+r+"███████"+b+"╗"+r+"█████"+b+"╗  "+r+"██"+b+"║  "+r+"██"+b+"║")
    print(r+" ██"+b+"╔"+r+"██"+b+"╗"+r+" ██"+b+"╔═══╝ "+r+"██"+b+"║   "+r+"██"+b+"║╚════"+r+"██"+b+"║"+r+"██"+b+"╔══╝  "+r+"██"+b+"║  "+r+"██"+b+"║")
    print(r+"██"+b+"╔╝ "+r+"██"+b+"╗"+r+"██"+b+"║     ╚"+r+"██████"+b+"╔╝"+r+"███████"+b+"║"+r+"███████"+b+"╗"+r+"██████"+b+"╔╝")
    print(b+"╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═════╝ ")
    print("                                         by"+Fore.RED+" Deipy")
    print("")
    print(Fore.RED+"This program checks if password have been compromised in data breaches, using the XPosed API.")

#Display banner and ask for password to test
banner()
print("")
print(Fore.RED+"[!]"+Fore.WHITE+" Enter a password : ")
password = str(input())

#hash password and keep only the 10 first characters
keccak_hash.update(bytes(password, encoding="UTF-8"))
password = str(keccak_hash.hexdigest())[0:10]

#making a request to the xposedornot api with 30s timeout and handling basic errors
try:
    req = requests.get("https://passwords.xposedornot.com/api/v1/pass/anon/"+password, timeout=30)
except requests.exceptions.ReadTimeout:
    print(Fore.RED + "[!]" + Fore.WHITE + " Error : request timed out.")
    quit();
except requests.exceptions.ConnectionError :
    print(Fore.RED + "[!]" + Fore.WHITE + " Error : Could not connect")
    quit();

#if server replied OK, print results
if req.status_code == 200:
    if "SearchPassAnon" in req.json() :
        print(Fore.RED+"[!] This password is not safe !")
        print(Fore.WHITE+"    This password has been observed "+req.json()['SearchPassAnon']['count']+" times")
        print("    troughout the collected XoN data breaches.")
    else :
        print(Fore.RED+"[!]"+Fore.WHITE+" There was an error, server replied OK but there is no data to be shown.")
elif req.status_code == 404:
    print(Fore.RED + "[!]" + Fore.WHITE + " Your password is safe !")
    print("    This password has not been observed in the colleced XoN data breaches")
else :
    print(Fore.RED + "[!]" + Fore.WHITE + " There was an error, server replied with unknown code")