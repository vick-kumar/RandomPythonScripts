from hashlib import sha256

input = "vanessa"

print(sha256(input.encode('utf-8')).hexdigest())

print("````")

inp1 = "bob"
inp2 = "vick"
print(sha256(inp1.encode('utf-8')).hexdigest())
print(sha256(inp2.encode('utf-8')).hexdigest())

print("````")

password_list = open('password_list.txt', 'r')
Lines = password_list.readlines()

count = 0

for line in Lines:
    count += 1

    print(sha256(line.encode('utf-8')).hexdigest())

    if input == sha256(line.encode('utf-8')).hexdigest():
        print("Password: {} found with hash of: {}".format(line.strip(), sha256(line.encode('utf-8')).hexdigest()))