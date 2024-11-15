def serie_geom(r,n):
    termo,soma = 0,0
    if n < 0: raise ValueError("serie_geom: argumento incorrecto")
    else:
        while termo <= n :
            soma = soma +r**termo
            termo = termo+1
    return soma