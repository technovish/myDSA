class Youtube:
    def __init__(self,username, subscriber=0, subscriptions=0):
        self.username = username
        self.subscriber = subscriber
        self.subscriptions = subscriptions
    def subscribe(self,user):
        user.subscriber+=1
        self.subscriptions+=1
        print(self.username,"has subscribed to",user.username)

vishal = Youtube("Vishal") 
mansi = Youtube("Mansi")
mansi.subscribe(vishal)
print("Mansi")
print(mansi.subscriber)
print(mansi.subscriptions)
print("Vishal")
print(vishal.subscriber)
print(vishal.subscriptions)


