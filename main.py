import datetime

import matplotlib.pyplot as plt
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display
class persianWriting():
    """
    Class containing the persian texts. source of the __str__ function:
    https://virgool.io/@vakily/%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%B1%D9%88%DB%8C-%D9%86%D9%85%D9%88%D8%AF%D8%A7%D8%B1-%D9%87%D8%A7-%D8%AF%D8%B1-matplotlib-winluz8b4fjz
    """
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return get_display(arabic_reshaper.reshape(u'%s' %str(self.text)))

def main() -> None:
    """

    :return:
    """
    print("اگه میخوای ببینی چه قولی داری میشنوی، همه‌ی سوالایی که پرسیده میشه رو به عدد انگلیسی وارد کن. برنامه یه گراف برات میکشه با یه عدد")
    while True:
        try:
            deposit = int(input(":اصل پولی که میخوای بذاری"))
            break
        except ValueError:
            print("فقط عدد به انگلیسی باشه لطفا")
            continue
    while True:
        try:
            interest_rate = int(input(":درصد سود ماهانه"))
            break
        except ValueError:
            print("فقط عدد به انگلیسی باشه لطفا")
            continue
    while True:
        try:
            duration = int(input(":چند ماه میخوای بمونه"))
            break
        except ValueError:
            print("فقط عدد به انگلیسی باشه لطفا")
            continue

    now = datetime.datetime.today()
    then = now + datetime.timedelta(days=(duration * 30))
    interest_rate = float(interest_rate / 100)
    duration = pd.date_range(now, then, freq='1M')
    total = deposit
    cumsum_total = []
    for i in range(len(duration)):
        cumsum_total.append(total)
        total = total+(total*interest_rate)
    cumsum_total = pd.Series(cumsum_total, index=duration)
    cumsum_total.plot()
    plt.xlabel(str(persianWriting("تاریخ")))
    plt.title(str(cumsum_total[-1]) + str(persianWriting("اگه قول طرف درست باشه آخرش این قدر پول خواهی داشت:")))
    plt.show()



if __name__ == '__main__':
    main()