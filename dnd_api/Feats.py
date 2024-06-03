from . import entry_builder
entries = ['grappler']
attributes = ['index', 'name', 'prerequisites', 'desc', 'url']
grappler = entry_builder.entry_builder(index = 'grappler',name = 'Grappler',prerequisites = [{'ability_score': {'index': 'str', 'name': 'STR', 'url': '/api/ability-scores/str'}, 'minimum_score': 13}],desc = ['You’ve developed the Skills necessary to hold your own in close--quarters Grappling. You gain the following benefits:', '- You have advantage on Attack Rolls against a creature you are Grappling.', '- You can use your action to try to pin a creature Grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both Restrained until the grapple ends.'],url = '/api/feats/grappler')
