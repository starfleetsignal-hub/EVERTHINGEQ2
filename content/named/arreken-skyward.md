---
title: Arreken Skyward
type: named
race: Drakota
level: '100'
difficulty: epic x4 ^^^
zone: '[[Dracur Prime: Sevalak Awakened]]'
location: in a dark alley
health: 700,000,000
specials: '*Call of Sky: focus *Destructive Shroud: focus *Heatclaw: heat *Impending Destruction: crushing (curable trauma detrimental) **See Special Attacks section for details *Skystorm: cold, aoe power drain, 44 second cooldown **See Special Attacks section for details *Viscious Bite: crushing *1000 Stings: heat'
drops:
- '[[Ancient Draconic Setting]]'
- '[[Azure Gemmed Ring of Storms]]'
- '[[Banded Dragonhide Girdle]]'
- '[[Hard Dragonskin Wrap]]'
- '[[Modulated Dragonscale Protective Brace]]'
- '[[Prime Drake Fang]]'
- '[[Pure Primal Velium Shard]] (2 if member)'
- '[[Radiant Engraved Draconic Ring]]'
- '[[Radiant Ring of Draconic Fury]]'
added_in: LU63
categories:
- 'Dracur Prime: Sevalak Awakened Named Monsters'
- Drakota
- Epic Named Monsters
- Epic x4 Named Monsters
- LU63 Named Monsters
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Tier 11 Epic x4 Named Monsters
- Tier 11 Named Monsters
source:
  title: Arreken Skyward
  url: https://eq2.fandom.com/wiki/Arreken_Skyward
  history: https://eq2.fandom.com/wiki/Arreken_Skyward?action=history
  revision: 2000023
  revised: '2026-05-02T18:42:34Z'
  license: CC BY-SA 3.0
---

## Special Attacks

### Impending Destruction

Effects:

- Inflicts 30.0% of max health in crushing damage on targets in Area of Effect.
  - This effect cannot be critically applied.
- If not cured this spell may cause extra abilities to manifest!
- Cannot be modified except by direct means

### Skystorm

Effects:

- Inflicts 331,326 - 615,320 cold damage on caster instantly and every 0.0 seconds.
  - Any distance up to 9 away and a forward arc of 180 degrees
  - Damage from this effect is harder than normal to mitigate.
- Inflicts 302,927 - 454,390 cold damage on caster instantly and every 0.0 seconds.
  - Any distance up to 9 away and a rear arc of 180 degrees
  - Damage from this effect is harder than normal to mitigate.
- Inflicts 247,124 - 370,687 cold damage on caster instantly and every 0.0 seconds.
  - Any distance up to 14 away and a forward arc of 180 degrees
  - Damage from this effect is harder than normal to mitigate.
- Inflicts 233,174 - 248,990 cold damage on caster instantly and every 0.0 seconds.
  - Any distance up to 14 away and a rear arc of 180 degrees
  - Damage from this effect is harder than normal to mitigate.
- Inflicts 107,619 - 131,534 cold damage on caster instantly and every 0.0 seconds.
  - Any distance up to 200 away and a forward arc of 180 degrees
  - Damage from this effect is harder than normal to mitigate.
- Inflicts 79,718 cold damage on caster instantly and every 0.0 seconds.
  - Any distance up to 200 away and a rear arc of 180 degrees
  - Damage from this effect is harder than normal to mitigate.
- Decreases power of targets in Area of Effect by 33.0%.
  - This effect cannot be critically applied.
- If not cured this spell may cause extra abilities to manifest!

## Strategy

- MT grabs the Drakota
- OT grabs the adds
- group stands at his tail, dps, kills the adds fast
- when you get a big message "You think you can evade me by staying behind me\? My tail will make quick work of you!" joust to his front.
- Tank needs a Death-prevent when Arreken bites.

<hr>
[[ACT]] Trigger for Tail swipe:<br>
<code>&lt;Trigger R=&quot;You think you can evade me by staying behind me\? My tail will make quick work of you!&quot; SD=&quot;Tail Swipe&quot; ST=&quot;3&quot; CR=&quot;F&quot; C=&quot;Dracur Prime: Sevalak Awakened&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
<hr>
[[ACT]] Trigger for Bite:<br>
<code>&lt;Trigger R=&quot;Standing in front of my mighty jaws puts you in a convenient place for a quick meal&quot; SD=&quot;Bite imminent - Death Prevent Tank&quot; ST=&quot;3&quot; CR=&quot;F&quot; C=&quot;Dracur Prime: Sevalak Awakened&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
<hr>
