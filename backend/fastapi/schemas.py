from pydantic import BaseModel


class PersonBase(BaseModel):
    name: str


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True


class ShowBase(BaseModel):
    title: str
    description: str
    show_type: str
    categories: str
    release_year: int
    director: list[Person]
    cast: list[Person]
    countries: str
    duration: str
    rating: str
    date_added: str


class ShowCreate(ShowBase):
    pass


class Show(ShowBase):
    id: int

    class Config:
        orm_mode = True

