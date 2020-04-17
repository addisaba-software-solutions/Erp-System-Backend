from rest_framework import serializers
from .models import *


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = claimModel
        fields = "__all__"
        depth = 2


class RoleSerializer(serializers.ModelSerializer):
    role_levels = ClaimSerializer(many=True, read_only=True,)

    class Meta:
        model = RoleModel
        fields = "__all__"


class EmployeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeModel
        fields = "__all__"
        depth = 1


class DepartmentSerializer(serializers.ModelSerializer):

    department_roles = RoleSerializer(many=True, read_only=True,)
    department_employes = EmployeReadSerializer(many=True, read_only=True,)

    class Meta:
        model = DepartmentModel
        fields = (
            "departmentId",
            "departmentName",
            "department_roles",
            "department_employes",
        )
        depth = 1


class EmployeSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    department = serializers.CharField()
    level = serializers.CharField()
    roles = serializers.CharField()

    def validate_email(self, val):

        """
        Validates user data.
        """
        if EmployeModel.objects.filter(email=val).exists():
            raise serializers.ValidationError("This email already exists")

        return val

    def validate_department(self, val):
        """
        Validates user data.
        """
        if not DepartmentModel.objects.filter(departmentId=val).exists():
            raise serializers.ValidationError("This department not exist")
        return val

    def validate_level(self, val):
        """
        Validates user data.
        """
        if not claimModel.objects.filter(levelId=val).exists():
            raise serializers.ValidationError("This claim not exist")
        return val

    def validate_roles(self, val):
        """
        Validates user data.
        """
        if not RoleModel.objects.filter(roleId=val).exists():
            raise serializers.ValidationError("This role not exist")
        return val

    class Meta:
        model = EmployeModel
        fields = "__all__"


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatagoryModel
        fields = "__all__"


class InventoryItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItemModel
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ["itemName", "quantity", "InventoryItem"]


class OrderSerializer(serializers.ModelSerializer):
    item_order = ItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = [
            "orderid",
            "orderNumber",
            "company",
            "orderName",
            "salesPerson",
            "description",
            "orderDate",
            "shipmentAddress",
            "item_order",
        ]

    def create(self, validated_data):
        print("the item is nokskfhkjdfshk")
        items_data = validated_data.pop("item_order")
        print(items_data)
        print("the destructed items from the dictinory")
        order = OrderModel.objects.create(**validated_data)

        for item_data in items_data:
            ItemModel.objects.create(order=order, **item_data)
        return order


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = "__all__"


class ShipmentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentScheduleModel
        fields = "__all__"


class SivItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = sivModel
        fields = "__all__"


class SivSerializer(serializers.ModelSerializer):
    siv_item = SivItemListSerializer

    class Meta:
        model = sivModel
        fields = ["sivDate", "warehouseName", "approve", "siv_item"]


class InvoiceItemLineSivSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLineItemModel
        fields = "__all__"


class InvoiceItemSerializer(serializers.ModelSerializer):
    invoice_item = InvoiceItemLineSivSerializer(many=True)

    class Meta:
        model = InvoiceModel
        fields = ["salesPerson", "subTotal", "Total", "Tax", "date", "invoice_item"]
