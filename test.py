import hashlib

# 사용자로부터 입력받기
input_value = input("Enter a value to hash: ")

# SHA-256 해시 객체 생성
m = hashlib.sha256()

# 입력받은 값을 바이트로 변환하여 해시 업데이트
m.update(input_value.encode('utf-8'))

# 해시 값을 16진수로 변환
pw = m.hexdigest()

print("The SHA-256 hash of the input value is:", pw)