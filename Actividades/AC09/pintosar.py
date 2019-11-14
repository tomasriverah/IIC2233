def reparar_comunicacion(ruta):
    chunks = []
    fixed_chunks = []

    with open(ruta, 'rb') as bytes_file:
        arreglo = bytearray(bytes_file)
        for i in range(0, len(arreglo), 16):
            chunk = bytearray(arreglo[i:i+16])
            chunks.append(chunk)

    for chunk in chunks:
        for number in chunk:
            
            if chunk[0] > number:
                chunk.remove(number)
        chunk_fixed = chunk[1:]
        fixed_chunks.append(fixed_chunks)

    with open('Docengelion.bmp', 'wb') as bytes_file:
        for chunk in fixed_chunks:
            bytes_file.write(chunk)



if __name__ == '__main__':
    try:
        reparar_comunicacion('EVA.xdc')
        print("PINTOSAR201: Comunicacion con pilotos ESTABLE")
    except Exception as error:
        print(f'Error: {error}')
        print("PINTOSAR301: CRITICO pilotos incomunicados DESCONEXION INMINENTE")