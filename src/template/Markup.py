import enum
from .Smile import Smile


class Markup(enum.Enum):
    Price = 'Прайс ' + Smile.Money.value
    Schedule = 'Расписание ' + Smile.Clock.value