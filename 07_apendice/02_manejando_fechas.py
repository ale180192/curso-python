"""
Los modulos datetime y timedelta nos permiten manejar fechas.
Todos estos modulos vienen en el paquete integrado datetime
"""

from datetime import (
    datetime,
    timedelta,
    timezone
)

# creando un objeto con el tiempo actual.
"""
Por defecto toma la zona horaria del sistema operativo.
Este objeto datetime es un objeto no consciente, es decir
su tiempo no esta atado a una zona en especifico. solo indica
que es tal hora pero sin hacer referencia a alguna zona horaria.
"""
now = datetime.now()
print(now)

# indicando la zona horaria.
"""
Para esto tenemos que crear un objeto timezone
con un offset relativo a UTC(hora cero)

"""
offset_cancun = timedelta(hours=-5)
tz = timezone(offset=offset_cancun)
now_cancun = datetime.now(tz=tz)
print(now_cancun)

# restando objetos datetime
"""
Podemos obtener la diferencia de tiempo entre dos fechas,
el unico requisito es que los dos objetos datetime sean
objetos consientes(son objetos que tienen un offset respecto a UTC)
"""
offset_cdmx = timedelta(hours=-6)
tz_cdmx = timezone(offset=offset_cdmx)
now_cdmx = datetime.now(tz=tz_cdmx)
print(now_cdmx)

diff_cdmx_and_cancun = now_cdmx - now_cancun
print(diff_cdmx_and_cancun)

# formateando fechas.
now_str = datetime.strftime(now_cdmx, "%Y-%m-%dT%H:%M:%SZ")
print(now_str)

# creando objetos datetime a partir de cadenas
str_now = "2021-08-06T00:49:15Z"
now_obj = datetime.strptime(str_now, "%Y-%m-%dT%H:%M:%SZ")
print(now_obj)