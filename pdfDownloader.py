'''For automatic downloading pdfs form URLS we must first import essential libraries'''
import urllib.request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

'''Add output from splitter.js to the arrays bellow'''
links = ["link_1", "link_2", "link_3", ..., "link_n"]
names = ["company_1", "company_2", "company_3", ..., "company_n"]

'''Zipping both arrays and after downloading link_1 the name of pdf will be company_1
if any error with downloading pdf occurs it will skip to another name and link automaticaly '''
for i, j in zip(links, names):
    try:
        print("actually working on: " + j + "with link: " + i)
        
        '''Add path to a folder where we want our pdfs to be placed as outputs'''
        urllib.request.urlretrieve(i, "D:/Desktop/pdfka/" + j + ".pdf")
        print(j + " is downloaded successfully!")

    except Exception as e:
        print(e)
        continue
