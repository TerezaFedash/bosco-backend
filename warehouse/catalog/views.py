import random
from django.http import HttpResponse
from .models import Product


def products_list(request):
    products = Product.objects.all()

    rows = ""
    for p in products:
        rows += f"""
        <tr>
            <td>{p.id}</td>
            <td>{p.name}</td>
            <td>{p.material}</td>
            <td>{p.dimensions}</td>
            <td>{p.color}</td>
            <td>{p.price} грн</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Меблі - Склад</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; background-color: #f4f6f9; }}
            h1 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; background: #ffffff; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #dddddd; padding: 12px; text-align: left; }}
            th {{ background-color: #34495e; color: white; }}
            tr:nth-child(even) {{ background-color: #f9f9f9; }}
        </style>
    </head>
    <body>
        <h1>Список меблів на складі</h1>
        <p>Усього найменувань: <strong>{products.count()}</strong></p>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Назва</th>
                    <th>Матеріал</th>
                    <th>Розміри (ШxГxВ)</th>
                    <th>Колір</th>
                    <th>Ціна</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)


def replenish_stock(request, count: int):
    sample_names = ["Стіл обідній", "Стілець", "Диван", "Шафа-купе", "Ліжко двоспальне", "Комод", "Крісло", "Тумба"]
    sample_materials = ["Дерево", "ДСП", "МДФ", "Метал", "Скло", "Тканина"]
    sample_colors = ["Білий", "Чорний", "Дуб сонома", "Венге", "Горіх", "Сірий"]

    new_items = []
    for _ in range(count):
        w = random.randint(40, 200)
        d = random.randint(40, 100)
        h = random.randint(40, 220)
        
        furniture = Product(
            name=f"{random.choice(sample_names)} {random.randint(100, 999)}",
            material=random.choice(sample_materials),
            dimensions=f"{w}x{d}x{h} см",
            color=random.choice(sample_colors),
            price=round(random.uniform(500.0, 15000.0), 2)
        )
        new_items.append(furniture)

    Product.objects.bulk_create(new_items)

    return HttpResponse(
        f"<h2>Успішно додано {count} нових одиниць меблів!</h2>"
        f'<p><a href="/products">Повернутися до каталогу</a></p>'
    )