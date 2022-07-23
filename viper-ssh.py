from ast import parse
import configparser
import os, sys
from os import path
import argparse

parser = argparse.ArgumentParser(description="viper-ssh simple and easy tool to save time from ansible inventory and playbook")
parser.add_argument('-i', required=True, help="The inventory file with extention of .ini or .cfg")
parser.add_argument('-playbook', required=True, help="Your script to execute no fucking playbook is needed")
parser.add_argument('-n', required=True, help="the name of hosts list see in viper-ssh docs")
parser.add_argument('-dest', help="The destination of playbook to push and run the script see in docs")
parser.add_argument('-havekey', action='store_true', help="If uou have the key stored in ~/.ssh/authorized_keys")
args = parser.parse_args()

inv = args.i
playb = args.playbook
nameofhosts = args.n
dest = args.dest
dest = str(dest)
keytrigger = args.havekey


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
    

def runwithkeys(host, user, script):
    push = 'scp ' + playb + ' ' + user + '@' + host + ':' + dest
    runbook = 'ssh ' + user + '@' + host + " '(bash " + dest + script + ")'"
    #print(push)
    print("Authenticating with stored keys ......................")
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
        print ("[*] Key trigger ", keytrigger)
        if keytrigger == True:
           print("[*] Use Key flag triggered....................")
           runwithkeys(host, user, script)
        else:
            run(host, user, passwd, script)
            print("[*] using password authentication............")


readandrun(nameofhosts, inv, playb)
