import PyPDF2

class PdfOperation:

    def __init__(self):
        return None;

    def AppendPages(self, PDFWriter, PDFReader, pageRange):
        #If pageRange =0, append all pages
        if type(pageRange)==type(1):
            copyNum = pageRange
            pageRange = []
            for i in range(copyNum):
                pageRange.extend(range(1, PDFReader.numPages+1))
        #Append papges
        for i in pageRange:
            PDFWriter.addPage(PDFReader.getPage(i-1))
        return PDFWriter


    def Merge(self, savePath, **kwargs):
        PDFWriter = PyPDF2.PdfFileWriter()
        for filePath, pageRange in kwargs.items():
            #Load pdf file
            PDFReader = PyPDF2.PdfFileReader(filePath)
            PDFWriter = self.AppendPages(PDFWriter, PDFReader, pageRange)
        f = open(savePath, 'wb')
        PDFWriter.write(f)
        f.close()



