## Eksempel: Penger tjent på spotify

> En algortime som regner ut hvor mye penger vi tjener på spotify

```pseudo
Hent inn antall streams
Hvis antall streams er større enn 30 000 000:
    Returner antall streams gange 70% (0.7)
Ellers hvis antall stream er større enn 1 400 000: 
    Returner antall streams gange 40% (0.4)
Ellers:
    returner 0
```

```pseudo-udir
SET antall_streams TO READ "Hvor mange streams?"
IF antall streams GREATHER THAN 30 000 000
    THEN DISPLAY antall_strems * 0.7
    
```



```python
# Oppgave: Skriv algortimen i vanlig python-kode:
antall_streams = int(input("Hvor mange streams?"))

if antall_streams > 30_000_000:
    print(antall_streams * 0.7)
elif antall_streams > 1_400_000:
    print(antall_streams * 0.4)
else:
    print (0)

```