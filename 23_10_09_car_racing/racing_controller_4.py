from racing_view import RacingView
from racing_model_5 import CarRacingModel
from racing_exception import IllegalArgumentException

# 대부분 model의 메소드를 사용하므로 model에서 자세히 설명 하겠습니다.

class RacingController:
    def __init__(self):
        self.__model = CarRacingModel()
        self.__view = RacingView()

    def insert_name(self):  # 이름을 입력 받는다.
        while True:  # 올바른 조건의 이름이 들어올 때 까지 반복해야 하므로 while True문 사용
            _name = []  # 이름을 저장할 리스트
            _break_num = 0  # _break_num이 1일때 continue를 이용해 while True 반복문의 새 phase를 시작한다.
            # split함수를 이용하면 여러 이름을 콤마로 구분하여 받을수 있다.
            _name = input("경주할 자동차의 이름을 입력해주세요. 이름은 쉽표(,)로 구분합니다: ").split(",")
            _break_num = self.__model.must_under_5(_break_num, _name)
            if _break_num == 1:  # 글자수가 5보다 커서 다시 입력 받으려고 조건문을 통해 continue 실행
                self.__view.length_must_under_5()
                continue
            if _break_num == 0:  # 글자수가 5보다 작아 for문을 무사히 통과 했다면 while문은 빠져나온다.
                break
        return _name  # while문을 빠져나왔다면 조건에 합당한 이름이므로 return으로 반환한다.

    def insert_round(self):
        """
        게임을 실행할 라운드수를 입력받는다.
        숫자가 아닌것을 입력하면 에러가 발생하여 예외처리를 한다.
        """
        while True:
            try:
                _round_num = input("라운드 수를 입력해 주세요: ")
                self.__model.is_valid_round_num(_round_num)
                break
            except IllegalArgumentException as e:
                self.__view.show_error_message(e)
        return int(_round_num)

    def get_random_num(self, name):
        """
        모델에서 random.choices 함수를 이용하여 0에서 9 사이의 숫자를 발생시킨다.
        """
        return self.__model.obtain_random_num(name)

    def make_temp_list(self, name, random_num):
        """
        숫자가 4보다 작으면 0을, 숫자가 4 이상이면 1을 할당한다.
        """
        return self.__model.append_temp_list(name, random_num)

    def make_car_list(self, name, zero_one_list, car_list):
        """
        첫번째 라운드일때 car 인스턴스들의 리스트를 만든다
        :param name: 플레이어 이름
        :param zero_one_list: 4 이상이면 1, 4보다 작으면 0
        :param car_list: car 인스턴스들의 리스트
        """
        for n in range(len(name)):
            self.__model.append_car_list(n, name, zero_one_list, car_list)
            self.__view.show_position(n, name, car_list)
        self.__view.use_line_changer()

    def increase_position_after_1(self, name, car_list, zero_one_list):
        """
        두번째 라운드부터 실행되는 메소드,
        car 인스턴스의 포지션 값이 변경된다.
        """
        for k in range(len(name)):
            self.__model.add_position_after_1(k, name, car_list, zero_one_list)
            self.__view.show_position(k, name, car_list)
        self.__view.use_line_changer()

    def get_winner_name(self, name, car_list):
        name_list = self.__model.obtain_winner_name(name, car_list)
        self.__view.congratulate_winner(name_list)

