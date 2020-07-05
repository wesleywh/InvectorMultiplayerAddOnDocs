[Back To Index](../../index.md)

# ArrowView

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[owner](#parameter-owner)<br>
[viewId](#parameter-viewId)<br>

------------------
### owner<a name="parameter-owner"></a>

> The transform owner of this arrow.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |Transform|None

[Back To Top](#)

------------------
### viewId<a name="parameter-viewId"></a>

> Reference value only, this will be set externally by different functions. " <br>This is the unique id for this arrow that will match the networked versions.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |int|0

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[NetworkSetPosRot](#NetworkSetPosRot)<br>

------------------
### public virtual void NetworkSetPosRot(RaycastHit hit)<a name="NetworkSetPosRot"></a>

>   Set the position and rotation over the network if this arrow is the owner based on the raycast hit information. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|hit|RaycastHit type, Where to set the position and rotation to over the network.|

[Back To Top](#)

