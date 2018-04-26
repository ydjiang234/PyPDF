from PdfOperation import PdfOperation

PO = PdfOperation()

#How to use the Merger:
'''
kwargs = {
        'D:/Google Drive/Documents/NUIG/VISA-2018-06/Application Summary.pdf':0, # merge all pages
        'D:/Google Drive/Documents/NUIG/VISA-2018-06/Hosting_Agreement_NUIG_signed_2018_04.pdf':range(2,4), # Merge pages 2-3 
        'D:/Google Drive/Documents/NUIG/Contract-2018-06/PhD_Proof.pdf':[1], #Merge page 1
        }
savePath = 'C:/Users/yjiang/Desktop/11.pdf'
PO.Merge(savePath, **kwargs)
'''
