var button;
var x;
var y;

function setup() {
  createCanvas(400, 300);
  button = createButton("Hello");

  background(50);
		button.mousePressed(randomRectangle);
} 

function draw() { 
	button.position(x,y);
}

function randomRectangle() {
    background(random (255),random (255), random(255));
	x= random(width);
	y= random(height);
	
}

function randomLocation() {
	
}