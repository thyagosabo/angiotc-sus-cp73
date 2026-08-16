import sys, extrai_dac as e
grupos={"g1":["SP"],"g2":["MG"],"g3":["RJ","RS"],"g4":["PR","SC","BA"],
        "g5":["CE","PE","PA","MA","GO","ES"],
        "g6":"PB PI RN AL SE MT MS DF AM RO TO AC AP RR".split()}
g=sys.argv[1]
e.roda("SIA", 2025, f"data-v2/dac_sia_{g}.csv", grupos[g])
