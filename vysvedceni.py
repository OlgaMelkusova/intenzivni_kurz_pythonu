schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

soucet_znamek = 0
for predmet in schoolReport :
    soucet_znamek += schoolReport[predmet]
prumer = soucet_znamek/len(schoolReport)
print(prumer)