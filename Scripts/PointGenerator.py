file = open('..\Province Borders for BTE')
content = file.readlines()

start = int(input("First Line: "))
end = int(input("Last Line: "))
lines = content[start-1:end]

MineCoordinates = []

for i in range(0, len(lines)):
    if '"' not in lines[i]:
        pass
    elif 'Unused' in lines[i]:
        pass
    else:
        lines[i] = lines[i].split('"')
        MineCoordinates.append(str(lines[i][1]))

# Variables
a = """{
            \"type\": \"line\",
            \"data\": {
                \"key\": \"\",
                \"points\": ["""

b = ""

c = """        
                ]
            },
            \"options\": {
                \"stroke\": {
                    \"weight\": 2,
                    \"color\": -65536
                },
                \"fill\": {
                    \"enabled\": false
                },
                \"tooltip\": {
                    \"content\": \"\", // Tooltip Name
                    \"direction\": 2,
                    \"sticky\": true
                }
            }
        },"""

# x/y setup
for i in range(0, len(MineCoordinates)):
    SimpCoordinates = MineCoordinates[i].split(", ")
    First = SimpCoordinates[0]
    Second = SimpCoordinates[1]
    if i != len(MineCoordinates) - 1:
        b = b + """\n                   {
                        \"x\": """ + First + """, // Point Name
                        \"z\": """ + Second + """
                    },"""
    else:
        b = b + """\n                   {
                        \"x\": """ + First + """, // Point Name
                        \"z\": """ + Second + """
                    }"""

# Output
print(a + b + c)
