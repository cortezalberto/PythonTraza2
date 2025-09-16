from typing import TypeVar, Generic, List, Optional
from paprika import data

T = TypeVar('T')

@data
class Entity(Generic[T]):
    id: Optional[int] = None

class InMemoryRepository(Generic[T]):
    def __init__(self):
        self.data: dict[int, T] = {}
        self._id_counter: int = 0

    def save(self, entity: T) -> T:
        self._id_counter += 1
        entity.id = self._id_counter  # Direct assignment
        self.data[self._id_counter] = entity
        return entity

    def find_by_id(self, id: int) -> Optional[T]:
        return self.data.get(id)

    def find_all(self) -> List[T]:
        return list(self.data.values())

    def update(self, id: int, updated_entity: T) -> Optional[T]:
        if id not in self.data:
            return None
        updated_entity.id = id  # Direct assignment
        self.data[id] = updated_entity
        return updated_entity

    def delete(self, id: int) -> Optional[T]:
        if id in self.data:
            return self.data.pop(id)
        return None

    def find_by_field(self, field_name: str, value) -> List[T]:
        return [entity for entity in self.data.values() if getattr(entity, field_name, None) == value]







from typing import Optional, List
from paprika import data  # Supuesto de que exista un decorador 'data' en Paprika

# Definición de una entidad usando @data de Paprika
@data
class MyEntity:
    id: Optional[int] = None
    name: str
    value: int

def main():
    # Crear un repositorio para MyEntity
    repo = InMemoryRepository[MyEntity]()

    # Crear algunas entidades
    entity1 = MyEntity(name="Entity1", value=100)
    entity2 = MyEntity(name="Entity2", value=200)

    # Guardar las entidades en el repositorio
    saved_entity1 = repo.save(entity1)
    saved_entity2 = repo.save(entity2)

    # Buscar por ID
    print("Find by ID 1:", repo.find_by_id(1))
    print("Find by ID 2:", repo.find_by_id(2))

    # Seleccionar todas las entidades
    print("All Entities:", repo.find_all())

    # Actualizar una entidad
    updated_entity1 = MyEntity(id=1, name="Entity1 Updated", value=150)
    repo.update(1, updated_entity1)
    print("Updated Entity 1:", repo.find_by_id(1))

    # Buscar por campo
    print("Find by name 'Entity2':", repo.find_by_field('name', 'Entity2'))

    # Eliminar una entidad
    repo.delete(2)
    print("All Entities after deletion:", repo.find_all())

if __name__ == "__main__":
    main()