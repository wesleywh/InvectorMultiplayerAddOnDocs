[Back To Index](../index.md)

# PlayerData

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[character](#parameter-character)<br>
[characterName](#parameter-characterName)<br>
[ground](#parameter-ground)<br>
[health](#parameter-health)<br>
[inventory](#parameter-inventory)<br>
[jump](#parameter-jump)<br>
[roll](#parameter-roll)<br>
[stamina](#parameter-stamina)<br>

------------------
### character<a name="parameter-character"></a>

> The actual gameobject name of this character.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### characterName<a name="parameter-characterName"></a>

> The nickname of your the photon room.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |string|""

[Back To Top](#)

------------------
### ground<a name="parameter-ground"></a>

> All of the group settings on this character.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerGrounded|new PlayerGrounded()

[Back To Top](#)

------------------
### health<a name="parameter-health"></a>

> All of the health data related to this character.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerHealth|new PlayerHealth()

[Back To Top](#)

------------------
### inventory<a name="parameter-inventory"></a>

> The inventory data from this characters inventory.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerInventory|new PlayerInventory()

[Back To Top](#)

------------------
### jump<a name="parameter-jump"></a>

> All of the jump settings on this character.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerJump|new PlayerJump()

[Back To Top](#)

------------------
### roll<a name="parameter-roll"></a>

> All of the roll settings on this character.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerRoll|new PlayerRoll()

[Back To Top](#)

------------------
### stamina<a name="parameter-stamina"></a>

> All of the stamina data related to this character.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |PlayerStamina|new PlayerStamina()

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[PlayerData](#PlayerData)<br>

------------------
### public PlayerData(vThirdPersonController controller)<a name="PlayerData"></a>

>   Takes a simple character controller inputs and extracts all of the following information from that character: health info, stamina info, roll settings, jump settings, group settings, and inventory data. It will then save that information into easily serializable classes that can be stored into a binary file. It's all self contained within this class. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|controller|The vThirdPersonController to scan|

[Back To Top](#)

