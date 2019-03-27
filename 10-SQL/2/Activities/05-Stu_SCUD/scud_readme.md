* **Instructions**:

    * Import the `GlobalFirePower.csv` into a new table within a localhost database.

    * There is an error with the column headers that have been generated. They have spaces in them. Find a means by which to [**CHANGE**](https://stackoverflow.com/a/40866162) this so that they work properly.  Or just use mysqlworkbench to change column names and you'll see the sql syntax to rename columns.

    * Note that if you have spaces in a column name, you can wrap it in single quotes and do your queries:
    ```
    select 'Total Population' from globalfirepower limit 5;
    ```

    * Find all of those rows that have a "ReservePersonnel" of 0 and then remove these rows from the dataset.

    * Every country in the world at least deserves one "FighterAircraft". Only seems fair. Lets add one to each nation that has none.

    * Oh no! By updating this column, the values within "TotalAircraftStrength" column are now off for those nations! We've got to [add one](https://stackoverflow.com/a/2680352) to the original number.

    * A new nation has been founded and you are declared its leader! Congratulations! Unfortunately for you, every other nation is now looking to take over your land. Perform some calcuations to find the [Averages](https://www.w3schools.com/sql/sql_count_avg_sum.asp) for the "Total" columns, take note of them, and then set those as the values for your nation's military.