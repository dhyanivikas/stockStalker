import org.pydev.dhyaniv.constants.constants as constants
from playsound import playsound as ps

import requests


def playMSFTAlert():
    ps(constants.MSFTALERTPATH)
    