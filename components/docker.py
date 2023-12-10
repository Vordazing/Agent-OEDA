import asyncio
import os
import re
import subprocess
import json


async def load_docker():
    while True:
        file_path = os.path.abspath('../oeda.config')
        with open(file_path, 'r') as file:
            content = file.read()
        match = re.search(r'component Obtain\s*=\s*(\S+)', content)
        obtain_value = match.group(1)
        if obtain_value == 'False':
            print('Все не ок')
            break
        elif obtain_value == 'True':
            result = execute_docker_command()
            lines = result.strip().split('\n')
            if 'CONTAINER ID   IMAGE' in lines:
                lines.remove('CONTAINER ID   IMAGE')
                output_file_path = os.path.abspath('output_docker.json')
                try:
                    with open(output_file_path, 'r') as json_file:
                        existing_data = json.load(json_file)
                        file_data_set = {next(iter(item.keys())) for item in existing_data}
                        filtered_input_data = [
                            item for item in lines if item.split()[0] not in file_data_set
                        ]
                except (FileNotFoundError, json.decoder.JSONDecodeError):
                    existing_data = []
                    filtered_input_data = lines

                for line in filtered_input_data:
                    container_id, image = re.search(r'(\S+)\s+(.+)', line).groups()
                    existing_data.append({container_id: {'image': image, 'category': 'new'}})

                with open(output_file_path, 'w') as json_file:
                    json.dump(existing_data, json_file, indent=2)
        print('Все ок')
        await asyncio.sleep(5)


def execute_docker_command():
    try:
        docker_command = "docker ps -a --format 'table {{.ID}}\t{{.Image}}'"
        result = subprocess.run(docker_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        return e


asyncio.run(load_docker())