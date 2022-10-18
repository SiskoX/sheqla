

# from mimetypes import common_types


# def main():
   

#     class Account:
#         def __init__(self,name,buying_power,balance) -> None:
#             self.name = name
#             self.buying_power= buying_power
#             self.balance = balance
         

        
#     class Commodity:

#         def __init__(self,price:float,commodity_type:str,tradable:False,acc:Account) :
#             self.price = price
#             self.commodity_type = commodity_type
#             self.tradable = tradable
#             self.acc = acc

            
#         @property
#         def check_blance (self):
#             if self.acc.buying_power - self.acc.balance > 15:
#                 self.tradable == True 
#                 self.price - self.acc.balance
#                 print (self.acc.balance)
#             else:
#                 print('balance to low')


  
        
 
#     class Node:
#         def __init__(self,data:Commodity):
#             self.dataInfo  = {
#                 'price':data.price,
#                 'commodity_Type':data.commodity_type,
#                 'tradable':data.tradable
                

#             }
#         def printdinfo(self)->list:
#             return print(self.dataInfo)
        
#         def check_tradeable(self)->None:

#             if self.dataInfo['tradable'] == True:
#                 print('tthis commodity is tradable  ',)
#             else:
#                 print('not tradeable')
            


           
#     account= Account('feysel',300,50)

#     commodity = Commodity(34.5,'coffe',True,account)
#     print (commodity.check_blance)
#     c = Node(commodity)
   
#     # p =c.printdinfo()
#     # check = c.check_tradeable()
#     # print(p.__hash__)


#     # print(c.printdinfo())
    
def main():
    class A:
        def __init__(self,a) -> None:
            print('A class')
            
    class B:
        def __init__(self,b) -> None:
            print('B class')
    class C(A,B):
        def __init__(self) -> None:
           
            super().__init__('C')
            print('C class')
 
    c1= C()

if __name__ == '__main__':
    main()