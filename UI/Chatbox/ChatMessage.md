[Back To Index](../../index.md)

# ChatMessage

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[message](#parameter-message)<br>
[playerName](#parameter-playerName)<br>

------------------
 ### message<a name="parameter-message"></a>
> A Text value to display the players message.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |Text|null

[Back To Top](#)

------------------
 ### playerName<a name="parameter-playerName"></a>
> A Text value to display the players name.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|private |Text|null

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[SetMessage](#SetMessage)<br>

------------------
 ### public virtual void SetMessage(SentChatMessage incoming)<a name="SetMessage"></a>
>   Sets the `playerName` and `message` text values based on the values in the `SentChatMessage` object. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|incoming|SentChatMessage type, this contains the player name and message|

[Back To Top](#)

