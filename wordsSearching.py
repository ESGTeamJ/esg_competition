'''For words searching we have to import esential libraries.'''
import re
import csv
import glob
import os

years = [""]
'''We define paths to the folders where are our txt documents (outputs from toTXT.py)
and to the folder where we want to have output as .csv document'''
path_base = ""
path_base_in = path_base + "testdir/"
path_base_out = path_base + "Analysis/"

if not os.path.exists(path_base_out): os.makedirs(path_base_out)

for year in years:
    path = path_base_in + year + "/"
    path_analysis = path_base_out
    print("I am currently working on:")
    '''Add name of output .csv file'''
    csv_file_name = path_analysis + "promises.csv"
    open(csv_file_name, 'w').close()

    clean_file_name = path_analysis + "clean_file_name.csv"

    open(clean_file_name, 'w').close()

    with open(csv_file_name, 'a') as file_:
        '''array head adds first row to a .csv file  with delimiter | between each word, which can be then transpose in .csv 
        file by few clicks'''
        writer = csv.writer(file_, delimiter="|", lineterminator='\n')
        head = ["name", "pledged", "we may", "could be", "imaginably", "conceivable", "likely", "maybe", "might be",
                "might possibly", "perhaps", "possibly", "probably", "we could", "we may", "perhaps", "we will try",
                "we would like"]

        writer.writerow(head)

    j = 0
    txt_list = glob.iglob(path + '*.txt')
    '''Looping through the txt documents and also evaluating for each txt. document 
    whether strings of head arrays appears in .txt doc or not binary: 1 or 0. Also
    these values are separated with delmiter "|" and are evaluated and logically placed under
    head words they belong to.'''
    for filename in txt_list:
        print('Currently working on this one:', filename)
        j += 1
        print(j)
        with open(csv_file_name, 'a', encoding='utf-8', ) as file_:
            try:
                writer = csv.writer(file_, delimiter="|", lineterminator='\n')

                with open(filename) as infile:
                    fname = filename
                    clean_file = filename
                    values = []

                    with open(clean_file, "r", encoding="utf-8") as file22parse:

                        file2parse = file22parse.read()
                        name = filename.removeprefix(path_base_in).removesuffix('.txt')
                        values.append(name)

                        for value in head[1:]:
                            regexp = re.compile(f"({value})", flags=re.IGNORECASE)
                            mo = regexp.search(file2parse)

                            if not mo:
                                values.append("0")
                            else:
                                values.append("1")

                        writer.writerow(values)

            except NotImplementedError:
                print("NotImplementedError: " + filename)
                pass

    clean_file_name = path_analysis + "clean_file_name.csv"
    open(clean_file_name, 'w').close()
    os.remove(clean_file_name)

print("All good !!!")
