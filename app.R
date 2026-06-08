# app.R -----------------------------------------------------------------------
# Entry point. Open in RStudio and click "Run App", or run shiny::runApp() with
# the working directory set to this folder.
#
# A single-file app does not auto-source global.R, so we source it here. global.R
# loads packages (including bslib), reads the data, defines the lookups, and
# sources every R/sec_*.R section file.
source("global.R")
#
# Wiring: Section A returns a reactive list (the chosen calm-period split and the
# re-labelled messages). That list is passed into every other section, so moving
# the calm-period slider on the first tab recomputes the others together.

ui <- page_navbar(
  title = "TenantThread Breach Explorer",
  theme = bs_theme(version = 5, primary = "#2C5282"),
  fillable = FALSE,
  nav_panel("Activity & abnormality", sec_activity_ui("activity")),
  nav_panel("The bypass",             sec_bypass_ui("bypass")),
  nav_panel("Network",                sec_network_ui("network")),
  nav_panel("Topics & evidence",      sec_topics_ui("topics")),
  nav_spacer(),
  nav_item(tags$span(style = "color:#718096;font-size:0.85em;",
                     "VAST 2026 MC1 · set the calm period on the Activity tab"))
)

server <- function(input, output, session) {
  # Section A runs first and produces the shared reactives.
  act <- sec_activity_server("activity")

  # Pass them into the other sections.
  sec_bypass_server ("bypass",  messages = act$messages)
  sec_network_server("network", messages = act$messages, split = act$split)
  sec_topics_server ("topics",  messages = act$messages)
}

shinyApp(ui, server)
