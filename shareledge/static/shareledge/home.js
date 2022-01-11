var myIndex = 0;
var myIndex2 = 0;
carousel();

function carousel() {
  var i, j;
  var x = document.getElementsByClassName("images");
  var y = document.querySelector(".text");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (j = 0; j < y.length; j++) {
    y[i].style.display = "none";
  }
  myIndex++;
  myIndex2++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 2000); // Change image every 2 seconds
  if (myIndex2 > y.length) {myIndex2 = 1}    
  y[myIndex2-1].style.display = "block";  
  setTimeout(carousel, 2000); // Change image every 2 seconds
}