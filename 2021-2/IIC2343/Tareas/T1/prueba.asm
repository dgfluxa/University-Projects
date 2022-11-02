.globl __start

.data:
    # set data
.text
    __start:
        li t0, 4 # (base) Guardamos 3 en t0
        li t3, 497 # (m)
        li t1, 13 # (exp) Movemos a1 a t1 para operar con esta variable temporal
        li a3, 1 # (result)

        while:
            ble t1, zero, exit # if exp <= 0 then exit
            andi t4, t1, 1 # (exp & 1) and logico entre el exponente y 1
            bgt t4, zero, if_act_func1 # if (exp & 1) > 0
            j else_act_func1 # caso contrario

            if_act_func1:
                mul t4, a3, t0 # t4 = result * base
                rem a3, t4, t3 # result = (result * base) % m
                j else_act_func1

            else_act_func1:
                srli t1, t1, 1 # exp >>= 1
                mul t4, t0, t0 # t4 = base * base
                rem t0, t4, t3 # base = (base * base) % m
                j while
    exit:
