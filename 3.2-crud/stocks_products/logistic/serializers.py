from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']
        # depth = 1


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']
        # depth = 1
    # настройте сериализатор для склада

    def create(self, validated_data):
        print('Validated_data:', validated_data)
        positions = validated_data.pop('positions')
        # for position in validated_data.pop('positions'):
        #     print('position:', position)
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            stock_product = StockProduct(
                stock=stock,
                product=position.get('product'),
                quantity=position.get('quantity'),
                price=position.get('price')
            )
            stock_product.save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        print(validated_data)
        positions = validated_data.pop('positions')
        print(positions)
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for position in positions:
            product = StockProduct.objects.filter(stock=stock.id,
                                                  product=position.get('product').id)
            product.update(quantity=position.get('quantity'),
                           price=position.get('price'))
        return stock
