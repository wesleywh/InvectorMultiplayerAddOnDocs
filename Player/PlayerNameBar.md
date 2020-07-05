[Back To Index](../index.md)

# PlayerNameBar

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[playerBar](#parameter-playerBar)<br>
[playerName](#parameter-playerName)<br>

------------------
### playerBar<a name="parameter-playerBar"></a>

> The holder object for the player name bar. Will disable this if not a network version of this player.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |GameObject|None

[Back To Top](#)

------------------
### playerName<a name="parameter-playerName"></a>

> The text to modify with the Network Nickname.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Text|None

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[SetPlayerName](#SetPlayerName)<br>

------------------
### public virtual void Awake()<a name="Awake"></a>

>   Removes the namebar if you're the owner player. Also sets the name on your networked versions via `SetPlayerName` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SetPlayerName(string nameText)<a name="SetPlayerName"></a>

>   Sets the name shown on the name bar to whatever is passed in via the input. Calls `NetworkSetPlayerName` RPC to set the name over the network. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|nameText|string type, the input name|

[Back To Top](#)

