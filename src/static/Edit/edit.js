const checkables = {
    "Navbar": ""
}

const droppables = {
    "Link": ""
}
 // 🤦‍♂️ you didn't see anything Yeah ok I didn't ;), what are we gonna put in droppables?
 // Links, Buttons, Cards, Any element that you can have multiple instances of, 
// We also need to copy this stuff into sites.py edit function, ok also we should have whole contact forms as droppables
// Probably checkables - These are optional things you can put on the site - but not multiple of them cwim? yes
// Ok so another problem: For checkables we need to hardcode where we put them: Like Navbar should automatically go at the start of body tag.
// Any ideas? well, HMMMMMMMMMMMMMMM webscraping? or 

// Here is what I'm thinking - We somehow give the function: Parent Element ID and position. So think like this
// Instead of checking multiple things, they can only go in order. So like first, we ask navbar. Near the end, we ask contact form, and last we ask footer
// So basically we can just "append" these checkables to the body as long as they go in order. Maybe in the future we can
// Give the checkables an "order" and do some complex calculations to allow the user to, for example, check that they wan
// Footer first and then check the Navbar option, and instead of putting the navbar below the footer it somehow know to put it above
// WOW that was a long paragraph 😅, yes it was and with the boilerplates we will be generating, we should have certain parts of the boiler plates 
// empty with a default value of none, that can be set to a droppable or a checkable

// Wait that is actually a great idea - Here are my thoughts (another long paragraph maybe)
// So we can do that - but ONLY for checkables. For droppables we have to do it differently
// So I'm thinking like this - we have pre-set <div>s that have a class of the checkable name
// So <div class="navbar"> and then we can GetElementByClass and append the checkables to the divs
// But for droppables we can't do that, we need it to be 100% drag-and-drop, so they can drop it ANYWHERE - 
// and that is where it gets complicated, but is probably on stack overflow - YEP StackOverflow is the best - 
// and how can we link all of this to the inspect element thingy thing

// So what I'm thinking is so you know how the demo had a part for the treemap and a part for the preview? 
// So instead of just the tag names in the treemap, we should actually have an option between just generating
// the tag names and showing the entire HTML de. So now here what we can do is we can edit the HTML code
// And whenever the user edits and then focuses out, we can use the same logic we used for Confirm Password
// To basically - render the HTML and display it in the window for the preview. That's what I'm thinking - very long 

// Keep going here any qns? Nope i understand what we have to do, but not all of how to do it obvs
// Yeah I see what you mean - but we have a pretty solid PLAN of what we're going to do, so I like it :)

// I'm actually thinking once we're done with this deliberation we can post and pin on Discord and use this

// So what we need to do is actually code the edit page first and make sure we have like a preview of the HTML code set up
// cause that seems pretty hard to do too, so we just get the boilerplate code, and we add variables in select areas of the boilerplate (defaulted to none) 
//and we append those variables according to the input from the user, and we can render this somehow

// First I think we should figure out how to render HTML... I'll look into it. 
// Actually - can you? It's dinnertime here so I'll be back in around ~20 mins, i will research for 20 mins 
// but i just realised it half past 11 but i will do that still

// Actually how is this - Since it's late you can sleep now - and since you'll wake up like 5 hrs before me you can research it then - 
// sure i will do that, is this goodbye? lol
// I guess... unless you're not sleepy and really want to work now and will still be working for 30+ mins, .... 
// ill research for a bit, and then i'll go off and report to you in the discord, won't be writing anymore 'code' tho
// Ok perfect! Today was really productive - I liked it! 
// So you can just start writing code when you wake up I G and then I'll join in and see what you've done and we can keep working! 
// Okay, I'll see you tommorow i guess ha
// CYA! goodbye!
// Good Night!