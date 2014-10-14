#!/usr/bin/env python
import sys
import os
import argparse
import shlex
import shutil
import subprocess
import http.server
import socketserver

BASEURL = 'ipython-books.github.io'

def call(cmd, wait=True):
    cmd_list = shlex.split(cmd)
    p = subprocess.Popen(cmd_list)
    if wait: 
     	p.wait()

def conf():
    "Generate the derivate conf files."
    
    with open('pelicanconf.py', 'r') as f:
        contents = f.read()
    
    loc = "SITEURL = '/'\n" + contents
    pub = ("SITEURL = 'http://%s'\n" % BASEURL) + contents
    
    with open('pelicanconf_loc.py', 'w') as f:
        f.write(loc)
    
    with open('pelicanconf_pub.py', 'w') as f:
        f.write(pub)

def build(local=True, monitor=True):
    "Build the local HTML site in output."
    monitor = monitor & local
    conf()
    which = 'loc' if local else 'pub'
    call("pelican -s=pelicanconf_%s.py %s" % (which, '-r' if monitor else ''), 
    	 wait=not(monitor))

def serve():
    "Launch a local HTTP server."
    build()
    os.chdir('output')
    # subprocess.Popen(["python", "-m", "http.server"])
    call("python -m http.server", wait=False)
    os.chdir('..')

def clean():
    "Clean all output and cache."
    shutil.rmtree('output')
    shutil.rmtree('cache')
    shutil.rmtree('__pycache__')

def upload(msg):
    """Build and push all changes online."""
    build(local=False)
    call("git add content/*.md")
    call("git add content/*.ipynb")
    call('git commit -am "%s"' % msg)
    call("git push")
    call("cp -ar output/. ../%s" % BASEURL)
    os.chdir("../%s" % BASEURL)
    call("git add --ignore-removal *")
    call('git commit -am "%s"' % msg)
    call('git push')

def kill():
    "Kill the running processes."
    call("killall python pelican")

commands = {
    # None: lambda: print("Please provide a command."),
    None: serve,
    'build': build,
    'serve': serve,
    'conf': conf,
    'clean': clean,
    'upload': upload,
    'kill': kill,
}

parser = argparse.ArgumentParser()
parser.add_argument('command', type=str, nargs='?')
parser.add_argument('args', type=str, nargs='*')

args = parser.parse_args()
commands[args.command](*args.args)
