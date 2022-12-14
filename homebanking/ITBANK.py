# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


""" class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.FloatField(blank=True, null=True)
    new_balance = models.FloatField(blank=True, null=True)
    old_iban = models.CharField(blank=True, null=True)
    new_iban = models.CharField(blank=True, null=True)
    old_type = models.TextField(blank=True, null=True)
    new_type = models.TextField(blank=True, null=True)
    user_action = models.CharField(blank=True, null=True)
    create_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta' """


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    customer_direccion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    type_account_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'


""" class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    calle = models.TextField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = 'direccion' """


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()
    employee_direccion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


""" class MarcaTarjeta(models.Model):
    brand_card_id = models.AutoField(primary_key=True)
    brand_card_name = models.TextField()
    card = models.ForeignKey('Tarjeta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'marca_tarjeta' """


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=True)
    num_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


""" class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal' """


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.IntegerField()
    card_expire = models.IntegerField()
    card_expire_date = models.IntegerField()
    card_cvv = models.IntegerField()
    card_type = models.TextField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'


""" class TipoCliente(models.Model):
    customer_type_id = models.AutoField(primary_key=True)
    customer_type_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cliente' """

""" class TipoCuenta(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    account_type_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta' """
