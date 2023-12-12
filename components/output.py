import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'output_docker.json')


def output_docker():
    with open(file_path, 'r') as file:
        data = json.load(file)
    grouped_data = {}
    for item in data:
        container_id, container_info = item.popitem()
        category = container_info['category']
        if category not in grouped_data:
            grouped_data[category] = []
        grouped_data[category].append((container_id, container_info))

    for category, containers in grouped_data.items():
        print(f'Сategory {category.upper()}')
        print("-" * 20)

        for container_id, container_info in containers:
            print(f"Container ID: {container_id}")
            print(f"Image: {container_info['image']}")
            print("-" * 20)

    return data


#Ваши функции которые отвечают за выводение информации компонента
def output_comp2():
    print('comp2')


def output_comp3():
    print('comp3')


def output_comp4():
    print('comp4')