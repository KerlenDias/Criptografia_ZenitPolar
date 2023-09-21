mensagem = input('Escreva uma mensagem:')
mensagem_cifrada =""
for letra in mensagem:
    if letra == 'Z' or letra == 'z':
       mensagem_cifrada = mensagem_cifrada + "p"
       continue;
    if letra == 'E' or letra == 'e':
       mensagem_cifrada = mensagem_cifrada + "o"
       continue;
    if letra == 'N' or letra == 'n':
       mensagem_cifrada = mensagem_cifrada + "l"
       continue;
    if letra == 'I' or letra == 'i':
       mensagem_cifrada = mensagem_cifrada + "a"
       continue;
    if letra == 'T' or letra == 't':
       mensagem_cifrada = mensagem_cifrada + "r"
       continue;
    if letra == 'P' or letra == 'p':
       mensagem_cifrada = mensagem_cifrada + "z"
       continue;
    if letra == 'O' or letra == 'o':
        mensagem_cifrada = mensagem_cifrada + "e"
        continue;
    if letra == 'L' or letra == 'l':
        mensagem_cifrada = mensagem_cifrada + "n"
        continue;
    if letra == 'A' or letra == 'a':
        mensagem_cifrada = mensagem_cifrada + "i"
        continue;
    if letra == 'R' or letra == 'r':
        mensagem_cifrada = mensagem_cifrada + "t"
        continue;

    mensagem_cifrada = mensagem_cifrada + letra
print(mensagem_cifrada)