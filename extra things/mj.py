import base64

MESSAGE = '''EVIdFAoHVEdFF0pPTkYOFlRVQhdGVUkCBghdUVdXHxBJQVNEFlFFRA8QAwQNQx0UEVUMEwETHRcW FAwQTRwAAhsBVV1UXA9SQkFOBVJcX1UcEAMEBxAWFAwQTQAADQYHWlFSF0ZVSRMIBlNdQkNNVVRB ThdQUlMXRlVJBwYLFhQMEE0CBw9IQ0w='''

KEY = '153639'

result = []
res = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    res.append(c)
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
print ''.join(res)
