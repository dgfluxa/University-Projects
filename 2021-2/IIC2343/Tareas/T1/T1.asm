.globl  start
.data
    # --- TERREMOTO ---
    I: .word H, P, G 	# porcentajes de cada uno de los ingredientes, siempre suman 100
    # No modificar
    Wa: .word 7, 3, 2 	# pesos w_a para el primer perceptron
    Wb: .word 4, 2, 8 	# pesos w_b para el segundo perceptron
    U:  .word 150 		# umbral
    # --- END TERREMOTO ---
    # de aca para abajo van sus variables en memoria

.text
    start:    
        # aca va su codigo :3
        la s0, I # Address de I
        la s1, Wa # Address de Wa
        la s2, Wb # Address de Wb
        la s3, U # Address de U

        mv a2, s1 # Movemos la direccion de Wa (s1) a a2 para llamar al perceptron A

        jal ra, perceptron # Llamamos a la funcion perceptron para A

        mv a1, a0 # guardamos return de perceptron A en a1

        # Llamamos funcion de activacion para el resultado del perceptron A en a1
        jal ra, act_func

        mv a3, a0 # Guardamos el resultado en a3 para llamar a heaviside

        # Llamamos heaviside para obtener el resultado final de f(xa)
        jal ra, heaviside

        mv a4, a0 # Guardamos el resultado de heaviside en a4 para ingresarlo a compare_results

        mv a2, s2 # Movemos la direccion de Wb (s2) a a2 para llamar al perceptron B

        jal ra, perceptron # Llamamos a la funcion perceptron para B

        mv a1, a0 # guardamos return de perceptron B en a1

        # Llamamos funcion de activacion para el resultado del perceptron B en a1
        jal ra, act_func

        mv a3, a0 # Guardamos el resultado en a3 para llamar a heaviside

        # Llamamos heaviside para obtener el resultado final de f(xb)
        jal ra, heaviside

        mv a5, a0 # Guardamos el resultado de act_func en a5 para ingresarlo a compare_results

        # Llamamos a compare_results para determinar finalmente el valor final (terremoto bueno o malo) y guardarlo en a0
        jal ra, compare_results

        # En este momento nuestro resultado deberia estar en a0 por lo que terminamos

        j end

    perceptron: # (a2)
        # Subrutina para perceptron. A o B depende de la direccion de a2
        lw t0, 0(a2) # w1
        lw t1, 4(a2) # w2
        lw t2, 8(a2) # w3
        lw t3, 0(s0) # H
        lw t4, 4(s0) # P
        lw t5, 8(s0) # G

        # Multiplicaciones de los inputs por sus ponderadores
        mul t0, t0, t3 
        mul t1, t1, t4
        mul t2, t2, t5

        # Sumamos los resultados y lo guardamos en a0
        add t0, t0, t1
        add a0, t0, t2

        jalr zero, 0(ra) # Retornamos


    act_func: #(a1)
        # Subrutina para la funcion de activacion. Dependiendo del resultado de un perceptron (x) guardado en a1 y el umbral (u) define si llamar a act_func1 o act_func2.
        lw t0, 0(s3) # umbral
        bgt a1, t0, act_func1 # Si x es mayor a u se va a la funcion act_func1
        j act_func2 # En caso contrario, si x es menor o igual u se va a la funcion act_func2
    
        act_func1: 
            # ejecuta (3**x % x) % 3 cuando x > u
            
            # Algoritmo rescatado de https://es.wikipedia.org/wiki/Exponenciaci%C3%B3n_modular y traducido

            li t0, 3 # (base) Guardamos 3 en t0
            mv t3, a1 # (m)
            mv t1, a1 # (exp) Movemos a1 a t1 para operar con esta variable temporal
            li a0, 1 # (result)

            li t5, 3 #Corresponde al ultimo mod

            while: # Calculamos (3**x % x)
                ble t1, zero, exit_act_func1 # if exp <= 0 then exit
                andi t4, t1, 1 # (exp & 1) and logico entre el exponente y 1
                bgt t4, zero, if_act_func1 # if (exp & 1) > 0
                j else_act_func1 # caso contrario

                if_act_func1:
                    mul t4, a0, t0 # t4 = result * base
                    rem a0, t4, t3 # result = (result * base) % m
                    j else_act_func1

                else_act_func1:
                    srli t1, t1, 1 # exp >>= 1
                    mul t4, t0, t0 # t4 = base * base
                    rem t0, t4, t3 # base = (base * base) % m
                    j while
            
            exit_act_func1:
                rem a0, a0, t5 # (3**x % x) % 3
                j exit
        
        act_func2: 
            # ejecuta (x-1) % x cuando x <= u
            li t0, -1 # Guardamos -1 en t0 (Este metodo en caso de que a1 sea un numero muy grande y addi no alcance para la resta)
            sub t0, a1, t0 # Hacemos x-1 y guardamos en t0
            rem a0, t0, a1 # Hacemos (x-1)%x y guardamos en a0
            j exit

        exit:
            jalr zero, 0(ra) # Retornamos

    heaviside: #(a3)
        # Subrutina que ejecuta la funcion heaviside al resultado de act_func1 o act_func2 en a3
        bgt a3, zero, uno # Si a3 es mayor que 0 retorna 1 en a0
        j cero # En caso contrario, si a3 es menor o igual a 0 retorna 0 en a0

        uno:
        li a0, 1
        #Return
        jalr zero, 0(ra)

        cero:
        li a0, 0
        #Return
        jalr zero, 0(ra)

    compare_results: #(a4, a5)
        # Subrutina que compara los resultados finales para A y B para determinar si el terremoto es Bueno (1) o Malo (0) y guarda el resultado en a0
        add t0, a4, a5 # Sumamos a4 y a5
        li t1, 2 # Seteamos t1 a 2
        beq t0, t1, if_compare_results # Si a4 + a5 = 2. Por lo tanto, ambos serian 1.
        j else_compare_results

        if_compare_results: # Si a4 = 1 y a5 = 1 entonces a0 = 1 y volvemos
            li a0, 1 
            jalr zero, 0(ra)

        else_compare_results: # Si a4 != 1 o a5 != 1 entonces a0 = 0 y volvemos
            li a0, 0
            jalr zero, 0(ra)

    end:
        
