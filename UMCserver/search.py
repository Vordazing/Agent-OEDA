import ipaddress
import yaml
import routeros_api


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


def find_microtik(object, ip):
    with open('microt.yaml', 'r') as file:
        data = yaml.safe_load(file)
    for key, value in data.items():
        if key == object:
            host_data = value
            api_pool = routeros_api.RouterOsApiPool(host_data.get('HOST'), username=host_data.get('USERNAME'), password=host_data.get('PASSWORD'), plaintext_login=True)
            api = api_pool.get_api()
            leases = api.get_resource('/ip/dhcp-server/lease').get(address=ip)
            if leases:
                mac_address = leases[0]['mac-address']
                return mac_address
            else:
                return None

a = find_microtik(object='Aша 1', ip='10.200.1.207')
print(a)