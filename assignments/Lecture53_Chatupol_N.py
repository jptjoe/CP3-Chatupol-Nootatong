def VatCalculate(TotalPrice):
    Result = TotalPrice+(TotalPrice*7/100)
    return Result
Price = int(input("How much"))
print("Total Price is " , VatCalculate(Price))