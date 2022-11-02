# Basado en codigo de Ayudantia RISCV2

.data
    result1:      .asciz "\nHan Pasado "
    result2:      .asciz " segundos!\n"
    timeNow:    .word 0xFFFF0018
    cmp:        .word 0xFFFF0020
    AskForTime: .ascii "\nIngrese un tiempo:\n"
.text
    main:
        # Pedir tiempo
        la a0, AskForTime # load address of AskForControl
        li a7, 4
        ecall # Call linux to output the string
        li a7, 5 # ReadInt
        mv a0, zero
        ecall # get int from console, store in a0

        li t0, 1000
        mul a1, a0, t0 #Guardamos el valor del tiempo en milisegundos en a1

        # armar el timer para que dispare cada a1 segundos
        lw a0, timeNow
        lw t2, 0(a0)
        add t1, t2, a1
        lw  a0, cmp
        sw  t1, 0(a0)

        
        # setetar la direccion del handler y activamos las interrupciones
        la	t0, handle
        csrrs	zero, 5, t0
        csrrsi	zero, 4, 0x10
        csrrsi	zero, 0, 0x1
        
        
    loop:
        nop
        j	loop


    handle:
        # guardar temporales
        addi	sp, sp, -20
        sw	t0, 16(sp)
        sw	t1, 12(sp)
        sw	t2, 8(sp)
        sw	a0, 4(sp)
        sw	a7, 0(sp)
        
        # imprimimos los segundos que pasaron
        li	a7, 4
        la	a0, result1
        ecall
        li t3, 1000
        div a0, a1, t3
        li a7, 1
        ecall
        li	a7, 4
        la	a0, result2
        ecall
        
        # Pedir tiempo
        la a0, AskForTime # load address of AskForTimw
        li a7, 4
        ecall # Call linux to output the string
        li a7, 5 # ReadInt
        mv a0, zero
        ecall # get int from console, store in a0

        li t0, 1000
        mul a1, a0, t0 #Guardamos el valor del tiempo en milisegundos en a1
        mv t1, a1

        li t4, 1
        blt a1, t4, done #Si se ingresa 0 o menor se termina

        # rearmar el timer para que dispare cada t1 segundos
        lw a0, timeNow
        lw t2, 0(a0)
        add t1, t2, t1
        lw t0, cmp
        sw t1, 0(t0)
        
        # recargar temorales y salir
        lw	t0, 16(sp)
        lw	t1, 12(sp)
        lw	t2, 8(sp)
        lw	a0, 4(sp)
        lw	a7, 0(sp)
        addi	sp, sp, 20	
        uret

    done:
        li	a7, 10
        ecall
        
