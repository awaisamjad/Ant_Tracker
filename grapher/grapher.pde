Table table;  // Declare a Table object to store data from the CSV file

void setup() {
  size(800, 600);  // Create a window with a size of 800 x 600 pixels
  table = loadTable("JS.csv", "header");  // Load the CSV file into the Table object, skip the first row (header)
}

void draw() {
  background(255);  // Set the background color to white
  stroke(0);  // Set the stroke color to black

  int numRows = table.getRowCount();  // Get the number of rows in the Table
  int[] ids = new int[numRows];  // Create an array to store unique identifiers
  float[][] data = new float[numRows][2];  // Create a 2D array to store x and y coordinate pairs
  int numIds = 0;  // Initialize the number of unique identifiers to zero

  // Loop through all rows in the Table
  for (int i = 0; i < numRows; i++) {
    TableRow row = table.getRow(i);  // Get a specific row from the Table
    int id = row.getInt(0);  // Get the identifier from the first column of the row
    float x = row.getFloat(1);  // Get the x-coordinate from the second column of the row
    float y = row.getFloat(2);  // Get the y-coordinate from the third column of the row
    boolean isNewId = true;  // Initialize a boolean to track whether the identifier is new or not

    // Loop through all previously stored identifiers
    for (int j = 0; j < numIds; j++) {
      if (id == ids[j]) {  // If the current identifier matches a stored identifier
        data[j][0] = x;  // Store the x-coordinate at the corresponding index
        data[j][1] = y;  // Store the y-coordinate at the corresponding index
        isNewId = false;  // Set the boolean to false since the identifier is not new
        break;  // Exit the loop since the identifier has been found
      }
    }

    if (isNewId) {  // If the identifier is new
      ids[numIds] = id;  // Store the new identifier
      data[numIds][0] = x;  // Store the x-coordinate at the corresponding index
      data[numIds][1] = y;  // Store the y-coordinate at the corresponding index
      numIds++;  // Increment the number of unique identifiers
    }
  }

// Loop through all unique identifiers and draw a line graph for each
  for (int i = 0; i < numIds; i++) {
    int id = ids[i];
    float[] xvals = new float[data[i].length];
    float[] yvals = new float[xvals.length];
    int index = 0;

    // Extract x and y coordinate pairs for the current identifier
    for (int j = 0; j < data[i].length; j+=2) {
      xvals[index] = data[i][j];
      yvals[index] = data[i][j+1];
      index++;
    }

    // Set the stroke color based on the current identifier and draw the line graph
    stroke(getColor(id));
    drawLineGraph(xvals, yvals);
  }
}

// Draw a line graph given an array of x-coordinates and an array of y-coordinates
void drawLineGraph(float[] xvals, float[] yvals) {
  float xmin = min(xvals);
  float xmax = max(xvals);
  float ymin = min(yvals);
  float ymax = max(yvals);
  float xrange = xmax - xmin;
  float yrange = ymax - ymin;

  float xprev = map(xvals[0], xmin, xmax, 50, width-50);
  float yprev = map(yvals[0], ymin, ymax, height-50, 50);

  for (int i = 1; i < xvals.length; i++) {
    float x = map(xvals[i], xmin, xmax, 50, width-50);
    float y = map(yvals[i], ymin, ymax, height-50, 50);
    line(xprev, yprev, x, y);
    xprev = x;
    yprev = y;
  }
}

int getColor(int id) {
  switch (id) {
    case 14:
      return color(255, 0, 0);
    case 15:
      return color(0, 0, 255);
    default:
      return color(0, 0, 0);
  }
}