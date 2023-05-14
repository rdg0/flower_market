import django
import os

from typing import Dict, Type

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
django.setup()

from app.models import DealItem, User


def get_sales() -> Dict[Type[User], Dict[Type[User], int]]:
    """Получаем продажи продавцов в разрезе клиентов."""

    # чтобы отразить всех продавцов, в том числе без продаж,
    # сделаем отдельно выборку всех юзеров с ролью seller
    sellers = User.objects.filter(role='seller')

    result = {seller: {} for seller in sellers}
    items = DealItem.objects.all()
    for item in items:
        if item.deal.buyer not in result[item.deal.seller]:
            result[item.deal.seller][item.deal.buyer] = (
                item.price * item.quantity
            )
            continue
        result[item.deal.seller][item.deal.buyer] += (
            item.price * item.quantity
        )
    return result


def main() -> None:
    """Основная функция."""

    print(get_sales())


if __name__ == '__main__':
    main()
