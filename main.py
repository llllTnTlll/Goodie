from cv_helper import *
from structure import *

import logit


def seats_occupying():
    # 脚本参数设定
    IS_ON_TIME = True                      # 是否在指定时间运行脚本
    START_TIME = "12/14/12:29:00"          # 脚本预执行时间
    RUN_TIME = "12/14/12:30:00"            # 脚本实际运行时间
    PRE_ROUNDS = 5
    OCC_ROUNDS = 10                        # 脚本最大抢选重复执行轮数
    STEP_RETRY = 5                         # 关键步骤重试次数

    # 初始化时间字符串
    start_time = START_TIME.replace("/", "").replace(":", "")
    run_time = RUN_TIME.replace("/", "").replace(":", "")

    # 启用日志输出
    logit.set_log()

    # 定时器
    if IS_ON_TIME:
        on_time(datetime=start_time)

    unlock_screen()

    for i in range(PRE_ROUNDS):
        print("------step1------")
        retry(STEP_RETRY)(confirm("confirm0.jpg")(click_into))("step1.jpg")

        print("------step2------")
        retry(STEP_RETRY)(confirm("confirm1.jpg")(click_into))("step2.jpg")

        print("------step3------")
        retry(STEP_RETRY)(confirm("confirm2.jpg")(click_into))("step3.jpg")

        print("------step4------")
        flag1 = retry(STEP_RETRY)(confirm("confirm3.jpg")(click_into))("step4.jpg")
        flag2 = retry(STEP_RETRY)(confirm("confirm4.jpg")(click_into))("refresh.jpg")
        # 确认是否准备完毕
        if flag1 is True and flag2 is True:
            print("READY FOR OCCUPYING...")
            break

    # 阻塞程序
    # 防止屏幕睡眠
    if IS_ON_TIME:
        keep_on(datetime=run_time)

    for i in range(OCC_ROUNDS):
        click_into("refresh.jpg")
        print("================round {}/{}================".format(i+1, OCC_ROUNDS))

        print("------first order------")
        key1 = retry(1)(confirm("confirm4.jpg")(click_into))("4289.jpg")

        print("------second order------")
        key2 = retry(1)(confirm("confirm4.jpg")(click_into))("4303.jpg")


def main():
    seats_occupying()


if __name__ == '__main__':
    main()
