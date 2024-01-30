personer = [
    {
        "navn": "Ravi",
        "alder": 33
    },
    {
        "navn": "Thor",
        "alder": 39
    },
    {
        "navn": "Ingrid",
        "alder": 21
    },
]

# sorterer lista med ordbøker (personer) i synkende rekkefølge på nøkkelen alder
sortert_personer = sorted(personer,key=lambda person:person["alder"], reverse=True)
topp_2 = sortert_personer[:2]
print(topp_2)