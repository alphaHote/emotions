
var isUpdate=false;
var slider_a = document.getElementById("myRange_a");
var output_a = document.getElementById("demo_a");
output_a.innerHTML = slider_a.value;
slider_a.oninput = function() {output_a.innerHTML = this.value; isUpdate=true;}


var slider_b = document.getElementById("myRange_b");
var output_b = document.getElementById("demo_b");
output_b.innerHTML = slider_b.value;
slider_b.oninput = function() {output_b.innerHTML = this.value; isUpdate=true;}



var slider_c = document.getElementById("myRange_c");
var output_c = document.getElementById("demo_c");
output_c.innerHTML = slider_c.value;
slider_c.oninput = function() {output_c.innerHTML = this.value; isUpdate=true;}


var slider_d = document.getElementById("myRange_d");
var output_d = document.getElementById("demo_d");
output_d.innerHTML = slider_d.value;
slider_d.oninput = function() {output_d.innerHTML = this.value; isUpdate=true;}


var slider_e = document.getElementById("myRange_e");
var output_e = document.getElementById("demo_e");
output_e.innerHTML = slider_e.value;
slider_e.oninput = function() {output_e.innerHTML = this.value ; isUpdate=true;}


var slider_f = document.getElementById("myRange_f");
var output_f = document.getElementById("demo_f");
output_f.innerHTML = slider_f.value;
slider_f.oninput = function() {output_f.innerHTML = this.value ; isUpdate=true;}



//try button push to post request
const button = document.getElementById('post-btn');
/*
button.addEventListener('click', async _ => {
  try {     
    const response = await fetch('/soumettre', {
      method: 'POST',
      body: {
        "v1" : slider_b.value,"v2" : slider_a.value
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});
*/

var output_g = document.getElementById("demo_g");

button.addEventListener('click', async _ => {
  if (isUpdate){
  output_g.innerHTML = 
  "("+slider_a.value+","+
      slider_b.value+","+
      slider_c.value+","+
      slider_d.value+","+
      slider_e.value+","+
      slider_f.value+")";
}
});
