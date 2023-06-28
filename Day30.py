'''
try:
    dic = {"key":"Success"}
    print(dic["key"])
# except:  #Run when try programs shows exception
#     print("Exception occurs")
except TypeError: #Run only when try block show type exception
    print("Type exception")
else:  #Run whe try program don't show any exception
    print("NO exception")
finally: #Run in every situation
    print("Run in every Situation")
 '''   

height = int(input("Enter yoiur height in m:-> "))

if height > 4:
    raise ValueError("Height is more then normal height.")

