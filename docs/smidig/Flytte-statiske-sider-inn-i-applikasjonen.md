# Flytte statiske sider inn i applikasjonen

1. Sidene er migrert inn i applikasjonen
   1. Info
      1. Se i app/views/pages for å finne de separate sidene.
      2. "Template" ligger i app/views/templates/application.html.erb
      3. Eventuelle nye sider må legges til i config/routes.rb
   2. Gjenstående
      1. Noe formattering med CSS er feil.
2. Caching er lagt inn
   1. rake deploy:<miljø> rydder opp i cache
