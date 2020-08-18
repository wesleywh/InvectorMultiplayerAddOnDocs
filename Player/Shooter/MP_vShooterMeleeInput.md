[Back To Index](../../index.md)

# MP_vShooterMeleeInput

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[BreakAttack](#BreakAttack)<br>
[FixedUpdate](#FixedUpdate)<br>
[LateUpdate](#LateUpdate)<br>
[OnAnimatorMove](#OnAnimatorMove)<br>
[OnDisableAttack](#OnDisableAttack)<br>
[OnEnableAttack](#OnEnableAttack)<br>
[OnRecoil](#OnRecoil)<br>
[ReceivePulledTrigger](#ReceivePulledTrigger)<br>
[ResetAttackTriggers](#ResetAttackTriggers)<br>
[ResetShooterAnimations](#ResetShooterAnimations)<br>
[SendPulledTrigger](#SendPulledTrigger)<br>
[TriggerStrongAttack](#TriggerStrongAttack)<br>
[TriggerWeakAttack](#TriggerWeakAttack)<br>
[Update](#Update)<br>
[UpdateMeleeAnimations](#UpdateMeleeAnimations)<br>
[UpdateShooterAnimations](#UpdateShooterAnimations)<br>

------------------
### public override void BreakAttack(int breakAtkID)<a name="BreakAttack"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void FixedUpdate()<a name="FixedUpdate"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void LateUpdate()<a name="LateUpdate"></a>

>   Overrides default functionality of invector to perform the same if you're the owner player. Otherwise will only update its aiming location based on what is received over the network. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnAnimatorMove()<a name="OnAnimatorMove"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnDisableAttack()<a name="OnDisableAttack"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnEnableAttack()<a name="OnEnableAttack"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnRecoil(int recoilID)<a name="OnRecoil"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Will also set the triggers for recoil and strong attack and reset the triggers for weak attack and strong attack for the networked players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void ReceivePulledTrigger()<a name="ReceivePulledTrigger"></a>

>   This is only used by networked versions of players to receive when the owner player is pulling or releasing the trigger to the shooter weapon. It is responsible for firing the target weapon or to stop firing the target weapon. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void ResetAttackTriggers()<a name="ResetAttackTriggers"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Als will reset the triggers for the networked players when called via the `ResetTriggers` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void ResetShooterAnimations()<a name="ResetShooterAnimations"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Sets the animator layer weights for the networked players to mimic the owner player via the `SetAnimatorLayerWeights` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator SendPulledTrigger()<a name="SendPulledTrigger"></a>

>   This is only called by the owner player. This will send when the weapon trigger is pulled or released. This is used in combination with the `ReceivePulledTrigger` function. It will send the weapon that is firing/not firing, the ammo for it, and where it is firing to. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void TriggerStrongAttack()<a name="TriggerStrongAttack"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Triggers the strong attack animation for networked players to mimic the owner player via the `SetTriggers` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void TriggerWeakAttack()<a name="TriggerWeakAttack"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Triggers the weak attack animation for networked players to mimic the owner player via the `SetTriggers` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void Update()<a name="Update"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Also calls the `ReceivePulledTrigger` function if a networked version of a player or the `SendPulledTrigger` function if the owner player. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void UpdateMeleeAnimations()<a name="UpdateMeleeAnimations"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Otherwise the functionality is the same but it also sets the animator layer weights for the networked players to mimic the owner player via the `SetAnimatorLayerWeights` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected override void UpdateShooterAnimations()<a name="UpdateShooterAnimations"></a>

>   Overrides default functionality of invector to only work if you're the owner player and will not work if this is called by a networked player. Sets the animator layer weights for the networked players to mimic the owner player via the `SetAnimatorLayerWeights` RPC. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

