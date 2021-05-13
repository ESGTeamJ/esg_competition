import re
import csv
import glob
import os
from bs4 import BeautifulSoup

directory_in = 'D:/Desktop/Kody_20210501/Companyreports/'
directory_out = 'D:/Desktop/Kody_20210501/Companyreports_analysis/'

path = directory_in
path_analysis = directory_out

csv_file_name = path_analysis + "final_parsed output.csv"
open(csv_file_name, 'w').close()
clean_file_name = path_analysis + "clean_file_name.csv"
open(clean_file_name, 'w').close()
indexerror = path_analysis + "index_error.csv"
open(indexerror, 'w').close()
not_impl_error = path_analysis + "not_impl_error.csv"
open(not_impl_error, 'w').close()


with open(csv_file_name, 'a') as file_:

    writer = csv.writer(file_, delimiter="|", lineterminator='\n')
    mylist = ["companyName", "phrase1", "phrase2", "phrase3"]
    writer.writerow(mylist)
j = 0
txt_list = glob.iglob(path + '*.txt')
for filename in txt_list:
    print('Currently working on this one:', filename)
    j += 1
    print(j)
    with open(csv_file_name, 'a', encoding='utf-8') as file_:
        try:
            writer = csv.writer(file_, delimiter="|", lineterminator='\n')

            with open(filename) as infile:

                soup = BeautifulSoup(infile, "html.parser")

                for script in soup(["script", "style"]):
                    script.extract()

                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip()
                          for line in lines for phrase in line.split("  "))

                clean_text = '\n'.join(chunk for chunk in chunks if chunk)
                clean_text = clean_text.encode('latin-1', 'replace')

                clean_filee = clean_file_name
                f = open(clean_filee, 'wb')
                f.write(clean_text)
                f.close()

                company_name = ""
                phrase1 = ""
                phrase2 = ""
                phrase3 = ""

                with open(clean_filee, "r", encoding="latin-1") as file22parse:

                    file2parse = file22parse.read()

                    company_name = filename[40:-4]

                    '''phrase1 we want to split with its sentence'''
                    regexp = re.compile(r"(.*CO2.*)")
                    mo = regexp.search(file2parse)
                    if not mo:
                        phrase1 = None
                        phrase1 = ""
                    else:
                        phrase1 = mo.group(0)

                    '''phrase2 we want to split with its sentence'''
                    regexp = re.compile(r"(.* net zero.*)")
                    mo = regexp.search(file2parse)
                    if not mo:
                        phrase2 = None
                        phrase2 = ""
                    else:
                        phrase2 = mo.group(0)

                    '''phrase3 we want to split with its sentence'''
                    regexp = re.compile(r"(.*Paris agreement.*)")
                    mo = regexp.search(file2parse)
                    if not mo:
                        phrase3 = None
                        phrase3 = ""
                    else:
                        phrase3 = mo.group(0)

                    '''list which should be displayed in .csv'''
                    mylist = [company_name,  phrase1, phrase2, phrase3,
                              ]

                    data = mylist
                    writer.writerow(data)

        except NotImplementedError:
            print("NotImplementedError: " + filename)
            f = open(not_impl_error, "a")
            myString = str(filename)
            f.write(myString + "\n")
            f.close()
            pass

clean_file_name = path_analysis + "clean_file_name.csv"
open(clean_file_name, 'w').close()
os.remove(clean_file_name)

print("OK!")
