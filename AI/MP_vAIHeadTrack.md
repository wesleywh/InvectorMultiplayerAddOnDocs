[Back To Index](../index.md)

# MP_vAIHeadTrack

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[FixedUpdate](#FixedUpdate)<br>
[GetLookPoint](#GetLookPoint)<br>
[LateUpdate](#LateUpdate)<br>
[RemoveMainLookTarget](#RemoveMainLookTarget)<br>
[SetMainLookTarget](#SetMainLookTarget)<br>

------------------
 ### protected override void FixedUpdate()<a name="FixedUpdate"></a>
>   Override or original FixedUpdate so I can control when to call fixed update with a variable that I have access to. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### protected override Vector3 GetLookPoint()<a name="GetLookPoint"></a>
>   Set the _lookAtPoint if you're the owner 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| |

**No parameters**

[Back To Top](#)

------------------
 ### protected override void LateUpdate()<a name="LateUpdate"></a>
>   Only perform the late update if you're the owner. Otherwise only rotate to specified locations and weights. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public override void RemoveMainLookTarget()<a name="RemoveMainLookTarget"></a>
>   When the main look target is removed, notify all the network versions to remove their target as well. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### public override void SetMainLookTarget(Transform target)<a name="SetMainLookTarget"></a>
>   When the main look target changes notify all the network versions to switch to the new target. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|target|***No found decription**|

[Back To Top](#)

