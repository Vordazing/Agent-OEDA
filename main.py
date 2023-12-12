import os
import sys
import yaml
from components import check
from components import output


def menu():
    logo = """
             OOOOO   EEEEEEE  DDDDD      AAA   
            OO   OO  EE       DD  DD    AAAAA  
            OO   OO  EEEEE    DD   DD  AA   AA 
            OO   OO  EE       DD   DD  AAAAAAA 
             OOOO0   EEEEEEE  DDDDDD   AA   AA           
            """
    print("INFO:OEDA:" + logo)
    while True:
        actions = {
            'p': print_white_list,
            's': settings_configuration,
            'e': exit_program
        }
        print("INFO:OEDA:\n============ Menu ============")

        for key, value in actions.items():
            print(f"{key}. {value.__name__.replace('_', ' ')}")

        choice = input("Select an action (p, s, e): -->")

        if choice in actions:
            actions[choice]()
        else:
            error_input()
            continue


def settings_configuration():
    print("""INFO:OEDA:\n
    Welcome to the script configuration section!
    You can change the configuration parameters directly in the "oeda.config" file. 
    However, despite your freedom, we recommend that you leave this file untouched to avoid possible errors.
    Instead, we offer you a convenient way to configure the parameters right here.
    """)

    while True:
        config_file = 'oeda.config'

        with open(config_file, 'r') as file:
            config_lines = file.readlines()

        config_data = {}
        for line in config_lines:
            key, value = line.strip().split(' = ')
            config_data[key] = value
            
        for i, (key, value) in enumerate(config_data.items(), start=1):
            print(f"({i}) {key} = {value}")
        choice = input("Select an option (1, 2, 3, 4, 5, e): --> ")
        if choice == 'e':
            write_config_data_to_file(config_file, config_data)
            back_menu()
        elif choice in ['1', '2', '3', '4']:
            check_function = {
                '1': check.check_docker,
                '2': check.check_user,
                '3': check.check_comp3,
                '4': check.check_comp4
            }.get(choice)
            check_function()
        elif choice == '5':
            check.update_ntfy_url(config_data)
        else:
            error_input()


def print_white_list():
    while True:
        print("INFO:OEDA:=========== Output of components ===========")
        print("(1) Display information about component Docker")
        print("(2) Display information about component 2")
        print("(3) Display information about component 3")
        print("(4) Display information about component 4")
        print("(m) Go back to the menu")
        print("(e) Exit the program.")
        choice = input("Select an option (1, 2, 3, 4, m, e): --> ")
        if choice == 'e':
            exit_program()
        elif choice == 'm':
            menu()
        elif choice in ['1', '2', '3', '4']:
            interact_with_component(int(choice))
        else:
            error_input()


def write_config_data_to_file(config_file, config_data):
    with open(config_file, 'w') as file:
        for key, value in config_data.items():
            file.write(f"{key} = {value}\n")


def interact_with_component(component_number):
    print(f"INFO:OEDA:Displaying information about component {component_number}")
    print(component_number)
    while True:
        #Сюда пишем ссылку на функцию которая отвечает за вывод данных вашего компонента
        components = {
            1: output.output_docker,
            2: output.output_comp2,
            3: output.output_comp3,
            4: output.output_comp4
        }

        if component_number in components:
            components[component_number]()

        print(f"(1) Reload {component_number}",
              "(2) Go back",
              "(e) Exit")

        sub_choice = input("Select an option (1, 2, e): --> ")

        actions = {
            '1': interact_with_component,
            '2': print_white_list,
            'e': exit_program,
        }
        if sub_choice in actions:
            actions[sub_choice](component_number)
        else:
            error_input()


def create_configuration_file(file_name):
    script_directory = os.path.dirname(__file__)
    file_path = os.path.join(script_directory, file_name)

    if os.path.exists(file_path):
        return

    with open(file_name, 'w') as file:
        data = {
            'Obtain': False,
            'Establish': False,
            'Deploy': False,
            'Active': False,
            'ntfy_url': 'noy'
        }
        yaml.dump(data, file, default_flow_style=False)


def main():
    create_configuration_file('oeda.yaml')
    menu()


def exit_program():
    print("INFO:OEDA:Exit the program.")
    sys.exit()


def error_input():
    text = "WARNING:OEDA:Incorrect input. Please select an existing option."
    return print(text)


def back_menu():
    print(f"INFO:OEDA:Returning to the menu.")
    return menu()


if __name__ == '__main__':
    main()

