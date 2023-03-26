#!/usr/bin/env python

import getpass
import os

def detonate():
    print("Perdeu, a bomba explodiu!")


def stall_the_defuser():
    jstll = None
    if not jstll:
        print("Oi")
        breakpoint()
        print("Tens certeza que queres desarmar a bomba?")
        breakpoint()
        print("É periogoso, você pode ser machucar")
        breakpoint()
        os.system('say "Vasco da Gama"')
        breakpoint()
        print("Sabe, eu imaginei que você estaria em um Mac... notou que a ventuinha está mais barulhenta?")
        breakpoint()
        print("Uma hora dessas o Anjos já está aloprando...")
        breakpoint()
        os.system('say "Vasco da Gama"')
        breakpoint()
        print("digita 'detonate()' pra eu ver uma parada?")
        breakpoint()
        print("dica: a senha são os números do seu cartão, com data de validade e a senha de segurança")
        breakpoint()
    return


def main():
    # porta de entrada
    breakpoint()
    try:
        stall_the_defuser()

        user_password = getpass.getpass("Quer mesmo desarmar a bomba? Digite a senha...")

        print("Primeiro nível")
        if not(not len(str(user_password)) == 3):
            print("okay...")
        else:
            raise Exception

        print("Segundo nível")
        if not('4' not in set(l for l in str(user_password))):
            print("okay...")
        else:
            raise Exception
    
        print("Terceiro nível")
        if int(user_password) < 12 ** 2:
            print("okay...")
        else:
            raise Exception
        
        print("Quarto nível")
        if int(user_password) % 11 == 0:
            print("okay...")
        else:
            raise Exception

        print("Último nível")
        if int(user_password) % 13 == 0:
            print("okay...")
        else:
            raise Exception

    except Exception:
        detonate()


if __name__ == '__main__':
    main()
