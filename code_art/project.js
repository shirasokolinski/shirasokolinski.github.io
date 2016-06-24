var cnv;

function centerCanvas() {
  var x = (windowWidth - width) / 2;
  var y = (windowHeight - height) / 2;
  cnv.position(x, y);
}

function setup() {
  cnv = createCanvas(windowWidth, windowHeight);
  centerCanvas();
  noFill();
  background(0);
}

function windowResized() {
  centerCanvas();
}


function setup() {
  createCanvas(windowWidth, windowHeight)
  noFill();
  background(0);
  angleMode(RADIANS);
   translate(windowHeight/2, windowWidth/2 );
}

var r = 0;
function draw() {
  rotate(4);
  //changes color slowly from yellow to white
  stroke(1.1 * r, 1.1 * r, 0.1 * r);
  arc(50, 50, r, r, 0, PI + QUARTER_PI, PIE);
  r += 4;

}

}
