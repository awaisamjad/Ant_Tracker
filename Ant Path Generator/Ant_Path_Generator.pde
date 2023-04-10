Table table ;

int currentLine = 0;
int timeDelay = 50; // the time delay between each line drawn

int[] x;
int[] y;
int [] ant_number;

void setup() {
  size(1900, 1000);
  strokeWeight(1);
  table = loadTable("colony_6_data_vid_1.csv", "header");
  x = new int[table.getRowCount()];
  y = new int[table.getRowCount()];
  ant_number = new int[table.getRowCount()];
  for (int i = 0; i < table.getRowCount(); i++) {
    TableRow row = table.getRow(i);
    x[i] = row.getInt("x");
    y[i] = row.getInt("y");
    ant_number[i] = row.getInt("ant");
  }
  print(x, " ");
  print(ant_number, " ");
  println(y);

}

void draw() {
  translate(0, height); // makes coordinate system bottom left as (0,0)
  stroke(200,0,200);
  scale(1, -1);// makes coordinate system bottom left as (0,0)
  background(250);
  
  // checks if x and y array length are equal
  if (x.length != y.length){ 
    noLoop();
    println("x and y array are not equal length");
  }
  else {
    for (int i = 1; i <= currentLine; i++) {
      if (ant_number[i] == 20){
        line(x[i-1], y[i-1], x[i], y[i]);
      }
    }
  }
  if (currentLine < x.length - 1) {
    delay(timeDelay);
    currentLine++;
  }

}

//Table table;
//int timeDelay = 400; // the time delay between each line drawn
//ArrayList<ArrayList<Integer>> antPaths; // array list to store the ant paths

//void setup() {
//  size(1900, 1000);
//  strokeWeight(1);
//  table = loadTable("colony_6_data_vid_1.csv", "header");
  
//  // create a new ArrayList for each ant
//  antPaths = new ArrayList<ArrayList<Integer>>();
//  for (int i = 0; i < 21; i++) {
//    antPaths.add(new ArrayList<Integer>());
//  }
  
//  // add x and y coordinates for each ant to their respective ArrayList
//  for (int i = 0; i < table.getRowCount(); i++) {
//    TableRow row = table.getRow(i);
//    int antNumber = row.getInt("ant");
//    int x = row.getInt("x");
//    int y = row.getInt("y");
//    antPaths.get(antNumber).add(x);
//    antPaths.get(antNumber).add(y);
//  }
//}

//void draw() {
//  translate(0, height); // makes coordinate system bottom left as (0,0)
//  scale(1, -1); // flips the coordinate system so it's top left as (0,0)
//  background(250);
  
//  // draw each ant's path
//  for (int i = 0; i < antPaths.size(); i++) {
//    ArrayList<Integer> path = antPaths.get(i);
//    if (path.size() > 2) { // if there are at least 2 points in the path
//      stroke(i*30, i*30, 0); // assign a different color to each ant
//      for (int j = 0; j < path.size() - 3; j += 2) { // iterate over each pair of points in the path
//        line(path.get(j), path.get(j+1), path.get(j+2), path.get(j+3)); // draw a line between each pair of points
//      }
//    }
//  }
  
//  delay(timeDelay); // delay once per frame
//}
