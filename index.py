# 🌠 Cosmic Sanctuary System: Combines Facility Management and Celestial Beings
class CosmicSanctuary:
    def __init__(self, name, sector, energy_core):
        self.name = name
        self.sector = sector
        self.energy_core = energy_core
        self.residents = []

    def activate_shields(self):
        print(f"🛡️ {self.name} activating {self.energy_core}-powered dimensional shields")

    def maintain(self):
        print(f"⚙️ Performing routine maintenance in {self.sector} sector")

    def add_resident(self, entity):
        self.residents.append(entity)
        print(f"✨ {entity.name} joined {self.name} sanctuary")

class NebulaNursery(CosmicSanctuary):
    def __init__(self, nebula_type):
        super().__init__(
            name=f"{nebula_type} Nebula Nursery",
            sector="Stellar Nursery Gamma",
            energy_core="Protostar"
        )
        self.nebula_phase = "Forming"
        self._stellar_material = 5000  # Encapsulated property

    def cultivate_stars(self):
        print(f"🌟 Cultivating new stars in {self.name}")
        self._stellar_material -= 100

    def maintain(self):  # Polymorphic override
        super().maintain()
        print("🔭 Calibrating star-formation sensors")

class CelestialEntity:
    def __init__(self, name, constellation):
        self.name = name
        self.constellation = constellation

    def move(self):
        raise NotImplementedError("Movement pattern undefined")

class SolarDrake(CelestialEntity):
    def move(self):
        print(f"🔥 {self.name} rides solar winds with flaming wings")

class VoidManta(CelestialEntity):
    def move(self):
        print(f"🌑 {self.name} undulates through dark matter fields")

class QuantumPhoenix(CelestialEntity):
    def __init__(self, name, constellation, rebirth_count=0):
        super().__init__(name, constellation)
        self.rebirth_cycle = rebirth_count

    def move(self):
        print(f"🌀 {self.name} phase-shifts through quantum foam")
        self.rebirth_cycle += 1

# 🌌 Demonstration
if __name__ == "__main__":
    print("=== Cosmic Sanctuary Initialization ===")
    orion_nursery = NebulaNursery("Orion")
    orion_nursery.activate_shields()
    
    celestial_beings = [
        SolarDrake("Ignarius", "Draco"),
        VoidManta("Nyxara", "Ursa Major"),
        QuantumPhoenix("Pyralis", "Ara", 42)
    ]

    for entity in celestial_beings:
        orion_nursery.add_resident(entity)
    
    print("\n=== Celestial Movement Patterns ===")
    for entity in celestial_beings:
        entity.move()
    
    print("\n=== Sanctuary Maintenance ===")
    orion_nursery.cultivate_stars()
    orion_nursery.maintain()