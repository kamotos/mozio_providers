import uuid
import factory
from services_areas.test.factories import ServiceAreaFactory


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Sequence(lambda n: uuid.uuid4())
    username = factory.Sequence(lambda n: 'testuser{}'.format(n))
    password = factory.Faker('password', length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    name = factory.Faker('company')
    phone_number = factory.Faker('phone_number')
    is_active = True
    is_staff = False

    @factory.post_generation
    def services(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        extracted = extracted or (ServiceAreaFactory(provider=self) for i in range(0, 4))
        for service_area in extracted:
            self.servicearea_set.add(service_area)
