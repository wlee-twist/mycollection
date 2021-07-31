
import datetime
from O365 import Account, Connection,  MSGraphProtocol, Message
#from exchangelib import IMPERSONATION, Account, Credentials, OAuth2Credentials, \
#    Configuration, OAUTH2, Identity


#from O365 import Account, Connection,  MSGraphProtocol, Message, MailBox, oauth_authentication_flow




#import O365
#from email import parser
#from O365 import Account

#credentials = ('b0a99a53-9960-4a65-9d93-e81508790962', 'hX-8T-Cs2jsSz-E3kOtz0.A~Z5P3y.369T')
#credentials = ('5b30b4cf-d89a-4101-b4dd-c4240f88ba27', 'b0a99a53-9960-4a65-9d93-e81508790962')

credentials = ('5b30b4cf-d89a-4101-b4dd-c4240f88ba27', 'hX-8T-Cs2jsSz-E3kOtz0.A~Z5P3y.369T')


client_id='5b30b4cf-d89a-4101-b4dd-c4240f88ba27'
client_secret='hX-8T-Cs2jsSz-E3kOtz0.A~Z5P3y.369T'
tenant_id='4c82da03-c0b2-4798-be0f-8f6f478333f8'


user='wlee@frbnp.com'

#credentials = OAuth2Credentials(
#    client_id=client_id,
#    client_secret=client_secret,
#    tenant_id=tenant_id,
#    identity=Identity(primary_smtp_address=user)
#)





scopes = ['https://graph.microsoft.com/.default']
#scopes=['basic', 'message_all']



#scopes = ['https://graph.microsoft.com/Mail.ReadWrite', 'https://graph.microsoft.com/Mail.Send']
#account = Account(credentials,scopes=scopes)
#account.authenticate()
#account = Account(credentials, auth_flow_type='credentials', tenant_id='my-tenant-id')

account = Account(credentials, auth_flow_type='credentials', tenant_id='4c82da03-c0b2-4798-be0f-8f6f478333f8', main_resource='wlee@frbnp.com')
if account.authenticate(scopes=scopes):
   print('Authenticated!')



#print(result = account.authenticate(scopes=['basic', 'message_all']))
#print(result = account.authenticate(scopes=['Email_Alalysis', 'message_all']))


#account = Account(credentials)
#account.authenticate()
#scopes = ['https://graph.microsoft.com/Mail.ReadWrite', 'https://graph.microsoft.com/Mail.Send']
#con = Connection(credentials, scopes=scopes)

account.connection.refresh_token()

mailbox = account.mailbox()
query = mailbox.new_query().on_attribute('isRead').equals(False).chain('and').on_attribute('created_date_time').greater(datetime.datetime(2022, 9, 15))
print(query)

inbox = mailbox.get_folder(folder_name='Inbox')


for message in inbox.get_messages(limit=25,query=query):
        myflag=message.flag
        myflag.set_flagged()
        print(message)
        print(message.categories)
        message.save_message()



#help(account)
#m = account.new_message()
#m.to.add('wlee@firstrepublic.com')
#m.subject = 'Testing!'
#m.body = "George Best quote: I've stopped drinking, but only while I'm asleep."
#m.send()




#message.categories=['Red Category','Potential Fraud Detected']
#message.save_message()



#query = mailbox.new_query() query = query.on_attribute('subject').contains('george best').chain('or').startswith('quotes')


#datetime.datetime(2018, 12, 31)