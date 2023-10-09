import random
from racing_car import Car
from racing_exception import IllegalArgumentException


class CarRacingModel:
    def __init__(self):
        pass

    def must_under_5(self, _break_num, _name):
        for i in range(len(_name)):  # 유저의 수만큼 for문이 실행된다.
            if len(_name[i]) > 5:  # 글자의 크기가 5보다 크면 _break_num이 1이 되고 break로 for문을 빠져나온다.
                _break_num = 1
                break
        return _break_num

    @staticmethod
    def is_valid_round_num(_round_num):
        if _round_num.isdigit() == False:
            raise IllegalArgumentException("[ERROR] 라운드 수는 반드시 숫자 이어야 합니다.")

    @staticmethod
    def obtain_random_num(name):  # 0에서 9 까지의 수를 랜덤하게 유저의 수만큼 생성
        return random.choices(range(0, 10), k=len(name))  # choice는 한개만 추출, choices는 여러개 추출

    def append_temp_list(self, name, random_num):
        temp_list = []  # 생성한 랜덤의 수를 4 이상이면 1, 4보다 작으면 0으로 temp_list에 저장 --> zero_one_list에 저장
        self.decide_based_on_4(name, random_num, temp_list)
        return temp_list

    @staticmethod
    def decide_based_on_4(name, random_num, temp_list):
        for n in range(len(name)):
            if random_num[n] >= 4:
                temp_list.append(1)
            elif random_num[n] < 4:
                temp_list.append(0)



    @staticmethod
    def append_car_list(n, name, zero_one_list, car_list):  # 첫번째 라운드일때
        car = Car(name[n])  # 첫번째 라운드일때 이므로 car객체 생성
        car.position += zero_one_list[n]
        car_list.append(car)


    @staticmethod
    def add_position_after_1(k, name, car_list, zero_one_list):  # 두번째 라운드, 첫번째 라운드에서 이미 객체가 생성된 상태
        car_list[k].position += zero_one_list[k]

    def obtain_winner_name(self, name, car_list):
        position_list = []
        name_list = []
        self.make_position_list(name, position_list, car_list)
        self.decide_winner(name, position_list, name_list)
        return name_list

    @staticmethod
    def make_position_list(name, position_list, car_list):
        for i in range(len(name)):
            position_list.append(car_list[i].position)  # position_list에 유저car객체의 모든 최종 position 값을 유저 순서대로 모은다.

    @staticmethod
    def decide_winner(name, position_list, name_list):
        for n in range(len(name)):
            if position_list[n] == max(position_list):
                name_list.append(name[n])  # position_list의 n번째 원소가 최대값이면 그 순서에 해당하는 이름을 name_list에 어펜드 한다.
