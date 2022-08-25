import enum


class Service(enum.Enum):
    PermanentEyebrowMakeup = {
        'name': 'Перманенентный макияж бровей',
        'price': 250
    }
    Coloring = {
        'name': 'Окрашивание',
        'price': 20
    }
    Correction = {
        'name': 'Коррекция (пинцет\воск)',
        'price': 15
    }
    LongTermStyling = {
        'name': 'Долговременная укладка без окрашивания',
        'price': 30
    }
    DepilationUpperLip = {
        'name': 'Депиляция верхней губы',
        'price': 5
    }
    ColoringAndCorrection = {
        'name': 'Окрашивание и коррекция',
        'price': 30
    }
    LongTermStylingWithColoringAndCorrection = {
        'name': 'Долговременная укладка с окрашиванием и коррекцией',
        'price': 50
    }
    
    