import requests

url = "https://raw.githubusercontent.com/5e-bits/5e-database/main/src/5e-SRD-"
suffix = ".json"

files = ["Ability-Scores","Alignments","Backgrounds","Classes","Conditions","Damage-Types","Equipment-Categories","Equipment","Feats","Features","Languages","Levels","Magic-Items","Magic-Schools","Monsters","Proficiencies","Races","Rule-Sections","Rules","Skills","Spells","Subclasses","Subraces","Traits","Weapon-Properties"]

for file in files:
    print(file)
    data = requests.get(f"{url}{file}{suffix}")
    data.encoding = 'cp1252'

    with open(f"data/{file}{suffix}", "w") as out:
        out.write(data.text)
