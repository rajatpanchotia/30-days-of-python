cars =["ok","ok","ok","ok","ok","ok","ok"]
all_successful =True
for status in cars:
    if status=="faulty":
        print("stop the production")
        print("found the faulty car..")
        break
    print(f"this is a {status}")
    print(f"shipping new car:")
##if all_successful:
else:
    print("all are bulit successfully no faulty car")

## NAIVE CODE

    
