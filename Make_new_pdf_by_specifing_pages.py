# extract pages from PDF and make another PDF that contain only these pages

import PyPDF2
pfr = PyPDF2.PdfFileReader(open("a.pdf", "rb"))

writer = PyPDF2.PdfFileWriter()

# now we extract same pages by page number <starting from 0>
extracted_page_19 = pfr.getPage(18)
extracted_page_26 = pfr.getPage(25)

# we specified 2 pages, now we create an another pdf with only these 2 pages
writer.addPage(extracted_page_19)
writer.addPage(extracted_page_26)

with open("allTables.pdf", "wb") as outputStream:
    writer.write(outputStream)