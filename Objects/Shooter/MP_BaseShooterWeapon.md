[Back To Index](../../index.md)

# MP_BaseShooterWeapon

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[ChildTreeCheck](#ChildTreeCheck)<br>
[RecieveNetworkEmptyClip](#RecieveNetworkEmptyClip)<br>
[RecieveNetworkOnChangerPowerCharger](#RecieveNetworkOnChangerPowerCharger)<br>
[RecieveNetworkOnDisableAim](#RecieveNetworkOnDisableAim)<br>
[RecieveNetworkOnEnableAim](#RecieveNetworkOnEnableAim)<br>
[RecieveNetworkOnFinishAmmo](#RecieveNetworkOnFinishAmmo)<br>
[RecieveNetworkOnFinishReload](#RecieveNetworkOnFinishReload)<br>
[RecieveNetworkOnFullPower](#RecieveNetworkOnFullPower)<br>
[RecieveNetworkReload](#RecieveNetworkReload)<br>
[RecieveNetworkShot](#RecieveNetworkShot)<br>
[RecieveNetworkShot](#RecieveNetworkShot)<br>
[SendNetworkEmptyClip](#SendNetworkEmptyClip)<br>
[SendNetworkOnFinishAmmo](#SendNetworkOnFinishAmmo)<br>
[SendNetworkOnFinishReload](#SendNetworkOnFinishReload)<br>
[SendNetworkOnFullPower](#SendNetworkOnFullPower)<br>
[SendNetworkReload](#SendNetworkReload)<br>
[SendOnChangerPowerCharger](#SendOnChangerPowerCharger)<br>
[SendOnDisableAim](#SendOnDisableAim)<br>
[SendOnEnableAim](#SendOnEnableAim)<br>
[SetArrowView](#SetArrowView)<br>
[Start](#Start)<br>
[ViewCheck](#ViewCheck)<br>
[WeaponCheck](#WeaponCheck)<br>

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   Makes sure there is a valid photon view at the root of this object where the vThirdPersonController is 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void ChildTreeCheck()<a name="ChildTreeCheck"></a>

>   Builds a child tree index to the targeted photon view if one is not already made. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkEmptyClip()<a name="RecieveNetworkEmptyClip"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the empty clip effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkOnChangerPowerCharger(float amount)<a name="RecieveNetworkOnChangerPowerCharger"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the on change power charger effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkOnDisableAim()<a name="RecieveNetworkOnDisableAim"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the on disable aim effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkOnEnableAim()<a name="RecieveNetworkOnEnableAim"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the on enable aim effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkOnFinishAmmo()<a name="RecieveNetworkOnFinishAmmo"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the on finished ammo effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkOnFinishReload()<a name="RecieveNetworkOnFinishReload"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the on finished reload effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkOnFullPower()<a name="RecieveNetworkOnFullPower"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the on full power effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkReload()<a name="RecieveNetworkReload"></a>

>   This is called by the RPC when the networked versions receives a request from the owner for them to play the reload effect. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void RecieveNetworkShot(Vector3 aimPos)<a name="RecieveNetworkShot"></a>

>   (Legacy) This function now simply returns. This logic has now been integrated into the MP_ShooterMeleeInput component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|aimPos|Vector3 type, The position to shoot at.|

[Back To Top](#)

------------------
### public virtual void RecieveNetworkShot()<a name="RecieveNetworkShot"></a>

>   (Legacy) This function now simply returns. This logic has now been integrated into the MP_ShooterMeleeInput component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendNetworkEmptyClip()<a name="SendNetworkEmptyClip"></a>

>   (Legacy) This function simply returns. It is now only kept as to not break current weapons that have unity events referencing this. This logic has now been integrated into the MP_ShooterMeleeInput component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendNetworkOnFinishAmmo()<a name="SendNetworkOnFinishAmmo"></a>

>   If owner will send an RPC to all networked versions to play the OnFinishAmmo function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendNetworkOnFinishReload()<a name="SendNetworkOnFinishReload"></a>

>   If owner will send an RPC to all networked versiosn to play the OnFinishedReload function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendNetworkOnFullPower()<a name="SendNetworkOnFullPower"></a>

>   If owner will send an RPC to all networked versions to play the OnFullPower function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendNetworkReload()<a name="SendNetworkReload"></a>

>   If owner will send an RPC to all networked versions to reload this weapon 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendOnChangerPowerCharger(float amount)<a name="SendOnChangerPowerCharger"></a>

>   If owner will send an RPC to all networked versions to play the OnChangerPowerCharger function with the amount of charge. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendOnDisableAim()<a name="SendOnDisableAim"></a>

>   If owner will send an RPC to all networked versions to play the OnDisableAim function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SendOnEnableAim()<a name="SendOnEnableAim"></a>

>   If owner will send an RPC to all networked versions to play the OnEnableAim function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void SetArrowView(vProjectileControl control)<a name="SetArrowView"></a>

>   This is called from the OnInstantiateProjectile UnityEvent to set the ArrowView components viewId on the instantiated arrow. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|control|vProjectileControl type, just to make this work with the UnityEvent, not used otherwise.|

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   Makes sure there is an index tree to the PhotonView for this weapon and it has a valid vShooterWeapon component attached. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void ViewCheck()<a name="ViewCheck"></a>

>   Sets the target PhotonView to the one that is on the root of this object tree where the vThirdPersonController is. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void WeaponCheck()<a name="WeaponCheck"></a>

>   Make sure there is a vShooterWeapon component targeted on this weapon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

