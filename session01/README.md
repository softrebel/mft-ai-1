<div dir="rtl">

#  جلسه اول

## تمرین‌ها

1. الگوریتم زیر را خط به خط توضیح دهید (از توضیح هر متغیر و هدف آن صرف نظر کنید و فقط توضیح عملیات خط به خط کفایت می‌کند):

![Algorithm Description](./perceptron.png)
<div dir="rtl">
جواب سوال 1:
خط اول دو عدد اینبوت 1 و 2 را   در وزنش ضرب کرده و بعد از آن مقدار بایس رو نیز در وزن بایس ضرب می کند و در نهایت حاصل ضرب 
ها را با هم جمع می کند

بعد از آن اگر این حاصل ضرب از صفر بزرگتر بود مقدار حاضل ضرب را به عدد یک تغییر می دهد و در غیر این صورت عدد صفر را در متغیر حاص ضرب ذخیره می کند

مقدار خطا را با بیدا کردن اختلاف متغیر اوت بوت و مقدار جدید حاصل ضرب محاسبه می کند

در نهایت وزن های جدید را برای اینبوت 1 و 2 و همچنین بایس با کمک این فرمول ها بیدا می کند


</div>


<div dir="rtl">

2.تابعی بنویسید که دو عدد صحیح مثبت a و b را دریافت کند و یک لیست از همه اعداد زوج بین a و b را برگرداند (شامل aباشد و شامل b نباشد).
```python

from typing import List

def even(a:int , b:int) -> List[int]:
    result = []
    try:
        a = int(a)
        b = int(b)
    except:
        print("lotfan adad haye dorost vared konid!")
        return
    for i in range(a , b):
        if i % 2 == 0 and i != 0:
            result.append(i)
    return result
  
print(even(0,10))  
print(even(1.5,10.75))  
print(even('a',10))
```
3.در رابطه با توابع all() و any() تحقیق کرده و کدهای زیر را refactor کنید


  </div>
  
  ```python
  number1=int(input('Enter Number 1:'))

  if number1%2 == 0 and number1 > 2:
    print('TADA')
  elif number1 > 10 or number1%3 == 0:
    print('OK')


  if any([number1 % 2 == 0, number1 > 10]) and all([number1 % 2 == 0, number1 > 2]):
      print('TADA')
  elif any([number1 > 10, number1 % 3 == 0]):
      print('OK')

  ```


<div dir="rtl">


## تحقیق
1. در مورد Zen of Python تحقیق کنید.
2. آیا استفاده از continue و break در روش‌های برنامه‌نویسی جدید توصیه می‌شود؟
3. تفاوت data type و data structure
4. تعاریف و تفاوت‌هایinital value, falsy value, zero value
5. مفهوم Pythonic
6. مفهوم Clean Code
7. نام‌گذاری متغیرها به صورت snake case و camel case

## مهارت‌های جانبی
1. نصب git
2. نصب github desktop
3. ساخت اکانت در github
