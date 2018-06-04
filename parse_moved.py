#!/usr/bin/env python
#this file tmp-cf.txt  content information in json format from CloudFlare account
#parse information from txt file and print domain with status

import json


def main():
	moved = json.load(open("tmp-cf.txt", "r"))
	for i in moved["result"]:
		print "%s %s %s" % (i["name"], i["id"], i["status"])


if __name__ == '__main__':
	main()
