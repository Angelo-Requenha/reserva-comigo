// autocomplete.js

// Inicializa o Autocomplete
function initAutocomplete() {
    var input = document.getElementById('autocomplete');
    var autocomplete = new google.maps.places.Autocomplete(input);
  
    // Adiciona um listener para preencher automaticamente os campos do formulário quando um lugar é selecionado
    autocomplete.addListener('place_changed', function() {
      var place = autocomplete.getPlace();
      fillFormFields(place);
  
      document.getElementById('registration-form').style.display = 'block';
    });
  }
  
  // Preenche os campos do formulário com os detalhes do lugar
  function fillFormFields(place) {
    document.getElementById('id_endereco').value = place.formatted_address || '';
    document.getElementById('id_cep').value = getAddressComponent(place, 'postal_code') || '';
    document.getElementById('id_pais').value = getAddressComponent(place, 'country') || '';
    document.getElementById('id_longitude').value = place.geometry.location.lng() || '';
    document.getElementById('id_latitude').value = place.geometry.location.lat() || '';
  }
  
  // Obtém um componente de endereço específico do lugar
  function getAddressComponent(place, componentType) {
    for (var i = 0; i < place.address_components.length; i++) {
      var component = place.address_components[i];
      for (var j = 0; j < component.types.length; j++) {
        if (component.types[j] == componentType) {
          return component.long_name;
        }
      }
    }
    return '';
  }
  
  // Tenta geolocalizar o usuário
  function geolocate() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var geolocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
  
        // Configure o raio de pesquisa para o usuário
        var circle = new google.maps.Circle({
          center: geolocation,
          radius: position.coords.accuracy
        });
      });
    }
  }
  