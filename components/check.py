import subprocess
import os
import re
from colorama import Fore, Style


def update_ntfy_url(config_data):
    new_url = input("Enter a new URL for ntfy_url: ")
    config_data['ntfy_url'] = new_url if new_url else 'noy'
    print(f"INFO:OEDA:ntfy_url successfully updated.")


def update_config_value(file_path, key, new_value):
    with open(file_path, 'r') as file:
        config_lines = file.readlines()

    for i, line in enumerate(config_lines):
        if f'{key} =' in line:
            config_lines[i] = f'{key} = {new_value}\n'
            break

    with open(file_path, 'w') as file:
        file.writelines(config_lines)


def check_docker():
    current_module_path = os.path.dirname(os.path.abspath(__file__))
    project_folder_path = os.path.dirname(current_module_path)
    file_path = os.path.join(project_folder_path, 'oeda.config')

    with open(file_path, 'r') as file:
        config_lines = file.readlines()

    for i, line in enumerate(config_lines):
        if 'component Obtain =' in line:
            match = re.search(r'component Obtain = (\w+)', line)
            current_value = match.group(1)
            try:
                version_result = subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE)
                docker_version = version_result.stdout.decode().strip()
                subprocess.run(["docker", "ps"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"INFO:OEDA:{docker_version}. There is access.")
                update_config_value(file_path, 'component Obtain', 'True' if current_value == 'False' else 'False')
            except FileNotFoundError:
                print("INFO:OEDA:Docker not installed. Install Docker by running the command: sudo apt-get install docker.io")
            except subprocess.CalledProcessError as e:
                if "Cannot connect to the Docker daemon" in e.stderr.decode():
                    print("WARNING:OEDA:I don't have access to the team docker ps.")
                else:
                    print(f"WARNING:OEDA:Error: {e}")
                    print("WARNING:OEDA:Check if it is installed Docker.")

#Ваши функции которые отвечают за проверку вашего компонента, будет ли работать или нет

def check_user():
    file = '/etc/passwd'
    startLinesNum = len(open(file, 'r').readlines())

    while True:
        runLinesNum = len(open(file, 'r').readlines())
        runLastLine = open(file, "r").readlines()[-1] #постоянный контроль конца
        if (runLinesNum > startLinesNum): #замечено изменение
            print("WARNING: OEDA: New user has been created: " + runLastLine.split(":")[0] + "| ID: " + runLastLine.split(":")[2])
            confirm = str(input('WARNING: OEDA: Was that you? [Y/N]: '))
            if (confirm.lower() == 'y'): #подтверждение изменения
                print(Fore.GREEN + Style.BRIGHT + 'OEDA: Confirmed.' + Style.RESET_ALL)
                startLinesNum = runLinesNum
            elif (confirm.lower() == 'n'):
                #функционал отбирания прав
                os.system(f'passwd -l {runLastLine.split(":")[0]}')
                print(Fore.RED + f'WARNING: OEDA: User {runLastLine.split(":")[0]} was locked.' + Style.RESET_ALL)
                startLinesNum = runLinesNum
            else: 
                print(Style.BRIGHT + Fore.CYAN +'WARNING: OEDA: FORBIDDEN INPUT' + Style.RESET_ALL)
                
        del runLinesNum


def check_comp3():
    print('comp3')


def check_comp4():
    print('comp4')