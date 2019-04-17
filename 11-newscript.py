#!/usr/bin/python3
"""Paramiko with SFTP and SSH | RZFeeser@alta3.com"""

import paramiko

## define servers we want to connect to
usercreds = [{"un": "bender",  "ip": "10.10.2.3"}, {"un": "fry", "ip": "10.10.2.4"}, {"un": "zoidberg" , "ip": "10.10.2.5"}]

## loop thru servers we want to connect to
for fc in usercreds:
    mytransport = paramiko.Transport(fc["ip"], 22)
    mytransport.connect(username=fc['un'], password="alta3")
    sftp = paramiko.SFTPClient.from_transport(mytransport)
    
    ## move mybash.sh to each server
    sftp.put("mybash.sh", "/tmp/mybash.sh")
    ## sftp.chmod("/tmp/mybash.sh", 755)

    ## done w/ sftp object
    sftp.close()
    mytransport.close()

    sshsession = paramiko.SSHClient()
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=fc['ip'], username=fc['un'], pkey=mykey)

    ## execute mybash.sh
    sshsession.exec_command('cd /tmp; chmod u+x mybash.sh; ./mybash.sh')

    ## cat both files (dtfile.txt) and (itworks.txt)
    

    ## close connections
    sshsession.close()


