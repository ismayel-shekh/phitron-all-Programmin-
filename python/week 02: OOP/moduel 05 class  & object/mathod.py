def call():
    print('coling someone i dont know')
    return 'call done'
class phone:
    price = '1cor'
    color = 'blue' 
    brand = 'akis'
    fature = ['camara','spacer','hammer']
    def call(self):
        print('call some one')
    def send_sms (self,phone,sms):
        text =f'sending sms to you : {phone} and massage :{sms}'
        return text
my_phone = phone()
print(my_phone.fature)
my_phone.call()
result = my_phone.send_sms(1869285696,'halar po')
print(result)