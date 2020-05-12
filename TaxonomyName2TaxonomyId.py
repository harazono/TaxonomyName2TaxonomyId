#! /usr/bin/env python3
import sys
import pprint
import argparse
import requests
import json
import xml.etree.ElementTree as ET
pp = pprint.PrettyPrinter(indent=4)


def main():
	parser = argparse.ArgumentParser(description = 'transform from taxonomy name to taxonomy id')
	parser.add_argument("filename", help = "a plane txt file which contains taxonomy name in each line")
	args = parser.parse_args()
	filename = args.filename
	name_id_pair_array = [] * 20
	with open(filename) as f:
		for line in f:
			taxonomy_name = line.strip().replace(' ', "%20")
			url  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.cgi?db=taxonomy&term=%s"%(taxonomy_name)
			res  = requests.get(url).text
			root = ET.fromstring(res)
			taxonomy_id   = root.find("IdList")[0].text
			taxonomy_name = line
			print("%s&%s||"%(taxonomy_name.strip(), taxonomy_id))

		print()


if __name__ == '__main__':
	main()

	#https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.cgi?db=taxonomy&term=Homo%20sapiens+OR+Mus%20musculus