from num2words import num2words 
  
Number = input("What is your number: ") 
Number = str(Number)
Final = num2words(Number).replace("-", "").replace(" ", "").replace(",", "") 


list = []
list.append(Final)

while Final != "four":
    Final = num2words(len(Final.replace("-", "").replace(" ", "").replace(",", "") ))
    list.append(Final.replace("-", "").replace(" ", "").replace(",", "") )

list = ["" if i=="four" else i for i in list]

while '' in list:
    list.remove('')

list.append("four")
print(list)

list = [""]
