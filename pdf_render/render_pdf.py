import os
import pymupdf

SRC = r"C:\Users\lenovo\Desktop\扫描全能王 2026-9-17 16.14.pdf"
OUT = r"C:\Users\lenovo\Desktop\Python\pdf_render"
ZOOM = 2.0

doc = pymupdf.open(SRC)
print("pages:", doc.page_count)
mat = pymupdf.Matrix(ZOOM, ZOOM)
for i, page in enumerate(doc, 1):
    pix = page.get_pixmap(matrix=mat)
    name = "page_%02d.png" % i
    pix.save(os.path.join(OUT, name))
    print(name, pix.width, pix.height)
doc.close()
print("done")
