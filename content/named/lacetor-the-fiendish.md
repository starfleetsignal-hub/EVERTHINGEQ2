---
title: Lacetor the Fiendish
type: named
expansion: Scars of Destruction
race: Chetari
level: '138'
difficulty: Epic x4 ^^^
zone: '[[Western Wastes: Temple Crater (Raid)]]'
location: '{{waypoint -196.50, -16.80, -506.81}}'
health: 250 Quadrillion
primary_damage: Crushing, Slashing
achievement_xp: true
added_in: Scars of Destruction
categories:
- Chetari
- Epic Named Monsters
- Epic x4 Named Monsters
- Monsters that award AA
- Named Monster needing location
- Named Monsters
- Scars of Destruction Named Monsters
- Tier 14 Epic x4 Named Monsters
- Tier 14 Named Monsters
- 'Western Wastes: Temple Crater (Raid) Named Monsters'
source:
  title: Lacetor the Fiendish
  url: https://eq2.fandom.com/wiki/Lacetor_the_Fiendish
  history: https://eq2.fandom.com/wiki/Lacetor_the_Fiendish?action=history
  revision: 1908288
  revised: '2025-10-22T03:25:23Z'
  license: CC BY-SA 3.0
---

Lacetor the Fiendish is a Tier 3 raid boss.

## Statistics

- Flurry Avoidance: 525.0
- Ability Doublecast Avoidance: 590.0
- Resolve: 11,195.0

## Abilities

- **Fiendish Scratching**
- An incurable trauma that deals fast ticking slashing damage and increases incoming elemental and arcane damage from all sources.
- **Mind Pressure I**
- A curable trauma that .
- **Fierce Screeching**
- A curable arcane that .
- **Reprising Thoughts I**
- A curable arcane that deals fast-growing damage over time.
- **Fierce Fiend**
- A curable elemental that .
- **Piercing Thought Process I**
- A curable trauma that .
- **Fiendish Fathoms**
- A curable noxious that deals fast ticking noxious damage and increases incoming arcane and physical damage from all sources.
- **Spellweaved Admonishment**
- A curable elemental that deals elemental damage and increases all other damage types. This effect only lands on mages.
- **Synergetic Storm**
- An incurable curse that debuffs offensive and defensive capabilities. It can only be removed by casting [[Balanced Synergy]]. Removing the curse does not require all four archetypes within the group.
- **Left in the Cold**
- A curse that roots the target and can only be cured if no other player is within 7 meters of the afflicted player. When it expires, it kills the entire raid.
- **Boneswarm Frenzy**
- A buff that decreases damage taken for each active bonestorm in the encounter. If there are more than 3 active bonestorms, then each new bonestorm heals Lacetor.
- **Teamwork**: Leader
- A buff that casts Tag Team Strike on the current target, if that target already has the effect from Teamwork: Member.

## Strategy

Lacetor continuously summons a [[Bonestorm (Lacetor the Fiendish)|bonestorm]] which has the Teamwork: Member buff.

## ACT Triggers

- &lt;Trigger R=&quot;\&amp;#35;00FF00&amp;quot;Left in the Cold&amp;quot; has been successfully removed from&quot; SD=&quot;&quot; ST=&quot;3&quot; CR=&quot;T&quot; C=&quot;Western Wastes: Temple Crater [Raid]&quot; T=&quot;T&quot; TN=&quot;Left in the Cold&quot; Ta=&quot;F&quot; /&gt;
- &lt;Spell N=&quot;Left in the Cold&quot; T=&quot;60&quot; OM=&quot;F&quot; R=&quot;F&quot; A=&quot;F&quot; WV=&quot;10&quot; RD=&quot;F&quot; M=&quot;F&quot; Tt=&quot;&quot; FC=&quot;-65536&quot; RV=&quot;-10&quot; C=&quot; General&quot; RC=&quot;F&quot; SS=&quot;&quot; WS=&quot;tts [curse soon, get to your flag]&quot; /&gt;
  - The trigger and timer above work together to count 60 seconds between castings of Left in the Cold. At 10 seconds remaining, it calls "curse soon, get to your flag".
- &lt;Spell N=&quot;Synergetic Storm&quot; T=&quot;64&quot; OM=&quot;F&quot; R=&quot;F&quot; A=&quot;T&quot; WV=&quot;5&quot; RD=&quot;F&quot; M=&quot;F&quot; Tt=&quot;&quot; FC=&quot;-16776961&quot; RV=&quot;-15&quot; C=&quot;Lacetor the Fiendish&quot; RC=&quot;F&quot; SS=&quot;&quot; WS=&quot;tts [synergy curse soon]&quot; /&gt;
  - A timer that counts 64 seconds between castings of Synergeetic Storm. At 5 seconds remaining, it calls "synergy curse soon".
