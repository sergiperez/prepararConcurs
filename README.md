Script per facilitar resolució dels problemes que planteja el jutge.org

Passes:
- Escriure un fitxer amb el nom que vulgueu i extensió txt. Per exemple 1.txt.
- En aquest fitxer escriure l'entrada exemple del problema del jutge.
- Programar en el fitxer nomtriatprimerpas.py la solució. Per exemple 1.py.
- Executar ./p.sh nomfitxertriat per exemple ./p.sh 1

Si s'ha de recollir multiples línies de valors d'entrada podeu fer codi inicial:
```python3=
import fileinput
lines=[]
for line in fileinput.input():
    lines.append(line[:-1])
```

A lines és una llista amb tots els valors rebuts a l'entrada. Teniu un exemple a l'arxiu sumofdigits.py
