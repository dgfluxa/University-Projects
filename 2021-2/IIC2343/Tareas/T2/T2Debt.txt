.globl start
.data
    # --- VIAJE ---
    # --- No modificar labels ---
    N: .word 3 # cantidad de amigues en el viaje
    amigues: .word 0, 1, 2 # ID de cada amigue
    G: .word 3 # cantidad de gastos realizados al final del viaje
    gastos: .float 0.0, 3000.0, 2.0, 0.0, 1.0, 1.0, 5000.0, 1.0, 2.0, 1.0, 1000.0, -1.0 # gastos realizados al final del viaje
    # --- End no modificar labels ---
    # --- END VIAJE ---
    # de aca para abajo van sus variables en memoria
    debe_a: .asciz "\ndebe a\n"
    salto: .ascii "\n"
    balances: .float 0.0
.text
    start:
        # aca va su codigo :3
        la s0, N
        la s1, amigues
        la s2, G
        la s3, gastos
        la s4, balances

        li a0, 1 # contador para create_array
        li a1, 4 # offset
        lw a2, 0(s0) # num de amigos
        flw fa0, 0(s4) # 0.0
        jal ra, create_array # Creamos array del largo correspondiente a la cantidad de amigos con 0.0 en todas sus posiciones

        li a0, 0 # Contador para add_payments
        li a1, 4 # offset
        mv t0, s3 # direccion actual en gastos
        lw a2, 0(s2) # num de gastos
        jal ra, add_payments # Agregamos el balance neto de los participantes en el array

        #flw fa0, 0(s4)
        #flw fa1, 4(s4)
        #flw fa2, 8(s4)

        li a3, 0 # contador para adjust_balances
        li a1, 4 # offset
        lw a2, 0(s0) # num de amigos
        jal ra, adjust_balances # Calculamos los pagos necesarios e imprimimos cada uno

        flw fa0, 0(s4)
        flw fa1, 4(s4)
        flw fa2, 8(s4)
        flw fa3, 12(s4)
        flw fa4, 16(s4)
        flw fa5, 20(s4)
        flw fa6, 24(s4)
        flw fa7, 28(s4)

        j end

    create_array: # Inputs a0, a1, a2 y fa0
        mul t0, a0, a1 # Obtenemos offset actual
        add t1, s4, t0 # Direccion actual
        fsw fa0, 0(t1) # Guardamos 0.0 en esa pos del array
        addi a0, a0, 1 # Sumamos 1 a nuestro contador
        blt a0, a2, create_array # if a0 < s0 then create_array

        jalr zero, 0(ra) # Retornamos

        

    add_payments:  # Inputs a0, a1, a2
        flw ft0, 0(t0) # Amigo que paga
        add t0, t0, a1 # Actualizamos direccion
        flw ft1, 0(t0) # Cantidad pagada
        add t0, t0, a1 # Actualizamos direccion
        flw ft2, 0(t0) # Numero de participantes

        # Agregar pago en balance neto de quien paga
        fcvt.w.s t1, ft0 #Convertimos indice float de amigo a int
        mul t2, t1, a1 # Offset en gastos para quien paga
        add t2, s4, t2 # Direccion del balance para quien paga
        flw ft3, 0(t2) # Gasto actual quien paga
        fsub.s ft3, ft3, ft1 # Actualizamos balance neto quien paga
        fsw ft3, 0(t2) # Actualizamos balance actual en array

        # Agregar pago en balance de participantes
        fcvt.w.s t1, ft2 #Convertimos num part de float a int
        li t2, -1
        beq t1, t2, all_friends # if t1 == t2 then all_friends
        j some_friends

        all_friends:
            lw t1, 0(s0) # Guardamos num part como total de amigos
            fcvt.s.w ft2, t1
            fdiv.s ft3, ft1, ft2 # Obtiene monto por persona ft3 = cantidad_pagada/num_part
            li t2, 0 # Contador
            loop_all_friends:
                mul t3, t2, a1 # Offset en gastos para amigo t2
                add t3, s4, t3 # Direccion del balance para amigo t2
                flw ft4, 0(t3) # Gasto actual amigo t2
                fadd.s ft4, ft4, ft3 # Sumamos monto a balance neto amigo t2
                fsw ft4, 0(t3) # Actualizamos balance actual en array
                addi t2, t2, 1 # Actualizamos contador
                blt t2, t1, loop_all_friends # Si el contador es menor al numero de participantes volvemos al loop
                j check_end_add_payments # Si el contador es mayor o igual al num de participantes continuamos

        some_friends:
            fdiv.s ft3, ft1, ft2 # Obtiene monto por persona ft3 = cantidad_pagada/num_part
            li t2, 0 # Contador
            loop_some_friends:
                add t0, t0, a1 # Actualizamos direccion
                flw ft2, 0(t0) # Indice participante actual
                fcvt.w.s t3, ft2 # Convertimos indice part de float a int
                mul t4, t3, a1 # Offset en gastos para amigo t3
                add t4, s4, t4 # Direccion del balance para amigo t3
                flw ft4, 0(t4) # Gasto actual amigo t3
                fadd.s ft4, ft4, ft3 # Sumamos monto a balance neto amigo t2
                fsw ft4, 0(t4) # Actualizamos balance actual en array
                addi t2, t2, 1 # Actualizamos contador
                blt t2, t1, loop_some_friends # Si el contador es menor al numero de participantes volvemos al loop
                j check_end_add_payments # Si el contador es mayor o igual al num de participantes continuamos

        check_end_add_payments:
            addi a0, a0, 1 # Actualizamos contador de gastos
            add t0, t0, a1 # Actualizamos direccion
            blt a0, a2, add_payments # Si hay mas gastos se vuelve a add_payments
            jalr zero, 0(ra) # Si no hay mas gastos se vuelve


    adjust_balances: # Inputs a3 = contador, a1 = offset, a2 = num de amigos
        li a4, 0 # Contador para loop_adjust_balances
        mul t1, a3, a1 # Offset en gastos para amigo a3
        add t1, s4, t1 # Direccion del balance para amigo a3
        flw ft0, 0(t1) # Gasto actual amigo a3
        loop_adjust_balances:
            mul t2, a4, a1 # Offset en gastos para amigo a4
            add t2, s4, t2 # Direccion del balance para amigo a4
            flw ft1, 0(t2) # Gasto actual amigo a4
            fcvt.s.w ft2, zero
            flt.s t3, ft2, ft0 # Vemos si el balance del amigo a3 es positivo
            li t4, 1
            beq t3, t4, if_balance1_positivo # De ser asi se va a if_balance1_positivo dado que ese amigo debe pagarle a alguien
            j check_end_adjust_balances #De no serlo, a ese amigo le deben o esta en 0 por lo que no debe pagar
        
            if_balance1_positivo: # Balance amigo indice a3 es positivo
                fcvt.s.w ft2, zero
                flt.s t3, ft1, ft2 # Vemos si el balance del amigo a4 es negativo
                li t4, 1
                beq t3, t4, if_balance2_negativo # De ser asi se va a if_balance2_negativo dado que a ese amigo debe pagarle a alguien
                j check_end_loop_adjust_balances #De no serlo, a ese amigo esta en 0 o el debe por lo que no le deben pagar

                if_balance2_negativo: # Balance amigo indice a4 es positivo
                    fcvt.s.w ft2, zero
                    fadd.s ft3, ft0, ft1 # Suma de los gastos de amigos a3 y a4
                    flt.s t3, ft3, ft2 # Vemos si la suma es negativa
                    li t4, 1
                    beq t3, t4, if_suma_negativa # De ser asi se va a if_suma_positiva
                    j else_suma_positiva #De no serlo, se va a else_suma_positiva
                
                    if_suma_negativa:
                        fmv.s ft4, ft0 # Valor a pagar es igual al balance de a3
                        j continue_if_balance2_negativo

                    else_suma_positiva:
                        li t3, -1
                        fcvt.s.w ft5, t3
                        fmul.s ft5, ft1, ft5
                        fmv.s ft4, ft5 # Valor a pagar es igual al balance de a4 * -1
                        j continue_if_balance2_negativo
                        
                    continue_if_balance2_negativo:
                        # Restar valor a balance a3 y actualizar array de balance
                        fsub.s ft0, ft0, ft4
                        fsw ft0, 0(t1)
                        # Sumar valor a balance a4 y actualizar array de balance
                        fadd.s ft1, ft1, ft4
                        fsw ft1, 0(t2)
                        # Hacer print
                        li a7, 1
                        mv a0, a3
                        ecall # Imprime indice a3 (El que debe)
                        li	a7, 4
                        la	a0, debe_a
                        ecall # Imprime "debe a"
                        li a7, 1
                        mv a0, a4
                        ecall # Imprime indice a4 (A quien le deben)
                        li a7, 4
                        la a0, salto
                        ecall # Imprime salto de linea
                        li a7, 2
                        fmv.s fa0, ft4
                        ecall # Imprime cantidad a pagar
                        li a7, 4
                        la a0, salto
                        ecall # Imprime salto de linea
                        j check_end_loop_adjust_balances
                
            check_end_loop_adjust_balances:
                addi a4, a4, 1 # Se suma 1 al contador de amigo a4
                blt a4, a2, loop_adjust_balances # Si el contador es menor al num de amigos se continua en el loop
                j check_end_adjust_balances # En caso contrario se sale del loop

        check_end_adjust_balances:
            addi a3, a3, 1 # Se suma 1 al contador de amigo a3
            blt a3, a2, adjust_balances # Si el contador es menor al num de amigos se continua en adjust_balances
            jalr zero, 0(ra) # En caso contrario se sale de adjust_balances


    end:
        li	a7, 10
        ecall




         
