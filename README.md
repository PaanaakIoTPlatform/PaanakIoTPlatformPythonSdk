# PaanakCloudPythonSdk
<div style="direction:rtl">
SDK پایتون پلت فرم اینرتنت اشیاء پاناک برای ارسال اطلاعات (اطلاعات سنسورها) و دریافت دستور(وضعیت رله‌ها) توسط دستگاه‌ها به پلت فرم پاناک با زبان برنامه نویسی پایتون است. 
برای استفاده از پلتفرم ابنترنت اشیاء پاناک باید ابتدا در آدرس    
<a href="https://paanaak-cloud.ir">https://paanaak-cloud.ir</a>
ثبتنام کنید و دستگاه مورد نظر خود را بسازید و سنسورهای آنرا تعریف کنید. پس از آن میتوانید با استفاده از کلید خصوصی دستگاه خود از SDK استفاده کنید.
پلت فرم از HTTPS و HTTP پشتیبانی می‌کند اما توصیه جدی ما استفاده از HTTPS است
<hr/>
متدها:
<h4 style="direction:ltr">
add_sensor(self, name: str, data_type: str)
</h4>
این متد به دستگاه شما یک سنسور اضافه میکند. سنسورها ابتدا باید در پلت فرم برای دستگاه تعرف شوند و پس از آن میتوان از این متد استفاده کرد. Name در این متد همان برچسب تعریف شده برای سنسور در پلت فرم است و نوع سنسور هم میتواند یکی از سه نوع عدد اعشاری(float)، دودویی(bool) یا رشته(string)  باشد.
<h4 style="direction:ltr">
send_sensors_values(self, sensor_values: dict, https=True)
</h4>
این متد نام و مقدار سنسورها را به شکل یک دیکشنری دریافت میکند و آنرا برای ذخیره به پلت فرم ارسال میکند. اگر مقدار یک سنسور با نوع آن مطابقت نداشته باشد این متد یک exception خواهد داد.
آرگومان HTTPS هم مشخص میکند که اطلاعات از طریق HTTPS ارسال شوند یا HTTP که به صورت پیشفرش true است.
خروجی این متد در صورت وجود رله‌ها در دستگاه تعریف شده آرایه‌ای از 0 و 1 است که وضعیت رله‌ها را مشخص میکند.
<h4 style="direction:ltr">
get_status(self, https=True)
</h4>
این متد آخرین وضعیت رله ها را به صورت آرایه ای از 0  و 1  ها بر میگرداند.
آرگومان HTTPS هم مشخص میکند که اطلاعات از طریق HTTPS ارسال شوند یا HTTP که به صورت پیشفرش true است.
<h4 style="direction:ltr">
send_relays_state(self, state, https=True):
</h4>
این متد وضعیت فعلی رله‌ها در دستگاه شما را به صوت یک رشته از 0 و 1 به سرور ارسال و وضعیت جدید را به صورت آرایه ای از 0  و 1  ها بر میگرداند.
آرگومان HTTPS هم مشخص میکند که اطلاعات از طریق HTTPS ارسال شوند یا HTTP که به صورت پیشفرش true است.
<h4 style="direction:ltr">
send_sensors_and_relays(self, sensor_values: dict,state, https=True):
</h4>
این متد مقادیر سنسورها را در یک دیکشنری و وضعیت فعلی رله‌ها به صورت یک رشته تشکیل شده از 0 و 1 به سرور ارسال میکند و وضعیت جدید رله ها را به صورت یک آرایه از 0 و 1 دریافت می‌کند.
آرگومان HTTPS هم مشخص میکند که اطلاعات از طریق HTTPS ارسال شوند یا HTTP که به صورت پیشفرش true است.
<hr/>
خطاهای ممکن:
<h4 style="direction:ltr">
too many requests:
</h4>
هر دستگاه قادر است هر 5 ثانیه یکبار به پلت فرم درخواست ارسال کند. در صورتی که زمان ارسال درخواست کمتر از 5 ثانیه باشد این ارور صادر و در خروجی تمام توابع مقدار فلگ آن true میشود.
<h4 style="direction:ltr">
requests limit:
</h4>
در صورتی که شارژ حساب کاربری شما تمام شده باشد این فلگ true و این ارور صادر میشود. در این صورت باید نسبت به افزایش اعتبار و خرید ریکوست اقدام کنید
<hr/>
آموزشها و اطلاعات بیشتر به صورت ویدئویی در لینک زیر قابل مشاهده هستند<br>
<a href="https://www.aparat.com/paanaak">https://www.aparat.com/paanaak</a>
