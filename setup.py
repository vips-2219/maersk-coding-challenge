#!/usr/bin/env
import subprocess
import os

def install():
	# install all python requirements
	with open('python_logs.txt','w') as f:
		if os.name=='nt':
			process = subprocess.Popen(["python", "-m","pip","install", "--upgrade", "pip"],shell=True,stdout=f)
			returncode = process.poll()
			while True:
				if returncode is not None:
					break
				returncode = process.poll()
			if returncode!=0:
				print("Failed with code:"+str(returncode))
				return
			process = subprocess.Popen(["pip", "install", "--upgrade", "wheel"],shell=True,stdout=f)
			returncode = process.poll()
			while True:
				if returncode is not None:
					break
				returncode = process.poll()
			if returncode!=0:
				print("Failed with code:"+str(returncode))
				return

		process = subprocess.Popen(["pip", "install", "--upgrade", "-r", "requirements.txt"],shell=True,stdout=f)
		returncode = process.poll()
		while True:
			if returncode is not None:
				break
			returncode = process.poll()
		if returncode!=0:
			print("Failed with code:"+str(returncode))
			return

		print("Python requirements successfully installed")

if __name__ == "__main__":
	install()