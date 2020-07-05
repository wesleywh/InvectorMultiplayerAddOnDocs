[Back To Index](../../index.md)

# MP_vSwimming

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[MP_EnterSwimState](#MP_EnterSwimState)<br>
[MP_ExitSwimState](#MP_ExitSwimState)<br>
[MP_SwimmingBehaviour](#MP_SwimmingBehaviour)<br>
[MP_UnderWaterBehaviour](#MP_UnderWaterBehaviour)<br>
[MP_WaterRingEffect](#MP_WaterRingEffect)<br>
[OnTriggerEnter](#OnTriggerEnter)<br>
[OnTriggerExit](#OnTriggerExit)<br>
[UpdateSwimmingBehavior](#UpdateSwimmingBehavior)<br>

------------------
 ### private void MP_EnterSwimState()<a name="MP_EnterSwimState"></a>
>   Calls the `NetworkOnEnterWater` UnityEvent for everyone in the photon room. Also plays the `Swimming` animation for everyone in the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### private void MP_ExitSwimState()<a name="MP_ExitSwimState"></a>
>   Calls the `NetworkOnExitWater` UnityEvent for everyone in the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### private void MP_SwimmingBehaviour()<a name="MP_SwimmingBehaviour"></a>
>   Calls the `MP_EnterSwimState` or `MP_ExitSwimState` based on your position in the water. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### void MP_UnderWaterBehaviour()<a name="MP_UnderWaterBehaviour"></a>
>   Calls the `NetworkOnUnderWater` UnityEvent for everyone in the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### private void MP_WaterRingEffect()<a name="MP_WaterRingEffect"></a>
>   Plays the `WaterRingEffect` for all networked versions in the photon room. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### void OnTriggerEnter(Collider other)<a name="OnTriggerEnter"></a>
>   Will send the `WaterImpactEffect` over the network via the `NetworkWaterImpactEffect` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

------------------
 ### void OnTriggerExit(Collider other)<a name="OnTriggerExit"></a>
>   Will send the `WaterDropsEffect` over the network via the `NetworkWaterDropsEffect` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

------------------
 ### protected override void UpdateSwimmingBehavior()<a name="UpdateSwimmingBehavior"></a>
>   Keeps the same logic as the based invector code but also calls the `MP_UnderWaterBehaviour` and `MP_SwimmingBehaviour` functions. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

