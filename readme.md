# Tinys SRD

This is a Python library for accessing data from the SRD. It provides access to information about ability scores, equipment, and other game elements.

## Usage

Here's an example of how to use the library:

```py
from tinys_srd import AbilityScores, Equipment

# Print the entries for ability scores
print(AbilityScores.entries)

# Print the attributes for equipment
print(Equipment.attributes)

# Print the strength ability score
print(AbilityScores.str)

# Print the damage for a battleaxe
print(Equipment.battleaxe.damage)
```

The library provides access to the following data:

AbilityScores,
Alignments,
Backgrounds,
Classes,
Conditions,
DamageTypes,
EquipmentCategories,
Equipment,
Feats,
Features,
Languages,
Levels,
MagicItems,
MagicSchools,
Monsters,
Proficiencies,
Races,
RuleSections,
Rules,
Skills,
Spells,
Subclasses,
Subraces,
Traits,
WeaponProperti,

<https://github.com/5e-bits> is where all this data originates

## Adding New Classes

To add a new class to the dataset, you can use the `entry_builder` class. Here's an example of how to use it, based on the implementation in `AbilityScores.py`:

```py
from tinys_srd import entry_builder

# Create instances of entry_builder for each entry

entry1 = entry_builder.entry_builder(attr1=value1, attr2=value2, ...)
entry2 = entry_builder.entry_builder(attr1=value1, attr2=value2, ...)
```

NOTE: The `entry_builder` class is not meant to be used directly. It is used to build the classes in this library. You should not need to create instances of it yourself. It does nothing except create a class from a dictionary, you have more control making the class yourself.

### Extending a class

```py
from tinys_srd import entry_builder
from tinys_srd.AbilityScores import *

# Create a new class that extends the AbilityScores class
entry1 = entry_builder.entry_builder(attr1=value1, attr2=value2, ...)
entry2 = entry_builder.entry_builder(attr1=value1, attr2=value2, ...)
```

You then import your file instead of AbilityScores. Do note that Intellisense suggestions may not work with this method and it may be better to keep the two seperate.
