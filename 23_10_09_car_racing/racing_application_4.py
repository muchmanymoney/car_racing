from racing_controller_4 import RacingController
from racing_car import Car
import random


class RacingApplication:
    def __init__(self):
        self.__ctrl = RacingController()  # 컨트롤러 클래스의 메소드를 사용할 예정

    def proceed_round(self, car_list, name, total_round):
        for i in range(1, total_round + 1):  # i는 라운드 수, 0부터 시작이 아닌 1부터 시작이기 때문에 total_round에 +1 해줌
            if i == 1:  # 첫번째 라운드일때
                __random_num = self.__ctrl.get_random_num(name)  # 0~9까지의 랜덤한 수를 유저의 수만큼 생성
                zero_one_list = self.__ctrl.make_temp_list(name, __random_num)  # 유저에게 4보다 작으면 0을, 4보다 크면 1을 할당함
                # 입력받은 이름들로 car객체를 생성하고, 할당받은 0과 1을 car객체의 __position에 더한다. 생성된 car객체는 car_list에 저장한다.
                self.__ctrl.make_car_list(name, zero_one_list, car_list)

            elif i != 1:  # 두번째 라운드부터...
                __random_num = self.__ctrl.get_random_num(name)  # 0~9까지의 랜덤한 수를 유저의 수만큼 생성
                zero_one_list = self.__ctrl.make_temp_list(name, __random_num)  # 유저에게 4보다 작으면 0을, 4보다 크면 1을 할당함
                # 라운드가 진행될수록 유저에게 랜덤한 0과 1일 할당되고 그 값을 유저 car클래스의 __position에 할당
                self.__ctrl.increase_position_after_1(name, car_list, zero_one_list)


    def play(self):
        name = self.__ctrl.insert_name()   # 이름을 입력 받는다. 입력받는 이름은 5자 이하여야 한다.
        total_round = self.__ctrl.insert_round()  # 총 라운드 수를 입력 받는다. 라운드 수는 반드시 숫자 이어야 한다.

        car_list = []   # 각 각 다른 이름의 car인스턴스를 저장할 리스트

        self.proceed_round(car_list, name, total_round)

        self.__ctrl.get_winner_name(name, car_list)   # 승리자의 이름을 print한다. 승리자가 여러명일 경우 여러명을 print한다.


if __name__ == "__main__":
    RacingApplication().play()