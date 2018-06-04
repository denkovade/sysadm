#!/usr/bin/env python
# this script is using to add dns records in CF ( CloudFlare account) using file domains-with-id.txt
#IP_address - add IP adres to point
#X-Auth-Email: add email which you are using to autenticate in CF (this info you can take from you CF account)
# X-Auth-Key: add authentification key (this info you can take from you CF account)
import subprocess


def main(): 
	f = open("domains-with-id.txt", "r")
	for l in f:
		if not l.strip():
			continue

		domain, ident = [i.strip() for i in l.split(" ")]
		p = ["curl", "-s", "-X", "POST", "https://api.cloudflare.com/client/v4/zones/%s/dns_records" % ident, "-H", "X-Auth-Email: c" , "-H", "X-Auth-Key: " , "-H", "Content-Type: application/json" , "--data" , '{"type":"A","name":"%s","content":"IP_address","proxied":true}' % domain]
		print "Executing: %s" % " ".join(p)
		subprocess.Popen(p).wait()
		p = ["curl", "-s", "-X", "POST", "https://api.cloudflare.com/client/v4/zones/%s/dns_records" % ident, "-H", "X-Auth-Email: ", "-H", "X-Auth-Key: ", "-H" , "Content-Type: application/json", "--data" , '{"type":"CNAME","name":"www","content":"%s","proxied":true}' % domain]
		print "Executing: %s" % " ".join(p)
		subprocess.Popen(p).wait()


if __name__ == '__main__':
	main()
