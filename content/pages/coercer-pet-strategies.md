---
title: Coercer Pet Strategies
type: page
aliases:
- Pet Strategies
categories:
- Coercer
source:
  title: Coercer Pet Strategies
  url: https://eq2.fandom.com/wiki/Coercer_Pet_Strategies
  history: https://eq2.fandom.com/wiki/Coercer_Pet_Strategies?action=history
  revision: 1789346
  revised: '2024-03-27T16:23:09Z'
  license: CC BY-SA 3.0
---

## Charm or Possess Essence

One of the decisions a higher level coercer (65+) will need to make is whether to use [[Possess Essence]] or [[Charm]].  A possessed essence has a huge amount of hit points for your level, and will never break.  A charmed pet, on the other hand, will have significantly fewer hit points but its damage capabilities are superior, particularly for mage pets.(As of my current testing this is not true, charmed pets are a hard form of cc or worthless)  Which one to take depends on your play style.  If you use the stunlock scenario discussed in the soloing heroics section, you can get more out of a mage pet nuking for high damage while you keep the mob locked down with your abilities.  However, it requires patience and timing to use.

On the other hand, you can make a possessed essence into a passable tank when you solo.  Buff him with [[Enraging Demeanor]] to increase his hate, [[Velocity]] for his DPS, and manage your aggro closely -- and he should be able to tank just about anything for you, even heroics, due to his large amount of HP.  When you get your mythical buff, [[Siren's Gift]], then you should have the concentration slots to put [[Peaceful Link]] on yourself, which will help your pet hold aggro even more.  If you're a raider, then acquiring [[Iilsaad's Control Rod]] will give your PE an amazing HP ward as well.   Finally, if you pull aggro from your PE tank, using [[Arcane Bewilderment]] or [[Amnesia]] will help him take it back.  Consider making a macro with [[Amnesia]] which first stops your autoattack (include the command "/auttoattack 0" first) so you don't accidentally hit the mob after casting it.

Apart from the uses above, the most significant difference between your charmed pet and a possessed essence are its roster of abilities.  A charmed pet will retain its original script and abilities, so some charmed pets are better than others and may come with unique powers.(As of my current testing this is false, a charmed pet simply auto attacks in a nerfed manner)  In contrast, a possessed essence will default to its class type and gain access to a limited selection of profession abilities (see below for more).

## Using Possess Essence

Part of the fun of [[Possess Essence]] is selecting a pet that has a class which complements your needs.  To tell what class you are getting, look at the buffs the mobs have on them when you target the mob.  For casters, the casting ring will often give you a clue - for example the defiler has a spider legs animation that is hard to miss.  Finally, you can always watch the combat log for ability names. See the next section for more details on PE classes.

Regardless of the possessed essence's class, its default attack is a melee strike called Confound, and it hits for Mental Damage. Thus, using your abilities with arcane debuffs (e.g., [[Obliterated Psyche]], [[Asylum]]) will help it do more damage.  Most of the PE's damage is supposed to come from Confound, so do not set your PE to ranged attacks if you can help it.

In addition to Confound, your essence will default to a limited script of abilities depending on its class.  This means it may not use abilities you saw it using a second earlier as a live mob, but instead it will gain a certain number of profession abilities and use them according to a probability script (with some skills coming up more often than others).  A possessed essence of any particular class appears to be the same as any other PE of that class, other than its different appearance.  The same is true for boss and named mobs, which will be eligible for possessing after GU58; they will not have special abilities and will be assigned a class just like any other PE. So, a PE berserker that is a tiny fish (FYI, you can posses marine pets and they travel on land!) is the same as a berserker that is a towering Sarnak.  Note that this is different than Charm, which tends to preserve the mob's original abilities and scripts (and which may vary per mob, even when they have the same class).

## Pet Stat Sharing

With the release of Destiny of Velious, controllable Pets, including Possess Essence and Charm, now share the following of their owner’s stats at a 1:1 ratio:

- Attributes
- Ability Modifier
- Potency
- Crit Bonus
- Crit Chance
- Toughness
- Spell Double Attack
- Ability Casting Speed
- Ability Recovery Speed
- Spell Reuse Speed
- Ability Reuse Speed

Since a coercer favors the INT stat, it may seem obvious that mage class pets gain the most from stat sharing.  However, a Possessed Essence appears to handle the same as a conjuror pet when it comes to stat conversion; that is, they all use INT, even when they would normally use a different stat due to their archetype.  So, just as conjuror scouts would use INT instead of AGI, a PE scout uses INT as well, and so on.

## Possess Essence Class Information

As mentioned above, your Possessed Essence will be assigned a class when it is created.  In general, the strength of its abilities depends on your level and the level of mastery for Possess Essence. However, its profession abilities (spells and combat arts) will do significantly less damage than its Confound autoattack (anywhere from 40-80% of the damage) and appear to be normalized across classes.  The exception to this rule are buffs and debuffs.  These seem to scale to your level and can be quite powerful.

Here is a list of the mob buffs and the classes they indicate, as well as some of the abilities you can expect to see them perform.  This list was created by watching PE actions in the combat log and with a parser, in a variety of encounters, zones, and health percentages (this research, as well as authoring for most of this article, was done by Gilli).

Additionally, AOE abilities are noted as follows: ^=Encounter AOE, ^^=Area AOE.  Debuffs to stats, mitigation, and combat or casting skill are noted with a super script d as follows: [[Ruin]]<sup>d</sup>.

### Fighter

All [[Fighter|Fighters]] - If an ability listed below has a threat component (e.g., [[Raging Blow]]) the threat amount does not actually happen.  However, if you cast [[Siren's Stare]] on a fighter pet you will sometimes see the mental damage show up attached to the name of a taunt, even though the taunt itself generates no threat.

- **[[Berserker]]**
  - Features: 2 blue AOEs, 1 encounter stun, 1 uncommon stun and an uncommon debuff to all melee skills.  Personal buff that procs for more attack speed and DPS.
  - Personal Buff: [[Berserk Rage]]
  - Common Skills: [[Rupture]], [[Rampage]]^^, [[Raging Blow]], [[Berserker Onslaught]]^^, [[Stunning Roar]]^ (a stun)
  - Uncommon Skills: [[Maul (Berserker)]]<sup>d</sup>, [[Demolish]] (a stun)
- **[[Bruiser]]**
  - Features: 2 blue AOEs.  Personal buff gives higher stats which translate to a DPS and avoidance boost.
  - Personal Buff: [[Bob and Weave (Bruiser)|Bob and Weave]]
  - Common Skills: [[Pummel]], [[Lightning Fists]], [[Beatdown]]^^, [[Savage Assault]]^^, [[One Hundred Hand Punch]]
  - Uncommon Skills: [[Merciless Stomp]], [[Slurred Insult]] (mental damage from [[Siren's Stare]] only)
- **[[Guardian]]**
  - Features: 1 blue AOE, common debuffs to DPS and melee weapons skills and an uncommon debuff to casting skills.  Personal buff sometimes roots the target.
  - Personal Buff is [[Hunker Down]]
  - Common Skills: [[Overpower]], [[Sever]]<sup>d</sup>, [[Ruin]]<sup>d</sup>, [[Assault]]^^
  - Uncommon Skills: [[Sentry Watch]], [[Concussion]]<sup>d</sup>, [[Provoke]] (mental damage from [[Siren's Stare]] only)
- **[[Monk]]**
  - Features: 1 blue AOE, common debuff to defense.  Personal buff gives higher stats which translate to a DPS and mitigation boost.
  - Personal Buff: [[Inner Calm]]
  - Common Skills: [[Waking Dragon]], [[Striking Cobra]]<sup>d</sup>, [[Crescent Strike]]^^, [[Lightning Palm]]
  - Uncommon Skills: [[Rising Dragon]], [[Silent Threat]] (mental damage from [[Siren's Stare]] only)
- **[[Paladin]]**
  - Features: Self-healer. 2 blue AOEs.  Personal buff procs for damage + stun.  Some abilities include small heals.
  - Personal Buff: [[Blessed Weapon]]
  - Common Skills: [[Faith Strike]], [[Holy Circle]]^^, [[Judgment]], [[Refusal of Atonement]]
  - Uncommon Skills: [[Consecrate]]^^, [[Clarion]] (mental damage from [[Siren's Stare]] only)
  - Personal Healing: At under 50% health, [[Holy Aid]] is common and [[Demonstration of Faith]] is uncommon.
- **[[Shadow Knight]]**
  - Features: 3 blue AOEs, common debuff to INT and STR. Personal buff procs for damage.  Some abilities include small lifetap heals.
  - Personal Buff: [[Innoruuk%27s Caress|Innoruk's Caress]]
  - Common Skills: [[Painbringer]], [[Siphon Strength]]<sup>d</sup>, [[Death Cloud]]^^, [[Shadow Coil]], [[Unending Agony]]^^, [[Unholy Blessing]]
  - Uncommon Skills: [[Tap Veins]]^^, [[Grave Sacrament]] (the old dumbfire pet version).
  - Special Note: Curiously, sometimes you'll see an Unholy Strike proc from the [[Unholy Hunger]] ability, though your PE will not appear to cast this buff. It also does a lot of damage!

### Mage

- All [[Summoner|Summoners]] - Summoners will summon a pet and you'll have two pets.  You can't give the helper pet commands.  This helper pet will only engage when its master is attacked, so if you send the master pet in first and he gets hit, his helper pet will aggro for more DPS.  The type of pet (mage, tank, scout) your master pet summons seems fixed at the time you grab the mob, and it won't necessarily be the pet you see walking around with the live mob.  Once you've gotten a PE of the mob, all other similar summoner mobs will summon that type of pet. However, if the helper pet dies a pet of another type might be summoned.  Not sure what causes the helper pet to reset, but if you come back another day and charm/possess the same summoner mob, his pet may be different.
  - **[[Conjuror]]**
    - Features: Helper pet. 1 blue AOE and 1 encounter AOE.
    - Personal Buff: Summoned Pet.  Usually you will see the pet standing right next to the Summoner.
    - Common Skills: [[Fiery Annihilation]], [[Ice Storm]]^, [[Earthquake]]^^
    - Uncommon Skills: [[Crystal Blast]]
  - **[[Necromancer]]**
    - Features: Helper pet. 1 blue AOE and 1 encounter AOE, 1 uncommon stun.  Some abilities return life to the caster. Once cast, [[Lich]] will persist, and it procs for damage + healing.
    - Personal Buff: Summoned Pet.  Usually you will see the pet standing right next to the Summoner.
    - Common Skills: [[Bloodcoil]], [[Bloodcloud]]^^ (a lifetap), [[Lich]], [[Pandemic]]^
    - Uncommon Skills: [[Soulrot]], [[Grasping Bones]] (a stun)
- **[[Coercer]]**
  - Features: Common debuff to all magical mitigation, common stun, and an uncommon stifle. Personal buff is a return damage shield.
  - Personal Buff: [[Peaceful Link]], but it returns damage when the Coercer is struck.
  - Common Skills: [[Medusa Gaze]] (a stun), [[Brainshock]], [[Hemorrhage]], [[Obliterated Psyche]]<sup>d</sup>
  - Uncommon Skills: [[Silence]]
- **[[Illusionist]]**
  - Features: Common debuff to all melee and ranged skills, common stun and a common mezz.  Personal buff procs for extra damage on a hostile spell.
  - Personal Buff: [[Synergism]]
  - Common Skills: [[Ultraviolet Beam]], [[Paranoia]] (a stun), [[Entrance]] (a mezz), [[Dismay]]<sup>d</sup>
  - Uncommon Skills: [[Prismatic Chaos]]
  - Special Note: This version of [[Entrance]] also causes "change target" - so watch out in groups and duos!
- **[[Warlock]]**
  - Features: 1 blue AOE and 2 encounter AOEs. Debuffs noxious mitigation of a group.
  - Personal Buff: None.
  - Common Skills: [[Dissolve]], [[Cataclysm]]^^, [[Absolution (Warlock)]]^ ,[[Vacuum Field]]^<sup>d</sup>
  - Uncommon Skills: [[Dark Nebula]]^, [[Distortion]]
- **[[Wizard]]**
  - Features: 1 blue AOE and a common stun.
  - Personal Buff: None.
  - Common Skills: [[Solar Flare]], [[Incinerate]], [[Magma Chamber]] (a stun), [[Firestorm]]^^
  - Uncommon Skills: [[Iceshield]], [[Ice Comet]]

### Priest

All [[Priest|Priests]] - At under 50% life, a self-healing script will activate and priest PEs sometimes cast healing spells on themselves (but never on you, sadly). [[Coercive Healing]] can be used on priest PEs.

- **[[Defiler]]**
  - Features: Self-healer. Common debuff to all attributes (STR, WIS, etc.), DPS and noxious mitigation. Common and uncommon attack speed debuff.
  - Personal Buff: None.
  - Common Skills: [[Abomination]]<sup>d</sup>, [[Atrophy]]<sup>d</sup>, [[Imprecate]]<sup>d</sup>
  - Uncommon Skills: [[Fuliginous Whip]]<sup>d</sup>
  - Personal Healing: At under 50% life, [[Dire Balm]] is common and [[Sacrificial Restoration]] is uncommon.
  - Special Note: If the tooltip is correct, this version of [[Abomination]] is percentage based (e.g., reduces abilities by x%), making it quite powerful.
- **[[Fury]]**
  - Features: Self-healer. Common debuff to defense, and group debuffs all casting skills, focus, and aggression. Personal buff is a return damage shield.
  - Personal Buff: [[Thornskin]]
  - Common Skills: [[Death Swarm]]<sup>d</sup>, [[Maddening Swarm]]^<sup>d</sup>, [[Tempest]]
  - Uncommon Skills: [[Fae Fire]], [[Thunderbolt]]
  - Personal Healing: At under 50% life, [[Nature's Salve]] is common and [[Nature's Elixir]] is uncommon.
- **[[Inquisitor]]**
  - Features: Self-healer. Common debuff to all mitigation types, an additional common arcane debuff and an uncommon group debuff to all melee and ranged skills. Uncommon root.
  - Personal Buff: None.
  - Common Skills: [[Invocation]], [[Condemn]]<sup>d</sup>, [[Purifying Flames]]<sup>d</sup>, [[Repentance]]
  - Uncommon Skills: [[Incarcerate]], [[Forced Obedience]]<sup>d</sup>
  - Personal Healing: At under 50% life, [[Ministration]] is common and [[Fanatical Healing]] is uncommon.
- **[[Mystic]]**
  - Features: Self-healer. Common debuff to attack speed and to all melee skills, a group debuff to attack speed and an uncommon debuff to DPS. Basic nuke has short duration slow.
  - Personal Buff: None.
  - Common Skills: [[Velium Winds]], [[Haze]]<sup>d</sup>, [[Lethargy]]^<sup>d</sup>
  - Uncommon Skills: [[Lamenting Soul]]<sup>d</sup>, [[Plague]]
  - Personal Healing: At under 50% life [[Rejuvenation]] is common and [[Ritual Healing]] is uncommon.
- **[[Templar]]**
  - Features: Self-healer. Common debuff to all physical mitigation, a common stun, and an uncommon debuff to divine mitigation plus a small heal. Uncommon group buff vs. control effects.
  - Personal Buff: None.
  - Common Skills: [[Divine Smite]], [[Rebuke]]<sup>d</sup>, [[Awestruck]]
  - Uncommon Skills: [[Mark of Divinity]]<sup>d</sup>, [[Sanctuary]]
  - Personal Healing: At under 50% life [[Meliorate]] is common and [[Restoration]] is uncommon.
- **[[Warden]]**
  - Features: Self-healer. Common root and an uncommon group root. Personal buff is a return damage shield.
  - Personal Buff: [[Thorncoat]]
  - Common Skills: [[Dawnstrike]], [[Root]]
  - Uncommon Skills: [[Icefall]], [[Undergrowth]]^
  - Personal Healing: At under 50% life [[Sylvan Bloom]] is common and [[Nature's Embrace]] is uncommon.

### Scout

All [[Scout|Scouts]] - Can use abilities which require stealth (e.g., [[Massacre]]) whether or not they are actually invisible.  Positional abilities (e.g., [[Ranger's Blade]]) also work regardless of position.

- [[Predator|Predators]] and [[Rogue|Rogues]] - Have a poisoned weapon buff.  Rangers and Assassins will have a poison called "Hemotoxin" whereas Brigands and Swashbuckler have a poison called "Poison."  Even at a master level PE spell, the poison buff on the PE will be significantly weaker than the poison buff on the live mob.
  - **[[Assassin]]**
    - Features: 2 blue AOEs, a common debuff to defense and physical mitigation and an uncommon stifle. Common self buff to piercing, slashing and DPS. Personal buff procs for damage.
    - Personal Buff: Poisoned Weapon (Hemotoxin)
    - Common Skills: [[Quick Strike]], [[Eviscerate]], [[Stealth Assault]]^^, [[Massacre]]^^, [[Masked Strike]], [[Torture]]<sup>d</sup>, [[Deadly Focus]]
    - Uncommon Skills: [[Jugular Slice]] (a stifle)
  - **[[Brigand]]**
    - Features: Common debuffs to attack speed, all magical mitigation, defense and AGI. Uncommon root. Common self buff to attack speed. Personal buff procs for damage.
    - Personal Buff: Poisoned Weapon (Poison)
    - Common Skills: [[Mug]]<sup>d</sup>, [[Puncture]]<sup>d</sup>, [[Deceit]], [[Bum Rush]], [[Murderous Rake]]<sup>d</sup>
    - Uncommon Skills: [[Entangle]]
  - **[[Ranger]]**
    - Features: Has a wide variety of skills when attacking at range, including 1 blue AOE and 1 encounter AOE. It cannot ranged autoattack however, so it just sits there until the probability script selects a ranged skill.  In melee, its personal buff procs for damage.
    - Personal Buff: Poisoned Weapon (Hemotoxin)
    - Common Skills: [[Sneak Attack]], [[Lightning Strike]] and [[Ranger's Blade]].
    - Uncommon Skills: [[Immobilizing Lunge]], occasional ranged skill at point-blank range (see below)
    - Ranged Skills: [[Searing Shot]], [[Natural Selection]]^^, [[Storm of Arrows]]^, [[Triple Shot]], [[Miracle Shot]] and [[Snaring Shot]]
  - **[[Swashbuckler]]**
    - Features: 1 blue AOE. Common debuffs to defense and WIS, physical mitigation and DPS. Personal buff procs for damage.
    - Personal Buff: Poisoned Weapon (Poison)
    - Common abilities: [[Double Cross]]<sup>d</sup>, [[Inspired Daring]], [[Kidney Stab]]<sup>d</sup>, [[Flash of Steel]]<sup>d</sup>, and [[Lucky Gambit]]^^.
    - Uncommon abilities: None observed yet.

![Dirge Songs buff provided by a possessed essence at level 86.](images/Dirge_Songs_2.jpg)
![Troubador Songs buff provided by a possessed essence at level 90.](images/Troubador_Songs.jpg)

- All [[Bard|Bards]] - Provide the group with the buff "Bard Songs."  This is an extremely powerful buff that combines several bard buffs into one, and which scales with your level. Note that this buff is often invisible until you actually possess the mob.
  - **[[Dirge]]**
    - Features: Powerful group buff. 1 uncommon encounter AOE, a common debuff to DPS and a common group debuff to STR and AGI. Several abilities lifetap heal.
    - Personal Buff: "Dirge Songs," which provides increased STA, AGI, DPS, Parry, and a proc for damage on combat hit to the group.
    - Common Skills:[[Luda's Nefarious Wail]], [[Disheartening Descant]]^<sup>d</sup>, [[Thuri's Doleful Thrust]] (a lifetap), [[Daro's Dull Blade]]<sup>d</sup>
    - Uncommon Skills: [[Howl of Death]] (a lifetap), [[Wail of the Banshee]]^, [[Garsin's Funeral March]]
  - **[[Troubador]]**
    - Features: Powerful group buff. 2 encounter AOEs. Common debuff to all magical mitigation and common group debuff to WIS.
    - Personal Buff: "Troubador Songs," which provides increased STR, STA, Attack Speed, Defense, and a proc for damage on a combat spell to the group.
    - Common Skills: [[Sandra's Deafening Strike]], [[Chaos Anthem]]^<sup>d</sup>, [[Perfect Shrill]], [[Dancing Blade]]<sup>d</sup>
    - Uncommon Skills: [[Lullaby]], [[Painful Lamentations]]^

**Key:** ^=Encounter AOE, ^^=Area AOE. Debuffs to stats, mitigation, and combat or casting skill are noted with a super script d as follows: Ruin<sup>d</sup>.

## Summary of Strategies for Possess Essence

Above all, have fun with your pet.  If possible, get the class you want in a cool-looking body.

### General PE Advice

- Most of your PEs damage will come a mix of combat arts/spells and autoattack, depending on the class you possess.
  - Make sure your PE is set to melee attack.  If you set your PE to ranged only it will not use its melee autoattack.
  - PE melee damage is melee damage, so melee debuffs will increase its damage, or DPS mod/attack speed buffs.
  - Direct damage profession abilities (e.g., [[Solar Flare]]) hit for around 75%-150% of the melee autoattack.
  - However, most buffs and debuffs scale generously with your level.  For example, a level 80 PE warlock using [[Vacuum Field]] decreases noxious mitigation to the encounter well over 1,000 points. Also, stat boosting profession buffs on the PE (e.g., [[Inner Calm]]) are immense.
- Note that many classes will use proximity-based AOE attacks, indicated above by ^^ (for example [[Consecrate]]^^).  If you ae in danger of unwanted pulls then consider a different class of PE.
- Which PE class is the best?  This opinion based.  Want damage?  Get a sorcerer.  Want debuffs?  Get a scout.  Want utility?  Get an enchanter.  Try them and figure out what works best for you.

### Class-Specific PE advice

- All classes will use a few of their class based abilities while possessed.  Some NPCs are more reliable than others.
- If you are soloing and want the most DPS, a conjuror, wizard, or warlock PE is great.  Sorcerers and summoners like to use AOE attacks, too, which can help you with groups.
- PEs with debuffs already covered by your party classes are less effective.  If your party inquisitor already casts [[Condemn]] frequently, it won't stack when your PE casts it.
- Otherwise, try and match debuffs to where they will do the most good.  For example, a warlock's [[Vacuum Field]] will help other classes relying on noxious damage, such as necromancers, shadowknights, defilers and mystics.  Alternately, an inquisitor's [[Condemn]] will reduce mitigation vs. all damage types, though it will be about half as powerful as [[Vacuum Field]].

## Soloing Heroics

Easiest method to soloing heroics is to charm a caster pet, root, then mezz the enemy, as soon as mezz refreshes attack with pet, as long as they start casting toss out your mezz, your mezz should land just after your pets nuke hits, back pet off as soon as they finish casting. Keep a close eye on pet, if they start to rush in back them off fast. As long as your timing is good on keeping your victim mezzed and rooted you should be able to take down almost any mob without ever getting hit.
For caster enemies you should expect your pet or you to get hit, you can toss in stifles to keep this to minimum but it is going to happen.

In order to bring victims out from roaming areas I like to root the mob and run to where I want to fight them, then cancel root and start tapping mezz until they get into range, its a fairly safe way of getting a mob to an open area where you can do your thing.

An alternate method is a little trickier and requires more timing but can be a lot quicker. First thing to do is get a priest pet, preferably at least 2 levels higher than the heroic you are fighting, next send your pet into battle, let them take a hit or two then start cycling your stuns, should buy you at least 10 seconds of no damage, throw out your wee little nuke and daze, if you have room use your AOE stun as well, as soon as your stuns run out and pet is low on health back him off and mezz the heroic, you can either wait for your pet to regen on its own now or do the pet attack/pet back off method to get it to throw a heal on itself as long as it is under 40% health. As soon as your pet is healed up send it back in and repeat as needed.

Using these two methods I have taken down some good heroics though I have always made it a point to fight a heroic lower level than me with a pet higher level than me, the first method has definitly proven to be safer, especially when a pet breaks charm, I have time to deal with it, the second method is a lot riskier but can be significantly faster if done right. These are not the only methods so try some alternates out and have fun.

Debuffing is also an important technique for fighting heroics. Use the [[Obliterated Psyche]] line of debuffs to increase your pet's damage. Cast it after mezzing the mob.

If you are not an Erudite with Aura Sense, then I would strongly suggest getting a pair of [[Thaumatoscopic Goggles]]. These will enable you to see which mobs are casters etc. when in an unfamiliar zone. (The goggles are currently described as head slot leather armor, but that's incorrect, the item is actually cloth armor).

## See Also

- [[Coercer Pets]]
