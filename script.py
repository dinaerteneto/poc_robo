import pyautogui
import pyperclip
import time
import easygui

# Exibir uma caixa de diálogo de confirmação
# pyautogui.alert('Clique em OK para iniciar o script.')

# Perguntar ao usuário o número de linhas do arquivo de texto
num_lines = easygui.integerbox(msg='Quantas linhas tem o arquivo de texto?',
                               title='Número de Linhas',
                               default=1,
                               lowerbound=1)

# Caminho completo do arquivo poc.txt na área de trabalho
poc_file_path = 'C:\\Users\\Dinaerte\\Documents\\code\\farme\\poc\\poc.txt'  # Substitua pelo caminho real do arquivo poc.txt

# Abrir o arquivo poc.txt no Bloco de Notas
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('notepad')
pyautogui.press('enter')
# Aguardar o Bloco de Notas abrir
time.sleep(2)

# Pressionar "Ctrl+O" para abrir o arquivo poc.txt no Bloco de Notas
pyautogui.hotkey('ctrl', 'o')
time.sleep(1)
pyautogui.write(poc_file_path)
pyautogui.press('enter')
time.sleep(2)

# Mover para a primeira linha do Bloco de Notas
pyautogui.hotkey('ctrl', 'home')

# Copiar a linha atual do Bloco de Notas
pyautogui.hotkey('ctrl', 'shift', 'right')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Abrir o libreoffice
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('libreoffice calc')
time.sleep(0.5)
pyautogui.press('enter')

# Aguardar o arquivo poc.txt abrir o LibreOffice Calc
time.sleep(6)

pyautogui.hotkey('ctrl', 'v')

# Retornar para o Bloco de notas
pyautogui.hotkey('alt', 'tab')    
time.sleep(0.5)

for _ in range(num_lines - 1):
    # Copiar a próxima linha do Bloco de Notas
    pyautogui.press('down')
    time.sleep(0.5)

    pyautogui.press('home')
    pyautogui.hotkey('ctrl', 'shift', 'right')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # Verificar se chegou ao final do texto
    copied_text = pyperclip.paste().strip()
    if copied_text == '===eof===':
        break

    # retorna para o LibreOffice Calc
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)

    # cola o conteúdo na linha de baixo do LibreOffice Calc
    pyautogui.hotkey('down')
    pyautogui.hotkey('ctrl', 'v')

    # Retorna para o bloco de notas
    pyautogui.hotkey('alt', 'tab')
    time.sleep(0.5)

# Fechar o Bloco de Notas
# pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('alt', 'f4')
time.sleep(0.5)
pyautogui.hotkey('alt', 'f4')
pyautogui.press('tab')
pyautogui.press('enter')
