from my_data import MyData
from utils import Utils

# /Users/andranikalajajyan/Desktop/technicalinterviewtaskkrisp/Model1_Score.log
# /Users/andranikalajajyan/Desktop/technicalinterviewtaskkrisp/Model2_Score.log
# /Users/andranikalajajyan/Desktop/technicalinterviewtaskkrisp/Model3_Score.log
# /Users/andranikalajajyan/Desktop/technicalinterviewtaskkrisp/Released_Score.log

if __name__ == '__main__':
    print('-----------\nWelcome!')
    print("Enter 'M' for input data model and 'R' for released file paths. Firstly input models and in the end "
          "released file: ")
    number_of_models = 1
    models = []
    released = []
    while True:
        input_command = Utils.input_m_or_f()
        if input_command == 'M':
            model_path = Utils.input_valid_path(f'Model[{number_of_models}]')
            print(f'Model[{number_of_models}] path is {model_path}')
            model = MyData(f'Model {number_of_models}', model_path)
            number_of_models += 1
            models.append(model)
            continue
        elif input_command == 'F':
            released_path = Utils.input_valid_path(f'Released Score')
            print(f'Released Score path is {released_path}')
            released_file = MyData('Released', released_path)
            released = released_file
            break
        else:
            print("'M' or 'F'")
            continue

    print(f"{released.name} mean is: {released.mean}")
    print(f"{released.name} std is: {released.stdev}")
    print(f"{released.name} variance is: {released.variance}")

    good_mean_model_name = ''
    good_mean = 1000
    good_f_test = 0
    good_f_test_model_name = ''

    for model in models:
        t_test = model.get_t_test(released)
        f_test = model.get_f_test(released)
        print(f"{model.name} mean is: {model.mean}")
        print(f"{model.name} std is: {model.stdev}")
        print(f"{model.name} variance is: {model.variance}")
        print(f"{model.name} t-test value is: {t_test}")
        print(f"{model.name} f-test value is: {f_test}")
        if released.mean - model.mean < good_mean:
            good_mean = released.mean - model.mean
            good_mean_model_name = model.name
        if f_test > good_f_test:
            good_f_test = f_test
            good_f_test_model_name = model.name

    print(
        f"As we see the nearest mean is in {good_mean_model_name}, but this not the prove that all data is represent "
        f"simply so I perform F-test and discover that the best Model is {good_f_test_model_name}")
