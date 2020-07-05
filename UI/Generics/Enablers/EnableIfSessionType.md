[Back To Index](../../../index.md)

# EnableIfSessionType

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[isOwner](#parameter-isOwner)<br>
[targets](#parameter-targets)<br>
[type](#parameter-type)<br>

------------------
 ### isOwner<a name="parameter-isOwner"></a>
> Enable these targets if you're the owner or not

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
 ### targets<a name="parameter-targets"></a>
> The list of targets to enable or disable.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |GameObject[]|new GameObject[] { }

[Back To Top](#)

------------------
 ### type<a name="parameter-type"></a>
> What type of photon session this has to be for these targets to enable.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |SessionType|SessionType.Public

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[FixedUpdate](#FixedUpdate)<br>
[SetIsActive](#SetIsActive)<br>

------------------
 ### protected virtual void FixedUpdate()<a name="FixedUpdate"></a>
>   Will enable or disable objects by calling the `SetIsActive` function. Will only enable them if the photon session type and isOwner match. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected virtual void SetIsActive(bool isActive)<a name="SetIsActive"></a>
>   Enable or disable all the targets based on the input value. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|isActive|bool type, active all the targets?|

[Back To Top](#)

