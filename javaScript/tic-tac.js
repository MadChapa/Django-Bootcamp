// Restart Game button
var restart= document.querySelector("#b");



// Grabs all the square
var squares= document.querySelectorAll('td');


//clear all the square
function clearBoard(){
  for(var i=0; i<squares.length; i++){
    squares[i].textContent= '';
  }
}
restart.addEventListener('click', clearBoard);

//check the square marker
// var cellOne=document.querySelector('#one')
// cellOne.addEventListener('click',function(){
//   if(  cellOne.textContent==''){
//     cellOne.textContent= 'X';
//   }else if (cellOne.textContent=='X'){
//     cellOne.textContent= 'o';
//   }else{
//     cellOne.textContent= '';
//   }
// })

//alternative
function changeMarker(){
  if(this.textContent==''){
    this.textContent= 'x';
  }else if (this.textContent=='x') {
    this.textContent='o';
  }else{
    this.textContent='';
  }
}
for(var i=0; i<squares.length;i++){
  squares[i].addEventListener('click',changeMarker)
}



//For Loop to add event Listeners to all the squares
