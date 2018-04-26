import ghostscript
#from svglib.svglib import svg2rlg
#from reportlab.graphics import renderPDF, renderPM

def pdf2jpeg(targetName, outputName, dpi=600):
    args = [b'pdf2jpeg', # actual value doesn't matter
            b'-dNOPAUSE',
            b'-sDEVICE=jpeg',
            bytes('-r'+str(dpi), encoding='ascii'),
            bytes('-sOutputFile=' + outputName, encoding='ascii'),
            bytes(targetName, encoding='ascii')]
    ghostscript.Ghostscript(*args)
