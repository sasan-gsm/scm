# Generated by Django 4.2.11 on 2025-03-24 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("request", "0001_initial"),
        ("materials", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "order_number",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Order Number"
                    ),
                ),
                ("order_date", models.DateField(verbose_name="Order Date")),
                (
                    "expected_delivery",
                    models.DateField(
                        blank=True, null=True, verbose_name="Expected Delivery"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("sent", "Sent to Supplier"),
                            ("confirmed", "Confirmed by Supplier"),
                            ("partially_received", "Partially Received"),
                            ("fully_received", "Fully Received"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="draft",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                ("notes", models.TextField(blank=True, verbose_name="Notes")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_purchase_orders",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Created By",
                    ),
                ),
            ],
            options={
                "verbose_name": "Purchase Order",
                "verbose_name_plural": "Purchase Orders",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Name")),
                (
                    "code",
                    models.CharField(max_length=50, unique=True, verbose_name="Code"),
                ),
                (
                    "contact_person",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Contact Person"
                    ),
                ),
                (
                    "email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Email"),
                ),
                (
                    "phone",
                    models.CharField(blank=True, max_length=50, verbose_name="Phone"),
                ),
                ("address", models.TextField(blank=True, verbose_name="Address")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
            ],
            options={
                "verbose_name": "Supplier",
                "verbose_name_plural": "Suppliers",
            },
        ),
        migrations.CreateModel(
            name="PurchaseOrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "quantity",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Quantity"
                    ),
                ),
                (
                    "received_quantity",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Received Quantity",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="materials.material",
                        verbose_name="Material",
                    ),
                ),
                (
                    "purchase_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="procurement.purchaseorder",
                        verbose_name="Purchase Order",
                    ),
                ),
                (
                    "request_item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="purchase_order_items",
                        to="request.requestitem",
                        verbose_name="Request Item",
                    ),
                ),
            ],
            options={
                "verbose_name": "Purchase Order Item",
                "verbose_name_plural": "Purchase Order Items",
            },
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="purchase_orders",
                to="procurement.supplier",
                verbose_name="Supplier",
            ),
        ),
    ]
