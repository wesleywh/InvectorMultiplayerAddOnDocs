[Back To Index](../../../index.md)

# TrackRandomSceneList

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[images](#parameter-images)<br>
[indexNumberToTrack](#parameter-indexNumberToTrack)<br>
[texts](#parameter-texts)<br>

------------------
### images<a name="parameter-images"></a>

> The images to manipulate.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image[]|new Image[] { }

[Back To Top](#)

------------------
### indexNumberToTrack<a name="parameter-indexNumberToTrack"></a>

> The index of the `_randomRoomList` on the UICoreLogic to track

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|0

[Back To Top](#)

------------------
### texts<a name="parameter-texts"></a>

> The Text values to manipulate.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text[]|new Text[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[FixedUpdate](#FixedUpdate)<br>
[SetSprite](#SetSprite)<br>
[SetText](#SetText)<br>

------------------
### protected virtual void FixedUpdate()<a name="FixedUpdate"></a>

>   Sets the `images` and the `texts` to whatever the current `indexNumberToTrack` integer is set to. Will get that info from the `UICoreLogic`'s `_randomRoomList` variable. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void SetSprite(Sprite newImage)<a name="SetSprite"></a>

>   Sets the input Sprite image value into all the `images` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|newImage|Sprite type, the image to set all the `images` to|

[Back To Top](#)

------------------
### protected virtual void SetText(string inputText)<a name="SetText"></a>

>   Used to set the `texts` values to be whatever the input value is 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputText|string type, the string value to set to the `texts`|

[Back To Top](#)

