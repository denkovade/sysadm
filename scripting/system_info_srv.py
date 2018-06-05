#!/usr/bin/env python
#this script will collect information from our servers
#-*- coding: utf-8 -*
 
 
import os
import sys
from argparse import ArgumentParser
import glob
import subprocess
 
 
PROFILES = {
    "basic": {
        "files": [
            '/etc/resolv.conf',
            '/etc/redhat-release',
            '/etc/postfix/*.cf',
            '/usr/sbin/*.sh',
            '/var/lib/jenkins/jobs/*/config.xml',
            '/etc/httpd/conf.d/*',
            '/etc/my.cnf',
            '/etc/bacula/bat.conf',
            '/etc/exports'
        ],

        "commands": [
            ['ifconfig' ,'-a'],
            ['crontab', '-l'],
            ['uname', '-a'],
            ['iptables','-L']
            ['docker','ps','-all'],
            ['docker', 'images'],
            ['df','-hT'],
            ['fdisk', '-l'],
            ['lscpu']
        ]
    }


    }

    "centos":{
        "files":[
            '/etc/mysql/*.conf',
        ],

        "commands":[
            ['chkconfig']
            ['sestatus','v']
            ['getsebool''a']
        ]
    
    }

def get_info_from_files(output_file_handler, files_to_look_for):
    delim = "=" * 40 + "\n"
    delim2 = "-" * 40 + "\n"
    for f in files_to_look_for:
        print "Info: Working on: %s" % f
        # Write the expected file name in the output file
        output_file_handler.write("Working on file: %s\n" % f)
        output_file_handler.write(delim)
        output_file_handler.write("\n"*5)
 
        gf = glob.glob(f)
        if(not gf):
            print >> sys.stderr, "Warining: No files for %s" % f
        for g in gf:
            print "Info: Working on file after glob: %s" % g
            output_file_handler.write("Working on after glob: %s\n" % g)
            output_file_handler.write(delim2)
            output_file_handler.write("\n"*5)
            try:
                o = open(g, 'r').read()
                output_file_handler.write(o)
            except IOError, err:
                print >> sys.stderr, "Warning: File %s could not be read: %s" % (g, str(err).strip())
            output_file_handler.write("\n"*5)
 
 
def get_info_from_commands(output_file_handler, commands):
    delim = "=" * 40 + "\n"
    for c in commands:
        print "Info: Executing Command: %s" % " ".join(c)
        # Write the expected file name in the output file
        output_file_handler.write("Command: %s\n" % " ".join(c))
        output_file_handler.write(delim)
        output_file_handler.write("\n"*5)
 
        p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        so, se = p.communicate()
        rc = p.returncode
        if(rc != 0):
            print >> sys.stderr, "Warning: Command %s failed with %i:\n Error message: %s" % (" ".join(c), rc, se.strip())
        else:
            output_file_handler.write(so)
        
        output_file_handler.write("\n"*5)
 
 
def get_args(profiles):
    parser = ArgumentParser(description="This is useful script and shows how to use option parser")
 
    parser.add_argument("-o", "--output-file",
                        help="File to write the data in")
    parser.add_argument("-p", "--profile",
                        choices=[i for i in profiles],
                        default=[i for i in profiles][0],
                        help="Choose from a predefined set of commands and files for particular purpose")
 
    args = parser.parse_args()
 
    if(not args.output_file):
        print >> sys.stderr, "Error: You have to supply --output-file"
        sys.exit(1)
 
    return args
 
 
def main():
    args = get_args(PROFILES)
    
    output_file = os.path.abspath(args.output_file)
    profile_name = args.profile
 
    print "Running Profile: %s" % profile_name
 
    with open(output_file, 'w') as o_f:
        get_info_from_files(o_f, PROFILES[profile_name]["files"])
        get_info_from_commands(o_f, PROFILES[profile_name]["commands"])
 
 
if(__name__ == "__main__"):
    main()
