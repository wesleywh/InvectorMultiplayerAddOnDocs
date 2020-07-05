[Back To Index](../../../index.md)

# TrackPhotonRoomName

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[texts](#parameter-texts)<br>

------------------
### texts<a name="parameter-texts"></a>

> List of Text values to set.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text[]|new Text[] { }

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[FixedUpdate](#FixedUpdate)<br>
[SetText](#SetText)<br>

------------------
### protected virtual void FixedUpdate()<a name="FixedUpdate"></a>

>   Set the text values according to the current photon room name dynamically. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void SetText(string inputText)<a name="SetText"></a>

>   Set the `texts` values according to the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|inputText|string type, the text string to set|

[Back To Top](#)

