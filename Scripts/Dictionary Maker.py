file = open('C:\\Users\\rivie\\Documents\\Minecraft Server BTE\\config\\pl3xmap\\markers\\minecraft-overworld\\Province Borders for BTE')
content = file.readlines()

organized = {}

#start = int(input("First Line: "))
start = 3
#end = int(input("Last Line: "))
end = 7

lines = content[start:end]

for i in range(0, len(lines)-1):
    lines[i] = lines[i].strip()

for x in lines:
    x = x.split(";")
    organized = {
        "Location": x[1],
        "LatLon": x[0],
        "Coords": x[2],
        "extra": x[3]
    }
    for i in organized:
        organized["Location"] = organized["Location"].replace('\t', '').replace('\n','').strip()
        organized["LatLon"] = organized["LatLon"].replace('\t', '').replace('\n','').strip()
        organized["Coords"] = organized["Coords"].replace('\t', '').replace('\n','').strip()
        organized["extra"] = organized["extra"].replace('\t', '').replace('\n','').strip()

    print(organized)
