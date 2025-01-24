from pydantic import BaseModel, EmailStr, Field,  field_validator, ValidationInfo

class Address(BaseModel):
    city: str = Field(..., min_length=2, description='City name (min 2 char)')
    street: str = Field(..., min_length=3, description='Street name (min 3 char)')
    house: int = Field(..., gt=0, description='House number')

class User(BaseModel):
    name: str = Field(..., min_length=2, pattern=r'^[A-Za-z\s]+$' ,description='User name, min 2 char')
    age: int = Field(..., ge=0, le=120, description='User age (between 0 and 120)')
    email: EmailStr
    is_employed: bool = Field(default=False, description='user\'s employment status', alias='employed')
    address: Address

    @field_validator('is_employed')
    def validate_age(cls, is_employed, values):
        age = values.data['age']
        print(is_employed, age)
        if not is_employed:
            return is_employed
        if is_employed and 65 > age > 18:
            return is_employed
        raise ValueError('Age must be between 18 and 65 if employed')




    def __str__(self):
        return f'{self.name} {self.address.city} {self.address.street}'\


valid_data = '''
{
        "name": "John Doe",
        "age": 33,
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
    print(json_unpack(valid_data))

