import json
print("Interface Status\n"
"================================================================================\n"
"DN                                                 Description           Speed    MTU\n"
"-------------------------------------------------- --------------------  ------  ------")
with open("sample-data.json", "r") as file:
    json_file = json.load(file)

    for i in json_file["imdata"]:
        print(f"{i['l1PhysIf']['attributes']['dn']}\t\t\t\t\t\t\t\t"
              f"{i['l1PhysIf']['attributes']['speed']}   {i['l1PhysIf']['attributes']['mtu']}")
