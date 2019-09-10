Purpose:
---------------------------
Identify the company name if MAC address is provided.

Prerequisite:
---------------------------
Linux machine with make installed and docker engine running

How to use:
---------------------------
Build a docker image out of the source code:

Command:

``make build`` 

Run the docker container along with a MAC address:

Command:

`` make run MAC='44:38:39:ff:ef:57' `` 

Sample run with valid MAC:
---------------------------
[root@ip-172-31-34-145 HCL-Cisco]# `` make run MAC='44:38:39:ff:ef:57'`` 

docker stop mac-customer

mac-customer

docker rm -f mac-customer

mac-customer

docker rm -f mac-customer

Error: No such container: mac-customer

make: [Makefile:7: run] Error 1 (ignored)

docker run --name mac-customer -d mac-customer /usr/nvaka/bin/mac-customer.py 44:38:39:ff:ef:57

7b6555e943c9e6ee6e99d635db67cccc0c82cad0afe67c00aa3bdfd9b741a6cd

docker logs -f mac-customer

`` Cumulus Networks, Inc`` 


Sample run with invalid MAC:
---------------------------

[root@ip-172-31-34-145 HCL-Cisco]# `` make run MAC='44:38:9:ff:ef:57'`` 

docker stop mac-customer

mac-customer

docker rm -f mac-customer

mac-customer

docker rm -f mac-customer

Error: No such container: mac-customer

make: [Makefile:7: run] Error 1 (ignored)

docker run --name mac-customer -d mac-customer /usr/nvaka/bin/mac-customer.py 44:38:9:ff:ef:57

7adec26080e96d500d8fc600c61d01b7a688b84dbfcc70250ae1946c6bdb5f7c

docker logs -f mac-customer

`` None`` 

[root@ip-172-31-34-145 HCL-Cisco]#
