from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator


class Address(BaseModel):
    city: str
    state: str
    street: str
    building_number: str

class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    address: Address


class Admin(User):
    access_level: int



if __name__ == '__main__':
    json_str = '''
    {
    "name": "Bob",
    "age": 35,
    "email": "bob@example.com",
    "address": {
        "city": "Los Angeles",
        "state": "CA",
        "street": "Sunset Boulevard",
        "building_number": "456"
    },
    "access_level": 1
}
    
    '''
    user = Admin.model_validate_json(json_str, strict=True)
    print(user)


class Abc(BaseModel):
    in_stock: bool = Field(default=True, alias="available")


data = '''
{
"in_stock": false
}
'''
a = Abc.model_validate_json(data, strict=True)



class User(BaseModel):
    name: str
    email: str

    @field_validator('name')
    def name_validate(cls, value):
        if not value.isalpha():
            raise ValidationError("Name must be bukva")
        return value

    @field_validator('email')
    def email_validate(cls, value):
        value = value.split('.')
        if value[-1] == 'com':
            print(value[-1])
            return value
        else:
            raise ValidationError("Email must be end .com")

user = User(name="Bob", email="andrey.com")









