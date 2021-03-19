from django.db import models
from django.conf import settings


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="사용자"
    )
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, verbose_name="상품"
    )
    quantity = models.IntegerField(verbose_name="수량")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="주문날짜")

    def __str__(self):
        return str(self.user) + " " + str(self.product)

    class Meta:
        db_table = "shop_order"
        verbose_name = "주문"
        verbose_name_plural = "주문"
