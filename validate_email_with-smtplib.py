import re
import smtplib
import dns.resolver

# Simple Regex for syntax checking

regex = '^[w.-]+@([w-]+.)+[w-]{2,4}$'

# Email address to verify
addressToVerify = input("Please enter the emailAddress to verify:").strip()

# regex check
if not(re.search(regex,addressToVerify)):
      raise ValueError('email seems invalid!')
         

# Get domain for DNS lookup
splitAddress = addressToVerify.split('@')
domain = str(splitAddress[1])
print('Domain:', domain)

# MX record lookup
records = dns.resolver.resolve(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

# SMTP lib setup
server = smtplib.SMTP()
# uncomment the below line if you want to see full output.
#server.set_debuglevel(1)

#This is just a fake email that doesn't probably exist for smtp.mail(fromAddress)  
fromAddress = 'just_a_place_holder@domain.com'

# SMTP Conversation
server.connect(mxRecord)
server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))
server.quit()

print("code:",code)
print("message:",message)

# Assume SMTP response 250 is success
if code == 250:
	print('Success')
else:
	print('Bad request')
