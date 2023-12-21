import json
import sys
from numpy import cumsum

if len(sys.argv)==2:
  fic = sys.argv[1]
else:
  fic = "patterns/patt_dumas_feval_min=4_max=5.json"
  print(f"Using default file :{fic}") 

f = open(fic)
dic = json.load(f)
f.close()

bouiboui = dic["all_files"]

for nomTxt, vecteur in bouiboui.items():
  effectif_total_patrons = cumsum(vecteur)[-1]
  vecteur_freq = [x/effectif_total_patrons for x in vecteur]
  bouiboui[nomTxt] = vecteur_freq

dic["all_files"]= bouiboui

w = open("%s_freq.json"%fic, "w")
w.write(json.dumps(dic, indent=2))
w.close()
