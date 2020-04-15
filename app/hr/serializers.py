from rest_framework import serializers
from .models import *

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model=claimModel
        fields = '__all__'
        depth=2

        
class RoleSerializer(serializers.ModelSerializer):
    role_levels=ClaimSerializer(
        many=True,
        read_only=True,
     )
    class Meta:
        model=RoleModel
        fields = '__all__' 


   
class EmployeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeModel
        fields = '__all__' 
        depth=1          
class DepartmentSerializer(serializers.ModelSerializer):

    department_roles= RoleSerializer(
        many=True,
        read_only=True,
     )
    department_employes= EmployeReadSerializer(
        many=True,
        read_only=True,
     )
    
    class Meta:
        model=DepartmentModel
        fields = ('departmentName','department_roles','department_employes')  
        depth=1

  

  



class EmployeSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    department=serializers.CharField()
    level=serializers.CharField()
    roles=serializers.CharField()

    def validate_email(self, val):

        """
        Validates user data.
        """
        if EmployeModel.objects.filter(email=val).exists():
              raise serializers.ValidationError('This email already exists')

        return val
 

    def validate_department(self, val):
        """
        Validates user data.
        """
        if not DepartmentModel.objects.filter(departmentId=val).exists():
              raise serializers.ValidationError('This department not exist')
        return val    
   
    def validate_level(self, val):
        """
        Validates user data.
        """
        if not claimModel.objects.filter(levelId=val).exists():
              raise serializers.ValidationError('This claim not exist')
        return val  

    def validate_roles(self, val):
        """
        Validates user data.
        """
        if not RoleModel.objects.filter(roleId=val).exists():
              raise serializers.ValidationError('This role not exist')
        return val  
    class Meta:
        model=EmployeModel
        fields = '__all__' 
    


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CatagoryModel
        fields = '__all__' 
        depth=1    
      
class ItemSerializer(serializers.ModelSerializer):
    # catagory = CatagorySerializer()

    class Meta:
        model=ItemModel
        fields = '__all__'  
        depth=1   

   

class InventoryItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryItemModel
        fields = '__all__'
        depth=1       

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model=OrderModel
        fields = ['orderName', 'salesPerson', 'orderNumber', 'description', 'orderDate', 'shipmentAddress', 'company', 'items' ]  
        depth=1                     

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