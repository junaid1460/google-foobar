
import base64

MESSAGE = '''EVIdFAoHVEdFF0pPTkYOFlRVQhdGVUkCBghdUVdXHxBJQVNEFlFFRA8QAwQNQx0UEVUMEwETHRcW FAwQTRwAAhsBVV1UXA9SQkFOBVJcX1UcEAMEBxAWFAwQTQAADQYHWlFSF0ZVSRMIBlNdQkNNVVRB ThdQUlMXRlVJBwYLFhQMEE0CBw9IQ0w='''

KEY = 'junaid1460'

# result = []
# for i, c in enumerate(base64.b64decode(MESSAGE)):
#     result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))
out = []
name = "junaid"
name = base64.b64encode(name)
name = base64.b16encode(name)
print name
password = name
length = len(name)
name = "Please get some more problems for me. Thank you"
name = base64.b64encode(name)
print "this", name
res = []
for i, c in enumerate(name):
    res  += [chr(ord(c) ^ ord(password[i % length]) + 3)]

crypt =  base64.b16encode(''.join(res))
print crypt
dcrypt = base64.b16decode(crypt)
print dcrypt
res = []
for i, c in enumerate(dcrypt):
    res  += [chr(ord(c) ^ ord(password[i % length]) + 3)]
print "this", ''.join(res)
print base64.b64decode(''.join(res))


x = "sdsfdsfd"
print min(x) 