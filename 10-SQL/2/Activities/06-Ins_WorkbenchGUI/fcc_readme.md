* So long as the table that users are working with includes a primary key with unique values, it is actually possible to create, update, and delete values using MySQL Workbench's GUI.

* Create a new table within the database using [comcastFccComplaints.csv](Activities/06-Ins_WorkbenchGUI/comcastFccComplaints.csv), alter the table so that it has a primary key, and then run a `SELECT * FROM` statement to open up the table viewer.

    * Double click on any value in any row to change these values. 

    * They can even add new rows entirely by scrolling down to the bottom of the table and filling in those cells that contain "NULL".

    * select the row that should be deleted and click on the "Delete Selected Row" button at the top of the viewer.

    * None of the changes are made permanent until the "APPLY" button is clicked in the lower right-hand portion of the viewer.