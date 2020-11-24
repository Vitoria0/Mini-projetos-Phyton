#Tratamento de Erros e Exceções

try: #-------tente
    a = int(input('Numerador: '))
    b = int(input('Dennominador: '))
    r = a / b

except ZeroDivisionError:
    print('Não se pode dividir por zero')

except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')

else:  #------Se não der erro:
    print(f'O resultado é {r:.1f}')

finally: #-------Finaliza com:
    print('Volte sempre!')
    