heights = input('输入你的身高(CM)：')
weights = input('输入你的体重(KG)：')
heights = float(heights)
weights = float(weights)
bmi = weights/((heights/100)**2)
print("%.2f" % bmi)
if  bmi<18.4:
        print('你的BMI类型是：偏瘦')
elif bmi >=18.4 and bmi < 23.9:
        print('你的BMI类型是：正常')
elif bmi >=24 and bmi <27.9:
        print('你的BMI类型是：偏胖')
elif bmi>=30:
        print('你的BMI类型是：肥胖')