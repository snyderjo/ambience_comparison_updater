Contains all of the components necessary to create a daily report of ambience comparison.  The query pulls the data necessary to render the rmarkdown documents.

The documents can be used to update the contents of a github.io project website.

### A couple of notes:  
rmarkdown's `render` command requires access to [pandoc](https://pandoc.org/), which does not come packaged with R.  Pandoc does come packaged with [Rstudio](https://posit.co/downloads/), R's IDE.
I've implemented the following solution:

Run the command
`Sys.getenv("RSTUDIO_PANDOC")`
on the machine on which I will run the script in question,

and create an `.Rprofile` file in the appropriate directory and add the command 
`Sys.setenv(RSTUDIO_PANDOC="/path/to/rstudio_pandoc/from/above")`
This leverages Rstudio's version of pandoc.

This solution is machine dependent.