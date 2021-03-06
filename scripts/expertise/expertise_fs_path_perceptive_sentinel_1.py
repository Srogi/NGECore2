import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.addSkill('expertise_fs_path_perceptive_sentinel_1')

	actor.addSkillMod('expertise_stance_perceptive_sentinel', 1)
	actor.addSkillMod('expertise_stance_perceptive_sentinel_pvp', 1)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'force_sensitive_1a':
		return

	actor.removeSkill('expertise_fs_path_perceptive_sentinel_1')

	actor.removeSkillMod('expertise_stance_perceptive_sentinel', 1)
	actor.removeSkillMod('expertise_stance_perceptive_sentinel_pvp', 1)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return
