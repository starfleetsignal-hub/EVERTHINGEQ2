---
title: Combat Mechanics
type: page
aliases:
- Auto attack
- Auto-attack
categories:
- User Guides
source:
  title: Combat Mechanics
  url: https://eq2.fandom.com/wiki/Combat_Mechanics
  history: https://eq2.fandom.com/wiki/Combat_Mechanics?action=history
  revision: 911658
  revised: '2018-11-05T03:47:16Z'
  license: CC BY-SA 3.0
---

EQ2 takes a common approach to combat, whether your character is a spellcaster or not.  You can always auto-attack to inflict melee damage, but most of your effectiveness comes from pressing buttons to cast spells or perform combat arts.

Generally, battles in EQ2 are decided in 30 seconds or so.  You should spend most of that time pressing buttons to perform abilities.  Your enemies will also be casting spells or combat arts against you - generally once every 6 seconds or so.

## Health and Power

You have two main resources to manage: Health and Power.  They are represented by the green and blue bars next to your character's name.
![](images/Health_power.jpg)
Managing these two resources is quite straight-forward:

- You lose health each time an enemy damages you.  If you run out of Health, then you die.
- You use Power to cast spells or perform combat arts.  If you run out of Power, then you can't use any of your abilities - all you can do is auto-attack.

Your opponent's health and power are displayed in two places: in your Target Window, and also above their head.  You can judge how the battle is unfolding by comparing your opponent's health against your own.

### Regenerating

*Main Article: [[Food and drink]]
Health and Power regenerate automatically - slowly while in combat, quickly when not in combat.  It is not necessary to sit or stand still to regenerate.  Your food and drink directly affect the rate that your health and power regenerate, when not in combat.  If you get hungry or thirsty, then your regeneration rate becomes very slow!

- It's also possible to buy health and power totems that function essentially like food, letting you regenerate much faster outside of combat.  Totems stack with food and drink.

### Healing

Your character might have spells or combat arts that will restore health.  The priest classes ([[Channeler]], [[Cleric|Clerics]], [[Druid|Druids]], and [[Shaman|Shamans]]) are specialized for healing.  For the healing classes, healing is an integral part of combat.  If your class can heal, then you'll probably need to heal during most battles.  An easier fight may require no heals or only a single cast of a heal spell, while a larger battle may require many heals or multiple heal spells running simultaneously.

Some monsters have healing capabilities, and those enemies will heal themselves and their allies during battle, although not as aggressively as a player would.

There are four kinds of heals in EQ2, and each healing class specializes in one type more than the other three:

- **Instant heals:** these restore a portion of health instantly. All Priest classes receive these spells, but Clerics get superior versions.
- **Heal over time:** these restore a smaller amount of health every few seconds until the spell expires. Druids specialize in these.
- **Reactive heals:** these have a chance of healing every time the recipient is damaged. Clerics specialize in these.
- **Wards:** these will absorb all damage taken up to a certain total. Shamans specialize in these.
  - *Note: Wards don't absorb all damage at higher levels, there is a chance that it bleeds through. Stacking different wards reduces this bleed through*
- **Interception:** these will take % of the damage and hit the Contruct instead. Channelers specialize in these.

If multiple different heals are cast on a player they take effect in the following way:

1. "Stoneskin" - Damage get's absorbed 100% by the stoneskin => no need to heal any damage
1. Interception
1. Wards from Shaman
1. Ward from Channeler (- level 32 Siphoned protection)
1. reactive heals
1. Instand heals / Heals over time

### Restoring Power

A few classes have the ability to restore power when their power is low.  For example:

- The enchanter and troubador classes can steal power from their enemies and share it with their group. (However, this won't prevent the enemy from performing his most dangerous abilities.)
- The necromancer can convert his own health into power.  For this class, both health and power are resources that can be interchanged as needed.

## Combat Mode

EQ2 has the concept of a "Combat Mode", and the gameplay changes slightly while you're in it.

### Entering Combat Mode

You'll enter combat mode whenever you perform an aggressive action against another creature - either auto-attack or a spell or combat art.  When you're in combat mode, a small "crossed swords" icon shows beside your character's name.  Being in combat has a few consequences to your character:

- Run speed enhancements are disabled.
- Regeneration of health/power is minimal.
- Other players are limited in how they can assist you.

### Leaving Combat Mode

Normally, once in combat mode you're stuck in combat mode, until the enemy is dead or has given up chasing you.  Alternatively, you can choose to leave combat mode at any time by *breaking the encounter*.  To do this, click the "Yell for Help" button that was placed on your hotkey bar, or type /yell.

When you break the encounter, you gain the benefits of being out of combat - namely run speed, regeneration, and assistance from others - but you also forfeit any rewards for beating the encounter.  That means no loot, no quest updates, and no experience.  Your enemy won't stop attacking, though - you'll still have to finish the fight or escape from it!

## The Elements of Battle

![](images/Target_ring.jpg)

### Auto-Attack

EQ2 has auto-attack for both types of physical attack: melee and range.  These can be assigned to hotkeys from the Knowledge->Abilities window, or directly bound to keys.

- To start melee auto-attacking, click the melee attack icon on your hotkey bar, or double-click your enemy, or press the ` (grave accent) key on your keyboard (upper left on QWERTY keyboards).
- To start range auto-attacking, click the range attack icon on your hotkey bar, or press shift and then grave accent (~, tilde).

The attack icons and the ` key act as toggles, so press them a second time to stop attacking.

**Note:** If you use an aggressive combat art, your auto-attack will also turn on (if it's not already on).

### Combat Bubbles

As you and your enemy attack each other, damage is reported above each combatant's head - orange for damage that you inflict, red for damage that's inflicted upon you.  If other players are involved in the fight, their damage is in gray.  These floating damage numbers are called "Combat Bubbles" in EQ2.

- Physical damage is listed in normal text.
- Non-physical damage is listed in **outlined text**.
- Critical hits are listed in **extra-large text**.

### Critical Hits

Each attack and heal has a small chance of being a critical hit.  A critical hit is guaranteed to be at least (your maximum normal hit+1)+33%+Crit bonus.

- You can find out the crit bonus multiplier by taking the % and dividing by 100 EX: 5,000%/100=50x
- You can do critical hits with 0% crit chance although its very small chance.
- You can improve how frequently you get critical hits by finding equipment that has an "Crit Chance" modifier, or you might be able to buy AA Abilities that improve your critical hit rate.
- 100% crit chance is 100% crit chance
- having more then 100% critchance increases the chance of legendary, fabled of mythical crits

### Damage Over Time

Damage over time (in short: DoT) attacks are attacks which typically deal instant damage, then deal additional damage every few seconds for a certain length of time.

- Often, the first hit of a DoT attack is the most powerful one, followed by slightly smaller amounts of damage every few seconds
- DoT attacks do slow, but continuous damage. This can be an advantage in long fights, where the long duration of many DoTs results in high damage
- Some DoTs cause their damage very slowly, others can do so very quickly
- Enemy DoTs will be shown in your "Detrimental Spell Effects" Window, they can be cured by classes posessing the required cure abilities

### Daze, Stuns and Stifles

Daze, Stun and Stifle are three detrimental effects that work alike on all creatures.

- Daze prevents the target from doing normal attacks, but not from using spells or combat arts
- Stuns will prevent you from moving, attacking and using any combat arts or spells.
  - Stuns usually have a very short duration, typically under five seconds. Common durations are between one and two seconds.
- Stifles prevent the target from using any spells or combat arts, but will not prevent movement or regular attacks.
  - If a mob is dazed and stifled they can't attack in any way or form, but they can move.

## Death

![Choosing a revive location.](images/Death.jpg)
When your health drops below zero, you die.  (Rarely, you might fall unconscious first, but recovery is unlikely.)  When you die, your view remains where you died, and you're given a list of revive locations to choose from.  The revive location is a safe spot, but might be far away.  Alternatively, another character could revive you at the location of your death.  Characters who can revive you are priest classes and a couple of others.

Regardless of which way you revive, you will have to face the consequences of death:

1. Resurrection sickness afflicts you for a couple of minutes, which reduces your effectiveness in combat.  It's a good idea to avoid combat until the sickness has passed.
1. Your equipment becomes 10% closer to being unusable.  You can address this by asking a Mender NPC to repair your equipment, or using a repair kit.
1. You receive an experience debt.  This shows up as a small red line on your XP bar, which you will have to earn at a reduced rate. Note this does not apply to PvP servers, as XP debt has been removed from them.

EQ2 does not have "corpse runs" or "debt buyback" as seen in other games.  You revive alive and breathing, with all of your equipment.  There is no reason to re-visit the location of your death. Note again, on a PvP server you may drop items in a chest after you are killed by another player, and anyone of opposing alignment, or yourself may loot this chest.

## Heroic Opportunities

*Main Article: [[Heroic Opportunities]]*
Heroic Opportunities are combinations of spells that produce a bonus effect during combat.  The bonus effect can be a buff on yourself, or a harmful effect on your enemies.  They can make a difference in battle, especially if you're struggling, so it pays to learn how to use them.

The sequence to complete a Heroic Opportunity goes like this:
<table align="center">
<tr align="center">
<th width="15%">1. Use your Starter Ability</th>
<th width="15%">2. Finish the Starter Chain</th>
<th width="15%">3. Finish the Combat Wheel</th>
</tr>
<tr align="center" valign="top">
<td>![](images/Ho_starter_ability_mage.jpg)</td>
<td>![](images/Ho_starter_chain.jpg)</td>
<td>![](images/Ho_wheel_duo.jpg)</td>
</tr>
</table>
Let's discuss each of these steps:

1. **Starter Ability:** You trigger Heroic Opportunities manually using a starter ability that you receive at level 5: [[Lucky Break]] for Scout archetype classes, [[Fighting Chance]] for Fighter archetype classes, [[Arcane Augur]] for Mage archetype classes and [[Divine Providence]] for Priest archetype classes.
1. **Starter Chain:** When you or your group friend uses their starter ability, you'll see the "Starter Chain" graphic appear on the right-hand side of your screen.  The flashing symbols show you the possible spells or combat arts that can produce a Heroic Opportunity.  There's no time limit on completing the starter chain, but if you cast a spell that doesn't satisfy the symbols, then the opportunity is lost.
1. **Combat Wheel:** Once the Starter Chain has been completed, the main Heroic Opportunity combat wheel appears.  The name of the bonus effect is shown below the wheel (which has been chosen randomly based on the Starter Chain that was completed).  To get the bonus effect, your group must cast spells or combat arts to match the symbols shown around the wheel.  You have 10 seconds to do this before the Heroic Opportunity expires; a circular bar graph shows you how much time remains.  Once all of the required symbols have been satisfied, the bonus effect takes place.

When you perform a Heroic Opportunity by yourself, you get a minor bonus effect.  When a group of players work together to perform a more complicated Heroic Opportunity, the bonus effect is more significant.  Completing Heroic Opportunities in groups requires a lot of attention but produces dramatic results.  For a discussion on group Heroic Opportunities, see the guide on [[Groups#Group Heroic Opportunities|Groups]].

## Fighting with a Pet

*Main Article: Pets*
Certain classes get pets that can assist them in combat.  Pets add another dimension to combat, and provide you with benefits as well as headaches.  With practice, you'll learn how best to utilize your pet.

### Controllable Pets

![A conjurer with her pet](images/Conjurer_mage_pet.jpg)
If your class gets a controllable pet, then you will summon it using a spell or AA ability.  Typically it takes a very long time to summon a pet, so you'll want to summon it in advance, before you start combat.

Some things about pets are worth noting here:

- Many classes have different types of pets, such as a melee tank or a ranged fighter. Be sure to pick the right pet for the situation. A melee pet will typically whitstand more damage than a ranged pet, for example.
- When your pet dies, all enemies that were previously attacking your pet will instantly start to attack you instead.
- A pet can safely wander around aggro mobs which would normally attack any player within a certain range. This can be used to your advantage.
- When fighting an encounter (several mobs acting as a group) with a melee pet, it helps to double-tap F1 to target your pet after sending it in for the attack. This has several benefits:
  - Your damage spells will always target the creature your pet currently is fighting, your beneficial spells will target your pet.
  - Your pet will automatically and quickly target the next enemy in the encounter after the first is dead. This way, you can keep casting without having to find out which enemy your pet currently is fighting.

### How to Control Your Pet

![The pet health bar and hotkeys](images/Pet_window.jpg)
When your pet is alive, the pet health bar and hotkeys are shown on your screen.  If you leave the controls alone, then your pet will automatically follow you around, and will automatically engage any creature that attacks you.  You can use the pet hotkeys to control what your pet is doing:

- Attack or Back Off
- Defend player and/or defend self
- Follow or Stay
- Dismiss the pet

Right-click the pet bar to open the Pet Options window.  Here you can control additional aspets of the pet's behavior:

- Whether the pet will attack from a distance, or close to melee
- Whether the pet will attempt to distract the enemy from you
- Specify a name for your pets

### Pet Stat Sharing

Controllable Pets share the following of their owner’s stats at a 1:1 ratio:

- Attributes
- Ability Modifier
- Potency
- Crit Bonus
- Crit Chance
- Toughness
- Doublecast
- Ability Casting Speed
- Ability Recovery Speed
- Spell Reuse Speed
- Ability Reuse Speed
- Resolve

Some stats do share but have different ratio to owner's stats at an ?:? ratio:

- DPS

### Dumbfire Pets

Dumbfire pets are "fire and forget" spells which last a limited time - usually 6 seconds or so.  They take the form of physical pets (usually several of them) which perform melee attacks on the targeted enemy.  You can't control these pets aside from choosing their initial target.  The dumbfire pets die when the spell expires or when their target dies.  The enemy can target these pets and kill them prematurely, and generally dumbfire pets succumb quickly to area attacks. (As of May 2013 they are immune to area attacks)

Use your dumbfire pets as if they were regular "damage over time" spells to augment your damage output.  They can distract your enemy from attacking you, and therefore can act as decoys, although they don't last long in this role.
