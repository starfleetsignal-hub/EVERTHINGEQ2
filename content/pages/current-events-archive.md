---
title: Current events/Archive
type: page
categories:
- EQ2i
source:
  title: Current events/Archive
  url: https://eq2.fandom.com/wiki/Current_events/Archive
  history: https://eq2.fandom.com/wiki/Current_events/Archive?action=history
  revision: 912592
  revised: '2018-11-11T00:09:57Z'
  license: CC BY-SA 3.0
---

This is the Archive page for [[Current events|Current Events]].

## Recent Template Changes

### 26 July 2007

- **New Template** - Template:HouseInformation - Use this to add player housing zones. In the process of trying to expand the housing fields of Template:IZoneInformation, this was forked to simplify code. At the time of creation, all current housing pages using IZI for housing were converted.

### 23 July 2007

- **New Template** - Template:VendorItem - Use this template in the ***obtain*** field of Items that can be bought from one or more vendors.

### 9 July 2007

- **WHOLE LOTTA CHANGES**
  - ItemInformation - added subtype to example and key, added spellgrade. Use spellgrade only when type=spellbook. I know we have stayed away from this in the past, but I want you to start adding, at least, Master drops to mob drop lists. Some of them are rare and only dropped by specific mobs! I do not expect us to link every single one, nor do I expect us to create Item pages for EVERY spellbook! Concentrate on the dropped books. Let the monster pages drive spellbook item creation.
  - **Dropped Items** - Added **Drops** to Zone and IZone linkbars. Whole new category tree, <zone> Dropped Items. This is only linked to if you use the &#123;&#123;DroppedItem}} tag in the obtain field on an Equip or Item page, so be sure to use it!

### 15 June 2007

- **New Fields:** for MonsterInformation - **trauma, arcane, noxious** and **elemental**. These are DOT types and will display a DOT icon on the monster box indicating that this monster has been known to use this type of DOT attack.

### 12 June 2007

- **New Fields:** for RaceInformation - **language, iname, idesc** and **text** will handle ALL of the needs for racial category pages.

### 3 June 2007

- **New Tag:** dab - use &#123;&#123;dab|PAGENAME of disambig page}} at the top of pages that are disambiguated to point back to the disambig page.

### 29 May 2007

- **New Tag:** LU - use &#123;&#123;LU|LU#}} at the top of the patch notes and category pages for any LU. This displays a line on each pointing to the other and adds the page to Live Updates.

### 26 May 2007

- **New Tag:** obsolete - use &#123;&#123;obsolete|message}} to tag articles that are no longer required but remain in the game, such as Access Quests for zones that no longer require an access quest.

### 14 April 2007

- **New Options:** for Loc and LocationInformation. If the first parameter (for Loc) or mapref (for LocationInformatiuon) is X, output is suppressed. If it is asterisk (*), the only output is (see below). This is useful when a mob roams or spawns all over the place (X) making a Loc ref useless, or when a mob has multiple spawn points (*). LocationInformation is used by all templates that use the location/mapref/uid trio of variables.

### 13 April 2007

- **New Template:** SubclassLink. This will be the new bottom-level template driving all the AllCats templates. as I update them I will be separating out the individual subclasses in the output. So instead of saying "All Crusaders" it will say "Paladin, Shadowknight"

### 9 April 2007

- **New Templates:** AuditRequest, and it's companion tag, AuditComplete. Please use these sparingly! See [[The Ruins of Varsoon]] for an example of appropriate use.
- **Reworked Template:** DroppedItem received a serious face lift. See the template page for new parameters and examples of use!

### 8 April 2007

- **New Template:** RecipeBook. Have a look at [[Advanced Alchemist Volume 39]], [[Blueprint Safety Recaller]], and [[Gift of the Golden Acorn]] for examples of use. Also see RecipeBookx. Use &#123;&#123;subst:RBIx}} to load the example to a page.

### 7 April 2007

- **New Template:** RepeatQuest for all types of Repeatable Quests.

### 22 March 2007

- **New Template:** CraftedItem, for use mainly in the ***obtain***' field of any ItemInformation or EquipInformation call. See the template page for the parameters.

### 20 March 2007

- **New Template Tag:** &#123;&#123;OnTest}} can now be used to indicate that information you're providing exists only on the Test Server and may still be in flux. Once verified as live, remove the OnTest tag from the page.

### 18 March 2007

- **New Field** for Coin, the 5th parameter is now for Status points (as in the price for a house), and I added color!

### 17 March 2007

- **Major Changes** to IZoneInformation for Housing! see new field, ***housing***, and the template page for an explanation. See [[Qeynos: 1 Room Apartment]] for an example of use.

### 15 March 2007

**BEWARE THE IDES OF MARCH!**

- **FIX AND UPDATE** for EquipInformation. I have finally fixed the problem with Usable Classes display for shields, AND have added support for all weapon types. NOTE: If wtype is blank, and dtype is NOT an armor type, it will be assumed the item can be used by ALL classes!

### 11 March 2007

- **NEW FIELDS** for ItemInformation, ***satiation*** and ***duration*** (for type=Food or Drink), and ***bagslots*** and ***wtreduce*** (for type=Container).

### 6 March 2007

- **Equipment Template Redesigned!** I have redesigned EquipInformation to mimic the in-game examine UI display. 2 new fields, ***effectlist*** and ***effectdesc***, and ***effects*** is deprecated.
- **New Tags!** &#123;&#123;CapCheck}}, &#123;&#123;CapOK}}, and &#123;&#123;SpellCheck}} (links to CapCheck) are for flagging pages that you think have misspelled or incorrectly capitalized titles. &#123;&#123;FactCheck}} and &#123;&#123;FactOK}} are for tagging pages that you think have an item in error. All of these ask visiting users to check in-game to verify or correct the issue. If verified as correct, remove the Check tag from the top and add the OK tag at the bottom of the page!

### 4 March 2007

- **New Templates:** &#123;&#123;CapCheck}} and &#123;&#123;CapOK}}. If you come across a page with a capitalization that looks wrong, i.e. does not match the more-or-less standards SOE seems to try to have, tag the top of the page with &#123;&#123;CapCheck}}. This will added it to Capitalization check requested. If you come across one of these tags and verify that it IS correct, remove the &#123;&#123;CapCheck}} tag from the top of the page and put &#123;&#123;CapOK}} at the bottom of the page so folks will know that it is just SOE being stupid, again.

### 25 February 2007

- **New Fields** for EquipInformation. Added discrete fields for focus, mastery skills, slashing, crushing, piercing and resistances. This means we can now create categories for all of these, and I am working on that now. Please see the template page for help with these new fields.

### 9 February 2007

- **New Fields** for PCInformation, ***stsclass*** and ***stslevel***. Now that we are on the new FAST server, expect to see many new template changes/improvements!

### 7 January 2007

- **New Template!** ResourceInformation for harvestable resources. See also: NodeInformation for some minor changes.

### 26 December 2006

- **New Fields** for NamedInformation. ***group*** (same as MonsterInformation) and ***ph***. If used, ph is for the name of the Placeholder.

### 18 December 2006

- **New Fields** for MonsterInformation. ***class, group, agro*** and ***social***. Class is there for sentient monsters that have player-like class abilities. Group is like faction except for mobs that do not have an in-game faction, yet are part of a social group. The example tempate has agro and social with default values of "y", as MOST monsters are both aggressive and social. AND... bfaction is deprecated. It was a failed parameter. Use the Faction template instead.

### 13 December 2006

- **New Field** for ItemInformation: ***rsr*** is for Rent Status Reduction. If non-blank, the item will be linked to Rent Status Reduction Items
- **NEW TEMPLATE**! CQuestInformation is for Collection Quests! Shortcut to the Ex template is CQIx.

### 11 December 2006

- **New Field** for ZoneInformation and IZoneInformation: ***zdiff*** is for the raid modifiier (x2, x3 or x4). It is ONLY used if ***instance*** is Group Raid, Raid or Public Raid.

### 10 December 2006

- EquipInformation now understands default **classes** when **wtype** is *Shield* and **dtype** is *Buckler, Round Shield, Tower Shield* or *Kite Shield* in the same way that **classes** is handled when **dtype** is an armor type (see [[#26 November 2006|Nov. 26 note re: Default Armor Types]] below). Be sure to check the output after you save your page to make sure the Equipment you are creating does not have extra restrictions!
- renamed sub-template AllArmorCats to sub-AllEquipCats
- Sub-AllEquipCats: Chain Armor should have had All Scouts, not just Bards and Rogues

### 5 December 2006

- **New Template**: Steps: Use &#123;&#123;steps|&lt;zone&gt;}} to flag a quest with missing steps. This is more precise than &#123;&#123;info}}. This links the quest article to Quest articles needing next step, and Quest articles needing next step in <zone> if <zone> is defined.

### 3 December 2006

- Userboxes: I have aggregated all the user boxes I have so far defined into a category so everyone can find them. If you create one, PLEASE add it to this category!
- NormalizeCharClass: Added Tinkerer and Transmuter

### 29 November 2006

- SpellInformation & CastingInformation: Removed **recovery** (SOE stopped displaying it with EOF, all times are .5s). Added new parameters, **hpcost, tick, costot, hpcostot**. See template page for more info. Also fixed display error in ConvertSeconds.

### 26 November 2006

- EquipInformation: So long as there are no extra restrictions, such as *Cloth Armor* that is Mage only, you can now leave **classes** blank, so long as **dtype** is *Cloth Armor, Leather Armor, Chain Armor* or *Plate Armor*, and the template will automatically restrict the output and linking to those classes that can use that armor type. If **dtype** is not an armor type, and **classes** is blank, the template will link to all adventurer classes, as always.
- Well, belatedly I realized that *Qeynos Guard* is both a faction and an item. All faction base pages are moved to <faction name> (Faction). The category page names are unchanged. It would be nice if someone volunteered to take the rest of the info from [[Factions]] and create the rest of the faction base pages, at the least.

### 25 November 2006

- EquipInformation: the default for **classes** is now All Adventurer Classes, rather than All Classes. Artisan Classes will no longer be added by default.
- **New Template** Class_SpelllinesEx You can use this to start a new Spelllines templte for a class, but you cannot use subst:tution to do it. Edit the Ex template and copy it. Otherwise it breaks all the nice noinclude sections.

### 24 November 2006

- **MAJOR CHANGE** A better way to do Spell Lines! Instead of creating a whole group of templates for each class with specific naming so SpellInformation can find them, I now create ONE template per class for all the spell lines! See Fury Spelllines. Each spell in a spell line will still need to be edited to hook into it. See SpellInformation field **series** (btw, notice **desc** while you are there and kill two edit-birds with one stone).
- **Bug Fixes**
  - Made a few edits to SpellInformation to fix a category and rendering error.
  - Changed NormalizeCharClass to add a few common misspellings and a message noting the correct spelling.

### 23 November 2006

- EquipInformation: Added new parameter, **set**. If defined and a **set** (Armor Set) page exists, the table will be included below the Equipment Information box.

### 22. November 2006

- **NEW TEMPLATES** FactionInformation is used to create a faction article. This is **not** a category page! FactionCategory goes on all 3 of the faction categories, (Faction), (Good Faction) and (Bad Faction). The template knows which one it is on, creates the correct links and uses inclusion to grab the information from the article page! See The Bloodskull Orcs (Faction) and [[Bloodskull Orcs (Faction)]] for am example!
- ClassInformation and SpellInformation will now display image:}_Icon.jpg, if it exists.

### 21. November 2006

- Merged BlessingInformation into MiracleInformation and added **Charges   2**. This change should be invisible to users.
- CastingInformation: if *cost* and *conc* are both blank, **Cost** line is now hidden.

### 20. November 2006

- The remainder of the AllCats Templates have been updated, thanks to Ijuakos!
- **NEW FIELD** ***purpose*** added to NPCInformation. Defines the reason for the NPC. Possible types are: Quest, Ecology, Lore, etc. If the NPC has a purpose under its name (like <Provisioner>, <Dismal Rage Priest>, <Broker>, etc.) use that WITHOUT the <> brackets! See NPC Types for all currently defined **purpose** categories. Default value if ***purpose*** is undefined or blank is "Quest" as that is what MOST of the defined NPCs here are.

### 19. November 2006

- **BIG CHANGE!** SpellInformation significantly changed, thanks to the creative work of DM78. **New Fields:** *wtype*, *desc* and *series*. see the template page for full information.
  - See more related changes in the following templates:
    - CastingInformation - added *border*
    - Spellline - no real changes, but many of you may never have seen this one. NOTE: all spelline templates should be named &#91;&#91;Template:&lt;class&gt; &lt;series&gt;]] to maintain function with SpellInformation
- **New Template!** UserTempSig: So everyone can put a cool tag on their templates for all to see!

### 18. November 2006

- **New sub-Template!** LocationInformation: Now used to combine and standardize the appearance of location text, mapref and eq2map uid into a single line in all templates that use them.
- **New Template!** Level2Tier: Used in QuestInformation, ItemInformation and EquipInformation to link to categories by Tier.
- links to Templates and Florence's Templates updated to sort under the template name, rather than under T for Template!
- **New Template!** htmlOption will hide options from those pesky If and wikitable structures!
- **New Template!** info will link to Articles needing more information (formerly Missing Info). I am updating all templates to use the new tag and cat asap.
- **New Template!** wikify Puts a infobox on the article begging for some nice person who understands wikicode to fix this mess. It probably needs a tech writer, too... (adds link to Articles needing wikification)

### 16. November 2006

- I have made a few minor and some major changes to some of our templates. As always, all Information templates can be found at Florence's Templates. Help about template usage can be found on the template's page.
  - LnLInformation - **series** now links to category:**series** (Book Series)
  - All templates with an image link use **iname** for alt image name, and **idesc** for alt text under the image. Also, all template images are thumbnailed.
  - ZoneInformation and ZoneLinks have a new link, **Explore**. This is activated by a new parameter, **discovery**, in POIInformation.
  - See AllCats Templates for information on these VERY cool time-saving tools.
  - See Help for New Editors for an article by yours truly aimed at newcomers here with an introduction to the less arcane aspects of wikicode, or Wiki Markup Language (WML)
