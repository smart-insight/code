from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTTextLineHorizontal, LTFigure, LTRect, LTLine, LTCurve


#  文件对象
pd_file = open("extract/国家医疗保障DRG（CHS-DRG）分组方案.pdf", "rb")

#  pdf文件解析对象
parser = PDFParser(pd_file)

# print(parser)
#  pdf文档对象
document = PDFDocument(parser)
parser.set_document(document)
document.set_parser(parser)

#  初始化文档密码
document.initialize()
if document.is_extractable:
    print(True)
else:
    raise PDFTextExtractionNotAllowed
#  存储文档资源
src = PDFResourceManager()

#  设备对象
device = PDFPageAggregator(src, laparams=LAParams())

#  解释器对象

inter = PDFPageInterpreter(src, device)

pages = document.get_pages()

for page in pages:
    # print(page.contents)
    inter.process_page(page)
    layout = device.get_result()
    for x in layout:
        if isinstance(x, LTTextBoxHorizontal):
            print(str(x.get_text()))
        # t = dir(x)
        # print(t)
        # print(type(x))
