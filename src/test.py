from boltiot import Bolt
api_key = "d538af7a-f798-40c6-b6d0-cc5411fc589a"
device_id  = "BOLT8023345"
mybolt = Bolt(api_key, device_id)


response = mybolt.isOnline()

print(response, " boared is online")
response = mybolt.version()
print(response, " boared version")