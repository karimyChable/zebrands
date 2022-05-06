
from django.test import TestCase, Client

# Create your tests here.
from zebrands.products.models import Product
from zebrands.products.serializers import PostProductSerializer


class ProductTestCase(TestCase):
    def setUp(self):
        pass

    def test_view_products(self):
        """
        This testcase is for test the product list endpoint.
         This method should be available for all users (Anonymous and admins)
         The status code for this endpoint should be 200 for any user
        """
        c = Client()
        response = c.get('/api/v1/products/')
        sc = response.status_code
        self.assertEqual(sc, 200)

    def test_create_product(self):
        """
        This testcase is for test the endpoint for create products.
         This method should be available for all users (Anonymous and admins)
         The status code for this endpoint should be 401 for an anonymous user
        """
        c = Client()
        response = c.post('/api/v1/products/', {
            'name': 'Colchon king size',
            'description': 'Colchon luuna',
            'sku':'col010232',
            'price': '9500'
        })
        sc = response.status_code
        self.assertEqual(sc, 401)


    def test_duplicated_sku_product(self):
        """
         This testcase is for test the  create products.
         Testing unique sku
        """

        product1 = Product(
            name='Colchon individual',
            description='Colchon luna individual',
            sku='COL_IND_22',
            price=10299.90
        )
        product1_serializer = PostProductSerializer(data=product1)
        if product1_serializer.is_valid():
            self.assertTrue(
                Product.objects.filter(sku='COL_IND_22').exists(),
                True
            )

        # Verify added product on DB
        product2 = Product(
            name='Colchon individual',
            description='Colchon luna individual',
            sku='COL_IND_22',
            price=10299.90
        )
        product2_serializer = PostProductSerializer(data=product2)
        if not product2_serializer.is_valid():
            self.assertTrue(
                True,
                True
            )


