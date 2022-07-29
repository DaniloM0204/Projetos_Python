# Partindo do princípio de Data Science e Analise de dados.

import csv
import pandas as pd
# Os import chamam o csv que é um import que transforma a data em csv, e a data vem do import do pandas, pra puxar os dados inseridos e transformar em csv
data = {"Nome":
        ["Danilo", "Ana Clara","Clarice Falcão", "Juliana"],
        "Idade":
            [22,21,32, 21]
        }
data = pd.DataFrame(data)
data.to_csv("Idade_Nome.csv", index=False)
print(data.head)
