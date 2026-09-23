---
title: The Arm of Lucan (Untold Heroic)
type: named
in_game_name: The Arm of Lucan
race: Animation
level: '143'
difficulty: Heroic ^^^
zone: '[[Gerion: Realm of Conquest (Untold Heroic)]]'
location: '{{waypoint -334.32, 0.95, 51.79}}'
primary_damage: Crushing, Magic
achievement_xp: true
added_in: LU131
categories:
- Animation
- 'Gerion: Realm of Conquest (Untold Heroic) Named Monsters'
- Heroic Named Monsters
- LU131 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: The Arm of Lucan (Untold Heroic)
  url: https://eq2.fandom.com/wiki/The_Arm_of_Lucan_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/The_Arm_of_Lucan_(Untold_Heroic)?action=history
  revision: 2022973
  revised: '2026-08-19T20:33:46Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes between stages (1-20/21+).

## Abilities

- **Force of Chaos**
- A buff that reduces all damage unless an enemy maintains Chaotic Presence.
- **The Reckoning Cometh**
- A buff with 20 increments that loses one increment per second. If dispelled by a class other than a mage, the caster is killed. When it reaches zero, The Arm of Lucan casts The Reckoning.
- **Elemental Aegis/Aether Barrier/Blight Shield/Earthen Wall**
- A buff that reflects hostile abilities of a specific type, increases combat mitigation, increases ability doublecast avoidance, and increases flurry avoidance. If all four siege breakers are present, the entire group is killed.
- **War Torn**
- An incurable elemental that inflicts heat damage over time, decreases power over time, and casts Defensive Breach, which deals magic damage.
- **Chaotic Presence**: 
- An incurable arcane that grants Chaotic Influence to the player and their allies. If the target moves too far from The Arm of Lucan, the spell evolves into the curse Chaotic Disturbance.
- **Chaotic Influence**
- A detriment that allows the target to bypass The Arm of Lucan's defenses.
- **Chaotic Disturbance**
- A curable curse that .
- **Downward Blow**
- An incurable noxious that inflicts poison damage over time and reduces the range and radius of most abilities. For non-fighter targets, it also makes the target fall down. It lands on a named target and all players within 10 meters of that target.
- **Battering Ram**
- A frontal attack that knocks players back.
- **Blast Furnace [21+]**
- An incurable elemental that decreases power over time, wounds health by 30%, and reduces fervor. If it lands on the same target twice, the target is killed.

## Strategy

The Arm of Lucan summons four types of siege breakers. The Arm reflects all hostile abilities matching the type of the active siege breaker.

- [[A Blighted Siege Breaker]] - resistant to noxious damage
- [[An Elemental Siege Breaker]] - resistant to elemental damage
- [[An Aether Siege Breaker]] - resistant to arcane damage
- [[An Earthen Siege Breaker]] - resistant to physical damage

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Arm)prepares for a frontal&quot; SD=&quot;frontal&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Realm of Conquest [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "frontal" when The Arm casts Battering Ram.
