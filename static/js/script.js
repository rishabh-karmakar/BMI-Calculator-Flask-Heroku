let st = document.getElementById("st");
let h = document.getElementById("h");
var i = 0;
function change() {
  //   var doc = document.getElementById("background");
  var color = ["rgb(118, 40, 170)", "darkgreen"];
  document.body.style.backgroundColor = color[i];
  if (document.body.style.backgroundColor == color[0]) {
    h.style.color = "darkgreen";
  } else if (document.body.style.backgroundColor == color[1]) {
    h.style.color = "rgb(118, 40, 170)";
  }
  i = (i + 1) % color.length;
}
setInterval(change, 1000);
if (st.innerText == "Thin") st.style.color = "orange";
else if (st.innerText == "Healthy") st.style.color = "green";
else if (st.innerText == "Overweight") st.style.color = "goldenrod";
else if (st.innerText == "Obese") st.style.color = "red";
