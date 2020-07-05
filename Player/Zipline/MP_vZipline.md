[Back To Index](../../index.md)

# MP_vZipline

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[MP_ExitZipline](#MP_ExitZipline)<br>
[MP_InitiateZipline](#MP_InitiateZipline)<br>
[MP_UsingZipline](#MP_UsingZipline)<br>
[OnTriggerEnter](#OnTriggerEnter)<br>
[OnTriggerExit](#OnTriggerExit)<br>
[OnTriggerStay](#OnTriggerStay)<br>

------------------
 ### void MP_ExitZipline()<a name="MP_ExitZipline"></a>
>   Sets the animation, rigidbody settings, and calls the `NetworkOnZiplineExit` RPC for all networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
 ### void MP_InitiateZipline(Collider other)<a name="MP_InitiateZipline"></a>
>   Sets the animation clip, rigidbody settings, and calls the `NetworkOnZiplineEnter` RPC for all networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

------------------
 ### void MP_UsingZipline(Collider other)<a name="MP_UsingZipline"></a>
>   Calls the `NetworkOnZiplineUsing` RPC for all networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

------------------
 ### private void OnTriggerEnter(Collider other)<a name="OnTriggerEnter"></a>
>   Only called by the owner player. Calls the `MP_InitiateZipline` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

------------------
 ### private void OnTriggerExit(Collider other)<a name="OnTriggerExit"></a>
>   Only called by the owner player. Calls the `MP_ExitZipline` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

------------------
 ### private void OnTriggerStay(Collider other)<a name="OnTriggerStay"></a>
>   Only called by the owner player. Calls `MP_InitiateZipline`, `MP_ExitZipline`, or `MP_UsingZipline` based on the current stat of the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|other|***No found decription**|

[Back To Top](#)

