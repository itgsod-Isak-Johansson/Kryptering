#coding: latin-1

def encrypt(cleartext, offset):
    """Om man skickar in en text(cleartext) och ett nummer(offset) som alphabetet ska förskjutas med, så får man ut en
    krypterad kod. Jag började med att göra om texten(cleartext) till stora bokstäver, därefter går programmet igenom
    varjebokstav i texten och tar sedan reda på dess index. Då behöver programmet bara lägga till bokstaven som ligger
    på platsen index+offset eller index+offset-26 om index+offset > 25. Den är inte snabb på längre texter som om man
    kunde skriva programmet med replace istället eftersom den måste gå igenom varje bokstav i listan."""
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
    """Den här funktionen fungerar likadant som encrypt, med några få justeringar: Jag började med att konvertera
    negativ offset -> positiv offset och tvärtom, sedan behövde jag också konvertera retur strängen till små bokstäver.
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
