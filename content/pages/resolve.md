---
title: Resolve
type: page
categories:
- Stats
- User Guides
source:
  title: Resolve
  url: https://eq2.fandom.com/wiki/Resolve
  history: https://eq2.fandom.com/wiki/Resolve?action=history
  revision: 1953351
  revised: '2026-01-12T03:40:55Z'
  license: CC BY-SA 3.0
---

## Resolve Overview

In the middle of the [[Terrors of Thalumbra]] era (2015-2016), a new stat, "Resolve", was added to character sheets and level 100+ armors.

Resolve is not a traditional stat, in the way stats like Stamina, Resists, Crit rate, or Haste (or many... many... other stats) behave.

It was added to the game to ensure that players are running content while wearing the most recent/accessible equipment available to them through those various eras of game content, and not relying on (potentially) overpowered heroic or raid-tier equipment from older content to advance through newer content.  It allows the Devs to design newer content around ensuring that most everybody starts out new eras and content on a relatively even playing field at the beginning of each major expansion or game update.

## How Resolve works

Each piece of equipable 'stat' gear at level 100 or higher has an accompanying blue 'resolve' stat on it.  That stat starts at 10 on a single piece of Terrors of Thalumbra-era level 100 gear - and goes up from there, through the many many content updates and expansions all the way to the current max level (whatever that may be when you're reading this in the future). Each expansion or content update introduces increasingly difficult dungeons, contested zones, and raid content, gradually increasing that minimum resolve required for a character to effectively play at that new increased difficulty.

For every point of resolve a character is BELOW the enemy's minimum Resolve requirement, that charcater will both DO less damage to and TAKE more damage from the encounter.

Generally, the requirements for each new era of gameplay are such that the gear reward from the initial Quests and [Solo] dungeons will give individual players enough minimum resolve to then begin attempting [Heroic] content, which will then reward equipment to raise minimum resolve even further to start tackling [Raid] content of that same era.

### Example

Here's a visual to help better understand.  Lets use the [[Rage of Cthurath]] era as an example. *(The numbers will change for each new expansion and content update, but the principles will be the same)*
At its launch, Cthurath gear had resolve values of 600, 610, 620, and 630, as show in the images of the equipment examination. (You can see the 'blue' Resolve stat in each listing)
<gallery>
Resolve_Example_600.png|
Resolve_Example_610.png|
Resolve_Example_620.png|
Resolve_Example_630.png|
</gallery>
When fighting early tier enemies, such as for quests and [Solo] dungeons, they do not have a minimum Resolve requirement for combat; such as this enemy from a [Solo] dungeon.
![](images/Resolve_Example_EnemyA.png)

However; as the player advances into more and more difficult content, eventually the passive buffs that enemies have in that era also increase, such as from this example of a passive buff on the exact same enemy as the last picture, BUT located in a more difficult [Heroic] dungeon...

![](images/Resolve_Example_EnemyB2.png)

The Resolve requirements are the very first thing listed, as it's (usually) the most important thing to pay attention to. *(There's also several other passive buffs this more difficult enemy has acquired compared to it's less-dangerous companion in the easier dungeon.... but we're here to talk about Resolve)*

That 13,020 number is the key in this example.  It is the minimum required resolve each individual player will need to have in order to both hit for full damage AND not take extra damage from that enemy.  Resolve for each player is calculated as the total amount of resolve stat across the 21 total gear slots available to be worn.
Here is the actual "math" taken straight from the Dec 2024 patch notes:

Resolve damage scaling has been modified to scale up at an increased rate the more resolve the enemy encounter has vs the character's resolve. The formula for increased damage done to the character, increased bleedthrough on the character, decreased damage done to the encounter is:

ResolveDifference*  ( 1+ResolveDifference*  0.002 ).

Examples below.

- Being 10 points of resolve below the encounter would increase the encounters damage to the character, bleedthrough on the character, and reduce the damage the character does to the encounter by 12%.
- Being 20 points below the encounters resolve would increase the encounters damage to the character, bleedthrough on the character, and reduce the damage the character does to the encounter by 28%.
- Being 50 points below the encounters resolve would increase the encounters damage to the character by 100%, grants 100% bleedthrough on the character, and makes the encounter immune to damage by the player.
- Being 100 points below the encounters resolve would increase the encounters damage to the character by 300%, grants 100% bleedthrough on the character, and makes the encounter immune to damage by the player.

- The player's own total resolve stat is compared to the minimum Resolve stat of an enemy.
- Conversely, going ABOVE an enemy's minimum resolve does NOT give any extra benefit; as the stat is intended as a form of minimum gate-keeping, to ensure individual players are properly geared to a bare minimum before attempting more difficult content.  It's not a stat that's meant to be 'stacked' to gain an advantage, simply a minimum standard to meet.  Once a player reaches that minimum, they do not need to worry about it anymore, until they're ready to move on to even more advanced content, which likely bears an even higher minimum resolve requirement.
- There aren't adorns, mount equipment, familiars, or mercs that give you more of this stat, it is purely from worn equipment itself. *(There used to be spells that each class in a group would cast to add additional Resolve to the whole group's total, and since each class's buff didn't stack with itself, it was a way to encourage variety (and increased numbers) in groups and raids - but this buff effect was eventually removed from the game - now only raw gear provides the stat.)*
- Players can view their individual Resolve totals in the 'combat stats' section of the Character screen, as seen in this example.

![You can see here, this player happens to have exactly the required minimum resolve for the above example encounter.](images/Resolve_Example_13020.png)

Since there's 21 slots of equipment, and the minimum required resolve of this example encounter is 13,020... that means if a player has an *average* of 620 resolve across all their different slots, then it will add up to that minimum 13,020 - resulting in no penalties when engaging this enemy.  Each individual piece of gear does not need to be that 620 number, they can any combinations of 600, 610, 620, and 630 gear, so long as it adds up to that minimum 13,020 amount.  In the Cthurath-era, 600 was the default Tishan's/Handcrafted level, 610 items were generally from questing and overland named enemies, 620 items were from [Solo] dungeon bosses and Mastercrafted gear, and 630 items were from [Signature Solo] and [Heroic] missions and dungeons.  Again, while the numbers in each era will generally be different (higher as you progress!), the same basic principles apply; guiding players in a progression from Entry of expansion -> Questing/[Solo] -> [Heroic] -> (More difficult encounters) -> [Raid] -> more advanced [Raid].

## Reminders

Again, if a player is below the minimum Resolve, they will both DO less damage and TAKE more damage.  In this example from the Cthurath-era, gear comes in 10pt increments, so even a single piece of gear holding the total back from that minimum 13,020 will cause the player to do *at minimum* 12% less damage and take more damage... or more, if it's several 10pt increments below that minimum.  Each piece holding a player back from that minimum, adds up quickly and can easily result in a situation where a player is now doing 0% damage, but taking 100's of % of extra damage if they're not paying attention to difficulty, or assume they'll somehow get 'carried' by the rest of the party.

Also again, going *over* Resolve minimums gives no benefit to characters.  Players also do not need to worry about 'wasting' Resolve that is over the minimum, as the Resolve stat itself, while one of the 'blue' stats on gear, is not part of the itemization budget of particular pieces of gear.  Having more Resolve on a piece of gear does not 'take away' from other stats present - it's simply meant as quick visual reference to the relative strength of an individual piece of gear compared to the stats of the opponents they will be facing in that particular game-era.

Actual minimum encounter/gear resolve numbers will change from expansion to expansion, but the same principles apply.
