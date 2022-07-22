from ast import parse
import configparser
import os, sys
from os import path
import argparse

parser = argparse.ArgumentParser(description="viper-ssh simple and easy tool to save time from ansible inventory and playbook")
parser.add_argument('-i', help="The inventory file with extention of .ini or .cfg")
parser.add_argument('-playbook', help="Your script to execute no fucking playbook is needed")
parser.add_argument('-n', help="the name of hosts list see in viper-ssh docs")
parser.add_argument('-dest', help="The destination of playbook to push and run the script see in docs")
args = parser.parse_args()

inv = args.i
playb = args.playbook
nameofhosts = args.n
dest = args.dest
dest = str(dest)
print ("Destination : ", dest)
if dest == "None":
    dest = "/tmp/"
    print("Setting Destination to /tmp")

print ("-----------------------------------------------------------------------------------------------------------")
print ("The args are [ inventory:", inv, " playbook(script_to_execute): ", playb, " Nameofhostlist:", nameofhosts)

def run(host, user, passwd, script):
    push = 'sshpass -p ' + passwd + ' scp ' + playb + ' ' + user + '@' + host + ':' + dest
    runbook = 'sshpass -p ' + passwd + ' ssh ' + user + '@' + host + " '(bash " + dest + script + ")'"
    #print(push)
    print("Pushing file ......................................", script)
    os.system(push)
    #print(runbook)
    print("[*] Executing that script .................................. ")
    print("[+] Showing results ...................................... Host " + user + '@' + host)
    os.system(runbook)
    

def readandrun(nameofhosts, inv, playb):
    hosts = configparser.ConfigParser()
    hosts.read(inv)
    hosts = hosts.get(nameofhosts, "hosts")
    hosts = hosts.split(',')
    for host in hosts:
        creds = host.split(" ")
        host = creds[0]
        user = creds[1]
        passwd = creds[2]
        script = os.path.basename(playb)
        #print (host , user, passwd, script)
        run(host, user, passwd, script)

readandrun(nameofhosts, inv, playb)