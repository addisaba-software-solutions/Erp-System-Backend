from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
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
        return self.destroy(request, employeId)


class EmployeListAdd(generics.ListCreateAPIView):
    queryset = EmployeModel.objects.all()
    lookup_field = "employeId"
    # permission_classes=[HrPermissionsAll]

    def get_serializer_class(self):
        if self.request.method == "POST":
            serializer_class = EmployeSerializer

        elif self.request.method == "GET":
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

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data,)

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


class ItemRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InventoryItemModelSerializer
    queryset = InventoryItemModel.objects.all()
    lookup_field = "inventoryItemId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, itemId=None):

        return self.retrieve(request, itemId)

    def put(self, request, itemId=None):

        return self.update(request, itemId)

    def delete(self, request, itemId=None):

        return self.destroy(request, itemId)


class ItemListAdd(generics.ListCreateAPIView):
    serializer_class = InventoryItemModelSerializer
    queryset = InventoryItemModel.objects.all()
    lookup_field = "inventoryItemId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


class OrderItemRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = ItemModel.objects.all()
    lookup_field = "itemId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, itemId=None):

        return self.retrieve(request, itemId)

    def put(self, request, itemId=None):

        return self.update(request, itemId)

    def delete(self, request, itemId=None):

        return self.destroy(request, itemId)


class OrderItemListAdd(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = ItemModel.objects.all()
    lookup_field = "itemId"
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

        if checkAvailability(request.data):
            serializer = OrderSerializer(data=request.data,)
            print(serializer)
            print("orders kjhdfskjnhfdkj")
            if serializer.is_valid(raise_exception=True):
                print("in the validslkafj")
                order = serializer.save()
                print("serialiserksjgknhekdfjneak")
                items = ItemModel.objects.filter(order_id=order)
                print("the item is  " + str(items))
                warehouseName = ""
                for item in items:
                    itemId = item.InventoryItem_id
                    warehouseName = InventoryItemModel.objects.values_list(
                        "warehouseName", flat=True
                    ).get(pk=itemId)
                siv = sivModel(warehouseName=warehouseName)
                siv.save()
                for item in items:
                    itemName = item.itemName
                    itemQuantity = item.quantity
                    item = {"itemName": itemName, "quantity": itemQuantity}
                    serializer = SivItemListSerializer(data=item)
                    if serializer.is_valid(raise_exception=True):
                        sivItemListModel.objects.create(
                            siv=siv, **serializer.validated_data
                        )

                    print("the item name is" + str(itemName) + " " + str(itemQuantity))

                return Response({"order success"}, status=HTTP_201_CREATED)
        else:
            return Response(
                "requested item amount is not available at the moment",
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
    lookup_field = "id"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, id=None):

        return self.retrieve(request, id)

    def put(self, request, id=None):

        return self.update(request, id)

    def delete(self, request, id=None):

        return self.destroy(request, id)


class StatusListAdd(generics.ListCreateAPIView):
    serializer_class = StatusSerializer
    queryset = StatusModel.objects.all()
    lookup_field = "id"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)

    def post(self, request):

        return self.create(request)


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
    lookup_field = "sivId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)


class SIVRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SivSerializer
    queryset = sivModel.objects.all()
    lookup_field = "sivId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, sivId=None):

        return self.retrieve(request, sivId)

    def put(self, request, sivId=None):

        return self.partial_update(request, sivId)

    # used to delete siv might be deleted depending on the requirements
    def delete(self, request, sivId=None):

        return self.destroy(request, sivId)


"""the end point to get invoice for order"""


class InvoiceListAdd(generics.ListAPIView):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceModel.objects.all()
    lookup_field = "invoiceId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request):

        return self.list(request)


class InvoiceRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceModel.objects.all()
    lookup_field = "invoiceId"
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, invoiceId=None):

        return self.retrieve(request, invoiceId)

    # used to delete siv might be deleted depending on the requirements
    def delete(self, request, invoiceId=None):

        return self.destroy(request, invoiceId)


# called after a new order is inserted to database


def issue_siv_invoice(sender, instance, **kwargs):
    print("the the status is  ")
    if instance.status == "Created":
        print("the status is creaded generate siv")
        print(instance.order)
        warehouseName = "kazanchis"
        items = ItemModel.objects.filter(order_id=25)
        print("the items in the order are")
        # salesPerson = OrderModel.objects.values_list("salesPerson", flat=True).get(
        #     pk=instance.order
        # )
        invoice = InvoiceModel(Total=100, subTotal=100, Tax=10, salesPerson="kidus")
        invoice.save()
        subTotal = 0
        tax = 0
        total = 0
        for item in items:

            print(item.InventoryItem_id)
            print(item.quantity)
            itemName = item.itemName  # the item name
            itemQuantity = item.quantity  # the item quantity
            itemId = item.InventoryItem_id  # the item id in the inventory
            unitPrice = InventoryItemModel.objects.values_list(
                "retailPrice", flat=True
            ).get(pk=itemId)
            invoicedata = {
                "itemName": itemName,
                "quantity": itemQuantity,
                "unitPrice": unitPrice,
            }

            serializer = InvoiceItemLineSerializer(data=invoicedata)
            print("the serializer issssssssss")
            print(serializer)

            if serializer.is_valid(raise_exception=True):
                InvoiceLineItemModel.objects.create(
                    invoice=invoice, **serializer.validated_data
                )
            print("the item price is")
            print(unitPrice)
            subTotal = subTotal + unitPrice
            print("the total amount is")
            print(subTotal)
        tax = subTotal * 0.15
        print("the tax is ssssss")
        print(tax)
        total = subTotal + tax
        print("the sub total isssss")
        print(total)

        # siv = sivModel(warehouseName=warehouseName)
        # siv.save()
    if instance.status == "Delivered":
        print("the invoice should be generated now")
        salesPerson = OrderModel.objects.values_list("salesPerson", flat=True).get(
            pk=instance.order
        )
        print(salesPerson)
        items = ItemModel.objects.filter(order_id=instance.order)
        # for item in items:
        #     print(item.itemName)
        #     print(item.quantity)


def updateStatus(sender, instance, **kwargs):
    # "update the status to created"
    print("the item model is populated")
    print(instance)
    status = StatusModel(status="Created", order_id=instance.orderNumber)
    status.save()


# update the order status to created after a data is inseted to the ordermodel
post_save.connect(updateStatus, sender=OrderModel)


# signal to track if siv is approved and invoice should be generated
post_save.connect(issue_siv_invoice, sender=StatusModel)

# checkes items availability and update after order
def checkAvailability(data):
    items = data["item_order"]
    print("the tegern")
    print(items)
    for item in items:
        print("the iten name is")
        item_name = item["itemName"]
        print(item_name)
        item_qty = item["quantity"]
        print(item_qty)

        # availableQuantity = InventoryItemModel.objects.values_list(
        #     "quantity", flat=True
        # ).get(
        #     pk="computer"
        # )  # just for test pk should be replaced with item_name
        # print(availableQuantity)

        # if availableQuantity <= item_qty:
        #     newQ = int(item_qty) - int(availableQuantity)
        #     item = InventoryItemModel.objects.get(pk=item_name)
        #     item.quantity = str(newItemQuantity)
        #     item.save()
    return True
