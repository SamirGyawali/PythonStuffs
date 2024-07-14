import hashlib


ip_string = "hello-world"
encoded_string = ip_string.encode('utf-8')
print(f".encode() generated = {encoded_string}")

sha1_hash = hashlib.sha1(encoded_string)
print(f"hashlib.sha1(encoded_string) generated = {sha1_hash}")

hex_digest = sha1_hash.hexdigest()

print(f"hex digest finally = {hex_digest}")