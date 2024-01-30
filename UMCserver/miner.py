from whatsminer import WhatsminerAccessToken, WhatsminerAPI
import socket
import json

def whatsminer(ip):
    try:
        token = WhatsminerAccessToken(ip_address=ip)
        pool_json = WhatsminerAPI.get_read_only_info(access_token=token, cmd="pools")
        devdetails_json = WhatsminerAPI.get_read_only_info(access_token=token, cmd="devdetails")
        model = devdetails_json['DEVDETAILS'][0]['Model']
        worker = pool_json['POOLS'][0]['User']
        return [model, worker]
    except Exception as e:
        return None

def get_data(HOST, command):
    PORT = 4028
    data = {"command": command}
    data_str = json.dumps(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.sendall(bytes(data_str, encoding="utf-8"))

            received_data = ''
            while True:
                chunk = s.recv(4026)
                if not chunk:
                    break
                received_data += chunk.decode("utf-8")
        except Exception as e:
            return None

    return json.loads(received_data[:-1])

def antminer(ip):
    try:
        stats_data = get_data(ip, "stats")
        model = stats_data['STATS'][0]['Type']
        pools_data = get_data(ip, "pools")
        worker = pools_data['POOLS'][0]['User']
        return [model, worker]
    except Exception as e:
        return None

def get_device_info(ip):
    try:
        result = antminer(ip)
        if result is None:
            result = whatsminer(ip)
        return result
    except Exception as e:
        return None


