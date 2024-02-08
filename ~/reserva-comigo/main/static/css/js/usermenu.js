// Seleciona o botão e a janela modal
var btn = document.getElementById("openModal");
var modal = document.getElementById("myModal");

// Seleciona o elemento de fechar
var span = document.getElementsByClassName("close")[0];

// Quando o usuário clicar no botão, a janela modal será exibida
btn.onclick = function() {
  modal.style.display = "block";
}

// Quando o usuário clicar no 'x', a janela modal será fechada
span.onclick = function() {
  modal.style.display = "none";
}

// Quando o usuário clicar fora da janela modal, ela será fechada
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
