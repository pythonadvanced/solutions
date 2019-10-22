
##################################################
# taxes
##################################################
# une solution très élégante proposée par adrienollier

# les tranches en ordre décroissant
TaxRate = (
    (150_000, 45),
    (45_000, 40),
    (11_500, 20),
    (0, 0),
)

def taxes(income):
    """
    U.K. income taxes calculator
    https://www.gov.uk/income-tax-rates
    """
    due = 0
    for floor, rate in TaxRate:
        if income > floor:
            due += (income - floor) * rate / 100
            income = floor
    return int(due)


##################################################
# taxes_bis
##################################################

# cette solution est plus pataude; je la retiens
# parce qu'elle montre un cas de for .. else ..
# qui ne soit pas trop tiré par les cheveux
# quoique

bands = [
    # à partir de 0. le taux est nul
    (0, 0.),
    # jusqu'à 11 500 où il devient de 20%
    (11_500, 20/100),
    # etc.
    (45_000, 40/100),
    (150_000, 45/100),
]

def taxes_bis(income):
    """
    Utilise un for avec un else
    """
    amount = 0

    # en faisant ce zip un peu étrange, on va
    # considérer les couples de tuples consécutifs dans
    # la liste bands
    for (band1, rate1), (band2, _) in zip(bands, bands[1:]):
        # le salaire est au-delà de cette tranche
        if income >= band2:
            amount += (band2-band1) * rate1
        # le salaire est dans cette tranche
        else:
            amount += (income-band1) * rate1
            # du coup on peut sortir du for par un break
            # et on ne passera pas par le else du for
            break
    # on ne passe ici qu'avec les salaires dans la dernière tranche
    # en effet pour les autres on est sorti du for par un break
    else:
        band_top, rate_top = bands[-1]
        amount += (income - band_top) * rate_top
    return int(amount)

