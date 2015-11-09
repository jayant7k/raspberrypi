#!/usr/bin/env python

import pygodaddy
import logging
import pif

godaddy_log_file = '/tmp/godaddy.log'
ip_address_file = '/home/pi/progs/ipaddress'

logging.basicConfig(filename=godaddy_log_file, format='%(asctime)s %(message)s', level=logging.INFO)
logging.getLogger("requests").setLevel(logging.DEBUG)

public_ip = pif.get_public_ip()
logging.info("INFO : ip_address = %s",str(public_ip))

ipfile = open(ip_address_file,'r')
old_public_ip = ipfile.read()
ipfile.close()

if public_ip == old_public_ip:
  logging.info("INFO : ip address %s not changed",str(old_public_ip))
  quit()

logging.info("INFO : Updating ip address")

client = pygodaddy.GoDaddyClient()
U = "username"
P = "password"
success = client.login(U,P)

if success:
    domains = client.find_domains()
    for domain in domains:
      logging.info("INFO : Domain - %s",str(domain))
      dns_records = client.find_dns_records(domain)      
      for record in dns_records:
        logging.info("INFO : processing >>> %s", str(record))
        if record.hostname == 'home':
          logging.info("INFO : Found domain - home | updating...")
          if record.value != public_ip:
            client.update_dns_record('home.jayantkumar.in', public_ip)
            logging.info("INFO : dns updated!!!")

logging.info("INFO : updating local file")
ipfile = open(ip_address_file,'w')
ipfile.truncate()
ipfile.write(public_ip)
ipfile.close()
logging.info("INFO : local file updated")

print("all done...\n")
