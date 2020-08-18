[Back To Index](../../index.md)

# MP_vShooterManager

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[AddAmmoToWeapon](#AddAmmoToWeapon)<br>
[LoadIKAdjust](#LoadIKAdjust)<br>
[NetworkAddAmmoToWeapon](#NetworkAddAmmoToWeapon)<br>
[NetworkCancelReloadRoutine](#NetworkCancelReloadRoutine)<br>
[NetworkRecoil](#NetworkRecoil)<br>
[NetworkReloadWeapon](#NetworkReloadWeapon)<br>
[Recoil](#Recoil)<br>
[ReloadWeapon](#ReloadWeapon)<br>
[SetLeftWeapon](#SetLeftWeapon)<br>
[SetRightWeapon](#SetRightWeapon)<br>
[Shoot](#Shoot)<br>
[UpdateAmmoDisplay](#UpdateAmmoDisplay)<br>

------------------
### protected override IEnumerator AddAmmoToWeapon(vShooterWeapon weapon, float delayTime, bool ignoreEffects = false)<a name="AddAmmoToWeapon"></a>

>   Calls the `NetworkAddAmmoToWeapon` IEnumerator on top of all its normal functions. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| |

| Parameter Name | Description |
|:---|:---|
|weapon|Read the invector docs.|
|delayTime|Read the invector docs.|
|ignoreEffects|Read the invector docs.|

[Back To Top](#)

------------------
### public override void LoadIKAdjust(string category)<a name="LoadIKAdjust"></a>

>   When the owner changes its IK adjust catagory it will call the `LoadIKAdjustCatagory` RPC which has the networked players set their catagory to the same thing as the owner. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|category|***No found decription**|

[Back To Top](#)

------------------
### IEnumerator NetworkAddAmmoToWeapon(vShooterWeapon weapon, float delayTime, bool ignoreEffects = false)<a name="NetworkAddAmmoToWeapon"></a>

>   When the owner player adds ammo to the weapon it triggers the network players to play the Reload animations via the `SetTriggers` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False| |

| Parameter Name | Description |
|:---|:---|
|weapon|Takes same inputs as `AddAmmoToWeapon` function|
|delayTime|Takes same inputs as `AddAmmoToWeapon` function|
|ignoreEffects|Takes same inputs as `AddAmmoToWeapon` function|

[Back To Top](#)

------------------
### IEnumerator NetworkCancelReloadRoutine()<a name="NetworkCancelReloadRoutine"></a>

>   When the owner player cancels the reload animations it calls `ResetTriggers` RPC which has the network players mimic the owner player by canceling their reload animations. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### IEnumerator NetworkRecoil(float horizontal, float up)<a name="NetworkRecoil"></a>

>   The owner sends the `SetTriggers` RPC for the network players to play the Shooting recoil animation. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|horizontal|Read the invector docs.|
|up|Read the invector docs.|

[Back To Top](#)

------------------
### IEnumerator NetworkReloadWeapon()<a name="NetworkReloadWeapon"></a>

>   When the owner player triggers the reload animation it calls `SetTriggers` RPC which makes the network players play the reload animation to mimic the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|private|False|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override IEnumerator Recoil(float horizontal, float up)<a name="Recoil"></a>

>   Calls the `NetworkRecoil` function on top of all it's normal functionality. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|horizontal|Read the invector docs.|
|up|Read the invector docs.|

[Back To Top](#)

------------------
### public override void ReloadWeapon()<a name="ReloadWeapon"></a>

>   Calls the `NetworkReloadWeapon` IEnumerator 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void SetLeftWeapon(GameObject weapon)<a name="SetLeftWeapon"></a>

>   When the owner changes their left weapon it calls the `vShooterManager_ReceiveSetLeftWeapon` RPC which has the network players set their left weapon to the same thing that the owner player has. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|weapon|GameObject type, the weapon to set as the left weapon|

[Back To Top](#)

------------------
### public override void SetRightWeapon(GameObject weapon)<a name="SetRightWeapon"></a>

>   When the owner changes their right weapon it calls the `vShooterManager_ReceiveSetRightWeapon` RPC which has the network players set their right weapon to the same thing that the owner player has. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|weapon|GameObject type, the weapon to set as the right weapon|

[Back To Top](#)

------------------
### public override void Shoot(Vector3 aimPosition, bool applyHipfirePrecision = false, bool useSecundaryWeapon = false)<a name="Shoot"></a>

>   Sets the `lastAimPos` parameter. This parameter is referenced by the `MP_ShooterWeapon` class. So when the Shot function on that component is called it knows where to fire based on the Vector3 position stored in the `lastAimPos` parameter in this class. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|aimPosition|Read the invector docs.|
|applyHipfirePrecision|Read the invector docs.|
|useSecundaryWeapon|Read the invector docs.|

[Back To Top](#)

------------------
### protected override void UpdateAmmoDisplay(int displayId)<a name="UpdateAmmoDisplay"></a>

>   This overrideds the default functionality of the invector logic to only work if you're the owner player and will not work if you're a networked player   This overrideds the default functionality of the invector logic to only work if you're the owner player and will not work if you're a networked player 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

