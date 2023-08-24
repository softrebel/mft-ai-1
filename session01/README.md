<div dir="rtl">

#  جلسه اول

## لینک‌های مفید

  </div>

- [What is computational thinking?](https://www.computationalthinking.org/)
- [Why I’m not moving to from VSCode to VSCodium](https://www.youtube.com/watch?v=Yf8O5c94KtY)
- [Why is it called Python?](https://docs.python.org/3/faq/general.html#do-i-have-to-like-monty-python-s-flying-circus)
- [Monty Python's Life of Brian](https://www.imdb.com/title/tt0079470/)
- [How to Write Pythonic Code](https://towardsdatascience.com/how-to-write-pythonic-code-208ec1513c49)
- [Python Naming conventions](https://peps.python.org/pep-0008/#naming-conventions)
- [Python Clean Code](https://github.com/zedr/clean-code-python)

<div dir="rtl">

## تمرین‌ها

1. الگوریتم زیر را خط به خط توضیح دهید (از توضیح هر متغیر و هدف آن صرف نظر کنید و فقط توضیح عملیات خط به خط کفایت می‌کند):

![Algorithm Description](./perceptron.png)


2. تابعی بنویسید که دو عدد صحیح مثبت a و b را دریافت کند و یک لیست از همه اعداد زوج بین a و b را برگرداند (شامل aباشد و شامل b نباشد).

3. در رابطه با توابع all() و any() تحقیق کرده و کدهای زیر را refactor نید

4. تابعی بنویسید که N .نظر از کاربر دریافت کند و با روش زیر مشخص کنند چه تعداد طرفدار سریال هستند

- اگر داخل متن عبارت 'House Of The Dragon' بود یک واحد به متغیر نظرهای مرتبط با  آن سریال اضافه شود.
- اگر داخل متن عبارت 'The Rings Of Power' بود، یک واحد به متغیر  نظرهای مرتبط با  آن سریال اضافه شود.
- در نهایت تعداد نظرهای هرکدام از سریال‌ها چاپ شود.

(راهنمایی: از عملگر عضویت استفاده کنید)

نمونه نظرها:

 </div>
 </div>

  ```
  N=5

  1. This slow-burn episode of House Of The Dragon is Game Of Thrones as we know it – for better or worse.

  2. In The Lord of the Rings: The Two Towers, we are told that male and female dwarves are indistinguishable from one another due to their heavy facial hair. Well, a female dwarf appears in The Rings of Power – Sophia Nomvete’s Princess Disa – and she only has minimal facial hair. It’s very easy to distinguish her from the male dwarves.

  3. The episode’s title, "Second Of His Name,"”" refers to the fact that baby Aegon shares a name with Aegon the Conqueror, the legendary warrior who united the Seven Kingdoms under Targaryen rule. Considering most of House Of The Dragon's power players assume young Aegon will supplant his big sister as heir, the name is a portentous one.

  4. Matt Smith plays Daemon as a vain and bitter man who nevertheless cannot quite betray his family name. He is a nasty piece of work, for sure, a misogynist and a sadist, but until episode six, he is the only truly despicable main player in King’s Landing. House of the Dragon takes its time to drip-feed the down-in-the-dirt baddies that are so enjoyable to rail against.

  5. whereas fewer people are complaining about House of the Dragon’s adaptation of George RR Martin’s Fire and Blood. Still, Rings of Power has broken every Amazon viewership record there is, so it’s doing what it needs to do for them.

  ```

  </div>


  ```python
  number1=int(input('Enter Number 1:'))

  if number1%2 == 0 and number1 > 2:
    print('TADA')
  elif number1 > 10 or number1%3 == 0:
    print('OK')

  # all()
  # any()

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
