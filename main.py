import matplotlib.pyplot as plt


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

    cumsum_total = []
    interest_rate = float(interest_rate/100)
    total = deposit
    for i in range(duration):
        cumsum_total.append(total)
        total = total+(total*interest_rate)

    plt.plot(cumsum_total)
    plt.xlabel("ماه")
    plt.ylabel("پولی که تو ماه داری")
    plt.xticks([i for i in range(len(cumsum_total))])
    plt.yticks(cumsum_total)
    plt.title(" :جمع پولی که بعد از این مدت داری" + str(cumsum_total[-1]))
    plt.show()



if __name__ == '__main__':
    main()