def is_prime(num):
    """Verifica se um número é primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def save_primes_to_file(start, end, filename):
    """Salva números primos entre start e end em um arquivo."""
    primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
    with open(filename, "w") as file:
        file.write("\n".join(primes))
    print(f"Números primos entre {start} e {end} foram salvos em '{filename}'.")

# Definição do intervalo e arquivo de saída
start_range = 1
end_range = 250
output_file = "results.txt"

# Salvar números primos no arquivo
save_primes_to_file(start_range, end_range, output_file)