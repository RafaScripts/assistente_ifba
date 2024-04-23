import subprocess

isMac = True  # Defina como True se estiver executando no macOS, caso contrário, defina como False

# Mapeamento entre os nomes dos aplicativos e os processos correspondentes no Linux
# aqui você deve mapear com os nomes dos seus devidos programas
processos_linux = {
    "navegador": "firefox",
    "notas": "gedit",  # Exemplo: Abrir o Gedit para notas
    "monitor": "gnome-system-monitor"  # Exemplo: Abrir o Monitor do Sistema no GNOME
}

def exec_cmd_open(cmd):
    executed = False
    try:
        if isMac:
            if cmd == "navegador":
                print("Abrindo navegador...")
                command = ["open", "-a", "Safari"]
                subprocess.run(command)
            elif cmd == "notas":
                print("Abrindo Bloco de Notas...")
                command = ["open", "-a", "Notes"]
                subprocess.run(command)
            elif cmd == "monitor":
                print("Abrindo Monitor...")
                command = ["open", "-a", "Activity Monitor"]
                subprocess.run(command)
        else:  # Se não estiver no macOS, assumimos que é Linux
            if cmd in processos_linux:
                print(f"Abrindo {cmd}...")
                subprocess.Popen([processos_linux[cmd]])
        executed = True
    except:
        executed = False

    return executed

def exec_cmd_close(cmd):
    executed = False
    try:
        if isMac:
            if cmd == "navegador":
                print("Fechando navegador...")
                command = ["osascript", "-e", 'quit app "Safari"']
                subprocess.run(command)
            elif cmd == "notas":
                print("Fechando Bloco de Notas...")
                command = ["osascript", "-e", 'quit app "Notes"']
                subprocess.run(command)
            elif cmd == "monitor":
                print("Fechando Monitor...")
                command = ["osascript", "-e", 'quit app "Activity Monitor"']
                subprocess.run(command)
        else:  # Se não estiver no macOS, assumimos que é Linux
            if cmd in processos_linux:
                print(f"Fechando {cmd}...")
                subprocess.run(["pkill", "-f", processos_linux[cmd]])

        executed = True
    except:
        ...

    return executed
def suspend():
    print("Suspendendo...")
    executed = False
    try:
        if isMac:
            command = ["open", "-a", "/System/Library/CoreServices/ScreenSaverEngine.app"]
            subprocess.run(command)
        else:  # Se não estiver no macOS, assumimos que é Linux
            # No Linux, você pode usar o comando "systemctl suspend" para suspender o sistema
            command = ["systemctl", "suspend"]
            subprocess.run(command)
        executed = True
    except:
        ...

    return executed
