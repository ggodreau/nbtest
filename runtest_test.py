import pytest
import logging
logging.basicConfig(filename='example.log',level=logging.ERROR)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# logger = logging.getLogger(__name__).addHandler(logging.NullHandler())
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_myfunc():
    with pytest.raises(NameError):
        from out import *
        #from out import wrap
        wrap()

#def test_myfunc_fail():
#    try:
#        from out import wrap
#        wrap()
#    except Exception as e:
#        pytest.fail(f'Unexpected MyError: {e}')

#    try:
#        from out import *
#    except Exception as e:
#        logging.exception("my message")
