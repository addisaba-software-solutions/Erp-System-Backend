from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
import json
from django.http import JsonResponse
from .models import (
    claimModel,
    RoleModel,
    EmployeModel,
    DepartmentModel,
    CatagoryModel,
    InventoryItemModel,
    CompanyModel,
    ItemModel,
    OrderModel,
    StatusModel,
    ShipmentScheduleModel,
    sivItemListModel,
    sivModel,
    InvoiceLineItemModel,
    InvoiceModel,
)
from .serializers import (
    EmployeSerializer,
    DepartmentSerializer,
    EmployeReadSerializer,
    RoleSerializer,
    ClaimSerializer,
    InventoryItemModelSerializer,
    ItemSerializer,
    CatagorySerializer,
    OrderSerializer,
    SivItemListSerializer,
    CompanySerializer,
    StatusSerializer,
    ShipmentScheduleSerializer,
    SivSerializer,
    InvoiceItemSerializer,
    InvoiceItemLineSerializer,
    
)

from rest_framework.views import APIView
from utilities.token import get_token, get_role
from manage_auth.permission import HrPermissionsAll
from django.db.models.signals import post_save
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_409_CONFLICT,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)

from utilities.token import get_token, get_role
from django.db.models.signals import post_save
from rest_framework.response import Response
from rest_framework import status



class EmployeRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeSerializer
    queryset = EmployeModel.objects.all()
    lookup_field = "employeId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [HrPermissionsAll]

    def get(self, request, employeId=None):
        return self.retrieve(request, employeId)

    def put(self, request, employeId=None):
        return self.update(request, employeId)

    def delete(self, request, employeId=None):
        obj = EmployeModel.objects.get(employeId=employeId)
        obj.delete()
        return Response({"success": "Delete"}, status=200)


class EmployeListAdd(generics.ListCreateAPIView):
   queryset = EmployeModel.objects.all()
   lookup_field = 'employeId'
   # permission_classes=[HrPermissionsAll]

   def get_serializer_class(self):
        if self.request.method == 'POST':
            serializer_class = EmployeSerializer           
        elif self.request.method == 'GET':
            serializer_class = EmployeReadSerializer        
        return serializer_class


   def post(self, request):
        serializer = EmployeSerializer(data=request.data,)
        if serializer.is_valid():
            department = DepartmentModel.objects.get(
                departmentId=request.data.get("department")
            )
            roles = RoleModel.objects.get(roleId=request.data.get("roles"))
            claim = claimModel.objects.get(levelId=request.data.get("level"))

            try:
                EmployeModel.objects.create(
                    department=department,
                    roles=roles,
                    level=claim,
                    firstName=request.data.get("firstName"),
                    lastName=request.data.get("lastName"),
                    email=request.data.get("email"),
                    hiredDate=request.data.get("hiredDate"),
                    telephone=request.data.get("telephone"),
                    birthDate=request.data.get("birthDate"),
                    termOfEmployment=request.data.get("termOfEmployment"),
                    country=request.data.get("country"),
                    region=request.data.get("region"),
                    city=request.data.get("city"),
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"errors": e.args}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )


class DepartmentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentModel.objects.all()
    lookup_field = "departmentId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[HrPermissionsAll]

    def get(self, request, departmentId=None):

        return self.retrieve(request, departmentId)

    def put(self, request, departmentId=None):

        return self.update(request, departmentId)

    def delete(self, request, departmentId=None):

        return self.destory(request, departmentId)


class DepartmentListAdd(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = DepartmentModel.objects.all()
    lookup_field = "departmentId"
    # permission_classes=[HrPermissionsAll]
   
    def post(self,request):
        serializer= DepartmentSerializer(
            data=request.data,
        ) 

        if serializer.is_valid():
            # role=Role.objects.get(roleId=request.data.get('role'))
            try:
                DepartmentModel.objects.create(
                    departmentName=serializer.validated_data["departmentName"],
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"errors": e.args}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )


class RoleRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoleSerializer
    lookup_field = "roleId"
    # permission_classes=[HrPermissionsAll]

    def get(self, request, roleId=None):

        return self.retrieve(request, roleId)

    def put(self, request, roleId=None):

        return self.update(request, roleId)

    def delete(self, request, roleId=None):

        return self.destroy(request, roleId)


class RoleListAdd(generics.ListCreateAPIView):
    serializer_class = RoleSerializer
    queryset = RoleModel.objects.all()
    lookup_field = "roleId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[HrPermissionsAll]

    def post(self, request):

        return self.create(request)


class LevelRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClaimSerializer
    queryset = claimModel.objects.all()
    lookup_field = "levelId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[HrPermissionsAll]

    def get(self, request, levelId=None):

        return self.retrieve(request, levelId)

    def put(self, request, levelId=None):

        return self.update(request, levelId)

    def delete(self, request, levelId=None):

        return self.destroy(request, levelId)


class LevelListAdd(generics.ListCreateAPIView):
    serializer_class = ClaimSerializer
    queryset = claimModel.objects.all()
    lookup_field = "levelId"

    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[HrPermissionsAll]

    def post(self, request):
        serializer = ClaimSerializer(data=request.data,)
        if serializer.is_valid():
            role = RoleModel.objects.get(roleId=request.data.get("role"))
            try:
                claimModel.objects.create(
                    level=request.data.get("level"), role=role,
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"errors": e.args}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        role = RoleModel.objects.get(roleId=request.data.get("role"))
        return self.create(request)


"""list of items in the order"""


class ItemRUD(
    generics.RetrieveUpdateDestroyAPIView
):  # Got some error in delete and view single item
    serializer_class = InventoryItemModelSerializer
    queryset = InventoryItemModel.objects.all()
    lookup_field = "InventoryItemId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, InventoryItemId=None):

        return self.retrieve(request, InventoryItemId)

    def put(self, request, InventoryItemId=None):

        return self.update(request, InventoryItemId)

    def delete(self, request, InventoryItemId=None):

        return self.destroy(request, InventoryItemId)


class ItemListAdd(generics.ListCreateAPIView):
    serializer_class = InventoryItemModelSerializer
    queryset = InventoryItemModel.objects.all()
    lookup_field = "InventoryItemId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


class OrderItemRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = ItemModel.objects.all()
    lookup_field = "itemName"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, itemName=None):

        return self.retrieve(request, itemName)

    def put(self, request, itemName=None):

        return self.update(request, itemName)

    def delete(self, request, itemName=None):

        return self.destroy(request, itemName)


class OrderItemListAdd(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = ItemModel.objects.all()
    lookup_field = "itemName"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


class CatagoryRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatagorySerializer
    queryset = CatagoryModel.objects.all()
    lookup_field = "catagoryId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, catagoryId=None):

        return self.retrieve(request, catagoryId)

    def put(self, request, catagoryId=None):

        return self.update(request, catagoryId)

    def delete(self, request, catagoryId=None):

        return self.destroy(request, catagoryId)


class CatagoryListAdd(generics.ListCreateAPIView):
    serializer_class = CatagorySerializer
    queryset = CatagoryModel.objects.all()
    lookup_field = "catagoryId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


class OrderRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    lookup_field = "orderNumber"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, orderNumber=None):

        return self.retrieve(request, orderNumber)

    def put(self, request, orderNumber=None):

        return self.update(request, orderNumber)

    def delete(self, request, orderNumber=None):

        return self.destroy(request, orderNumber)


"""item order which have list of items in one order"""


class OrderListAdd(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    lookup_field = "orderNumber"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    

    def get(self, request):

        return self.list(request)

    def post(self, request):
        # Call checkAvailability when the request arrives
        available = checkAvailability(request.data)
        if available[0]:
            serializer = OrderSerializer(data=request.data,)
            if serializer.is_valid(raise_exception=True):
                order = serializer.save()
                items = ItemModel.objects.filter(order_id=order)
                warehouseName = ""
                for item in items:
                    itemId = item.InventoryItem_id
                    warehouseName = InventoryItemModel.objects.values_list(
                        "warehouseName", flat=True
                    ).get(pk=itemId)
                siv = sivModel(order_id=order.orderNumber, warehouseName=warehouseName)
                siv.save()
                for item in items:
                    itemName = item.itemName
                    itemQuantity = item.quantity
                    item = {
                        "order_id": order,
                        "itemName": itemName,
                        "quantity": itemQuantity,
                    }
                    serializer = SivItemListSerializer(data=item)
                    if serializer.is_valid(raise_exception=True):
                        sivItemListModel.objects.create(
                            siv=siv, **serializer.validated_data
                        )
                for item in items:
                    itemName = item.itemName
                    for itemQty in available[1]:
        
                        if itemName == itemQty["itemName"]:
                            inventoryItem = InventoryItemModel.objects.get(
                                itemName=itemName
                            )
                            inventoryItem.quantity = itemQty["quantity"]
                            inventoryItem.save()

                return Response({"order success"}, status=HTTP_201_CREATED)
        else:
            return Response(
                {
                    "Error": "requested for item is not available at the moment",
                    "item": available[1],
                    
                    
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class CompanyRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyModel.objects.all()
    lookup_field = "companyId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, companyId=None):

        return self.retrieve(request, companyId)

    def put(self, request, companyId=None):

        return self.update(request, companyId)

    def delete(self, request, companyId=None):

        return self.destroy(request, companyId)


class CompanyListAdd(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = CompanyModel.objects.all()
    lookup_field = "companyId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


class StatusRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()
    lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, order=None):

        return self.retrieve(request, order)

    def put(self, request, order=None):

        return self.partial_update(request, order)

    def delete(self, request, order=None):

        return self.destroy(request, order)


class StatusListAdd(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()
    lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
    
    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)

class StatusOrderListAdd(generics.ListCreateAPIView):
    # serializer_class = OrderStatusSerializer
    # queryset = StatusModel.objects.all()
    # lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]
   

    def get(self, request):
        status = []
        for orderstatus in StatusModel.objects.all():
            status.append({
                "orderNumber":orderstatus.order.orderNumber,
                "orderName":orderstatus.order.orderName,
                "salesPerson":orderstatus.order.salesPerson,
                "description":orderstatus.order.description,
                "orderDate":str(orderstatus.order.orderDate),
                "company":str(orderstatus.order.company),
                "shipmentAddress":orderstatus.order.shipmentAddress,
                "status":orderstatus.status,
            })

        return JsonResponse(status, safe=False)



class ShipmentScheduleRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentScheduleSerializer
    queryset = ShipmentScheduleModel.objects.all()
    lookup_field = "shipmentId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, shipmentId=None):

        return self.retrieve(request, shipmentId)

    def put(self, request, shipmentId=None):

        return self.update(request, shipmentId)

    def delete(self, request, shipmentId=None):

        return self.destroy(request, shipmentId)


class ShipmentScheduleListAdd(generics.ListCreateAPIView):
    serializer_class = ShipmentScheduleSerializer
    queryset = ShipmentScheduleModel.objects.all()
    lookup_field = "shipmentId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


class SivListAdd(generics.ListAPIView):
    serializer_class = SivSerializer
    queryset = sivModel.objects.all()
    # lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)


class SIVRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SivSerializer
    queryset = sivModel.objects.all()
    lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, order=None):

        return self.retrieve(request, order)

    def put(self, request, order=None):
        siv = sivModel.objects.get(order=order)
        if request.data["sivStatus"] == "Approved":
            status = StatusModel.objects.get(order_id=siv.order_id)
            status.status = "Issued"
            status.save()

        return self.partial_update(request, order)

    # used to delete siv might be deleted depending on the requirements
    def delete(self, request, order=None):

        return self.destroy(request, order)


"""the end point to get invoice for order"""


class InvoiceListAdd(generics.ListAPIView):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceModel.objects.all()
    lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)


class InvoiceRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceModel.objects.all()
    lookup_field = "order"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, order=None):

        return self.retrieve(request, order)

    # used to delete siv might be deleted depending on the requirements
    def delete(self, request, order=None):

        return self.destroy(request, order)


def issue_invoice(sender, instance, **kwargs):
    if instance.status == "Delivered":
        items = ItemModel.objects.filter(order_id=instance.order_id)
        salesPerson = OrderModel.objects.values_list("salesPerson", flat=True).get(
            pk=instance.order_id
        )
        invoice_dict = {}
        i = 0
        subTotal = 0
        for item in items:
            invoice_item_dict = {}
            invoice_item_dict["itemName"] = item.itemName
            invoice_item_dict["quantity"] = item.quantity
            itemId = item.InventoryItem_id
            unitPrice = InventoryItemModel.objects.values_list(
                "retailPrice", flat=True
            ).get(pk=itemId)
            invoice_item_dict["unitPrice"] = unitPrice
            invoice_item_dict["amount"] = unitPrice * item.quantity
            invoice_dict[i] = invoice_item_dict
            i = i + 1

        for i in invoice_dict:
            ammount = invoice_dict[i]["amount"]
            subTotal = subTotal + ammount
        tax = subTotal * 0.15
        total = subTotal + tax
        invoice = InvoiceModel(
            order_id=instance.order_id,
            Total=total,
            subTotal=subTotal,
            Tax=tax,
            salesPerson=salesPerson,
        )
        invoice.save()
        for item in items:
            itemName = item.itemName
            itemQuantity = item.quantity
            itemId = item.InventoryItem_id
            unitPrice = InventoryItemModel.objects.values_list(
                "retailPrice", flat=True
            ).get(pk=itemId)
            invoicedata = {
                "itemName": itemName,
                "quantity": itemQuantity,
                "unitPrice": unitPrice,
            }
            serializer = InvoiceItemLineSerializer(data=invoicedata)
            if serializer.is_valid(raise_exception=True):
                InvoiceLineItemModel.objects.create(
                    invoice=invoice, **serializer.validated_data
                )

        status = StatusModel.objects.get(order_id=instance.order_id)
        status.status = "Invoiced"
        status.save()


def updateStatus(sender, instance, **kwargs):
    """update the status to created"""
    status = StatusModel(status="Created", order_id=instance.orderNumber)
    status.save()


def updateDeliveryStatus(sender, instance, **kwargs):
    """update the status to created"""
    status = StatusModel.objects.get(order_id=instance.order_id)
    status.status = "Delivery Scheduled"
    status.save()


# update the order status to created after a data is inseted to the ordermodel
post_save.connect(updateStatus, sender=OrderModel)
post_save.connect(updateDeliveryStatus, sender=ShipmentScheduleModel)


# signal to track if siv is approved and invoice should be generated
post_save.connect(issue_invoice, sender=StatusModel)

# checkes items availability
def checkAvailability(data):
    
    items = data["item_order"]
    updatedItemQuantity = []

    for item in items:
       
        InventoryItemId = item["InventoryItem"]
        orderedItemQuantity = item["quantity"]

        if item["InventoryItem"]=="":
            return  (
                False,
                {"itemName": "Please select an item!", "available":"It is not a valid input"}),

        orderedItemName =  InventoryItemModel.objects.values_list( "itemName", flat=True).get(InventoryItemId=InventoryItemId)
        availableQuantity = InventoryItemModel.objects.values_list(
            "quantity", flat=True
        ).get(pk=InventoryItemId)
       
        if int(availableQuantity) < int(orderedItemQuantity):
            # this should return the item name and the available item quantity for this itemname
            return (
                False,
                {"itemName": orderedItemName, "available": availableQuantity},
            )
    
        newItemQuantity = int(availableQuantity) - int(orderedItemQuantity)
        updatedQuantity = {"itemName": orderedItemName, "quantity": newItemQuantity}
        
        updatedQuantity_copy = updatedQuantity.copy()
        updatedItemQuantity.append(updatedQuantity_copy)
    return (True, updatedItemQuantity)
