1. If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!
2. Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!
3. Explain the differences between margin, border, and padding, and how to implement these three things!
4. Explain the concepts of flex box and grid layout along with their uses!
5. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

1. Inline(Direct Appliance) > ID (Specific object) > Class (Elements Identification) > Elements (Generic, low specificity)
2. Some devices have irregular size and it's possible the viewer missed some important details when the size requirement doesn't fit. example is https://github.com for one that have and old .gov web for those that doesn't
3. Spacing :
	3. 1. Margin (outside, seperate)
	3. 2. Border (element's boundaries)
	3. 3. Padding (content widened)
4. Diff :
	4. 1. FlexBox (flexible, Width based)
	4. 2. Grid (Complex, Pixel based)
5. Tutorial 4 > Changed models.py > changed forms.py > deleted "Add Product" button on main.html > Added "Add Product" button onto navbar.html > Changed all color schemes > Redesign [card_info.html, card_mood.html] > Deleted last_login from main.html > Added last_login to navbar.html >