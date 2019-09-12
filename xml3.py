import json
data = '''{
    "name" : "Abhinav",
    "phone" : {
        "type": "intl",
        "number": "+91 776 600 6343"
    },
    "email":{
        "hide": "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Name:', info["email"]["hide"])
