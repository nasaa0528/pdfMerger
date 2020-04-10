# pdfMerger
## Enlsih - Readme
```merge.py``` - is simple pdf merger solution for all platform which supports python. This solution works similar as 
```**/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py**```
on mac devices. 

It is built on top of **PyPDF2** library. You can download and install **PyPDF2** library using **pip** package manager with 
```
$:pip install PyPDF2 # case-sensitive
```
command. 

Also, if you know about basics of Python, it will give you power of manipulating pdf files as you wish. 

In the source code, ```pageObj = pdfReader.getPage(pageNum)``` - section defines each oage of the pdf file. Therefore, you can give specific rule of page manipulation on this page using PyPDF2 library. 

Prerequisites: 
```
 - python==3.6.8
 - PyPDF2==1.26.0
```
Tested Environment:
```
 - MacOS Catalina, 10.15.4
```

## Монгол
<br>
```merge.py``` - скрипт нь Мак үйлдлийн систем дээр байдаг 
```**/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py**```
програмтай төстэй үйлдлийг гүйцэтгэнэ. Өөрөөр хэлбэл, Python3 дэмжиж буй бүх платформ дээр pdf файлыг нэгтгэх боломжийг олгох хэрэглүүр юм.

Энэхүү скрипт нь **PyPDF2** санг ашигласан тул, хэрвээ та шууд эх кодыг ашиглан ажиллуулах бол **PyPDF2** санг суулгасан байх шаардлагатай. 
**PyPDF2** санг суулгахдаа **pip** ашиглан 
```
$:pip install PyPDF2 
```
командыг ажиллуулснаар суулгах боломжтой юм. 

Цаашлаад, хэрвээ та **Python** хэлний үндсэн мэдлэгтэй бол, энэхүү эх кодыг ашиглан өөрийн pdf файлыг өөрчлөх, нэгтгэх, засах боломжийг энэхүү эх кодыг өөрчлөх замаар гарган авах боломжтой юм. Эх кодын ```pageObj = pdfReader.getPage(pageNum)``` хэсэг дэх хувьсагч нь pdf файлын хуудсыг заах бөгөөд энэхүү хуудас хэсгийг өөрчлөх замаар pdf файлд өөрчлөлт оруулах боломжтой юм. 


