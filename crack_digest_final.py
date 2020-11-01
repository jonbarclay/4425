from hashlib import md5


method_uri = "GET:/".encode('utf-8')


hash2 = md5(method_uri).hexdigest()


realm = "members only".encode('utf-8')


colon = ":".encode('utf-8')


qop = "auth".encode('utf-8')


cnonce = "6bc37926abce6649".encode('utf-8')


nonce = "cPmikbouBQA=92809400a6834c1fbc7b098b91e0fe759da84dcd".encode('utf-8')


nc = "00000001".encode('utf-8')

response = "19c247a1cb6718b06f986ff2be144837"



usrs = open("usrlst.txt", 'r')



for usr in usrs.read().split('\n'):

	usr2=usr.encode('utf-8')

	pwds = open("pwdlst.txt", 'r')

	for pwd in pwds.read().split('\n'):

		pwd2=pwd.encode('utf-8')

		hash1 = md5(usr2+colon+realm+colon+pwd2).hexdigest()

		computed_response = md5(hash1.encode('utf-8')+colon+nonce+colon+nc+colon+cnonce+colon+qop+colon+hash2.encode('utf-8')).hexdigest()

		if computed_response in response:

			print('Cracked successfully')

			print('The computed response value: %s'%computed_response)

			print('The username: %s'%usr)

			print('The password: %s'%pwd)

		else:

        		pass
