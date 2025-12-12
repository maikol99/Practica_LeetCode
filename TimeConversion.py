
def timeConversion(s):
    # Extraer horas, minutos, segundos y periodo usando split
    parts = s.split(':')
    hours = int(parts[0])
    minutes = parts[1]
    seconds_with_period = parts[2]  # Ejemplo: "45PM"
    
    # Separar segundos del periodo AM/PM
    seconds = seconds_with_period[0:2]
    period = seconds_with_period[2:4]
    
    # Convertir según las reglas
    if period == 'AM':
        if hours == 12:
            hours = 0  # Medianoche: 12 AM -> 00
    else:  # PM
        if hours != 12:
            hours += 12  # 1-11 PM -> 13-23
        # 12 PM se queda como 12
    
    # Formatear con ceros a la izquierda
    return f'{hours:02d}:{minutes}:{seconds}'

# Ejemplos de prueba
print(timeConversion('12:01:00PM'))  # 12:01:00
print(timeConversion('12:01:00AM'))  # 00:01:00
print(timeConversion('07:05:45PM'))  # 19:05:45