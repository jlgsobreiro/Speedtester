import os

import csv
import datetime


def make_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as arquivo_csv:
            escrita_csv = csv.writer(arquivo_csv, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
            linha = ["Dia", "Horario", "Download", "Upload"]
            escrita_csv.writerow(linha)
            arquivo_csv.close()
        return True
    else:
        return False


def write_file(file_path, upload_rate, download_rate):
    with open(file_path, "a", newline="") as arquivo_csv:
        escrita_csv = csv.DictWriter(arquivo_csv, fieldnames=["Dia", "Horario", "Download", "Upload"])
        linha = {"Dia": datetime.datetime.today().date(),
                 "Horario": datetime.datetime.today().time(),
                 "Download": download_rate,
                 "Upload": upload_rate}
        escrita_csv.writerow(linha)
        arquivo_csv.close()
