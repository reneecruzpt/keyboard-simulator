def fibonacci_nth(n): #retorna o n-ésimo número
    if n < 0:
        print('Entrada inválida!')
        return None
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[n]

def fibonacci_c(n): #retorna a sequência completa até n
    fib_list = [0, 1]  # Reinicia a lista a cada execução
    if n < 0:
        print('Entrada inválida!')
        return None
    for i in range(2, n + 1):
        fib_list.append(fib_list[-1] + fib_list[-2]) #adiciona os dois números no fim da lista
    return fib_list

print(fibonacci_nth(9))
print(fibonacci_c(9))