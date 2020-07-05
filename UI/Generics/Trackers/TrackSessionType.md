[Back To Index](../../../index.md)

# TrackSessionType

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[texts](#parameter-texts)<br>

------------------
 ### texts<a name="parameter-texts"></a>
> The Text values to manipulate to display what session type your currently in

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
>   Dynamically sets all the `texts` values to display what type of session your currently in. Public/Private 

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

