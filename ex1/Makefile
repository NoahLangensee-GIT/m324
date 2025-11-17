all: address

ip:
	hostname -I | cut -d' ' -f1 > ip

host:
	hostname > host

address: ip host
	echo "$$(cat host)@$$(cat ip)" > address

version:
	make --version

clean:
	rm -f ip host address

.PHONY: all version clean