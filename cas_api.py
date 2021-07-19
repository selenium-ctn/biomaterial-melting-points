import requests
import json

paramee = {
    "q": "pentose*",
    "size": "200"
}
response = requests.get("http://commonchemistry.cas.org/api/search", params=paramee)

info = response.json()
#print(response.json())

rn_list = []
cou = 0
for i in info["results"]:
    rn_list.append(i["rn"])
    cou += 1

print(cou)

print(info["count"])
print(len(rn_list))
prop_list = []
cou = 0
for i in rn_list:
    paramee = {
        "cas_rn": i
    }
    response = requests.get("http://commonchemistry.cas.org/api/detail", params=paramee)
    prop_list.append(response.json()["experimentalProperties"])
    if response.json()["experimentalProperties"] != []:
        cou += 1

print(prop_list)
print(len(prop_list))
print(cou)