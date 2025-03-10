require(rmarkdown)

find_pandoc()

render("dailyReport.Rmd")
render("index.Rmd")