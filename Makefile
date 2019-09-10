all: build run

build:
	docker build --pull --rm=true -t mac-customer .

run: delete
	- docker rm -f mac-customer
	docker run --name mac-customer -d mac-customer /usr/nvaka/bin/mac-customer.py $(MAC)
	docker logs -f mac-customer

delete:
	- docker stop mac-customer
	- docker rm -f mac-customer

logs:
	docker logs -f mac-customer
