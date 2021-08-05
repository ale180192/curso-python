# Excepciones en pytho
"""
Errores detectados durante la ejecucion son llamados excepciones
y no son incondicionalmente fatales.
"""
# ejemplo de una excepcion. Podemos ver que el programa arroja
# un error de tipo excepcion y termina el programa imprimiendo
#  el traceback del error. la excepcion es de tipo "ValueError"

# numero = int(input("Ingresa un numero: "))


# Como podemos manejar las excepciones, y decidir si queremos
# que nuestro programa continue o termine?
while True:
    try:
        # numero = int(input("Ingresa un numero: "))
        break
    except ValueError:
        print("Opss! Eso no fue un numero valida, intenta de nuevo de favor ..")


"""
La sentencia try funciona como sigue:

- Primero, el cuerpo de la clausula try es ejecutado.

- Si ninguna excepcion ocurre, la clausula "except" es saltada/ignorada
    y la sentencia try es terminada.

- Si alguna excepcion ocurre durante la ejecucion de la clausula "try",
    el resto de la clausula es saltado. Entonces si el tipo de excepcion
    lanzado por el error es igual al nombre definido despues de la palabra
    clave "except", la clausula except es ejectada y entonces la ejecucion
    continua despues de la sentencia "try".

- Si una excepcion ocurre y esta no es identica a la exception nombrada en
    nuestra clausula "except", Es pasada a sentencias "try" externas; si ningun
    manejador es encontrado, es una excepcion no manejada y la ejecucion se detiene
    con un mensaje del traceback.


Podemos capturar mas de un tipo de excepcion en una misma clausula "except":

except (RuntimeError, TypeError, NameError):
    pass


# Todas las excepciones heredan de la clase base "Exception" y una clase
    en la en una clausula "except" sera compatible(hara match) si es la misma
    clase, o una clase base.

 - Sentencia else se ejecutara solo si ninguna excepcion fue lanzada.

 - Sentencia finally se ejecutara siempre, si hubo alguna excepcion y
    esta no fue manejada, se ejecutara finally primero y despues sera re-lanzada
    la excepcion. Si la excepcion es manejada primero se ejecuta el bloque "except"
    y despues el bloque "finally"

"""
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

try:
    # utilizamos "raise" emitir excepciones.
    raise B()
    raise Exception()
    print("ok")
    raise C()
    raise D()
    raise ValueError
except D as e:
    print("D", e)
    print(type(e))
except C as e:
    print("C", e)
    print(type(e))
except B as e:
    print("B")
    print(type(e))
except ValueError as e: # Usar esta sentencia con cautela. Cualquier error que suceda sera atrapado por esta clausula.
    print("Exception no identificada", e)
    print(type(e))
else: # esta clausula se ejecutara solo si ninguna excepcion fue lanzada.
    print("Todo ok.")
finally:
    print("cerrar conexion con base de datos.")


# Exceptions personalizadas
class StockException(Exception):
    
    def __init__(self, msg):
        self.msg = msg

class CustomException(Exception):
    pass


"""
Notas:

- Usar las exceptions tanto como tengamos necesidad de comunicar los errores
    que pasen en nuestros programas.

- Usar bloques try-except lo mas pequeños posibles para poder delimitar las lineas
    de codigo que nos pueden arrojar excepciones.

- Nunca hacer sentencias try-except para toda nuestro codigo, tampoco atrapar las excepciones
    con la clase base Exception, Si tenemos bien identificado el tipo de Excepcion que puede
    ser lanzada, usar este tipo para capturarla.

- Siempre sera mejor que nuestro programa termine si detecta un error que no estamos preparados
    para manejarlo, a que se capture esta excepcion desconocida y sea silenciada. Si el programa
    continua puede comportarse de forma no esperada y sera dificil encontrar estos comportamientos
    extraños, si falla sabremos exactamente dondes fallo y podremos corregir el error.

- Definir nuestras propias excepciones para comunicar errores que tengan el contexto
    de nuestro programa(NoExisteUsuarioException, CuentaBancariaSinFondosException, etc)

- Usar el modulo "logging" de python para tener todos los logs a la mano, en caso de fallo podemos
    ir diractamente a este archivo de logs y ver el traceback de nuestro error.

"""
