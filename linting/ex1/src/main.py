import os
from house import House

username = os.getenv("username")
password = os.getenv("password")

if not username or not password:
	exit(1)

input_username = input("Username: ")
input_password = input("Password: ")

if username == input_username and password == input_password:
	villa = House()
	villa.SetName("Neverland")
	villa.GetName()
