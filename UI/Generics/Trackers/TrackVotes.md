[Back To Index](../../../index.md)

# TrackVotes

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[indexNumberToTrack](#parameter-indexNumberToTrack)<br>
[texts](#parameter-texts)<br>

------------------
### indexNumberToTrack<a name="parameter-indexNumberToTrack"></a>

> The index of the `sceneVotes` variable to track.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |int|0

[Back To Top](#)

------------------
### texts<a name="parameter-texts"></a>

> The Text values to manipulate to show how many votes at the selected index there currently are.

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

>   Dynamically sets the `texts` values to be what the current number of votes there are at the selected `indexNumberToTrack` index. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

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

