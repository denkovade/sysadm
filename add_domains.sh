#!/bin/bash
#add domains in CF via txt file which is using domain_list.txt 
#fill email and key from your account in variables below
CF_API_EMAIL=""
CF_API_KEY=""
for domain in $(cat domain_list.txt); do \
  curl -s -X POST -H "X-Auth-Key: $CF_API_KEY" -H "X-Auth-Email: $CF_API_EMAIL" \
  -H "Content-Type: application/json" \
  "https://api.cloudflare.com/client/v4/zones" \
  --data '{"name":"'$domain'","jump_start":true}' | jq; done
