function initMap() {
    var latitudeString = document.getElementById('latitude').getAttribute('data-latitude');
    var longitudeString = document.getElementById('longitude').getAttribute('data-longitude');


    // Converte as strings para números   
    var latitude = parseFloat(latitudeString);
    var longitude = parseFloat(longitudeString);
    

    var map = new google.maps.Map(document.getElementById('map'), {
      center: { lat: latitude, lng: longitude },
      zoom: 15
    });
    
    var marker = new google.maps.Marker({
      position: { lat: latitude, lng: longitude },
      map: map,
      title: 'Local do Estabelecimento'
    });
  }

initMap();