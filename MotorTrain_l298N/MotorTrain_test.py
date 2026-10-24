from MotorTrain_l298N import MotorTrain_l298N
bot = MotorTrain_l298N(12, 11, 9, 10)

def main():
    bot.stop()
#bot.move(left_power_in_percent, right_power_in_percent, time in sec)
    bot.move(70, 50, 2)
    bot.stop()

if __name__ == "__main__":
    main()