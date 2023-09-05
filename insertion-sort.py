def insertion_sort_stable(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Mova os elementos maiores que a chave para a direita
        # apenas se a chave for menor que eles e mantenha a ordem relativa
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insira a chave na posição correta
        arr[j + 1] = key

# Exemplo de uso:
my_list = [(3, "Alice"), (2, "Bob"), (3, "Eve"), (1, "Charlie")]
insertion_sort_stable(my_list)
print(my_list)