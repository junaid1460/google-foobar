import base64
str_ = 'EVIdFAoHVEdFF0pPTkYOFlRVQhdGVUkCBghdUVdXHxBJQVNEFlFFRA8QAwQNQx0UEVUMEwETHRcW FAwQTRwAAhsBVV1UXA9SQkFOBVJcX1UcEAMEBxAWFAwQTQAADQYHWlFSF0ZVSRMIBlNdQkNNVVRB ThdQUlMXRlVJBwYLFhQMEE0CBw9IQ0w='

user = 'junaid1460'
count = 0
st = ""
for i in base64.b64decode(str_):
    st += str( chr(ord(i) ^ ord(user[count])))
    count += 1
    count %= len(user)
print st
