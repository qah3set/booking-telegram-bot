import enum
from .Smile import Smile


class Markup(enum.Enum):
    Price = 'Прайс ' + Smile.Money.value
    Schedule = 'Расписание ' + Smile.Clock.value
    Yes = 'Да' + Smile.CheckMark.value 
    No = 'Нет' + Smile.Сross.value
    Add = 'Добавить' + Smile.Plus.value
    Delete = 'Удалить' + Smile.Trashcan.value
    Edit = 'Редактировать' + Smile.WritingHand.value
    View = 'Просмотреть' + Smile.Folder.value