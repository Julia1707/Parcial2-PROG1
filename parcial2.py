def is_mutant(dna):
    def check_sequence(sequence):
        return (sequence.count("AAAA") or sequence.count("aaaa"))>= 1 or (sequence.count("TTTT")or sequence.count("tttt") )>= 1 or (sequence.count("CCCC") or sequence.count("cccc")) >= 1 or (sequence.count("GGGG")or sequence.count("gggg")) >= 1

    # Verificar filas
    for row in dna:
        if check_sequence(row):
            return True

    # Verificar columnas
    for col in range(len(dna[0])):
        column_sequence = "".join(dna[row][col] for row in range(len(dna)))
        if check_sequence(column_sequence):
            return True

    # Verificar diagonales principales
    for i in range(len(dna) - 3):
        for j in range(len(dna[0]) - 3):
            diagonal_sequence = "".join(dna[i + k][j + k] for k in range(4))
            if check_sequence(diagonal_sequence):
                return True

    # Verificar diagonales secundarias
    for i in range(len(dna) - 3):
        for j in range(len(dna[0]) - 3):
            diagonal_sequence = "".join(dna[i + k][j + 3 - k] for k in range(4))
            if check_sequence(diagonal_sequence):
                return True

    return False

def main():
    # Solicitar al usuario las secuencias de ADN y almacenarlas en una lista
    dna = []
    for i in range(6):
        valid_input = False
        while not valid_input:
            row = input(f"Ingrese la secuencia de ADN para la fila {i + 1}: ").upper()
            if all(base in "ATCG" for base in row):
                valid_input = True
                dna.append(row)
            else:
                print("Error: La secuencia de ADN solo puede contener las letras A, T, C y G. Inténtelo de nuevo.")

    # Verificar si es mutante
    if is_mutant(dna):
        print("El ADN ingresado corresponde a un mutante.")
    else:
        print("El ADN ingresado no corresponde a un mutante.")

if __name__ == "__main__":
    main()
