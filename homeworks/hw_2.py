from pydantic import BaseModel, EmailStr, Field,  field_validator, ValidationInfo

class Address(BaseModel):
    city: str = Field(..., min_length=2, description='City name (min 2 char)')
    street: str = Field(..., min_length=3, description='Street name (min 3 char)')
    house: int = Field(..., gt=0, description='House number')

class User(BaseModel):
    name: str = Field(..., min_length=2, description='User name, min 2 char')
    age: int = Field(..., ge=0, le=120, description='User age (between 0 and 120)')
    email: EmailStr
    is_employed: bool = Field(default=False, description='user\'s employment status', alias='employed')
    address: Address


    @field_validator('age')
    def validate_age(cls, age, info: ValidationInfo):
        is_employed = info.data.get('is_employed', False)
        if is_employed and (age < 18 or age > 65):
            raise ValueError('Age must be between 18 and 65 if employed')
        return age


    @field_validator('name')
    def validate_name(cls, value):
        if value.replace(' ', '').isalpha():
            return value
        raise ValueError('Name must be char')

    def __str__(self):
        return f'{self.name} {self.address.city} {self.address.street}'\


valid_data = '''
{
        "name": "John Doe",
        "age": 70,
        "email": "john.doe@example.com",
        "employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house": 123
        }
    }

'''

invalid_data = '''
    "name": "John123",
    "age": 70,
    "email": "john.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "NY",
        "street": "5",
        "house_number": -1
    }
}

'''



def json_unpack(data_json):
    user = User.model_validate_json(data_json)
    return user.model_dump_json(indent=2)

if __name__ == '__main__':
    print(json_unpack(invalid_data))

