import Magic_Calc.basic_ops
import Magic_Calc.advanced_ops

#
print("Basic Operations:")
result1 = Magic_Calc.basic_ops.add(10,5)
print('add', result1)

result2 = Magic_Calc.basic_ops.subtract(10,5)
print('subtract', result2)

result3 = Magic_Calc.basic_ops.multiply(10,5)
print('multiply', result3)

result4 = Magic_Calc.basic_ops.divide(10,5)
print('divide', result4)

#
print("Advanced Operations:")
result5 = Magic_Calc.advanced_ops.power(2,3)
print('power', result5)

result6 = Magic_Calc.advanced_ops.sqrt(10)
print(f"10+5={result1} 10의 제곱근은 {result6}입니다.")
