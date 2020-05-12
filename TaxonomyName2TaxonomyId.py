#! /usr/bin/env python3
import sys
import pprint
import argparse
import requests
import json
import openpyxl
import xml.etree.ElementTree as ET
pp = pprint.PrettyPrinter(indent=4)

def TaxonomyName2TaxonomyId(name):
	name4url = name.strip().replace(' ', "%20")
	url      = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.cgi?db=taxonomy&term=%s"%(name4url)
	try:
		res  = requests.get(url).text
		root = ET.fromstring(res)
		taxonomy_id = root.find("IdList")[0].text
		return "%s&%s"%(name.strip(), taxonomy_id)
	except:
		return sys.exc_info()

#def manageExcelFile:

def main():
	parser = argparse.ArgumentParser(description = 'transform from taxonomy name to taxonomy id')
	parser.add_argument("filename", help = "a plane txt file which contains taxonomy name in each line")
	#parser.add_argument("", help = "a plane txt file which contains taxonomy name in each line")
	args = parser.parse_args()
	filename = args.filename
	name_id_pair_array = [] * 20
	with open(filename) as f:
		for line in f:
			name_id_pair_array.append(TaxonomyName2TaxonomyId(line))
	print("||\n".join(name_id_pair_array))

if __name__ == '__main__':
	main()
