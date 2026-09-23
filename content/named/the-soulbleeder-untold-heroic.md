---
title: The Soulbleeder (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: The Soulbleeder
level: '143'
difficulty: Heroic ^^^
zone: '[[Gerion: Dominion of Pain (Untold Heroic)]]'
location: Death's Draw {{waypoint 487.47, 0.53, 151.81}}
primary_damage: Disease, Cold
achievement_xp: true
added_in: Rage of Cthurath
categories:
- 'Gerion: Dominion of Pain (Untold Heroic) Named Monsters'
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: The Soulbleeder (Untold Heroic)
  url: https://eq2.fandom.com/wiki/The_Soulbleeder_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/The_Soulbleeder_(Untold_Heroic)?action=history
  revision: 2028596
  revised: '2026-09-09T01:42:08Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes at stages (1-20/21-40/41+).

## Abilities

- **Penitence**
- An incurable trauma that deals crushing damage and drains power over time. It also procs Defensive Breach, which deals large amounts of magic damage.
- **Blood of the Drake (green)**
- A buff that increases flurry multiplier mitigation, flurry, and flurry multiplier. At 60 increments, it kills the entire party. (1-20) It increments by 1 per second while the pool of drake blood (east) remains unoccupied by a mage. (21+) It increments by 2 per second while the pool of drake blood (east) remains unoccupied by two people, including at least one mage.
- **Blood of the Dragon (red)**
- A buff that increases fervor and riposte chance. At 60 increments, it kills the entire party. (1-20) It increments by 1 per second while the pool of dragon blood (center) remains unoccupied by a fighter.  (21+) It increments by 2 per second while the pool of dragon blood (center) remains unoccupied by two people, including at least one fighter.
- **Blood of the Wyvern (blue)**
- A buff that increases ability doublecast avoidance and melee multiplier, and it dispels hostile effects instantly and every 3 seconds.At 60 increments, it kills the entire party. (1-20) It increments by 1 per second while the pool of wyvern blood (west) remains unoccupied by a priest.  (21+) It increments by 2 per second while the pool of wyvern blood (west) remains unoccupied by two people, including at least one priest.
- **Wing Buffet**
- A knockback that hits all players in front of The Soulbleeder. It turns to face a random party member when it starts to cast this spell. This attack also resets the reuse timer for Cure Curse.
- **Fiery Breath**
- A curable elemental that inflicts increasing heat damage over time, and disarms primary, secondary, and ranged slots of the target.
- **Drakerot**
- A curable curse that inflicts disease damage over time (if mage) and increasing disease damage over time (if not mage). It also increases the range of most abilities. Priests additionally have line-of-sight requirements removed.
- **Dragonrot**
- A curable curse that inflicts disease damage over time (if fighter) and increasing disease damage over time (if not fighter). It also increases the range of most abilities. Priests additionally have line-of-sight requirements removed.
- **Wyvernrot**
- A curable curse that inflicts disease damage over time (if priest) and increasing disease damage over time (if not priest). It also increases the range of most abilities. Priests additionally have line-of-sight requirements removed.
- **Clawed Grip**
- A cancelable detriment that inflicts 20% of max health instantly and 10% of max health every 2 seconds, plus an additional 10% of max health every tick, and it roots the target. This can be cancelled at any time.

## Strategy

At stages 1-40, the abilities Blood of the Drake/Dragon/Wyvern arrive one at a time. At stages 41+, the three abilities arrive two at a time, requiring players in two pools simultaneously.

Clicking on a claw next to a pool grants Clawed Grip, which deals damage in exchange for protection from the knockback.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Soulbleeder)faces (?&amp;lt;player&amp;gt;\w+)&quot; SD=&quot;${player} has knockback&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Gerion**: Dominion of Pain [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "<player> has knockback" when The Soulbleeder starts casting Wing Buffet.
