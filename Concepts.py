1 main style sheet
1 utility style sheet
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="utils.css">

https://getbootstrap.com/docs/5.3/examples/pricing/
rightclick->inspect




<div class="topleft flex items-center">
                        <h1>the best gym in the city</h1>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo tempore sequi et officiis
                            consequatur, tenetur quas quaerat. Facere itaque expedita nihil eveniet error ipsa ex
                            blanditiis. Assumenda alias facere voluptatem. Molestias, doloremque praesentium! Provident
                            porro neque harum cum?</p>
                    </div>
   //Because of this "the best gym in the city" comes on the side                
<div class="topleft flex items-center flex-col">




.flex-col {
    flex-direction: column;
}
"The best gym city comes on top"






.justify-between {
    justify-content: space-between;
}
Using this the nav section"Home About Contact Us Services" went to the right






.topleft {
    width: 50%;
    height: 50vh;
}
.topright {
    height: 50vh;
    width: 50%;
}
Didn't put "height=50vh" so the lorem paragarph didn't come in the middle







.btn {
    padding: 7px 12px;
    border: 2px solid white;
    cursor: pointer;
    border-radius: 6px;
    color: white;
    background-color: rgb(29, 88, 214);
}
// "cursor: pointer" changes the cursor into glove when we hover on the button







<h1 class="my-1">The best gym in the city</h1>
.my-1 {
    margin-top: 13px;
    margin-bottom: 13px;
}
//Created space on the top and bottom of the heading











Using this
 <h1 class="my-1 text-center">The Best Fitness Gym in the City </h1>
 and this
 .text-center {
    text-align: center;
}
we got "The best fitness gym in the city" in center









<img class="gymimg" src="running.png" alt="">
and
.topright .gymimg {
    width: 466px;
}
Got the running.png smaller










.container {
    max-width: 80vw;
    height: 12px;
    font-family: 'Ubuntu', sans-serif;
}
gave the same font to everything







<h1 class="text-center">Pricing</h1>
//got pricing in the middle








.section2 {
    padding-left: 63px;
    padding-right: 63px;
}
made the lorem paragraph look neater





.box ul {
    list-style-type: none;
}
To remove the bullets







.box ul li {
    margin: 12px 2px;
}
This got spaces between 
"₹0
Beginner Classes
Personal Training
Foundation Training
Olympic Weightlifting"
and the 2px shifted this to the left a bit





.box {
    padding: 8px 0;
    margin: 22px 22px;
    min-width: 20vw;
    border: 2px solid rgb(243, 80, 5);
    text-align: center;
    border-radius: 8px;
}
"border: 2px solid black;" this line made those 3 boxes
"min-width: 20vw" this line made the 3 boxes smaller to prevent from going out of bound
"border-radius" curved the edges of the box




<div class="boxes flex">
This line sets the boxes side by side if this is removed then the
boxes will be placed one below each other




<div class="boxes flex justify-center">
This positioned the 3 boxes in the middle






<p class="my-2">
created spaces between the line "Pricing" and the paragaraph







.box h2 {
    font-size: 2rem;
    padding: 15px 0;
}
"padding: 15px 0;"
Created space between box boundary, popular and price





.section3 {
    padding-left: 63px;
    padding-right: 63px;
}
The table moved slightly towards the left





.section3 table th {
    width: 23vw;
    border-bottom: 2px solid black;
}
Makes rows




.section3 table {
    width: 54vw;
    margin: 40px 0;
    border-collapse: collapse;
}
//"border-collapse: collapse" removes the gaps in the line





.section3 table {
    width: 100%;
    margin-bottom: 100px 0;
    border-collapse: collapse;
}
"width 100%" made the table lines longer






.section2 {
    padding: 93px;
}
made it more open






align-items: center;
To put things in Center





flex-direction: column;