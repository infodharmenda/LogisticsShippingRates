#Shipping Cost Calculator

## Input of weight and rate of the goods
weight = float(input("Enter the package weight in kilograms : "))
rate = float(input("Enter the shipping rate per kilograms : "))

##Calculate Shipping Cost  
shipping_cost = weight * rate

##Display the Result
print("Shipping Cost: {shipping_cost} USD")
