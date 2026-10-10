def duree (debut : tuple, fin : tuple) -> tuple:
    tp_passe_hr = fin[0] - debut[0]
    tp_passe_min = fin[1] - debut[1]
    if tp_passe_hr <= 0 :
        tp_passe_hr += 24
    if tp_passe_min <= 0 :
        tp_passe_min += 60
        tp_passe_hr -= 1
    return (tp_passe_hr, tp_passe_min)

