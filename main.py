import PyPDF2
from time import sleep
import re
import datetime
import pandas as pd
import csv
import glob
import os

# datasource

data_source = pd.read_excel(os.path.join(os.getcwd(), "data.xlsx"))

#try:
#	data_source = pd.read_excel('./data.xlsx')
#except:
#	data_source = pd.read_excel('.\\data.xlsx')
	
data_source['Email'] =  [re.sub('\D','', str(x)) for x in data_source['Email']]

# file check

pdfFileObj = open(os.path.join(os.getcwd(), "pdf.pdf"), "rb")

#try:
#	pdfFileObj = open('./pdf.pdf', 'rb')
#except:
#	pdfFileObj = open('.\\pdf.pdf', 'rb')
	
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print("total : ( %s )" % pdfReader.numPages)
input("\n tekan enter \n")

n = 0

ld = [] # #######################

while True:
	print("Page [%s]" % n)
	try:
		pageObj = pdfReader.getPage(n)
	except:
		break

	datax = []

	for data in pageObj.extractText().split("\n"):
		try:
			datetime.datetime.strptime(data, "%d/%m/%y %H:%M:%S")
			data_ = (">>>" +data)
		except:
			data_ = (data)

		datax.append(data_)

	mystring = " "
	for data in datax:
		mystring += " "+ data 

	wr = open(os.path.join(os.getcwd(), "data", "result_"+str(n)+".txt"), "w")	
	# wr = open("data/result_"+str(n)+".txt", "w")
	wr_ = csv.writer(wr)
	
	ldi = [] # ##############

	for d in mystring.split(">>>"):
		print("proses filter..")
		dl = d.split(" ")
		# print(dl[0], dl[1])
		try:
			datetime.datetime.strptime("{} {}".format(dl[0], dl[1]), "%d/%m/%y %H:%M:%S")

			if re.search(r"(?<=FROM)\w+", d):
				m = re.search(r'(?<=FROM)\w+', d)
				kode = (m.group(0)[:4])
				#### pandas ###
				# data['Email'] =  [re.sub('\D','', str(x)) for x in data['Email']]
				result = data_source[data_source['Email'] == kode]
				# result_ = result["Alamat Kantor Bank"].values.item()
				
				# filter Provinsi
				if "jawa timur" == result["Provinsi"].values.item().lower():
					data__ = "{} (Kode Unit {}) (Bank Detail : {}) (Nama Bank {}) {}".format(d, kode, result["Alamat Kantor Bank"].values.item(), result["Nama Kantor Bank"].values.item(), result["Provinsi"].values.item())
					print(data__)
					wr_.writerow([data__])

			else:
				pass

			sleep(0.05)
			# ldi.append(data__) # ################	
		except:
			pass
	
	# ld.extend(ldi)	# ################

	n+=1

#try:
#	wr = open("data/result_.txt", "w")
#except:
#	wr = open("data\\result_.txt", "w")
#	
#wr_ = csv.writer(wr)
#
#for printed in ld:
#	print("proses cetak, please wait..")
#	wr_.writerow([printed])

pdfFileObj.close()

# ------------------------------------


# readfile
filenames = glob.glob(os.path.join(os.getcwd(), "data", "*.txt"))
# filenames = glob.glob(os.getcwd()+"/data/*.txt")

# Open file3 in write mode
with open('ALL_FILE.txt', 'w') as outfile:
	for names in filenames:
		with open(names) as infile:
			outfile.write(infile.read())
		outfile.write("\n")

