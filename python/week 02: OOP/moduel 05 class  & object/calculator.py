class  calculator:
    band = 'nosto'
    def sumation(num1,num2):
        sum = num1+num2
        return sum
    def defrance(num1,num2):
        defa = num1-num2
        return defa
    def devide(sum1,sum2):
        dev = sum1/sum2
        return dev
result = calculator.band
result1 = calculator.sumation(4,5)
result2 = calculator.defrance(5,4)
result3 = calculator.defrance(6,2)
print(result,result1,result2,result3)