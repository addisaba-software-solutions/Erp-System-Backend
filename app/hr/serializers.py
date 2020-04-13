from rest_framework import serializers
from .models import EmployeModel,DepartmentModel,RoleModel,claimModel,ItemModel,CatagoryModel,OrderModel,CompanyModel,StatusModel,ShipmentScheduleModel, sivModel, InventoryItemModel

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeModel
        fields = '__all__' 
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DepartmentModel
        fields = '__all__' 

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoleModel
        fields = '__all__' 

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model=claimModel
        fields = '__all__'  
class EmployeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    level = ClaimSerializer()
    roles  = RoleSerializer()

    class Meta:
        model=EmployeModel
        fields = '__all__'         

      
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemModel
        fields = ('itemId', 'itemName', 'quantity', 'order')       

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CatagoryModel
        fields = '__all__'    

class InventoryItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryItemModel
        fields = '__all__'   

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model=OrderModel
        fields = ['orderName', 'salesPerson', 'orderNumber', 'description', 'orderDate', 'shipmentAddress', 'company', 'items' ]                   

    def create(self, validated_data):
        items = validated_data.pop('items')
        orderModel = OrderModel.objects.create(**validated_data)
        for item in items:
            ItemModel.objects.create(itemID=orderModel, **item)
        return orderModel

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyModel
        fields = '__all__'  

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatusModel
        fields = '__all__'          


class ShipmentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShipmentScheduleModel
        fields = '__all__' 

class SivSerializer(serializers.ModelSerializer):
    class Meta:
        model=sivModel
        fields = '__all__' 

        # def update(self, instance, validated_data):
        #     print("updating a single approve value")
        #     sivModel = sivModel.objects.get(pk=instance.id)
        #     sivModel.objects.filter(pk=instance.id)\
        #                     .update(**validated_data)
        #     return sivModel