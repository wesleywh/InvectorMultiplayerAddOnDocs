[Back To Index](../../index.md)

# MP_vMeleeCombatInput

[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[BreakAttack](#BreakAttack)<br>
[OnDisableAttack](#OnDisableAttack)<br>
[OnEnableAttack](#OnEnableAttack)<br>
[OnReceiveAttack](#OnReceiveAttack)<br>
[OnRecoil](#OnRecoil)<br>
[ResetAttackTriggers](#ResetAttackTriggers)<br>
[TriggerStrongAttack](#TriggerStrongAttack)<br>
[TriggerWeakAttack](#TriggerWeakAttack)<br>

------------------
### public override void BreakAttack(int breakAtkID)<a name="BreakAttack"></a>

>   This makes this action only callable by the owner and networked players will not react to the input of the owner players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnDisableAttack()<a name="OnDisableAttack"></a>

>   This makes this action only callable by the owner and networked players will not react to the input of the owner players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnEnableAttack()<a name="OnEnableAttack"></a>

>   This makes this action only callable by the owner and networked players will not react to the input of the owner players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnReceiveAttack(vDamage damage, vIMeleeFighter attacker)<a name="OnReceiveAttack"></a>

>   This makes this action only callable by the owner and networked players will not react to the input of the owner players. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void OnRecoil(int recoilID)<a name="OnRecoil"></a>

>   When the owner player recoils it calls `SetTriggers` RPC and `ResetTriggers` RPC for all network players to mimic what the owner player is doing. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|recoilID|***No found decription**|

[Back To Top](#)

------------------
### public override void ResetAttackTriggers()<a name="ResetAttackTriggers"></a>

>   This makes this action only callable by the owner and networked players will not react to the input of the owner players. Also Calls the `ResetTriggers` with `WeakAttack` and `StrongAttack` over the network for the networked players to execute. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void TriggerStrongAttack()<a name="TriggerStrongAttack"></a>

>   When the owner makes a weak attack it calls `SetTriggers` RPC which has the network players make a strong attack to mimic what the owner player is doing. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public override void TriggerWeakAttack()<a name="TriggerWeakAttack"></a>

>   When the owner makes a weak attack it calls `SetTriggers` RPC which has the network players make a weak attack to mimic what the owner player is doing. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

**No parameters**

[Back To Top](#)

