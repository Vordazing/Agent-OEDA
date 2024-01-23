import ipaddress
import yaml


def find_network(ip):
    with open('microt.yaml', 'r') as file:
        data = yaml.safe_load(file)

    target_ip = ipaddress.IPv4Address(ip)
    partial_ip = ".".join(str(target_ip).split('.')[1:3])

    for key, value in data.items():
        if 'HOST' in value and 'dopHOST' in value:
            host_ip = value['HOST'].split('.')
            dop_ip = value['dopHOST'].split('.')
            if 'dopHOST2' in value:
                dop2_ip = value['dopHOST2'].split('.')
                if host_ip[1:3] == partial_ip.split('.') or dop_ip[1:3] == partial_ip.split('.') or dop2_ip[
                                                                                                    1:3] == partial_ip.split(
                        '.'):
                    return key
            else:
                if host_ip[1:3] == partial_ip.split('.') or dop_ip[1:3] == partial_ip.split('.'):
                    return key

    return None


