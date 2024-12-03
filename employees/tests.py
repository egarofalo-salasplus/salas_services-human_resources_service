from django.test import TestCase
from .models import Empleado, Empresa, Direccion


class EmployeeTestCase(TestCase):
    def setUp(self):
        # Crear una nueva dirección
        self.direccion = Direccion.objects.create(
            pais='España',
            region='Madrid',
            ciudad='Madrid',
            codigo_postal='28001',
            calle='Gran Vía',
            complemento='1º A'
        )

        # Crear una nueva empresa
        self.empresa = Empresa.objects.create(
            nombre='Mi Empresa S.A.',
            CIF='A12345678',
            direccion=self.direccion,
            telefono='912345678',
            email='contacto@miempresa.com'
        )

    def test_company_created(self):
        # Verificar que la empresa se haya creado correctamente
        self.assertEqual(Empresa.objects.count(), 1)
        self.assertEqual(self.empresa.nombre, 'Mi Empresa S.A.')
        self.assertEqual(self.empresa.CIF, 'A12345678')
        self.assertEqual(self.empresa.direccion, self.direccion)    

    def test_direction_created(self):
        # Verificar que la dirección se haya creado correctamente
        self.assertEqual(Direccion.objects.count(), 1)
        self.assertEqual(self.direccion.pais, 'España')
        self.assertEqual(self.direccion.calle, 'Gran Vía')

    def test_create_employee(self):
        """Test de modelo empleado
        """
        primer_nombre = "Empleado"
        segundo_nombre = ""
        primer_apellido = "Prueba"
        segundo_apellido = ""
        dni = "007"
        email = "eprueba@salas.plus"
        sexo = "Masculino"
        fecha_nacimiento = "1990-01-01"
        empresa = self.empresa
        direccion = self.direccion
        telefono = "555-5555"
        estado = None

        employee = Empleado.objects.create(primer_nombre=primer_nombre,
                                           segundo_nombre=segundo_nombre,
                                           segundo_apellido=segundo_apellido,
                                           dni=dni,
                                           email=email,
                                           sexo=sexo,
                                           fecha_nacimiento=fecha_nacimiento,
                                           empresa=empresa,
                                           direccion=direccion,
                                           telefono=telefono,
                                           estado=estado)
        self.assertEqual(employee.primer_nombre, primer_nombre)
        self.assertEqual(employee.email, email)
        employee.delete()
    
    def test_delete_all(self):
        self.empresa.delete()
        self.direccion.delete()
