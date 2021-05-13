'''For pdf to txt converting we have to importg essential libraries.'''
from io import StringIO
import json
import os
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

'''Adding path to the folder where we have pdfs from pdfDownloader.py'''
pdfs_path = 'D:/Desktop/test/' 
txt_path = 'D:/Desktop/testText/'

'''Looping through whole folder and all pdf pages which are converted to txt documents 
which take the same name as the pdf they are converted from.  '''
for filename in os.listdir(pdfs_path):
    if filename.endswith(".pdf"):
        try:
            name = os.path.join(filename)
            output_string = StringIO()
            with open(pdfs_path + filename, 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                textName = filename[:-3] + "TXT"

                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)
                    text_file = open(txt_path + textName, "wt")
                    string = json.dumps(output_string.getvalue())
                    os.remove(pdfs_path + filename)
                    n = text_file.write(string)
                    text_file.close()
                    print(filename + " is successfully converter to: " + textName)

        except Exception as e:
            print(e)
            continue
