import re
from excepciones import IngresoInvalido


def revisar_usuario(usuario):
    if re.fullmatch("^[a-zA-Z0-9_]{3,8}@[a-zA-Z0-9.]{4,12}", usuario):
        if len(re.findall("\.", usuario)) == 1:
            return True
        else:
            print()
            raise IngresoInvalido("Tu usuario debe tener un único punto")
    else:
        print()
        raise IngresoInvalido("El usuario ingresado es inválido")


def revisar_clave(clave):
    if re.fullmatch("\w{8,12}", clave):
        if re.search("[A-Z]", clave):
            return True
        else:
            print("Tu contraseña debe tener al menos una mayúscula.\n")
            raise IngresoInvalido("Tu contraseña debe tener al"
                                  " menos una mayúscula")
    else:
        print("Tu contraseña debe tener entre 8 y 12 caracteres.\n")
        raise IngresoInvalido("Tu contraseña debe tener entre"
                              " 8 y 12 caracteres")
