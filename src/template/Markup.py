import enum
from .Smile import Smile


class Markup(enum.Enum):
    Price = 'Прайс ' + Smile.Money.value
    Schedule = 'Расписание ' + Smile.Clock.value
    Yes = 'Да' + Smile.Yes.value 
    No = 'Нет' + Smile.No.value
    Add = 'Добавить' + Smile.Add.value
    Delete = 'Удалить' + Smile.Delete.value
    Edit = 'Редактировать' + Smile.Edit.value
    View = 'Просмотреть' + Smile.View.value