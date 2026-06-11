class MagicCreature:
    pass

def create_magic_creature() -> str:
    creature = MagicCreature()
    return str(type(creature))

result = create_magic_creature()
