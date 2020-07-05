[Back To Index](../index.md)

# FloatingBar

[Jump To Parameters](#parameter-definitions)<br/>
[Jump To Function Definitions](#functions-definitions)<br/>

--------------------------------------------------------
## Parameter Definitions<a name="parameter-definitions"></a>

Select the parameter name from below to jump directly to it on this page.

[allImages](#parameter-allImages)<br>
[allTexts](#parameter-allTexts)<br>
[colorBarFillOffset](#parameter-colorBarFillOffset)<br>
[coloredBar](#parameter-coloredBar)<br>
[controller](#parameter-controller)<br>
[displayBarNumber](#parameter-displayBarNumber)<br>
[displayTime](#parameter-displayTime)<br>
[displayType](#parameter-displayType)<br>
[fadeOut](#parameter-fadeOut)<br>
[fadeSpeed](#parameter-fadeSpeed)<br>
[fillBar](#parameter-fillBar)<br>
[fillDelay](#parameter-fillDelay)<br>
[fillSpeed](#parameter-fillSpeed)<br>
[onlyEnableForNoneOwner](#parameter-onlyEnableForNoneOwner)<br>
[realTimeTracking](#parameter-realTimeTracking)<br>
[startHidden](#parameter-startHidden)<br>
[type](#parameter-type)<br>

------------------
### allImages<a name="parameter-allImages"></a>

> All images to fade in and out

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image[]|new Image[] { }

[Back To Top](#)

------------------
### allTexts<a name="parameter-allTexts"></a>

> All texts to fade in and out

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text[]|new Text[] { }

[Back To Top](#)

------------------
### colorBarFillOffset<a name="parameter-colorBarFillOffset"></a>

> If the bars are not quite the same size then you need to have the bars at a different fill amount." <br> Use this offset to achieve this

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.076f

[Back To Top](#)

------------------
### coloredBar<a name="parameter-coloredBar"></a>

> The actual colored bar to resize according to the selected number.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image|null

[Back To Top](#)

------------------
### controller<a name="parameter-controller"></a>

> Required if using real time tracking. Will always keep track of the " <br>values in the controller and update the bars for you.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |vThirdPersonController|null

[Back To Top](#)

------------------
### displayBarNumber<a name="parameter-displayBarNumber"></a>

> The text to show based on the current value of your bar.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Text|null

[Back To Top](#)

------------------
### displayTime<a name="parameter-displayTime"></a>

> How long to display this UI before disabling it after a change (Only matters if fade out is true).

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|6.0f

[Back To Top](#)

------------------
### displayType<a name="parameter-displayType"></a>

> How to display your tracked number in the displayBarNumber field.\n\n" <br>Whole = Convert float to int.\n" <br>Percent = Convert the number to a percent value\n" <br>Raw = Display the raw tracked number

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |NumberDisplayType|NumberDisplayType.Percent

[Back To Top](#)

------------------
### fadeOut<a name="parameter-fadeOut"></a>

> Instead of just turning off the elements you want to slowly fade this images out.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
### fadeSpeed<a name="parameter-fadeSpeed"></a>

> How fast to fade the texts/images.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.4f

[Back To Top](#)

------------------
### fillBar<a name="parameter-fillBar"></a>

> Will adjust a set delay later after the colored bar.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |Image|null

[Back To Top](#)

------------------
### fillDelay<a name="parameter-fillDelay"></a>

> How long to wait before adjusting the fill bar.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|1.5f

[Back To Top](#)

------------------
### fillSpeed<a name="parameter-fillSpeed"></a>

> How fast to adjust the fill bar.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |float|0.4f

[Back To Top](#)

------------------
### onlyEnableForNoneOwner<a name="parameter-onlyEnableForNoneOwner"></a>

> Only show this bar if this is a networked player that you are not controlling. (i.e. other players that are not you)

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
### realTimeTracking<a name="parameter-realTimeTracking"></a>

> If you want to have this function be the thing that is keeping " <br>track of the values. Uses the update method. Less efficent but saves " <br>you some extra work.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
### startHidden<a name="parameter-startHidden"></a>

> Will only display for set amount of time only if the tracked number changes.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|protected |bool|true

[Back To Top](#)

------------------
### type<a name="parameter-type"></a>

> What type of floating bar is this?\n\n" <br>Health = Track the vThirdPersonController's health.\n" <br>Stamina = Track the vThirdPersonController's stamina\n" <br>Custom = Input a custom component that exposes a function called \"CustomOutputValue\" " <br>that outputs a float value for you to track.

| Exposed Value | Type | Default Value |
|:---|:---|---:|
|public |FloatingBarType|FloatingBarType.Health

[Back To Top](#)

## Function Definitions<a name="functions-definitions"></a>

Select the function name from below to jump directly to it on this page.

[Awake](#Awake)<br>
[DelayAdjustFillBar](#DelayAdjustFillBar)<br>
[DelayFadeElements](#DelayFadeElements)<br>
[GetRemaining](#GetRemaining)<br>
[GetWholeNumber](#GetWholeNumber)<br>
[SetBarValue](#SetBarValue)<br>
[SetElementsAlpha](#SetElementsAlpha)<br>
[Start](#Start)<br>
[Update](#Update)<br>
[UpdateMaxValue](#UpdateMaxValue)<br>
[UpdateTrackedValue](#UpdateTrackedValue)<br>

------------------
### protected virtual void Awake()<a name="Awake"></a>

>   Sets the starting fill amount and the starting alpha values. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator DelayAdjustFillBar()<a name="DelayAdjustFillBar"></a>

>   Makes it so the fill amount doesn't adjust to the new amount for a few seconds. The wait time is based on the `fillDelay` parameter. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual IEnumerator DelayFadeElements()<a name="DelayFadeElements"></a>

>   Will not fade the elements after changing for a few seconds. Then calls the `SetElementsAlpha` function. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual float GetRemaining()<a name="GetRemaining"></a>

>   Returns a percentage float comparing the current with the max values. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| float percentage|

**No parameters**

[Back To Top](#)

------------------
### protected virtual int GetWholeNumber()<a name="GetWholeNumber"></a>

>   Returns the current value as a whole number 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True| whole number representing the current value|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void SetBarValue()<a name="SetBarValue"></a>

>   Sets the text and fill amounts based on the `displayType` parameter. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void SetElementsAlpha(float setAlpha)<a name="SetElementsAlpha"></a>

>   Sets the alpha values on the images and text elements in the `allTexts` and `allImages` list. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|setAlpha|float type, the alpha value to set the elements to.|

[Back To Top](#)

------------------
### protected virtual void Start()<a name="Start"></a>

>   Finds and sets the bar values based on the current settings in the `vThirdPersonController` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### protected virtual void Update()<a name="Update"></a>

>   Dynamically updates the alpha and fill amount values based on changes in the `vThirdPersonController` and the settings on this component. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|protected|True|Does not return anything|

**No parameters**

[Back To Top](#)

------------------
### public virtual void UpdateMaxValue(float value)<a name="UpdateMaxValue"></a>

>   Can override the max value to compare against. This value is used to display percentages. This is normally the `maxStamina` or `maxHealth` values in the `vThirdPersonController`. 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|value|***No found decription**|

[Back To Top](#)

------------------
### public virtual void UpdateTrackedValue(float value)<a name="UpdateTrackedValue"></a>

>   Can override the value to be displayed. This is normally the `currentHealth` or `currentStamina` in the `vThirdPersonController` 

| Expose Value | Overrideable | Returns |
|:---|:---|---:|
|public|True|Does not return anything|

| Parameter Name | Description |
|:---|:---|
|value|***No found decription**|

[Back To Top](#)

