import os

import yaml
import routeros_api
import gspread
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials
import json
import time
from dataclasses import dataclass
from googleapiclient.discovery import build

@dataclass
class A1Range:
    sheet_name: str
    start_row: int
    start_col: int
    end_row: int
    end_col: int

    def format(self) -> str:
        start = f"{self.col_number_to_letter(self.start_col)}{self.start_row}"
        end = f"{self.col_number_to_letter(self.end_col)}{self.end_row}"
        return f"{self.sheet_name}!{start}:{end}"

    def iter_rows(self):
        return range(self.start_row, self.end_row + 1)

    def iter_cols(self):
        return range(self.start_col, self.end_col + 1)

    @staticmethod
    def col_number_to_letter(j: int) -> str:
        if 1 <= j <= 26:
            return chr(ord('A') + j - 1)
        elif 27 <= j <= 26 * 26:
            first_letter = chr(ord('A') - 1 + (j - 1) // 26)
            second_letter = chr(ord('A') + (j - 1) % 26)
            return first_letter + second_letter
        else:
            raise ValueError(f"Col number is out of range: {j!r}")

    @staticmethod
    def col_letter_to_number(letters: str) -> int:
        letters = letters.upper()
        if len(letters) == 1 and (ord(letters) < ord('A') or ord(letters) > ord('Z')):
            raise ValueError(f"Col letter is out of range: {letters!r}")

        if len(letters) == 2 and (ord(letters[1]) < ord('A') or ord(letters[1]) > ord('Z')):
            raise ValueError(f"The second Col letter is out of range: {letters!r}")

        if len(letters) == 1:
            return ord(letters) - ord('A') + 1
        elif len(letters) == 2:
            return (ord(letters[0]) - ord('A') + 1) * 26 + ord(letters[1]) - ord('A') + 1

    @staticmethod
    def extract_letters(text) -> str:
        only_letters = ''
        for t in text:
            if t.isalpha():
                only_letters += t
        return only_letters

    @staticmethod
    def extract_digits(text) -> str:
        only_digits = ''
        for t in text:
            if t.isdigit():
                only_digits += t
        return only_digits

    @classmethod
    def parse_a1_range(cls, a1: str):
        if "!" in a1 and ":" in a1:
            sheet_name, cell_range = a1.split('!')
            range_start, range_end = cell_range.split(':')
            start_col, start_row = cls.extract_letters(range_start), cls.extract_digits(range_start)
            end_col, end_row = cls.extract_letters(range_end), cls.extract_digits(range_end)
            return cls(
                sheet_name=sheet_name,
                start_col=cls.col_letter_to_number(start_col),
                start_row=int(start_row),
                end_col=cls.col_letter_to_number(end_col),
                end_row=int(end_row),
            )
        else:
            raise ValueError(f'Error! For method "parse_a1_range()" must be full address!')

    @classmethod
    def create_a1range_from_list(cls, sheet_name, from_row, from_col, array):

        count_rows = len(array)
        count_cols = 0
        for row in array:
            if len(row) > count_cols:
                count_cols = len(row)
        return cls(
            sheet_name=sheet_name,
            start_col=from_col,
            start_row=from_row,
            end_col=from_col+count_cols-1,
            end_row=from_row+count_rows-1,
        )
def read_yaml():
    with open('microt.yaml', 'r') as file:
        data = yaml.safe_load(file)
    return data


def connect_to_router(host, username, password):
    connection = routeros_api.RouterOsApiPool(host, username=username, password=password, plaintext_login=True)
    api = connection.get_api()
    return api, connection

def process():
    data = read_yaml()
    all_entry_info = []
    for device_name, info in data.items():
        if device_name != 'connect':
            ip = info.get('HOST', '')
            username = info.get('USERNAME', '')
            password = info.get('PASSWORD', '')
            api, connection = connect_to_router(host=ip, username=username, password=password)

            if api:
                try:
                    leases = api.get_resource('/ip/dhcp-server/lease')
                    lease_data = leases.get()

                    for entry in lease_data:
                        address = entry.get('address', '')
                        mac_address = entry.get('mac-address', '')
                        host = entry.get('host-name', '')

                        if mac_address is not None and host is not None:
                            entry_info = {
                                "Object": device_name,
                                "IP Address": address,
                                "MAC Address": mac_address,
                                "HOST": host
                            }
                            all_entry_info.append(entry_info)
                        elif mac_address is not None:
                            entry_info = {
                                "Object": device_name,
                                "IP Address": address,
                                "MAC Address": mac_address,
                                "HOST": None
                            }
                            all_entry_info.append(entry_info)
                        elif host is not None:
                            entry_info = {
                                "Object": device_name,
                                "IP Address": address,
                                "MAC Address": None,
                                "HOST": host
                            }
                            all_entry_info.append(entry_info)
                        else:
                            entry_info = {
                                "Object": device_name,
                                "IP Address": address,
                                "MAC Address": None,
                                "HOST": None
                            }
                            all_entry_info.append(entry_info)


                except Exception as e:
                    print(f"Error processing {device_name}: {e}")

                finally:
                    connection.disconnect()
    return all_entry_info



info = process()
simple_list = []

for entry in info:
    simple_entry = [entry["Object"], entry["IP Address"], entry["MAC Address"], entry["HOST"]]
    simple_list.append(simple_entry)

def write_data_to_sheet():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'loaddate-192d6721eff9.json')
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials).spreadsheets().values()

    SAMPLE_RANGE_NAME = 'Общая'
    array = {'values': simple_list}
    range_ = A1Range.create_a1range_from_list(SAMPLE_RANGE_NAME, 2, 1, array['values']).format()
    response = service.update(spreadsheetId='1U-mrSfoep1QeWZKIHMRBEzWhaWJ9oG2kv2I4Uiv5RtM',
                              range=range_,
                              valueInputOption='USER_ENTERED',
                              body=array).execute()
    return response


def start():
    gc = gspread.service_account(filename='loaddate-192d6721eff9.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])
    spreadsheet_id = '1U-mrSfoep1QeWZKIHMRBEzWhaWJ9oG2kv2I4Uiv5RtM'
    spreadsheet = gc.open_by_key(spreadsheet_id)
    worksheet_name = 'Общая'
    worksheet = spreadsheet.worksheet(worksheet_name)
    cells_to_clear = worksheet.range('A2:D' + str(worksheet.row_count))
    for cell in cells_to_clear:
        cell.value = ''
    worksheet.update_cells(cells_to_clear)

    write_data_to_sheet()


start()



