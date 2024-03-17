import requests
import hashlib

def check_pwned_password(password):
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    # print(hashed_password)
    prefix = hashed_password[:5]
    # print(prefix)
    api_call = f'https://api.pwnedpasswords.com/range/{prefix}'
    
    try:
        response = requests.get(api_call)
        if response.status_code == 200:
            hashes = response.text.split('\r\n')
            found = next((h.split(':') for h in hashes if h.startswith(hashed_password[5:])), None)
            if found:
                count = int(found[1])
                print(f'This password has been seen {count} times before')
            else:
                print('Good news — no pwnage found')
        else:
            print(f'Error: {response.status_code}')
    except Exception as e:
        print(f'Error: {e}')
