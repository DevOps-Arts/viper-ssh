# DESCRIPTION

Its general perpose is learning devops and time saving of DevOps engineers
*uck playbook..yaml replace with your shell script

#Config syntax

[name of your host list]

hosts=(host1) (user) (password),(host2) (user) (password)

Eg. 

[orgnization]

hosts=182.213.434.2 ec2 password123,128.1326.132.23 ec2 password213

# Usage

pyhon3 viper-ssh.py -i config.ini -playbook [script] -n [name of section] -dest [where to land the script DEFAULT: /tmp/]

If you want to use stored keys then add this flag "-havekey" and add fake password in hosts list 

Eg.

in shell : pyhon3 viper-ssh.py -i config.ini -playbook [script] -n [name of section] -dest [where to land the script DEFAULT: /tmp/] -havekey
in inventory : hosts=127.213.353.12 Username Fakepasswordcauseuadded


# How to add ssh key



The first thing you’ll need to do is make sure you’ve run the keygen command to generate the keys:

ssh-keygen -t rsa

Then use this command to push the key to the remote server, modifying it to match your server name.

cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'

