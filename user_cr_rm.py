#!/usr/bin/env python

# Create user @host with password, shell, gecos
# Change user attributes

import crypt
import os
import sys
import paramiko
import socket


## print it needs root user privilege to run this script
uid = os.getuid()

if uid != 0:
    print "You need to be a root user to run this script."
    sys.exit()


# Receiving user input 
cr_user = 1
rm_user = 2

user_inp = raw_input("Enter 1 to create an User, Enter 2 to remove an User:> ")


# Create user with user input
if user_inp == "1":
    print "Creating an User"
    # Get hostname
    h_name = raw_input("Enter Server name: ")

    try:
        print ("Establishing ssh connection")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #client.connect('localhost', username='samy', password='LL2/?q#/0')
        client.connect(h_name, username = 'user1', password = "password")
        stdin, stdout, stderr = client.exec_command("uptime")
        print "Server is up and running"
        print stdout.read()
    except paramiko.SSHException, e:
        print "Password is invalid:" , e
    except paramiko.AuthenticationException:
        print "Authentication failed for some reason"
    except socket.error, e:
        print "Socket connection failed:", e
    client.close()
    
    # Get owner name, IBM or Client
    o_name = raw_input("Enter Owner name: ")
    print o_name

    if o_name == "ibm" or o_name == "IBM" or o_name == "Ibm":
        # Get IBM employee ID for IBM user
        emp_id = raw_input("Enter IBM Employee ID: ")
        print emp_id

        # Get user name
        u_name = raw_input("Enter User name to create: ")
        print u_name

        # Get password
        p_word = raw_input("Enter password: ")
        encrpass = crypt.crypt(p_word,"md5")

        # Get first name of user
        f_name = raw_input("Enter First name of User: ")
        print f_name

        # Get last name of user
        l_name = raw_input("Enter Last name of User: ")
        print l_name

        # Add user with provided input
        ibm_gecos = "744/IN"+"/"+emp_id+"/"+f_name+"."+l_name
        u_home = "/home/"+u_name
        sh_bash = "/bin/bash"

        if o_name == "ibm" or o_name == "IBM" or o_name == "Ibm":
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #client.connect('localhost', username='samy', password='LL2/?q#/0')
            client.connect(h_name, username = 'user1', password = 'password')
            #stdin, stdout, stderr = client.exec_command("uptime")
            stdin, stdout, stderr = client.exec_command("sudo useradd -d %s -m -c %s -p %s -s %s %s" % (u_home, ibm_gecos, encrpass, sh_bash, u_name))
            print stdout.read()
            client.close()

    if o_name == "schibsted" or o_name == "SCHIBSTED" or o_name == "Schibsted":

        # Get user name
        u_name = raw_input("Enter User name to create: ")
        print u_name

        # Get password
        p_word = raw_input("Enter password: ")
        encrpass = crypt.crypt(p_word,"md5")        

        # Get first name of user
        f_name = raw_input("Enter First name of User: ")
        print f_name

        # Get last name of user
        l_name = raw_input("Enter Last name of User: ")
        print l_name

        # Add user with provided input
        c_gecos = "NO/C//SCH02"+"/"+u_name    
        u_home = "/home/"+u_name
        sh_bash = "/bin/bash"

        if o_name == "schibsted" or o_name == "SCHIBSTED" or o_name == "Schibsted":
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #client.connect('localhost', username='samy', password='LL2/?q#/0')
            client.connect(h_name, username = 'user1', password = 'password')
            #stdin, stdout, stderr = client.exec_command("uptime")
            stdin, stdout, stderr = client.exec_command("sudo useradd -d %s -m -c %s -p %s -s %s %s" % (u_home, c_gecos, encrpass, sh_bash, u_name))
            print stdout.read()
            client.close()

#    sys.exit(0)


# Remove an User
if user_inp == "2":
    print ('.' * 30) + "Removing an User" + ('.' * 30)
    # Get hostname
    h_name = raw_input("Enter Server name:> ")
    print h_name

    # Get user name
    u_name = raw_input("Enter User name to remove:> ")
    print u_name

    pwd.getpwnam(name).pw_name

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(h_name, username = 'user1', password = 'password')
    stdin, stdout, stderr = client.exec_command("sudo userdel -f -r %s" % (u_name))
    print u_name,"is removed on",h_name
    client.close()
