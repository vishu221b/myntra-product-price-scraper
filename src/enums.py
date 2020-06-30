"""Created by Vishal Dogra on 30-06-2020"""

from enum import Enum
from . import constants


class EndpointMap(Enum):
    # all the views must be added in constants and then here as a variable and in the Endpoints MAP
    HEADPHONES = constants.HEADPHONES
    HOME_DECOR = constants.HOME_DECOR
    BOYS_T_SHIRT = constants.BOYS_T_SHIRT


ALL_ENDPOINTS_MAP = {
    1: EndpointMap.HEADPHONES,
    2: EndpointMap.HOME_DECOR,
    3: EndpointMap.BOYS_T_SHIRT
}
