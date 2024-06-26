from . import entry_builder
entries = ['acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning', 'necrotic', 'piercing', 'poison', 'psychic', 'radiant', 'slashing', 'thunder']
attributes = ['index', 'name', 'desc', 'url']
acid = entry_builder.entry_builder(index = 'acid',name = 'Acid',desc = ["The corrosive spray of a black dragon's breath and the dissolving enzymes secreted by a black pudding deal acid damage."],url = '/api/damage-types/acid')
bludgeoning = entry_builder.entry_builder(index = 'bludgeoning',name = 'Bludgeoning',desc = ['Blunt force attacks, falling, constriction, and the like deal bludgeoning damage.'],url = '/api/damage-types/bludgeoning')
cold = entry_builder.entry_builder(index = 'cold',name = 'Cold',desc = ["The infernal chill radiating from an ice devil's spear and the frigid blast of a white dragon's breath deal cold damage."],url = '/api/damage-types/cold')
fire = entry_builder.entry_builder(index = 'fire',name = 'Fire',desc = ['Red dragons breathe fire, and many spells conjure flames to deal fire damage.'],url = '/api/damage-types/fire')
force = entry_builder.entry_builder(index = 'force',name = 'Force',desc = ['Force is pure magical energy focused into a damaging form. Most effects that deal force damage are spells, including magic missile and spiritual weapon.'],url = '/api/damage-types/force')
lightning = entry_builder.entry_builder(index = 'lightning',name = 'Lightning',desc = ["A lightning bolt spell and a blue dragon's breath deal lightning damage."],url = '/api/damage-types/lightning')
necrotic = entry_builder.entry_builder(index = 'necrotic',name = 'Necrotic',desc = ['Necrotic damage, dealt by certain undead and a spell such as chill touch, withers matter and even the soul.'],url = '/api/damage-types/necrotic')
piercing = entry_builder.entry_builder(index = 'piercing',name = 'Piercing',desc = ["Puncturing and impaling attacks, including spears and monsters' bites, deal piercing damage."],url = '/api/damage-types/piercing')
poison = entry_builder.entry_builder(index = 'poison',name = 'Poison',desc = ["Venomous stings and the toxic gas of a green dragon's breath deal poison damage."],url = '/api/damage-types/poison')
psychic = entry_builder.entry_builder(index = 'psychic',name = 'Psychic',desc = ['Mental abilities such as a psionic blast deal psychic damage.'],url = '/api/damage-types/psychic')
radiant = entry_builder.entry_builder(index = 'radiant',name = 'Radiant',desc = ["Radiant damage, dealt by a cleric's flame strike spell or an angel's smiting weapon, sears the flesh like fire and overloads the spirit with power."],url = '/api/damage-types/radiant')
slashing = entry_builder.entry_builder(index = 'slashing',name = 'Slashing',desc = ["Swords, axes, and monsters' claws deal slashing damage."],url = '/api/damage-types/slashing')
thunder = entry_builder.entry_builder(index = 'thunder',name = 'Thunder',desc = ['A concussive burst of sound, such as the effect of the thunderwave spell, deals thunder damage.'],url = '/api/damage-types/thunder')
