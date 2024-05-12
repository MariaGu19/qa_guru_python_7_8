"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def copybook():
    return Product("pen", 50, "This is a book", 3000)


@pytest.fixture
def pen():
    return Product("copybook", 27, "This is a book", 500)


@pytest.fixture
def cart():
    cart = Cart()
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        equal_quantity = product.quantity
        assert product.check_quantity(equal_quantity), 'not correct with quantity equal product.quantity'

        less_quantity = product.quantity - 1
        assert product.check_quantity(less_quantity), 'not correct with quantity less than product.quantity'

        more_quantity = product.quantity + 1
        assert not product.check_quantity(more_quantity), 'not correct with quantity more than product.quantity'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        equal_quantity = product.quantity
        product.buy(equal_quantity)
        assert product.quantity == 0, 'failed with equal quantity'

        less_quantity = product.quantity - 1
        product.buy(less_quantity)
        assert product.quantity == 1, 'failed with less quantity'

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        more_quantity = product.quantity + 1
        with pytest.raises(ValueError):
            assert product.buy(more_quantity) is ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, pen, cart):
        cart.add_product(pen, quantity=5)
        assert cart.products[pen] == 5

        cart.add_product(pen, quantity=100)
        assert cart.products[pen] == 105

    def test_remove_product(self, product: Product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

        cart.clear()
        cart.add_product(product, 1)
        cart.remove_product(product, 5000)
        assert product not in cart.products

    def test_clear(self, product, copybook, pen, cart):
        cart.add_product(copybook, 150)
        cart.add_product(pen, 400)
        cart.clear()

        assert cart.products == {}

    def test_get_total_price(self, product, copybook, pen, cart):
        cart.clear()
        cart.add_product(product,1)
        cart.add_product(copybook, 2)
        cart.add_product(pen, 4)

        assert cart.get_total_price() == 300

    def test_buy(self, product, copybook, pen, cart):
        cart.clear()
        cart.add_product(product, 1)
        cart.add_product(copybook, 2)
        cart.add_product(pen, 4)
        cart.buy()

        assert cart.get_total_price() == float(300)
        assert product.quantity == 999
        assert pen.quantity == 996
        assert copybook == 2998

    def test_buy_more_then_stock(self, product, cart):
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError):
            cart.buy()




