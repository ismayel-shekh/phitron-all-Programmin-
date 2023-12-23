class phone:
    manufactured = 'china'
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,hi,sms):
        text = f'sending to : {hi}{sms}'
        print(text)
# phone = phone()
# result = phone.send_sms(46565,'dur bal')
# print(result)
my_phone = phone('kala chan','oppo',9800)
print(my_phone.owner,my_phone.brand,my_phone.price)
her_phone = phone('my bow','iphon',120000)
print(her_phone.owner,her_phone.brand,my_phone.price)
dad_phone = phone('abbu','nokia',3000)
print(dad_phone.owner,dad_phone.brand,dad_phone.price)
