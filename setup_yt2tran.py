# Install requirements

import os
def install_deps():
    upgrade_pip = 'pip install --upgrade pip'
    install_colorama = "pip install colorama"
    install_selenium = 'pip3 install selenium'


    install_list = [upgrade_pip, install_colorama, install_selenium]
    for command in install_list:
        
        install_output = os.system(command)
        
        if install_output == 0:
            print('\nPackage', str(install_list.index(command) + 1), 'of', str(len(install_list)), 'done')
            if install_selenium == command:
                from colorama import Fore
                print(Fore.GREEN)
                print('Dependancies installation complete!')
                print(Fore.WHITE)
        else:
            print('Install failed')

install_deps()


def replace_filepath():
    from colorama import Fore
    fp_from = str(input('What is the file path to the geckodriver? '))
    for i in range(len(fp_from)):
        
        if fp_from[i] == '"':
            fp_from = fp_from.replace('"', '')
            break
        elif fp_from[i] == "'":
            fp_from = fp_from.replace("'", '')
            break
    change_fp = open('firefox_get_yt_transcript.py', 'r')
    file_list = change_fp.readlines()
    for line_index in range(len(file_list)):
        if file_list[line_index] == "get_fp_from_usr = 'replace_this'\n":
            file_list[line_index] = f"get_fp_from_usr = '{fp_from}'\n"
            break
        
    write_fp = open('firefox_get_yt_transcript.py', 'w')
    for line in file_list:
        write_fp.write(line)
    print(Fore.GREEN)
    print('Done!')
    print(Fore.WHITE)

replace_filepath()