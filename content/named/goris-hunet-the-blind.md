---
title: G'Oris Hunet the Blind
type: named
expansion: Rage of Cthurath
level: '143'
difficulty: Epic x4 ^^^
zone: '[[Zon Zobboz: Gaze of the Oglth (Raid)]]'
location: Blighted Shoal {{waypoint 426.00, 7.83, 738.32}}
primary_damage: Crushing
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- Tier 15 Epic x4 Named Monsters
- Tier 15 Named Monsters
- 'Zon Zobboz: Gaze of the Oglth (Raid) Named Monsters'
source:
  title: G'Oris Hunet the Blind
  url: https://eq2.fandom.com/wiki/G'Oris_Hunet_the_Blind
  history: https://eq2.fandom.com/wiki/G'Oris_Hunet_the_Blind?action=history
  revision: 1991872
  revised: '2026-03-27T01:03:52Z'
  license: CC BY-SA 3.0
---

G'Oris Hunet the Blind is a Tier 1 raid boss. He gains an additive advantage for each player below 12 in the raid and beyond a soft time limit of 60 minutes.

## Statistics

- Flurry Avoidance 250.0
- Ability Doublecast Avoidance 700.0
- Resolve 13,230.0

## Abilities

- **Watchful Eye**
- A buff that protects the caster from any targets that the curse Spotted by the Wandering Eye.
- **Spotted by the Wandering Eye**
- An incurable curse that reduces maximum health and power pools by 50% and debuffs offensive and defensive ability for 2 minutes. If the player dies while the curse is active and is revived, the curse reapplies with the full 2 minute duration.
- **Surging Flails**
- An incurable trauma that deals increasing physical and arcane damage to health and power over time.
- **Overbearing Influence I**
- An incurable detriment that causes power usage to also cost health based on the amount of power used.
- **Blind Flail**
- An incurable noxious that applies disease damage to health and power and blinds targets in front of G'Oris.
- **Flying Shard Attuned**
- A buff that increases outgoing damage for each player caught by the attack Flying Shards. This buff cannot be dispelled, but it does expire naturally.
- **Flying Shards**
- An incurable trauma that deals increasing physical damage over time and adds one increment to Flying Shard Attuned for each player it. The range of this effect is 22 meters.
- **Confusion Pulse**
- A curable arcane that dazes and roots targets within 25 meters and deals fast ticking increasing arcane damage and increases physical damage from all sources.
- **Arcane Burst I**
- A curable arcane that deals increasing magic damage to targets within 25 meters. This ability can be blocked.
- **Powerful Boom**
- A curable trauma that deals slashing damage over time and knocks the target back to all targets within 15 meters. Damage from this effect has 100% bleedthrough.
- **Barrage**
- An incurable curse that can only be blocked with [[Bulwark of Order]].

## Strategy

Throughout the fight, G'Oris summons [[The Wandering Eye]], a non-aggressive mob that wanders the island. The Eye has a large (visible) ring around itself; players standing within that ring receive the curse Spotted by the Wandering Eye.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;GOris)prepares himself to launch deadly shards&quot; SD=&quot;Joust 23&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "Joust 23" when G'Oris begins to cast Flying Shards.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;GOris)prepares to send his foes flying&quot; SD=&quot;Knock up&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Zon Zobboz**: Gaze of the Oglth [Raid]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "Knock up" when G'Oris begins to cast Powerful Boom.
