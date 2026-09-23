---
title: Death Spark (Untold Heroic)
type: named
expansion: Rage of Cthurath
in_game_name: Death Spark
level: '143'
difficulty: Heroic ^^^
zone: '[[The Unknown: Sacrificial Pursuits (Untold Heroic)]]'
location: '{{waypoint -939.74, -20.76, 946.85}}'
primary_damage: Heat, Disease
achievement_xp: true
added_in: Rage of Cthurath
categories:
- Heroic Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monster needing race
- Named Monsters
- Rage of Cthurath Named Monsters
- 'The Unknown: Sacrificial Pursuits (Untold Heroic) Named Monsters'
- Tier 15 Heroic Named Monsters
- Tier 15 Named Monsters
source:
  title: Death Spark (Untold Heroic)
  url: https://eq2.fandom.com/wiki/Death_Spark_(Untold_Heroic)
  history: https://eq2.fandom.com/wiki/Death_Spark_(Untold_Heroic)?action=history
  revision: 2028523
  revised: '2026-09-08T20:56:26Z'
  license: CC BY-SA 3.0
---

Ability and strategy information changes between stages (1-20/21-40/41+).

## Abilities

- **Pungent Vapors**
- A buff that has a 10% chance to cast Miasmic Jolt when damaged. Miasmic Jolt inflicts disease damage over time and decreases power over time. It also interrupts the target if there is an ally within 5 meters of the target.
- **Sacrificial Lamb**
- An incurable trauma that deals slashing damage over time and decreases power over time. It also procs Defensive Breach, which deals significant magic damage.
- **Attention Attenuation**
- A buff that, when dispelled, drops the hate amount of Death Spark's most hated enemy to 1. The buff is immediately reapplied.
- **Glinting Contagion**
- A curable noxious that inflicts increasing disease damage over time and decreases power over time. It also stifles the target.
- **Disarming Brand**
- An incurable trauma that disarms the primary and secondary slots of the target. It also deals increasing crushing damage over time, decreases power over time, and decreases threat priority every tick. If the target is not standing within the red circle when [[Emblazoned soul spark]] dies, the target also dies, and the soul spark is revived. This detriment only lands on fighters.
- **Ire Radiation**
- An incurable arcane that wounds the target's health by 20%, reduces the target's fervor by 20%, and increases threat priority every tick. If the target is not standing within the yellow circle when [[Luminous soul spark]] ides, the target also dies, and the soul spark is revived. This detriment only lands on priests.
- **Null Vacuum**
- An incurable elemental that wounds the target's power by 50%, reduces the target's crit bonus by 10%, and increases threat priority every tick. If the target is not standing within the blue circle when [[Esoteric soul spark]] dies, the target also dies, and the spark is revived. This detriment only lands on mages.
- ****
- An incurable noxious that inflicts increasing poison damage over time, disables threat transfers to and from the target, and prevents the target from seeing Death Spark. If the target is not standing within the black circle when [[Fading soul spark]] dies, the target also dies, and the spark is revived. This detriment only lands on scouts.
- **Soul Tug**
- A curable curse that kills the target on expiration. The cursed target must be the only one within 2 meters of their chosen soul ally (shown in chat) to be cured without dying.
- **Reductive Resonance [21+]**
- An incurable detriment that increases all damage done to target if within range of another ally. The distance to the nearest ally is represented by displayed increments. This spell does not affect targets who are within any soul spark circle.

## Strategy

Death Spark places four colored circles (red, blue, yellow, black) on the ground shortly after the fight starts. At certain percentage points, the four circles each move to a new location. Players should stand within the correct circle, based on their class. If there are no players of the corresponding class, one random player is selected instead.

- Fighters = red, emblazoned
- Scouts = black, fading
- Mages = blue, esoteric
- Priests = yellow, luminous

This is a slow DPS fight as you don't want the circles to change position as one of the sparks dies. Players should also slow DPS while the curse is active, since players will need to step out of their circles to successfully cure the curse.

## ACT Triggers

- **<code>&lt;Trigger R=&quot;(?&amp;#35;Spark)releases a contagion&quot; SD=&quot;group cure&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Sacrificial Pursuits [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "group cure" when Death Spark casts Glinting Contagion.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Spark)The circles (foreshadow|change)&quot; SD=&quot;move to circles&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Sacrificial Pursuits [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "move to circles" when the four colored circles change positions.
- **<code>&lt;Trigger R=&quot;(?&amp;#35;Spark)Your soul tugs at (?&amp;lt;Player&amp;gt;\w+)'s&quot; SD=&quot;joust with ${Player}&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;The Unknown**: Sacrificial Pursuits [Untold Heroic]&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
- Calls "joust with <player>" when Death Spark casts Soul Tug, naming the player that must stand with the cursed target.
