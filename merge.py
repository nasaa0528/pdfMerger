#!/usr/bin/python3
'''
merge.py - Merges given pdf files into output pdf file with given name. 

Author: Nasantogtokh Amarsaikhan 
Date: 10-04-2020
Version: 1.0 
'''
import os, sys, argparse, PyPDF2
def main():
	parser = argparse.ArgumentParser(description="Merge given input pdf files into single pdf file")
	parser.add_argument("-o", "--output",default="merged.pdf" ,type=str, help="Name of merged pdf files, default value is 'merged.pdf'")
	parser.add_argument("input", help="List of input pdf files to merge", nargs="+")
	args = parser.parse_args()
	pdfFiles = [os.path.abspath(filename) for filename in args.input] 
	outputFile = os.path.abspath(args.output)
	fileNotExist = False
	for pdfFile in pdfFiles: 
		if not (os.path.exists(pdfFile)) or not (pdfFile.endswith('.pdf')): 
			print(os.path.basename(pdfFile) + " file does not exist in given path or file extension does not match") 
			fileNotExist = True 
	if fileNotExist: 
		print("Please verify input files and try again with appropriate input files") 
		sys.exit(-1)
	if os.path.exists(outputFile): 
		print('Output file will overwrite existing file named "' + os.path.basename(outputFile) + '"!')
	
	pdfWriter = PyPDF2.PdfFileWriter()
	for pdfFile in pdfFiles: 
		pdfFileObj = open(pdfFile, 'rb') 
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		for pageNum in range(pdfReader.numPages): 
			pageObj = pdfReader.getPage(pageNum) 
			pdfWriter.addPage(pageObj)
	with open(outputFile, 'wb') as pdfOutput: 
		pdfWriter.write(pdfOutput)
	print('Merged all files successfully')

if __name__=='__main__': 
	main()
