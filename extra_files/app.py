import json

d = dict()

with open("timezones.json","r") as file:
    d = json.load(file)
    
for i in d.items():
    timeDifference = i[1]
    finalDifference = 0
    if ":" in timeDifference:
        timeDifference = timeDifference.split(":")[0]
        finalDifference += 30*60
    finalDifference += int(timeDifference[1:])*60*60
    if "-" in timeDifference:
        finalDifference *= -1
    d[i[0]] = finalDifference
    
print(d)

with open("timezones_new.json","w") as file:
    json.dump(d, file)