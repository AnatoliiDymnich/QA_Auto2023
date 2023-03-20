from modules.ui.page_objects.cropp import Cropp_shop
import pytest

@pytest.mark.ui
def test_item_add_to_cart():
    cropp_shop = Cropp_shop('beisbolka-0861s-00x')

    cropp_shop.go_to()

    cropp_shop.add_to_cart()

    assert cropp_shop.check_cart()

    cropp_shop.close()
