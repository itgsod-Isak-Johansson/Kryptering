#coding: latin-1

def encrypt(cleartext, offset):
    """Om man skickar in en text(cleartext) och ett nummer(offset) som alphabetet ska f�rskjutas med, s� f�r man ut en
    krypterad kod. Jag b�rjade med att g�ra om texten(cleartext) till stora bokst�ver, d�refter g�r programmet igenom
    varjebokstav i texten och tar sedan reda p� dess index. D� beh�ver programmet bara l�gga till bokstaven som ligger
    p� platsen index+offset eller index+offset-26 om index+offset > 25. Den �r inte snabb p� l�ngre texter som om man
    kunde skriva programmet med replace ist�llet eftersom den m�ste g� igenom varje bokstav i listan."""
    cleartext = cleartext.upper()
    output = ""
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if len(cleartext) == 0:
        raise ValueError("can not encrypt empty string")
    if offset == 0:
        raise ValueError("offset must not be zero")
    for letter in cleartext:
        if letter not in alphabet:
            output += letter
        else:
            i = alphabet.index(letter)
            if i+offset > 25:
                output += alphabet[i+offset-26]
            else:
                output += alphabet[i+offset]
    return output


def decrypt(cleartext, offset):
    """Den h�r funktionen fungerar likadant som encrypt, med n�gra f� justeringar: Jag b�rjade med att konvertera
    negativ offset -> positiv offset och tv�rtom, sedan beh�vde jag ocks� konvertera retur str�ngen till sm� bokst�ver.
    """
    offset = -offset
    cleartext = cleartext.upper()
    output = ""
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if len(cleartext) == 0:
        raise ValueError("can not encrypt empty string")
    if offset == 0:
        raise ValueError("offset must not be zero")
    for letter in cleartext:
        if letter not in alphabet:
            output += letter
        else:
            i = alphabet.index(letter)
            if offset+i > 25:
                output += alphabet[(i+offset)-26]
            else:
                output += alphabet[i+offset]
    return output.lower()
