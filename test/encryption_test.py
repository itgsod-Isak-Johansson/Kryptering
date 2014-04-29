#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('..')

from encryption import encrypt


def setup():
    global cleartext, offset
    cleartext = 'the quick brown fox jumps over the lazy dog'
    offset = 3


@with_setup(setup())
def test_encrypt_takes_a_string_and_offset_as_arguments():

    assert_raises(TypeError, encrypt)
    assert_raises(TypeError, encrypt, cleartext)

# Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C eller A-nivå
def test_encrypt_raises_ValueError_if_called_with_empty_string():
    with assert_raises(ValueError) as e:
        encrypt('', offset)
    assert_equal(e.exception.message, 'can not encrypt empty string')


 #Detta test kan kommenteras bort om man inte vill testa 'Undantagshantering' på C eller A-nivå
def test_encrypt_raises_ValueError_if_called_with_zero_offset():
    with assert_raises(ValueError) as e:
        encrypt(cleartext, 0)
    assert_equal(e.exception.message, 'offset must not be zero')


def test_decrypt_returns_a_string():
    assert_is_instance(encrypt(cleartext, offset), str)


def test_encrypt_returns_the_encrypted_string_capitalized():
    assert_equal(encrypt(cleartext, 3), 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ')
    assert_equal(encrypt(cleartext, 13), 'GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT')
    assert_equal(encrypt(cleartext, 5), 'YMJ VZNHP GWTBS KTC OZRUX TAJW YMJ QFED ITL')


def test_encrypt_works_with_negative_offsets():
    assert_equal(encrypt(cleartext, -2), 'RFC OSGAI ZPMUL DMV HSKNQ MTCP RFC JYXW BME')
    assert_equal(encrypt(cleartext, -11), 'IWT FJXRZ QGDLC UDM YJBEH DKTG IWT APON SDV')
    assert_equal(encrypt(cleartext, -4), 'PDA MQEYG XNKSJ BKT FQILO KRAN PDA HWVU ZKC')


def test_encrypt_accepts_lower_and_upper_case_letters():
    assert_equal(encrypt('The quiCk broWn fox JUMPS over the lazY dog', offset), 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ')