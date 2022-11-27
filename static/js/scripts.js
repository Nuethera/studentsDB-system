const gr = $("#greeting")[0];
const hour = new Date().getHours();
const welcomeTypes = ["Good Morning", "Good Afternoon", "Good Evening"];
let welcomeText = "";

if (hour < 12) welcomeText = welcomeTypes[0];
else if (hour < 18) welcomeText = welcomeTypes[1];
else welcomeText = welcomeTypes[2];

gr.innerHTML = welcomeText;