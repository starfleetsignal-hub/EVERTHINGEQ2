---
title: Pharinich the Forlorn
type: named
expansion: Chains of Eternity
race: Lizardman
level: '102'
difficulty: epic x4 ^^^
zone: '[[Altar of Abhorrence (Raid)]]'
location: Temple of the Faceless
added_in: Chains of Eternity
image: images/Pharinich_the_Forlorn.jpg
categories:
- Altar of Abhorrence (Raid) Named Monsters
- Chains of Eternity Named Monsters
- Epic Named Monsters
- Epic x4 Named Monsters
- Lizardman
- Named Monster pages that need EQ2MAP uid
- Named Monsters
- Tier 11 Epic x4 Named Monsters
- Tier 11 Named Monsters
source:
  title: Pharinich the Forlorn
  url: https://eq2.fandom.com/wiki/Pharinich_the_Forlorn
  history: https://eq2.fandom.com/wiki/Pharinich_the_Forlorn?action=history
  revision: 581017
  revised: '2013-01-14T13:11:03Z'
  license: CC BY-SA 3.0
---

## Strategy

- Tank turns him to face the wall where he stands. Group right behind on his heel in a bulk, dps away.
- JOUST: Red on-screen text "Pharinich the Forlorn begins to chant a devastating ritual!" - Whole group moves back into the entry-hallway just behind them (not sure if Tank also jousts or puts up a shield...).
- CURSE: Red on-screen text to individual players "You have been marked with Touch of Famine, which will spread if not isolated from other players!" - individual player(s) move either to the left or the right inside the room, wait until the curse is gone, rejoin the group.
- rinse and repeat above.

<hr>
[[ACT]] Trigger for the JOUST:<br>
<code>&lt;Trigger R=&quot;Pharinich the Forlorn begins to chant&quot; SD=&quot;Joust&quot; ST=&quot;3&quot; CR=&quot;F&quot; C=&quot;Altar of Abhorrence&quot; T=&quot;F&quot; TN=&quot;&quot; Ta=&quot;F&quot; /&gt;</code>
<hr>
CURSE Trigger?<br>
I haven't found the initial curse infection text in the logfile.<br>
All I see is:<br>
Pharinich's Touch of Famine hits (PLAYERNAME) for 2919 disease damage.<br>
Pharinich's Touch of Famine diseases (PLAYERNAME) draining 2641 points of power.<br>
If somebody has a working ACT trigger for this, please update!
<hr>
